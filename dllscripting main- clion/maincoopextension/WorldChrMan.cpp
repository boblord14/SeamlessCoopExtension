#include "WorldChrMan.h"
#include "Signature.h"
#include "pch.h"


static void** WorldChrManIns;
static void** GameManIns;

//TODO: refactor GameMan's impl here
void** InitHelper() {
    ModuleData EldenRingData("eldenring.exe");
    Signature worldChrManSig = Signature("48 8B 05 ?? ?? ?? ?? 48 85 C0 74 0F 48 39 88");
    WorldChrManIns = (void**)worldChrManSig.Scan(&EldenRingData, 0x3, 0x7);

    Signature gameManSig = Signature("48 8B 05 ?? ?? ?? ?? 80 B8 ?? ?? ?? ?? 0D 0F 94 C0 C3");
    GameManIns = (void**)gameManSig.Scan(&EldenRingData, 0x3, 0x7);

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
    WorldChrManIns = InitHelper();
    if(*WorldChrManIns != NULL)
        return WorldChrMan(WorldChrManIns);
    else return nullptr;
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

int WorldChrMan::getCurrentAnimIdForOtherPlayer(int playerSlot) {
    int64_t playerOffset = 0x10 * playerSlot;
    int animId = *PointerChain::make<int>(WorldChrManIns, 0x10EF8, playerOffset, 0x190, 0x18, 0x20);
    return animId; 
}


int WorldChrMan::getPlayerSlotFromChrIns(ChrIns *chrIns) {

    for(int i = 0; i<getPlayerCount(); i++){
       ChrIns* arrayChrIns = PointerChain::make<PlayerStruct>(WorldChrManIns, 0x10EF8, i)->playerIns;
       if(arrayChrIns == chrIns) return i;
    }
    return -1;
}

/*
 * Least significant bit(pos 0) is on the right here.
 * Simple flag checker
 */
bool WorldChrMan::readBitFlag(int value, int pos){
    int mask = (1 << pos);
    return ((value & mask) != 0);
}

bool WorldChrMan::isInIframes(int playerSlot){
    int64_t playerOffset = 0x10 * playerSlot;
    int flagData = PointerChain::make<int>(WorldChrManIns, 0x10EF8, playerOffset, 0x190, 0x8, 0x40);
    return readBitFlag(flagData, 1);
}


//try [[GameMan]+D60]+14(or +1C) as a total player in session value
//horribly hacky and unclean temp solution(not even a worldchrman aob)
int WorldChrMan::getPlayerCount(){
    int playerCount = PointerChain::make<int>(GameManIns, 0xD60, 0x1C);//either 0x1C or 0x14 here. Unsure which
    return playerCount;
}

