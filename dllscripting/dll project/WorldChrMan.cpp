#include "WorldChrMan.h"
#include "PointerChain.h"
#include "Signature.h"
#include "ModUtils.h"
#include "stdint.h"

void** WorldChrManAddr;
static uintptr_t WorldChrManVal;
uintptr_t p = NULL;
using hp_pointer = decltype(PointerChain::make<int>(p, 0x10EF8, 0, 0x190u, 0, 0x138));
hp_pointer playerHP;

WorldChrMan::WorldChrMan()
{
	WorldChrManAddr = getWorldChrMan();

}

void** WorldChrMan::getWorldChrMan() {
	ModuleData EldenRingData("eldenring.exe");
	Signature worldChrManSig = Signature("48 8B 05 ?? ?? ?? ?? 48 85 C0 74 0F 48 39 88");

	// This pointer when derefenced and at a character is where the stuff begins.
	return (void**)worldChrManSig.Scan(&EldenRingData, 0x3, 0x7);
}

bool WorldChrMan::validateAobUsage()
{
	WorldChrManVal = *(uintptr_t*)WorldChrManAddr;
	if (WorldChrManVal) {
		return true;
	}
	else {
		return false;
	}
}

bool WorldChrMan::loadMainAobs()
{
	if (validateAobUsage()) {
		playerHP = PointerChain::make<int>(WorldChrManVal, 0x10EF8, 0, 0x190u, 0, 0x138);
		return true;
	}
	else return false;
}

int WorldChrMan::getHP()
{
	if (validateAobUsage()) {
		return *playerHP;
	}
	else return -1;
}

int WorldChrMan::setHP(int value)
{
	if (validateAobUsage()) {
		*playerHP = value;
		return 0;
	}
	else return -1;
}


