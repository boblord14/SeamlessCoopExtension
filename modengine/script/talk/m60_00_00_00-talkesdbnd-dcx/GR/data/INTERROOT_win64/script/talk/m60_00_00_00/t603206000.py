# -*- coding: utf-8 -*-
def t603206000_1():
    """State 0,1"""
    t603206000_x4(flag1=1238470400, flag2=1038479200)
    Quit()

def t603206000_x0(flag1=1238470400, flag2=1038479200, z1=101785, z2=101799, val1=270750, z3=8):
    """State 0"""
    while True:
        """State 2"""
        call = t603206000_x1(flag1=flag1, flag2=flag2, z1=z1, z2=z2, val1=val1, z3=z3)
        assert not GetEventFlag(flag1)
        """State 1"""
        assert GetEventFlag(flag1) == 1
    """Unused"""
    """State 3"""
    return 0

def t603206000_x1(flag1=1238470400, flag2=1038479200, z1=101785, z2=101799, val1=270750, z3=8):
    """State 0"""
    while True:
        """State 2"""
        call = t603206000_x5(flag1=flag1, flag2=flag2, z1=z1, z2=z2, val1=val1)
        assert not GetWhetherEnemiesAreNearby(z3)
        """State 3"""
        assert t603206000_x7()
        """State 1"""
        assert GetWhetherEnemiesAreNearby(z3) == 1
    """Unused"""
    """State 4"""
    return 0

def t603206000_x2(flag2=1038479200, z1=101785, z2=101799, val1=270750):
    """State 0,4"""
    ClearTalkActionState()
    """State 5"""
    SetWorkValue(0, 0)
    def ExitPause():
        SetWorkValue(0, 0)
    assert t603206000_x3(val1=val1)
    """State 1"""
    OpenDupeShop(1, z1, z2)
    if DidYouDoSomethingInTheMenu(4) == 1:
        """State 2"""
        SetEventFlag(flag2, 1)
        assert not (CheckSpecificPersonMenuIsOpen(32, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    elif not (CheckSpecificPersonMenuIsOpen(32, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
        """State 3"""
        assert not (CheckSpecificPersonMenuIsOpen(32, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 6"""
    return 0

def t603206000_x3(val1=270750):
    """State 0"""
    while True:
        """State 1"""
        SetEventFlag(val1 + GetWorkValue(0) * 10, 0)
        SetWorkValue(0, GetWorkValue(0) + 1)
        if GetWorkValue(0) > 25:
            break
        else:
            pass
    """State 2"""
    return 0

def t603206000_x4(flag1=1238470400, flag2=1038479200):
    """State 0"""
    while True:
        """State 2"""
        call = t603206000_x0(flag1=flag1, flag2=flag2, z1=101785, z2=101799, val1=270750, z3=8)
        assert IsClientPlayer() == 1
        """State 1"""
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t603206000_x5(flag1=1238470400, flag2=1038479200, z1=101785, z2=101799, val1=270750):
    """State 0"""
    while True:
        """State 2"""
        if not GetEventFlag(flag2):
            """State 3"""
            # actionbutton:6430:"Examine remains"
            assert (t603206000_x6(actionbutton1=6430, flag3=6001, flag4=6000, flag5=6000, flag6=6000,
                    flag7=6000, flag8=6000))
            """State 4"""
            assert t603206000_x2(flag2=flag2, z1=z1, z2=z2, val1=val1)
        else:
            """State 1"""
            Quit()
    """Unused"""
    """State 5"""
    return 0

def t603206000_x6(actionbutton1=6430, flag3=6001, flag4=6000, flag5=6000, flag6=6000, flag7=6000, flag8=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag3) == 1 or GetEventFlag(flag4) == 1 or GetEventFlag(flag5) == 1 or GetEventFlag(flag6)
                == 1 or GetEventFlag(flag7) == 1)
        """State 4"""
        assert not GetEventFlag(flag8)
        """State 2"""
        if GetEventFlag(flag8) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag3) and not GetEventFlag(flag4) and not GetEventFlag(flag5) and not
              GetEventFlag(flag6) and not GetEventFlag(flag7)):
            pass
        # actionbutton:6430:"Examine remains"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t603206000_x7():
    """State 0,1"""
    if not CheckSpecificPersonTalkHasEnded(0):
        """State 7"""
        ClearTalkProgressData()
        StopEventAnimWithoutForcingConversationEnd(0)
        """State 6"""
        ReportConversationEndToHavokBehavior()
    else:
        pass
    """State 2"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 3"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 4"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 5"""
        ForceCloseMenu()
    else:
        pass
    """State 8"""
    return 0

