#include <windows.h>

#include "pch.h"
#include "Signature.h"
#include "ModUtils.h"
#include "MinHook.h"
#include "GameFunctions.h"
#include <iostream>
#include <fstream>
#include "ModFunctions.h"

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
    std::cout << "CURRENT FUNCTIONS" << std::endl;
    std::cout << "_________________" << std::endl;
    std::cout << "f11- printline test" << std::endl;
    std::cout << "f10- enable damage hook" << std::endl;
    std::cout << "f9- get player chrins address from gamefunctions" << std::endl;
    std::cout << "f8- apply speffect to entity that last hit player(requires damagehook)" << std::endl;
    std::cout << "f7- add entity who last hit the player to the tracking board(requires damagehook)" << std::endl;
    std::cout << "f6- print out the entity with the most \"kills\" on the tracking board(requires damagehook)" << std::endl;

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
        }else if (GetAsyncKeyState(VK_F8) & 1) {
            std::cout << "chrins addr of entity who last hit player: " << std::hex << damageHook::getLastHitByEntity() << std::dec << std::endl;
            std::cout << "applying speffect to entity" << std::endl;
            gameFunctions->applyEffect(1790300, damageHook::getLastHitByEntity());
        }else if(GetAsyncKeyState(VK_F7) & 1){
            std::cout << "adding entity who last hit to tally board" << std::endl;
            ModFunctions::register_kill(damageHook::getLastHitByEntity(), 1);
        }else if(GetAsyncKeyState(VK_F6) & 1){
            auto kill_results = ModFunctions::get_best_player();
            std::cout << "entity who hit the player the most times:" << std::endl;
            std::cout << "chrins addr-" << std::hex << kill_results.first << std::endl;
            std::cout << "hit count- " << kill_results.second << std::endl;
        }
	}
	myfile.close();
	return 0;
}
//TODO: build this logic back in and the false death functionality
//full while loop- if host
//wait for someone's hp to hit 0, do nothing otherwise
//then break and do kill attribution
//then check your own hp and do the respawn
/* old nodead code, port this in.
 *
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