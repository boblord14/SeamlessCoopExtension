#include "EventFlag.h"
#include "Signature.h"

ModuleData EldenRingData("eldenring.exe");
Signature eventFlagManager = Signature("48 8B 3D ?? ?? ?? ?? 48 85 FF ?? ?? 32 C0 E9");
Signature eventFlagSetCall = Signature("?? ?? ?? ?? ?? 48 89 74 24 18 57 48 83 EC 30 48 8B DA 41 0F B6 F8 8B 12 48 8B F1 85 D2 0F 84 ?? ?? ?? ?? 45 84 C0");
Signature eventFlagGetCall = Signature("44 8B 41 ?? 44 8B DA 33 D2 41 8B C3 41 F7 F0");

void** eventFlagMan = (void**)eventFlagManager.Scan(&EldenRingData, 0x3, 0x7);
void** eventSetIns = (void**)eventFlagSetCall.Scan(&EldenRingData);
void** eventGetIns = (void**)eventFlagGetCall.Scan(&EldenRingData);

void** EventFlag::eventFlagManager = eventFlagMan;
FnSetEventFlag setEventFlag = reinterpret_cast<FnSetEventFlag>(reinterpret_cast<uint8_t*>(eventSetIns));
FnGetEventFlag getEventFlag = reinterpret_cast<FnGetEventFlag>(reinterpret_cast<uint8_t*>(eventGetIns));

EventFlag::EventFlag(uint32_t id) {
    
 this->id = id;

}

bool EventFlag::getFlagState() {
    if (eventFlagManager) {
        return getEventFlag(*eventFlagManager, (int)id);
    }
    return NULL;
}

void EventFlag::setFlagState(bool state) {
    if (eventFlagManager) {
        setEventFlag((uint64_t)*eventFlagManager, &id, state);
    }
}