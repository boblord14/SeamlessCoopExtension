//
// Created by false on 4/13/2024.
//

#include <vector>
#include <random>
#include "ModFunctions.h"

/*
 * Generic logging function for kill tracking. Written in a way allowing for the actual value to be set in the function call.
 * This allows for kill counts to be negative, such as if a player dies to pve a bunch instead of actual players.
 */
void ModFunctions::register_kill(ChrIns *player, int num) {
    auto player_log = main_player_table.find(player);
    if(player_log == main_player_table.end()){
        //couldn't find player in table, log first entry of said player
        main_player_table[player] = num;
    }else{
        //player exists, update their entry
        player_log->second = (player_log->second+num);
    }
}

/*
 * Wipes the kill tally clean.
 */
void ModFunctions::wipe_kill_data(){
    main_player_table.clear();
}

/*
 * Returns the ChrIns addr of the player with the highest kill count, along with the actual value.
 *
 * In the case of a tie, the winner is picked randomly from any of the players with the highest score.
 */
std::pair<ChrIns*, int>  ModFunctions::get_best_player(){
    auto best_player = main_player_table.begin();
    bool tie_flag = false;

    for(auto i = main_player_table.begin(); i != main_player_table.end(); i++){
        if(i->second > best_player->second){
            best_player = i;
            tie_flag = false;
        } else if(i->second == best_player->second){
            tie_flag = true;
        }
    }

    std::pair<ChrIns*, int> winner_info;
    winner_info.second = best_player->second;

    if(!tie_flag){
        winner_info.first = best_player->first;
    }else{

        //in the case that 2 players have the same high score, create a list of all players with the high score and pick one randomly
        std::vector<ChrIns*> tied_players;
        for(auto i = main_player_table.begin(); i != main_player_table.end(); i++){
            if(i->second == best_player->second){
                tied_players.push_back(i->first);
            }
        }

        //"statistically superior" random method according to somebody on stackexchange
        std::random_device rd;
        std::mt19937 eng(rd());
        std::uniform_int_distribution<> distr(0, (int)tied_players.size() - 1);

        winner_info.first = tied_players.at(distr(eng));
    }
    return winner_info;
}