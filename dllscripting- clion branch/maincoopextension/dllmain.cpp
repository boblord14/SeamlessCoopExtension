#include <windows.h>

#include "pch.h"
#include "Signature.h"
#include "ModUtils.h"
#include "MinHook.h"
#include "GameFunctions.h"
#include <iostream>
#include <fstream>

using namespace ModUtils;

std::unique_ptr<GameFunctions> gameFunctions = nullptr;

DWORD WINAPI MainThread(LPVOID lpParam)
{

	AllocConsole();
	std::ofstream myfile;
	myfile.open(R"(C:\Users\false\Desktop\templog.txt)");
    myfile << "loaded \n" << std::endl;
    FILE* f;
    freopen_s(&f, "CONOUT$", "w", stdout);
    std::cout << "Open" << std::endl;

    gameFunctions = GameFunctions::Make();


	while (true) {
		if (GetAsyncKeyState(VK_F11) & 1) {
            myfile << "test works \n" << std::endl;
            std::cout << "test printout" << std::endl;
		}else if (GetAsyncKeyState(VK_F10) & 1) {
            myfile << "starting hook \n" << std::endl;
            std::cout << "hooking" << std::endl;

            if(gameFunctions->enableDamageHooking()){
                std::cout << "hook returned true" << std::endl;
            }
		}else if (GetAsyncKeyState(VK_F9) & 1) {
            std::cout << "player chrins addr via dllmain gamefunctions: " << std::hex << gameFunctions->getChrIns(10000) << std::dec << std::endl;
        }
	}
	myfile.close();
	return 0;
}

/* old nodead code, port this in when able. 
 * if (NoDead == true) {
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
 */

BOOL WINAPI DllMain(HINSTANCE module, DWORD reason, LPVOID)
{
	if (reason == DLL_PROCESS_ATTACH)
	{
		DisableThreadLibraryCalls(module);
		CreateThread(0, 0, &MainThread, 0, 0, NULL);
	}
	return 1;
}