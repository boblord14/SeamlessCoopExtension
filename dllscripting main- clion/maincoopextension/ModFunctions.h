//
// Created by false on 4/13/2024.
//

#ifndef MAINCOOPEXTENSION_MODFUNCTIONS_H
#define MAINCOOPEXTENSION_MODFUNCTIONS_H

#include <unordered_map>
#include "GameFunctions.h"
#include "EventFlag.h"
#include <windows.h>

static std::unordered_map<ChrIns*, int> main_player_table;
class ModFunctions{


public:
    static void register_kill(ChrIns* player, int num);
    static void wipe_kill_data();
    static std::pair<ChrIns*, int> get_best_player();
    static void respawn_player(WorldChrMan* mainBase);

};


#endif //MAINCOOPEXTENSION_MODFUNCTIONS_H
