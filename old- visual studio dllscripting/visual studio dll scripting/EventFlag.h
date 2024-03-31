#ifndef _EVENT_FLAG_H_
#define _EVENT_FLAG_H_
#include "PointerChain.h"
#include "WorldChrMan.h"

using FnSetEventFlag = void (*)(const uint64_t event_man, uint32_t* event_id, bool state);
using FnGetEventFlag = int (*)(void* manager, int flagID);



class EventFlag
{

private:
	uint32_t id;
	
	static void** eventFlagManager;


public:
	EventFlag(uint32_t id);
	bool getFlagState();
	void setFlagState(bool state);
};
#endif // _EVENT_FLAG_H_