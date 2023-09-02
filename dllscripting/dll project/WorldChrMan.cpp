#include "WorldChrMan.h"
#include "Signature.h"


void** InitHelper() {
    ModuleData EldenRingData("eldenring.exe");
    Signature worldChrManSig = Signature("48 8B 05 ?? ?? ?? ?? 48 85 C0 74 0F 48 39 88");
    void** WorldChrManIns = (void**)worldChrManSig.Scan(&EldenRingData, 0x3, 0x7);
    return WorldChrManIns;
}

WorldChrMan::WorldChrMan(void** add) : Address((void*)*(uintptr_t*)add),
php(*(uintptr_t*)add, 0x10EF8, 0, 0x190u, 0, 0x138), 
pmhp(*(uintptr_t*)add, 0x10EF8, 0, 0x190u, 0, 0x13C), 
ianim(*(uintptr_t*)add, 0x10EF8, 0, 0x190u, 0x58, 0x18), 
canim(*(uintptr_t*)add, 0x10EF8, 0, 0x190u, 0x58, 0x20), 
lxcoord(*(uintptr_t*)add, 0x10EF8, 0, 0x190u, 0x68, 0x70), 
lycoord(*(uintptr_t*)add, 0x10EF8, 0, 0x190u, 0x68, 0x78), 
lzcoord(*(uintptr_t*)add, 0x10EF8, 0, 0x190u, 0x68, 0x74) {
}

bool WorldChrMan::isLoaded() {
    if (address) {
        return true;
    }
    else {
        return false;
    }
}

WorldChrMan WorldChrMan::Make() {
    void** WorldChrManIns = InitHelper();
    return WorldChrMan(WorldChrManIns);
}

int WorldChrMan::getHP() {
    if (address) {
        return *php;
    }
    return -1;
}

void WorldChrMan::setHP(int hp) {
    if (address) {
        *php = hp;
    }
}

int WorldChrMan::getMaxHP() {
    if (address) {
        return *pmhp;
    }
    return -1;
}

void WorldChrMan::setIdleAnim(int idleAnimId) {
    if (address) {
        *ianim = idleAnimId;
    }
}

int WorldChrMan::getCurrentAnimID() {
    if (address) {
        return *canim;
    }
    return -1;
}

void WorldChrMan::setLocalCoords(float x, float y, float z) {
    if (address) {
        if (x != NULL) {
            *lxcoord = x;
        }
        if (y != NULL) {
            *lycoord = y;
        }
        if (z != NULL) {
            *lzcoord = z;
        }
    }
}