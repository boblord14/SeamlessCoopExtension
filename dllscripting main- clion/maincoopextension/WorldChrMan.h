#ifndef _WORLD_CHR_MAN_H_
#define _WORLD_CHR_MAN_H_

#include "PointerChain.h"
#include "damageHook.h"

struct PlayerStruct {
    ChrIns* playerIns;
    char unk[0x8];
};


using PlayerHpPointer = decltype(PointerChain::make<int>(uintptr_t(), 0x10EF8, 0, 0x190u, 0, 0x138));
using PlayerMaxHpPointer = decltype(PointerChain::make<int>(uintptr_t(), 0x10EF8, 0, 0x190u, 0, 0x13C));
using PlayerIdleAnimation = decltype(PointerChain::make<int>(uintptr_t(), 0x10EF8, 0, 0x190u, 0x58, 0x18));
using PlayerCurrentAnimation = decltype(PointerChain::make<int>(uintptr_t(), 0x10EF8, 0, 0x190u, 0x58, 0x20));
using PlayerLocalXCoord = decltype(PointerChain::make<float>(uintptr_t(), 0x10EF8, 0, 0x190u, 0x68, 0x70));
using PlayerLocalYCoord = decltype(PointerChain::make<float>(uintptr_t(), 0x10EF8, 0, 0x190u, 0x68, 0x78));
using PlayerLocalZCoord = decltype(PointerChain::make<float>(uintptr_t(), 0x10EF8, 0, 0x190u, 0x68, 0x74));

class Address {
protected:
    void* address;
public:
    Address(void* address) :address(address) {};
    void* GetAddress() {
        return address;
    }
};

class WorldChrMan : public Address
{
private:
    PlayerHpPointer php;
    PlayerMaxHpPointer pmhp;
    PlayerIdleAnimation ianim;
    PlayerCurrentAnimation canim;
    PlayerLocalXCoord lxcoord;
    PlayerLocalYCoord lycoord;
    PlayerLocalZCoord lzcoord;
    WorldChrMan(void** address);
    static bool readBitFlag(int value, int pos);

public:
    static WorldChrMan Make();
    bool isLoaded();
    int getHP();
    void setHP(int hp);
    int getMaxHP();
    void setIdleAnim(int idleAnimId);
    int getCurrentAnimID();
    void setLocalCoords(float x, float y, float z);
    int getCurrentAnimIdForOtherPlayer(int playerSlot);
    static int getPlayerSlotFromChrIns(ChrIns* chrIns);
    bool isInIframes(int playerSlot);
};
#endif // _WORLD_CHR_MAN_H_