//
// Created by false on 3/30/2024.
//
#include "GameFunctions.h"

#ifndef MAINCOOPEXTENSION_DAMAGEHOOK_H
#define MAINCOOPEXTENSION_DAMAGEHOOK_H
struct StaggerModule {
    uint8_t undefined[0x10];
    float stagger;
    float staggerMax;
    uint8_t undefined2[0x4];
    float resetTimer;
};

struct ChrModuleBag {
    uint8_t undefined[0x40];
    StaggerModule* staggerModule;
};

struct ChrIns {
    uint8_t undefined[0x8];
    unsigned long long handle;
    uint8_t undefined2[0x180];
    ChrModuleBag* chrModulelBag;
    uint8_t undefined3[0x508];
    unsigned long long targetHandle;
};

struct DamageStruct {
    char unk[0x228];
    int damage;
};

struct ChrDamageModule {
    char unk[0x8];
    ChrIns* playerIns;
};

typedef void AddDamage(ChrDamageModule* damageModule, ChrIns* chrIns, DamageStruct* damageStruct, unsigned long long param_4, char param_5);

class damageHook{

    static void storeLastHitByEntity(ChrDamageModule* damageModule, ChrIns* chrIns, DamageStruct* damageStruct, unsigned long long param_4, char param_5);
    static void setDamageOriginal(ChrDamageModule* damageModule, ChrIns* chrIns, DamageStruct* damageStruct, unsigned long long param_4, char param_5);public:
    static bool initalizeDmgHook();
    static AddDamage* addDamageOriginal;
};



#endif //MAINCOOPEXTENSION_DAMAGEHOOK_H
