#include <Windows.h>

#include "ModUtils.h"
#include "Signature.h"
#include "PointerChain.h"
#include "EventFlag.h"
#include "Psapi.h"
#include "CallHook.h"

using namespace ModUtils;

using FnSetEventFlag = void (*)(const uint64_t event_man, uint32_t* event_id, bool state);
using FnApplyEffect = void (*)(void* ChrIns, int spEffectId);
using FnEraseEffect = void (*)(void* CSSpecialEffect, int spEffectId);

struct SpEffectOut {
	void* paramEntry;
	int spEffectId;
	int : 4;
};

#define IBO_GET_SPEFFECTPARAM_FN 0xD19B30

void spEffectParamHook(SpEffectOut& out, int paramId) {//basic hooking example from callhook. prints out a console output on specific effects when theyre called
	//hooking applyEffect seems to act up so I didn't use that one
	if (paramId == 3515) {
		AllocConsole;
		Log("player used str knot effect, effect id:");
		Log(paramId);
	}
	else if (paramId == 100) {
		AllocConsole;
		Log("player rested at grace, effect id:");
		Log(paramId);
	}
	else if (paramId == 15022) {//honestly idk where this id comes from lmao but it works
		AllocConsole;
		Log("player triggered invisibility effect, effect id:");
		Log(paramId);
	}
}

void setupHooks() {
	if (!CallHook::initialize()) return;
	CallHook::CallMap callMap{};
	auto calls = callMap.getCalls(IBO_GET_SPEFFECTPARAM_FN);
	auto hook1 = CallHook::hookFunction<EntryHook>(calls, spEffectParamHook);
}

DWORD WINAPI MainThread(LPVOID lpParam)
{
	ModuleData EldenRingData("eldenring.exe");
	Signature worldChrManSig = Signature("48 8B 05 ?? ?? ?? ?? 48 85 C0 74 0F 48 39 88");

	Signature spEffectApplyCall = Signature("48 8B C4 48 89 58 08 48 89 70 10 57 48 81 EC ?? ?? ?? ?? 0F 28 05 ?? ?? ?? ?? 48 8B F1 0F 28 0D ?? ?? ?? ?? 48 8D 48 88");
	Signature spEffectRemoveCall = Signature("48 83 EC 28 8B C2 48 8B 51 08 48 85 D2 ?? ?? 90");
	Signature eventFlagManager = Signature("48 8B 3D ?? ?? ?? ?? 48 85 FF ?? ?? 32 C0 E9");
	Signature eventFlagSetCall = Signature("?? ?? ?? ?? ?? 48 89 74 24 18 57 48 83 EC 30 48 8B DA 41 0F B6 F8 8B 12 48 8B F1 85 D2 0F 84 ?? ?? ?? ?? 45 84 C0");

	void** WorldChrManIns = (void**)worldChrManSig.Scan(&EldenRingData, 0x3, 0x7);
	void** speApplyCallIns = (void**)spEffectApplyCall.Scan(&EldenRingData);
	void** speRemoveCallIns = (void**)spEffectRemoveCall.Scan(&EldenRingData);
	void** eventFlagMan = (void**)eventFlagManager.Scan(&EldenRingData, 0x3, 0x7);
	void** eventSetIns = (void**)eventFlagSetCall.Scan(&EldenRingData);

	FnApplyEffect applyEffect = reinterpret_cast<FnApplyEffect>(reinterpret_cast<uint8_t*>(speApplyCallIns));
	FnEraseEffect removeEffect = reinterpret_cast<FnEraseEffect>(reinterpret_cast<uint8_t*>(speRemoveCallIns));
	FnSetEventFlag setEventFlag = reinterpret_cast<FnSetEventFlag>(reinterpret_cast<uint8_t*>(eventSetIns));

	AllocConsole();
	FILE* f;
	freopen_s(&f, "CONOUT$", "w", stdout);
	std::cout << "Open" << std::endl;

	bool NoDead = false;
	float defaultXCoord = (-3.507);
	float defaultYCoord = (-0.8775);
	float defaultZCoord = (2.595);
	uint32_t flagid = 1024622001;
	uintptr_t WorldChrMan;

	while (true) {
		
		if (GetAsyncKeyState(VK_NUMPAD1) & 1) {
			WorldChrMan = *(uintptr_t*)WorldChrManIns;
			if (WorldChrMan) {
				NoDead = !NoDead;
			}
			else {
				std::cout << "Currently nullptr, cannot enable" << std::endl;

			}
			std::cout << "Custom nodead status:" << NoDead << std::endl;

		} 
		else if (GetAsyncKeyState(VK_NUMPAD2) & 1) {
			setupHooks();
			std::cout << "applyEffect hook enabled"<< std::endl;

		}
		else if (GetAsyncKeyState(VK_NUMPAD3) & 1) {
			WorldChrMan = *(uintptr_t*)WorldChrManIns;
			auto playerHP = PointerChain::make<int>(WorldChrMan, 0x10EF8, 0, 0x190u, 0, 0x138);
			*playerHP = 0;

		}


		if (NoDead == true) {
			WorldChrMan = *(uintptr_t*)WorldChrManIns;
			if (WorldChrMan) {
				auto playerHP = PointerChain::make<int>(WorldChrMan, 0x10EF8, 0, 0x190u, 0, 0x138);
				if (*playerHP < 1) {
					Log("triggered");
					auto idleAnim = PointerChain::make<int>(WorldChrMan, 0x10EF8, 0, 0x190u, 0x58, 0x18);
					auto currentAnim = PointerChain::make<int>(WorldChrMan, 0x10EF8, 0, 0x190u, 0x58, 0x20);
					auto pMaxHP = PointerChain::make<int>(WorldChrMan, 0x10EF8, 0, 0x190u, 0, 0x13C);
					auto xCoord = PointerChain::make<float>(WorldChrMan, 0x10EF8, 0, 0x190u, 0x68, 0x70);
					auto yCoord = PointerChain::make<float>(WorldChrMan, 0x10EF8, 0, 0x190u, 0x68, 0x78);
					auto zCoord = PointerChain::make<float>(WorldChrMan, 0x10EF8, 0, 0x190u, 0x68, 0x74);
					Sleep(100);
					*playerHP = 1;
					Sleep(1000);
					setEventFlag((uint64_t) *eventFlagMan, &flagid, 1);
					auto chrIns = PointerChain::make<void*>(WorldChrMan, 0x1E508);
					Sleep(1100);
					applyEffect(*chrIns, 15022);
					Sleep(2500);
					if (*currentAnim != 67011) {
						*idleAnim = 67011;
					}
					*xCoord = defaultXCoord;
					*yCoord = defaultYCoord;
					*zCoord = defaultZCoord;
					*playerHP = *pMaxHP;
					Sleep(2500);
					*idleAnim = 63020;
					setEventFlag((uint64_t)*eventFlagMan, &flagid, 0);
					auto CSSpecialEffect = PointerChain::make<void*>(WorldChrMan, 0x1E508, 0x178);
					removeEffect(*CSSpecialEffect, 15022);
				}
			}
			else {
				std::cout << "Currently nullptr, turning off" << std::endl;
				NoDead = false;
			}

		}
	}
	CloseLog();
	return 0;
}

BOOL WINAPI DllMain(HINSTANCE module, DWORD reason, LPVOID)
{
	if (reason == DLL_PROCESS_ATTACH)
	{
		DisableThreadLibraryCalls(module);
		CreateThread(0, 0, &MainThread, 0, 0, NULL);
	}
	return 1;
}