# -*- coding: utf-8 -*-
def t622006000_1():
    """State 0,1"""
    # actionbutton:6612:"Enter Colosseum combat"
    t622006000_x3(val1=2, val2=5, actionbutton1=6612)
    Quit()

def t622006000_x0(actionbutton1=6612, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=6000):
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
        # actionbutton:6612:"Enter Colosseum combat"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t622006000_x1():
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

def t622006000_x2(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t622006000_x3(val1=2, val2=5, actionbutton1=6612):
    """State 0"""
    while True:
        """State 2"""
        call = t622006000_x4(val1=val1, val2=val2, actionbutton1=actionbutton1)
        assert IsClientPlayer() == 1
        """State 1"""
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t622006000_x4(val1=2, val2=5, actionbutton1=6612):
    """State 0"""
    while True:
        """State 2"""
        call = t622006000_x5(val1=val1, actionbutton1=actionbutton1)
        assert GetDistanceToPlayer() > val2
        """State 3"""
        assert t622006000_x1()
        """State 1"""
        assert GetDistanceToPlayer() < val2
    """Unused"""
    """State 4"""
    return 0

def t622006000_x5(val1=2, actionbutton1=6612):
    """State 0"""
    while True:
        """State 4"""
        assert (t622006000_x0(actionbutton1=actionbutton1, flag1=6001, flag2=6000, flag3=6000, flag4=6000,
                flag5=6000, flag6=6000))
        """State 5"""
        call = t622006000_x7(val1=val1)
        if call.Get() == 1:
            """State 6"""
            # action:26231001:"No Colosseum rules available for selection"
            assert t622006000_x2(action1=26231001)
        elif call.Get() == 2:
            """State 7"""
            assert t622006000_x8(mode1=0)
        elif call.Done():
            """State 1"""
            c1_151(val1, GetEventFlag(60350), GetEventFlag(60360), GetEventFlag(60370))
            """State 3"""
            SetEventFlag(710880, 1)
            """State 2"""
            def WhilePaused():
                GiveSpEffectToPlayer(9640)
            assert not (CheckSpecificPersonMenuIsOpen(34, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """Unused"""
    """State 8"""
    return 0

def t622006000_x6(val1=2):
    """State 0"""
    if not val1:
        """State 1"""
        if GetEventFlag(60350) == 1:
            pass
        else:
            """State 7"""
            Label('L0')
            return 1
    elif val1 == 1:
        """State 2"""
        if GetEventFlag(60360) == 1:
            pass
        else:
            Goto('L0')
    elif val1 == 2:
        """State 3"""
        if GetEventFlag(60370) == 1:
            pass
        else:
            Goto('L0')
    elif val1 == 3:
        """State 4"""
        if GetEventFlag(60350) == 1 or GetEventFlag(60360) == 1 or GetEventFlag(60370) == 1:
            pass
        else:
            Goto('L0')
    else:
        """State 5"""
        Goto('L0')
    """State 6"""
    return 0

def t622006000_x7(val1=2):
    """State 0,1"""
    call = t622006000_x6(val1=val1)
    if call.Get() == 1:
        """State 3"""
        return 1
    elif call.Done() and not GetIsOnline():
        """State 4"""
        return 2
    elif call.Done():
        """State 2"""
        return 0

def t622006000_x8(mode1=0):
    """State 0"""
    if not mode1:
        """State 1"""
        # action:26201000:"Colosseums are only available online"
        assert t622006000_x2(action1=26201000)
    elif mode1 == 1:
        """State 2"""
        # action:26211000:"Colosseums are only available online"
        assert t622006000_x2(action1=26211000)
    elif mode1 == 2:
        """State 3"""
        # action:26221000:"Colosseums are only available online"
        assert t622006000_x2(action1=26221000)
    elif True:
        """State 5"""
        # action:26201000:"Colosseums are only available online"
        assert t622006000_x2(action1=26201000)
    elif mode1 == 3:
        """State 4"""
        # action:26231000:"Colosseums are only available online"
        assert t622006000_x2(action1=26231000)
    """State 6"""
    return 0

