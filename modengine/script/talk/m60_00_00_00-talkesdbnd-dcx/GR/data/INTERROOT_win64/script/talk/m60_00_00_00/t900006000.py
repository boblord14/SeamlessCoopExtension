# -*- coding: utf-8 -*-
def t900006000_1():
    """State 0,1"""
    t900006000_x0()
    Quit()

def t900006000_x0():
    """State 0"""
    if not IsClientPlayer():
        """State 2"""
        Label('L0')
        call = t900006000_x1()
        assert IsClientPlayer() == 1
    else:
        pass
    """State 1"""
    call = t900006000_x2()
    assert not IsClientPlayer()
    Goto('L0')
    """Unused"""
    """State 3"""
    return 0

def t900006000_x1():
    """State 0"""
    while True:
        """State 1"""
        # actionbutton:6000:"Talk"
        assert (t900006000_x5(actionbutton1=6000, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000,
                flag6=6000))
        """State 3"""
        call = t900006000_x3()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 3:
            pass
        """State 2"""
        assert t900006000_x6()
    """Unused"""
    """State 4"""
    return 0

def t900006000_x2():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t900006000_x3():
    """State 0"""
    if not GetEventFlag(3000):
        """State 8,10"""
        # action:99990404:"Request absolution? (仮)"
        call = t900006000_x4(action2=99990404)
        if call.Get() == 0:
            """State 1,7"""
            # goods:2130:Celestial Dew
            if ComparePlayerInventoryNumber(3, 2130, 2, 0, 0) == 1:
                """State 3,6"""
                # goods:2130:Celestial Dew
                PlayerEquipmentQuantityChange(3, 2130, -1)
                """State 5"""
                SetEventFlag(3000, 1)
                """State 11"""
                # action:99990401:"Your sins have been pardoned"
                assert t900006000_x7(action1=99990401)
            else:
                """State 4,12"""
                # action:99990405:"No item (仮)"
                assert t900006000_x7(action1=99990405)
        elif call.Done():
            """State 2"""
            pass
    else:
        """State 9,13"""
        # action:99990403:"You are already absolved"
        assert t900006000_x7(action1=99990403)
    """State 14"""
    return 0

def t900006000_x4(action2=99990404):
    """State 0,1"""
    # action:99990404:"Request absolution? (仮)"
    OpenGenericDialog(8, action2, 3, 4, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == 1:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t900006000_x5(actionbutton1=6000, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=6000):
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
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t900006000_x6():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t900006000_x7(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

