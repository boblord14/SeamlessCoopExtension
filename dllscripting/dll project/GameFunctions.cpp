#include "GameFunctions.h"
#include "Signature.h"
#include "MinHook.h"

static ChrIns* lastEntityHitBy;
AddDamage* addDamageOriginal = nullptr;

GameFunctions::GameFunctions(void** applySpE, void** removeSpE, void** eIDtocID, void** wChrMan) : Address((void*)*(uintptr_t*)wChrMan) {
    applyEffectChrIns = reinterpret_cast<FnApplyEffect>(reinterpret_cast<uint8_t*>(applySpE));
    removeEffectChrIns = reinterpret_cast<FnRemoveEffect>(reinterpret_cast<uint8_t*>(removeSpE));
    getChrInsFromEntityId = reinterpret_cast<FnEntityToChrIns>(reinterpret_cast<uint8_t*>(eIDtocID));
}

GameFunctions GameFunctions::Make() {

    ModuleData EldenRingData("eldenring.exe");
    Signature spEffectApplyCall = Signature("48 8B C4 48 89 58 08 48 89 70 10 57 48 81 EC ?? ?? ?? ?? 0F 28 05 ?? ?? ?? ?? 48 8B F1 0F 28 0D ?? ?? ?? ?? 48 8D 48 88");
    Signature spEffectRemoveCall = Signature("48 83 EC 28 8B C2 48 8B 51 08 48 85 D2 ?? ?? 90");
    Signature entityIdtoChrInsCall = Signature("48 89 5c 24 08 48 89 74 24 10 48 89 7c 24 18 41 56 48 83 ec ?? 48 8b 3d ?? ?? ?? ?? 33 db 49 8b f0 4c 8b f1 48 85 ff");
    Signature worldChrManSig = Signature("48 8B 05 ?? ?? ?? ?? 48 85 C0 74 0F 48 39 88");

    void** WorldChrManIns = (void**)worldChrManSig.Scan(&EldenRingData, 0x3, 0x7);
    void** speApplyCallIns = (void**)spEffectApplyCall.Scan(&EldenRingData);
    void** speRemoveCallIns = (void**)spEffectRemoveCall.Scan(&EldenRingData);
    void** entityIdtoChrInsIns = (void**)entityIdtoChrInsCall.Scan(&EldenRingData);
    return GameFunctions(speApplyCallIns, speRemoveCallIns, entityIdtoChrInsIns, WorldChrManIns);
}

void GameFunctions::applyEffect(int spEffectId, int entityID)
{
    if (address) {
        applyEffectChrIns(getChrIns(entityID), spEffectId);
    }
}

void GameFunctions::removeEffect(int spEffectId, int entityID)
{
    if (address) {
        ChrIns* entity = getChrIns(entityID);
        auto CSSpecialEffect = PointerChain::make<void*>(entity, 0x178);
        removeEffectChrIns(*CSSpecialEffect, spEffectId);
    }
}

ChrIns* GameFunctions::getChrIns(int entityID) {
    if (address) {
        return getChrInsFromEntityId(&entityID);
    }
    return NULL;
}

void GameFunctions::storeLastHitByEntity(ChrDamageModule* damageModule, ChrIns* chrIns, DamageStruct* damageStruct, unsigned long long param_4, char param_5) {

    GameFunctions tempFunctions = GameFunctions::Make();

    if (damageModule->playerIns == (tempFunctions.getChrIns(10000))) { //confirming the player is the one being attacked here
        if (damageStruct->damage != 0) {
            lastEntityHitBy = chrIns;
        }
    }
    addDamageOriginal(damageModule, chrIns, damageStruct, param_4, param_5);
}

ChrIns* GameFunctions::getLastHitByEntity() {
    return lastEntityHitBy;
}
bool GameFunctions::initalizeDmgHook() {

    uintptr_t _addDamageAddress = 0;

    ModuleData EldenRingData("eldenring.exe");
    Signature applyDmgCall = Signature("4C 8B DC 55 53 56 57 41 56 41 57 49 8D 6B 88 48 81 EC 48 01 00 00");

    _addDamageAddress = (uintptr_t)applyDmgCall.Scan(&EldenRingData);

    if (!_addDamageAddress) {
        return false;
    }

    if (MH_CreateHook((void*)_addDamageAddress, (void*)&GameFunctions::storeLastHitByEntity, (void**)&addDamageOriginal) == MH_OK) {
        MH_EnableHook((void*)_addDamageAddress);
        return true;
    }

    return false;
}