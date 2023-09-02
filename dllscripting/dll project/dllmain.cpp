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

	AllocConsole();
	FILE* f;
	freopen_s(&f, "CONOUT$", "w", stdout);
	std::cout << "Open" << std::endl;

	bool NoDead = false;

	WorldChrMan mainBase = WorldChrMan::Make();
	EventFlag mainFlag = EventFlag::Make();
	GameFunctions mainFunctions = GameFunctions::Make();

	while (true) {
		
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
			std::cout << "applyEffect hook enabled"<< std::endl;

		}
		else if (GetAsyncKeyState(VK_NUMPAD3) & 1) {
			mainBase.setHP(0);

		}

		if (NoDead == true) {
			if (mainBase.isLoaded()) {
				if (mainBase.getHP() < 1) {
					Log("triggered");
					Sleep(100);
					mainBase.setHP(1);
					Sleep(1000);
					mainFlag.setFlagState(1024622001, 1);
					Sleep(1100);
					mainFunctions.applyEffect(15022, 10000);
					Sleep(2500);
					if (mainBase.getCurrentAnimID() != 67011) {
						mainBase.setIdleAnim(67011);
					}
					mainBase.setLocalCoords(-3.507, -0.8775, 2.595); //some coords in limgrave near first step
					mainBase.setHP(mainBase.getMaxHP());
					Sleep(2500);
					mainBase.setIdleAnim(63020);
					mainFlag.setFlagState(1024622001, 0);
					mainFunctions.removeEffect(15022, 10000);
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