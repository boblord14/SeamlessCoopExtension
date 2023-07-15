# -*- coding: utf-8 -*-
def t610006000_1():
    """State 0,1"""
    t610006000_x1()
    Quit()

def t610006000_x0(actionbutton3=_, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag1) == 1 or GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1 or GetEventFlag(flag4)
                == 1 or GetEventFlag(flag5) == 1)
        """State 4"""
        assert not GetEventFlag(flag6)
        """State 2"""
        if GetEventFlag(flag6) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag1) and not GetEventFlag(flag2) and not GetEventFlag(flag3) and not
              GetEventFlag(flag4) and not GetEventFlag(flag5)):
            pass
        elif CheckActionButtonArea(actionbutton3):
            break
    """State 5"""
    return 0

def t610006000_x1():
    """State 0"""
    while True:
        """State 1"""
        call = t610006000_x2()
        assert IsClientPlayer() == 1 or GetEventFlag(1049532710) == 1
        """State 2"""
        call = t610006000_x3()
        assert not IsClientPlayer() and not GetEventFlag(1049532710)
    """Unused"""
    """State 3"""
    return 0

def t610006000_x2():
    """State 0,1"""
    Label('L0')
    # goods:8107:Rold Medallion
    if ComparePlayerInventoryNumber(3, 8107, 4, 1, 0) == 1:
        """State 6"""
        Label('L1')
        # actionbutton:9700:"Hoist medallion"
        call = t610006000_x0(actionbutton3=9700, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000,
                             flag6=6000)
        if call.Done():
            """State 2"""
            Label('L2')
            SetEventFlag(1049532500, 1)
        # goods:8175:Haligtree Secret Medallion (Left), goods:8176:Haligtree Secret Medallion (Right)
        elif (ComparePlayerInventoryNumber(3, 8175, 4, 1, 0) == 1 and ComparePlayerInventoryNumber(3,
              8176, 4, 1, 0) == 1):
            """State 5"""
            Label('L3')
            # actionbutton:9700:"Hoist medallion", actionbutton:9701:"Hoist secret medallion"
            call = t610006000_x4(actionbutton1=9700, actionbutton2=9701)
            if call.Get() == 0:
                Goto('L2')
            elif call.Done():
                """State 3"""
                Label('L4')
                SetEventFlag(1049532504, 1)
            # goods:8107:Rold Medallion
            elif ComparePlayerInventoryNumber(3, 8107, 0, 0, 0) == 1:
                """State 7"""
                Label('L5')
                # actionbutton:9701:"Hoist secret medallion"
                call = t610006000_x0(actionbutton3=9701, flag1=6001, flag2=6000, flag3=6000, flag4=6000,
                                     flag5=6000, flag6=6000)
                if call.Done():
                    Goto('L4')
                # goods:8107:Rold Medallion
                elif ComparePlayerInventoryNumber(3, 8107, 4, 1, 0) == 1:
                    Goto('L3')
                # goods:8175:Haligtree Secret Medallion (Left), goods:8176:Haligtree Secret Medallion (Right)
                elif (ComparePlayerInventoryNumber(3, 8175, 0, 0, 0) == 1 or ComparePlayerInventoryNumber(3,
                      8176, 0, 0, 0) == 1):
                    Goto('L0')
            # goods:8175:Haligtree Secret Medallion (Left), goods:8176:Haligtree Secret Medallion (Right)
            elif (ComparePlayerInventoryNumber(3, 8175, 0, 0, 0) == 1 or ComparePlayerInventoryNumber(3,
                  8176, 0, 0, 0) == 1):
                Goto('L1')
        # goods:8107:Rold Medallion
        elif ComparePlayerInventoryNumber(3, 8107, 0, 0, 0) == 1:
            Goto('L0')
    # goods:8175:Haligtree Secret Medallion (Left), goods:8176:Haligtree Secret Medallion (Right)
    elif (ComparePlayerInventoryNumber(3, 8175, 4, 1, 0) == 1 and ComparePlayerInventoryNumber(3, 8176,
          4, 1, 0) == 1):
        Goto('L5')
    """State 4"""
    assert GetCurrentStateElapsedTime() > 1
    Goto('L0')
    """Unused"""
    """State 8"""
    return 0

def t610006000_x3():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t610006000_x4(actionbutton1=9700, actionbutton2=9701):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 2"""
        if not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()):
            pass
        # actionbutton:9701:"Hoist secret medallion"
        elif CheckActionButtonArea(actionbutton2):
            """Pass"""
            SetTalkTime(0.05)
            """State 4"""
            return 1
        # actionbutton:9700:"Hoist medallion"
        elif CheckActionButtonArea(actionbutton1):
            """Pass"""
            SetTalkTime(0.05)
            break
    """State 3"""
    return 0

