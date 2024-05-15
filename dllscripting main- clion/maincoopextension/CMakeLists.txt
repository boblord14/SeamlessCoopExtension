cmake_minimum_required(VERSION 3.27)
project(maincoopextension)

set(CMAKE_CXX_STANDARD 17)


add_library(maincoopextension SHARED dllmain.cpp
        dllmain.cpp
        framework.h
        GameFunctions.cpp
        GameFunctions.h
        ini.h
        MinHook.h
        ModUtils.h
        pch.cpp
        pch.h
        PointerChain.h
        Signature.cpp
        Signature.h
        WorldChrMan.cpp
        WorldChrMan.h
        damageHook.cpp
        damageHook.h
        ModFunctions.cpp
        ModFunctions.h
        EventFlag.cpp
        EventFlag.cpp
)
target_link_libraries(maincoopextension ${CMAKE_CURRENT_SOURCE_DIR}/MinHook.x64.lib)

