#ifndef _GAME_FUNCTIONS_H_
#define _GAME_FUNCTIONS_H_
#include "PointerChain.h"
#include "WorldChrMan.h"
#include "damageHook.h"
#include <memory>

using FnApplyEffect = void (*)(void* ChrIns, int spEffectId);
using FnRemoveEffect = void (*)(void* CSSpecialEffect, int spEffectId);
using FnEntityToChrIns = ChrIns * (*)(int* entityId);
static ChrIns* lastEntityHitBy;

class GameFunctions : public Address
{

private:
	FnApplyEffect applyEffectChrIns;
	FnRemoveEffect removeEffectChrIns;
	FnEntityToChrIns getChrInsFromEntityId;

	GameFunctions(void** eventFlagMan, void** setAddr, void** getAddr, void** worldChrMan);

public:

	static std::unique_ptr<GameFunctions> Make();
	void applyEffect(int spEffectId, int entityID);
    void applyEffect(int spEffectId, ChrIns* ChrIns);
	void removeEffect(int spEffectId, int entityID);
    void removeEffect(int spEffectId, ChrIns* ChrIns);
	ChrIns* getChrIns(int entityID);
	static ChrIns* getLastHitByEntity();
	static void setLastHitByEntity(ChrIns* data);
    bool enableDamageHooking();

};
static GameFunctions mainFunctions();
#endif // _GAME_FUNCTIONS_H_