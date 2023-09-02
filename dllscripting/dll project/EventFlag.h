#ifndef _EVENT_FLAG_H_
#define _EVENT_FLAG_H_
#include "PointerChain.h"
#include "WorldChrMan.h"

using FnSetEventFlag = void (*)(const uint64_t event_man, uint32_t* event_id, bool state);
using FnGetEventFlag = int (*)(void* manager, int flagID);



class EventFlag : public Address
{
private:
	FnGetEventFlag getEventFlag;
	FnSetEventFlag setEventFlag;
	EventFlag(void** eventFlagMan, void** setAddr, void** getAddr);
	static void** eventFlagManager;

public:
	static EventFlag Make();
	bool getFlagState(int flag);
	void setFlagState(int flag, bool state);
};
#endif // _EVENT_FLAG_H_