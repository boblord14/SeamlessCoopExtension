#include <Windows.h>

#include "ModUtils.h"
#include "PointerChain.h"
#include "Psapi.h"
#include "CallHook.h"

#include "WorldChrMan.h"
#include "EventFlag.h"
#include "GameFunctions.h"

using namespace ModUtils;

struct SpEffectOut {
	void* paramEntry;
	int spEffectId;
	int : 4;
};

#define IBO_GET_SPEFFECTPARAM_FN 0xD19B30

void spEffectParamHook(SpEffectOut& out, int paramId) {//basic hooking example from callhook. prints out a console output on specific effects when theyre called
	//hooking applyEffect seems to act up so I didn't use that one
	if (paramId == 3520) {
		Log("player used str knot effect, effect id:");
		Log(paramId);
	}
	else if (paramId == 100) {
		Log("player rested at grace, effect id:");
		Log(paramId);
	}
	else if (paramId == 15022) {//honestly idk where this id comes from lmao but it works
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

	AllocConsole();
	FILE* f;
	freopen_s(&f, "CONOUT$", "w", stdout);
	std::cout << "Open" << std::endl;

	bool NoDead = false;

	while (true) {
		if (GetAsyncKeyState(VK_NUMPAD0) & 1) {

			WorldChrMan mainBase = WorldChrMan::Make();
			EventFlag nodeadTrigger = EventFlag(1024622001);
			GameFunctions mainFunctions = GameFunctions::Make();
			Log("base classes built");
			while (true) {
				ChrIns* currentChrIns;
				if (GetAsyncKeyState(VK_NUMPAD1) & 1) {
					if (mainBase.isLoaded()) {
						NoDead = !NoDead;
					}
					else {
						std::cout << "Currently nullptr, cannot enable" << std::endl;

					}
					std::cout << "Custom nodead status:" << NoDead << std::endl;

				}
				else if (GetAsyncKeyState(VK_NUMPAD2) & 1) {
					setupHooks();
					std::cout << "applyEffect hook enabled" << std::endl;

				}
				else if (GetAsyncKeyState(VK_NUMPAD3) & 1) {
					mainBase.setHP(0);
				}
				else if (GetAsyncKeyState(VK_NUMPAD4) & 1) {
					Log("player chrins addr");
					currentChrIns = mainFunctions.getChrIns(10000);
					Log(currentChrIns);
				}
				else if (GetAsyncKeyState(VK_NUMPAD5) & 1) {
					Log("varre chrins addr");
					currentChrIns = mainFunctions.getChrIns(1042360700);
					Log(currentChrIns);
				}
				else if (GetAsyncKeyState(VK_NUMPAD6) & 1) {
					Log("set chrins max hp to 2222");
					auto chrInsMaxHp = PointerChain::make<int>(currentChrIns, 0x190, 0x0, 0x144);
					*chrInsMaxHp = 2222;
				}
				else if (GetAsyncKeyState(VK_NUMPAD7) & 1) {
					Log("set chrins max hp to 200");
					auto chrInsMaxHp = PointerChain::make<int>(currentChrIns, 0x190, 0x0, 0x144);
					*chrInsMaxHp = 200;
				}

				if (NoDead == true) {
					if (mainBase.isLoaded()) {
						if (mainBase.getHP() < 1) {
							Log("triggered");
							Sleep(100);
							mainBase.setHP(1);
							Sleep(1000);
							nodeadTrigger.setFlagState(true);
							Sleep(1100);
							mainFunctions.applyEffect(15022, 10000);
							Sleep(2500);
							if (mainBase.getCurrentAnimID() != 67011) {
								mainBase.setIdleAnim(67011);
							}
							mainBase.setLocalCoords(-3.507f, -0.8775f, 2.595f); //some coords in limgrave near first step
							mainBase.setHP(mainBase.getMaxHP());
							Sleep(2500);
							mainBase.setIdleAnim(63020);
							nodeadTrigger.setFlagState(false);
							mainFunctions.removeEffect(15022, 10000);
						}
					}
					else {
						std::cout << "Currently nullptr, turning off" << std::endl;
						NoDead = false;
					}

				}
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