//
// Created by false on 3/30/2024.
//
#include "GameFunctions.h"
#include "Signature.h"
#include "MinHook.h"
#include "ModUtils.h"
#include "pch.h"
#include "damageHook.h"

extern std::unique_ptr<GameFunctions> gameFunctions;

AddDamage* damageHook::addDamageOriginal = nullptr;

void damageHook::storeLastHitByEntity(ChrDamageModule* damageModule, ChrIns* chrIns, DamageStruct* damageStruct, unsigned long long param_4, char param_5) {
    std::cout << "hook function running" << std::endl;

     if (damageModule->playerIns == (gameFunctions->getChrIns(10000))) { //confirming the player is the one being attacked here
         std::cout << "player hit by enemy" << std::endl;
         if (damageStruct->damage != 0) {
             std::cout << "player damaged by enemy" << std::endl;
             std::cout << "charIns addr of the entity that just hit the player: " << std::endl;
             std::cout << std::hex<< chrIns << std::endl;
             GameFunctions::setLastHitByEntity(chrIns);
         }
     }
    damageHook::setDamageOriginal(damageModule, chrIns, damageStruct, param_4, param_5);
}

bool damageHook::initalizeDmgHook() {

    ModuleData EldenRingData("eldenring.exe");
    Signature applyDmgCall = Signature("4C 8B DC 55 53 56 57 41 56 41 57 49 8D 6B 88 48 81 EC 48 01 00 00");

    auto _addDamageAddress = (uintptr_t)applyDmgCall.Scan(&EldenRingData);
    addDamageOriginal = reinterpret_cast<AddDamage*>(reinterpret_cast<uint8_t*>(_addDamageAddress));

    if (!_addDamageAddress) {
        std::cout << "unable to find damage function address" << std::endl;
        return false;
    }

    MH_Initialize();
    MH_STATUS info = MH_CreateHook((void*)_addDamageAddress, (void*)&damageHook::storeLastHitByEntity, (void**)&addDamageOriginal);

    if (info == MH_OK) {
        MH_EnableHook((void*)_addDamageAddress);
        std::cout << "hook successful" << std::endl;
        return true;
    } else{
        std::cout << "hook failure" << std::endl;
        std::cout<< "MH status: " << MH_StatusToString(info) << std::endl;
        return false;
    }

}

void damageHook::setDamageOriginal(ChrDamageModule* damageModule, ChrIns* chrIns, DamageStruct* damageStruct, unsigned long long param_4, char param_5) {
    addDamageOriginal(damageModule, chrIns, damageStruct, param_4, param_5);
}