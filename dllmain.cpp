#include <Windows.h>

#include "ModUtils.h"
#include "Signature.h"
#include "PointerChain.h"

using namespace ModUtils;


DWORD WINAPI MainThread(LPVOID lpParam)
{
	Log("Activating DisableRuneLoss...");
	std::string aob = "b0 01 ? 8b ? e8 ? ? ? ? ? 8b ? ? ? 32 c0 ? 83 ? 28 c3";
	std::string expectedBytes = "e8";
	std::string newBytes = "90 90 90 90 90";
	uintptr_t patchAddress = AobScan(aob);
	size_t offset = 5;
	if (patchAddress != 0)
	{
		patchAddress += offset;
		ReplaceExpectedBytesAtAddress(patchAddress, expectedBytes, newBytes);
	}
	ModuleData EldenRingData("eldenring.exe");
	Signature worldChrManSig = Signature("48 8B 05 ?? ?? ?? ?? 48 85 C0 74 0F 48 39 88");
	Signature eventFlagSetCall = Signature("48 89 5C 24 ?? 44 8B 49 ?? 44 8B D2 33 D2 41 8B C2 41 F7 F1");
	Signature spEffectApplyCall = Signature("48 8B C4 48 89 58 08 48 89 70 10 57 48 81 EC ?? ?? ?? ?? 0F 28 05 ?? ?? ?? ?? 48 8B F1 0F 28 0D ?? ?? ?? ?? 48 8D 48 88");
	Signature spEffectRemoveCall = Signature("48 83 EC 28 8B C2 48 8B 51 08 48 85 D2 ?? ?? 90");

	// This pointer when derefenced and at a character is where the stuff begins.
	void** WorldChrManIns = (void**)worldChrManSig.Scan(&EldenRingData, 0x3, 0x7);
	uintptr_t speApplyCallIns = *(uintptr_t *)spEffectApplyCall.Scan(&EldenRingData);//unsure if this type is right. probably not but its not like i can test it rn


	Log("WorldChrManIns");
	Log(WorldChrManIns);
	Log(*(uintptr_t*)WorldChrManIns);
	
	AllocConsole();
	FILE* f;
	freopen_s(&f, "CONOUT$", "w", stdout);
	std::cout << "Open" << std::endl;
	bool NoDead = false;
	float defaultXCoord = (-3.507208586);
	float defaultYCoord = (-0.8775705099);
	float defaultZCoord = (2.595876455);

	while (true) {
		uintptr_t WorldChrMan;
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


		if (NoDead == true) {
			WorldChrMan = *(uintptr_t*)WorldChrManIns;
			if (WorldChrMan) {
				auto playerHP = PointerChain::make<int>(*(uintptr_t*)WorldChrManIns, 0x10EF8, 0, 0x190u, 0, 0x138);
				if (*playerHP < 1) {
					Log("triggered");
					auto idleAnim = PointerChain::make<int>(*(uintptr_t*)WorldChrManIns, 0x10EF8, 0, 0x190u, 0x58, 0x18);
					auto currentAnim = PointerChain::make<int>(*(uintptr_t*)WorldChrManIns, 0x10EF8, 0, 0x190u, 0x58, 0x20);
					auto pMaxHP = PointerChain::make<int>(*(uintptr_t*)WorldChrManIns, 0x10EF8, 0, 0x190u, 0, 0x13C);
					auto xCoord = PointerChain::make<float>(*(uintptr_t*)WorldChrManIns, 0x10EF8, 0, 0x190u, 0x68, 0x70);
					auto yCoord = PointerChain::make<float>(*(uintptr_t*)WorldChrManIns, 0x10EF8, 0, 0x190u, 0x68, 0x78);
					auto zCoord = PointerChain::make<float>(*(uintptr_t*)WorldChrManIns, 0x10EF8, 0, 0x190u, 0x68, 0x74);
					*playerHP = 1;
					Sleep(1000);
					//set flag 1024622001 to 1
					//apply effect 7202001
					Sleep(2500);
					if (*currentAnim != 67011) {
						*idleAnim = 67011;
					}
					*xCoord = defaultXCoord;
					*yCoord = defaultYCoord;
					*zCoord = defaultZCoord;
					*playerHP = *pMaxHP;
					Sleep(3500);
					*idleAnim = 63020;
					//set flag 1024622001 to 0
					//remove effect 7202001
				}
			}
			else {
				std::cout << "Currently nullptr, turning off" << std::endl;
				NoDead = false;
			}

		}



	}
	//FreeConsole();
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