//
// Created by false on 4/13/2024.
//

#ifndef MAINCOOPEXTENSION_MODFUNCTIONS_H
#define MAINCOOPEXTENSION_MODFUNCTIONS_H

#include <map>
#include "GameFunctions.h"

//change this to an unordered map
static std::map<ChrIns*, int> main_player_table;
class ModFunctions{


public:
    static void register_kill(ChrIns* player, int num);
    static void wipe_kill_data();
    static std::pair<ChrIns*, int> get_best_player();
};


#endif //MAINCOOPEXTENSION_MODFUNCTIONS_H
