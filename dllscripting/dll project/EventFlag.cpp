#include "EventFlag.h"
#include "Signature.h"

EventFlag::EventFlag(void** eventFlagMan, void** setAddr, void** getAddr) : Address((void*)*(uintptr_t*)eventFlagMan) {
    setEventFlag = reinterpret_cast<FnSetEventFlag>(reinterpret_cast<uint8_t*>(setAddr));
    getEventFlag = reinterpret_cast<FnGetEventFlag>(reinterpret_cast<uint8_t*>(getAddr));
    eventFlagManager = eventFlagMan;
}

EventFlag EventFlag::Make() {
    ModuleData EldenRingData("eldenring.exe");
    Signature eventFlagManager = Signature("48 8B 3D ?? ?? ?? ?? 48 85 FF ?? ?? 32 C0 E9");
    Signature eventFlagSetCall = Signature("?? ?? ?? ?? ?? 48 89 74 24 18 57 48 83 EC 30 48 8B DA 41 0F B6 F8 8B 12 48 8B F1 85 D2 0F 84 ?? ?? ?? ?? 45 84 C0");
    Signature eventFlagGetCall = Signature("44 8B 41 ?? 44 8B DA 33 D2 41 8B C3 41 F7 F0");
    void** eventFlagMan = (void**)eventFlagManager.Scan(&EldenRingData, 0x3, 0x7);
    void** eventSetIns = (void**)eventFlagSetCall.Scan(&EldenRingData);
    void** eventGetIns = (void**)eventFlagGetCall.Scan(&EldenRingData);
    return EventFlag(eventFlagMan, eventSetIns, eventGetIns);
}

bool EventFlag::getFlagState(int flagID) {
    if (address) {
        return getEventFlag(*eventFlagManager, flagID);
    }
    return -1;
}

void EventFlag::setFlagState(int flagID, bool state) {
    uint32_t castFlag = flagID;
    if (address) {
        setEventFlag((uint64_t)*eventFlagManager, &castFlag, 1);
    }
}