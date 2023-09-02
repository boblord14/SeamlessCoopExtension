#ifndef _GAME_FUNCTIONS_H_
#define _GAME_FUNCTIONS_H_
#include "PointerChain.h"
#include "WorldChrMan.h"

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

using FnApplyEffect = void (*)(void* ChrIns, int spEffectId);
using FnRemoveEffect = void (*)(void* CSSpecialEffect, int spEffectId);
using FnEntityToChrIns = ChrIns * (*)(int* entityId);

class GameFunctions : public Address
{
private:
	FnApplyEffect applyEffectChrIns;
	FnRemoveEffect removeEffectChrIns;
	FnEntityToChrIns getChrInsFromEntityId;
	GameFunctions(void** eventFlagMan, void** setAddr, void** getAddr, void** worldChrMan);

public:
	static GameFunctions Make();
	void applyEffect(int spEffectId, int entityID);
	void removeEffect(int spEffectId, int entityID);
};
#endif // _GAME_FUNCTIONS_H_