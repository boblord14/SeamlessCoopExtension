# SeamlessCoopExtension

This project aims to add custom gamemodes to Elden Ring, via the existing seamless coop framework. Seamless coop is a mod which enables for players to connect and play through the entire game in functionally one sitting. As part of seamless, there is an experiemental build that increases the player cap from 5 to hundreds of players. 

The pvp in Elden Ring by default is, at it's core, not well made. This project seeks to remedy that, by adding in custom gamemodes such as capture the flag, deathmatch, defend the point, etc. All of them are custom made via souls modding tools, reverse engineering tools, and custom written dll scripts. 

The dll scripting- clion folder contains the main dll work. This is done in c++ and involves finding functions and values in memory, then calling, hooking, reading, or writing to them. Most of the heavily technical/programming/reverse engineering work can be found here. The old visual studio folder for dllscripting is outdated, it merely exists as a code repository for anything I had before I rewrote signifigant parts of the project. 

The modengine section is the mod files for soulsmodding, they go in modengine2 or the like(from mapstudio/darkscript and whatnot). Don't bother trying to open these or use them unless you're famillar with making or using souls mods. Even still, don't bother. They're useless for now. 

The Cheat Engine section is used for fully functional proof of concept scripts for the dll mod. This helps with hammering out a quick proof of concept script(for things like respawn) to test before trying to create them in the dll variant. These might not work perfectly with cheat engine, they need the TGA cheat table to work. Even then, you may need to mess with the tga ce table a bit to get the script to run but all the pieces are included in this folder. 
