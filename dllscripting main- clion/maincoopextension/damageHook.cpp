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

//check where in the damage this is
//does this occur before or after the actual player's hp changes?
//TODO: check via comparing the player's hp at the moment this script runs- is this the player hp pre or post damage calculation
void damageHook::storeLastHitByEntity(ChrDamageModule* damageModule, ChrIns* chrIns, DamageStruct* damageStruct, unsigned long long param_4, char param_5) {
    std::cout << "hook function running" << std::endl;

     if (damageModule->playerIns == (gameFunctions->getChrIns(10000))) { //confirming the player is the one being attacked here
         if (damageStruct->damage != 0) {
             std::cout << "player damaged by enemy, chrIns addr " << std::hex<< chrIns << std::endl;
             damageHook::setLastHitByEntity(chrIns);
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

//TODO: use a map and track for every player in lobby, not just the player character
//update the modfunctions attribution stuff accordingly
//log this somewhere as well.
void damageHook::setLastHitByEntity(ChrIns* data) {
    lastEntityHitBy = data;
}

ChrIns* damageHook::getLastHitByEntity() {
    return lastEntityHitBy;
}