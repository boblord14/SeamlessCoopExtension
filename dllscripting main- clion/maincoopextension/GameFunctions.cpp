 #include "GameFunctions.h"
#include "Signature.h"
#include "MinHook.h"
#include "ModUtils.h"
#include "pch.h"

GameFunctions::GameFunctions(void** applySpE, void** removeSpE, void** eIDtocID, void** wChrMan) : Address((void*)*(uintptr_t*)wChrMan) {
    applyEffectChrIns = reinterpret_cast<FnApplyEffect>(reinterpret_cast<uint8_t*>(applySpE));
    removeEffectChrIns = reinterpret_cast<FnRemoveEffect>(reinterpret_cast<uint8_t*>(removeSpE));
    getChrInsFromEntityId = reinterpret_cast<FnEntityToChrIns>(reinterpret_cast<uint8_t*>(eIDtocID));
}

std::unique_ptr<GameFunctions> GameFunctions::Make() {

    ModuleData EldenRingData("eldenring.exe");
    Signature spEffectApplyCall = Signature("48 8B C4 48 89 58 08 48 89 70 10 57 48 81 EC ?? ?? ?? ?? 0F 28 05 ?? ?? ?? ?? 48 8B F1 0F 28 0D ?? ?? ?? ?? 48 8D 48 88");
    Signature spEffectRemoveCall = Signature("48 83 EC 28 8B C2 48 8B 51 08 48 85 D2 ?? ?? 90");
    Signature entityIdtoChrInsCall = Signature("48 89 5c 24 08 48 89 74 24 10 48 89 7c 24 18 41 56 48 83 ec ?? 48 8b 3d ?? ?? ?? ?? 33 db 49 8b f0 4c 8b f1 48 85 ff");
    Signature worldChrManSig = Signature("48 8B 05 ?? ?? ?? ?? 48 85 C0 74 0F 48 39 88");

    void** WorldChrManIns = (void**)worldChrManSig.Scan(&EldenRingData, 0x3, 0x7);
    void** speApplyCallIns = (void**)spEffectApplyCall.Scan(&EldenRingData);
    void** speRemoveCallIns = (void**)spEffectRemoveCall.Scan(&EldenRingData);
    void** entityIdtoChrInsIns = (void**)entityIdtoChrInsCall.Scan(&EldenRingData);

    while((void*)*(uintptr_t*)WorldChrManIns == nullptr){}
    std::cout << "gamefunctions fully initialized" << std::endl;

    return std::unique_ptr<GameFunctions>(new GameFunctions(speApplyCallIns, speRemoveCallIns, entityIdtoChrInsIns, WorldChrManIns));
}

void GameFunctions::applyEffect(int spEffectId, int entityID)
{
    if (address) {
        applyEffectChrIns(getChrIns(entityID), spEffectId);
    }
}
 void GameFunctions::applyEffect(int spEffectId, ChrIns* ChrIns)
 {
     if (address) {
         applyEffectChrIns(ChrIns, spEffectId);
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

 void GameFunctions::removeEffect(int spEffectId, ChrIns* ChrIns)
 {
     if (address) {
         auto CSSpecialEffect = PointerChain::make<void*>(ChrIns, 0x178);
         removeEffectChrIns(*CSSpecialEffect, spEffectId);
     }
 }

ChrIns* GameFunctions::getChrIns(int entityID) {
    if (address) {
        return getChrInsFromEntityId(&entityID);
    }
    return nullptr;
}

void GameFunctions::setLastHitByEntity(ChrIns* data) {
    lastEntityHitBy = data;
}

ChrIns* GameFunctions::getLastHitByEntity() {
    return lastEntityHitBy;
}

bool GameFunctions::enableDamageHooking(){
    return damageHook::initalizeDmgHook();
}

