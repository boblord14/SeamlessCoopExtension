# -*- coding: utf-8 -*-
def t330016000_1():
    """State 0,1"""
    t330016000_x0()
    Quit()

def t330016000_x0():
    """State 0"""
    if not IsClientPlayer():
        """State 2"""
        Label('L0')
        call = t330016000_x1()
        assert IsClientPlayer() == 1
    else:
        pass
    """State 1"""
    call = t330016000_x2()
    assert not IsClientPlayer()
    Goto('L0')
    """Unused"""
    """State 3"""
    return 0

def t330016000_x1():
    """State 0"""
    while True:
        """State 1"""
        # actionbutton:6370:"Atone"
        assert (t330016000_x5(actionbutton1=6370, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000,
                flag6=6000))
        """State 3"""
        call = t330016000_x3()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 3:
            pass
        """State 2"""
        assert t330016000_x6()
    """Unused"""
    """State 4"""
    return 0

def t330016000_x2():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t330016000_x3():
    """State 0,8"""
    if (not GetEventFlag(1037469280) and not GetEventFlag(1037469281) and not GetEventFlag(1037469282)
        and not GetEventFlag(1037469283) and not GetEventFlag(1037469284) and not GetEventFlag(1037469285)
        and not GetEventFlag(1037469286) and not GetEventFlag(1037469287) and not GetEventFlag(1037469288)):
        """State 15"""
        # action:23301001:"You don't need absolution"
        assert t330016000_x7(action1=23301001)
    else:
        """State 12"""
        # action:23301003:"Use Celestial Dew to receive absolution?"
        call = t330016000_x4(action2=23301003)
        if call.Get() == 0:
            """State 1,7"""
            # goods:2130:Celestial Dew
            if ComparePlayerInventoryNumber(3, 2130, 2, 0, 0) == 1:
                """State 3,9"""
                TurnCharacterToFaceEntity(-1, 10000, -1, -1)
                assert GetWhetherChrEventAnimHasEnded(10000) == 1 and GetCurrentStateElapsedFrames() > 1
                """State 10"""
                TurnCharacterToFaceEntity(60560, 10000, -1, -1)
                """State 11"""
                assert GetCurrentStateElapsedTime() > 3.5
                """State 6"""
                # goods:2130:Celestial Dew
                PlayerEquipmentQuantityChange(3, 2130, -1)
                """State 5"""
                SetEventFlag(1037469289, 1)
                """State 13"""
                # action:23301004:"Your sins are absolved"
                assert t330016000_x7(action1=23301004)
            else:
                """State 4,14"""
                # action:23301002:"No Celestial Dew in inventory"
                assert t330016000_x7(action1=23301002)
        elif call.Done():
            """State 2"""
            pass
    """State 16"""
    return 0

def t330016000_x4(action2=23301003):
    """State 0,1"""
    # action:23301003:"Use Celestial Dew to receive absolution?"
    OpenGenericDialog(8, action2, 3, 4, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == 1:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t330016000_x5(actionbutton1=6370, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=6000):
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
        # actionbutton:6370:"Atone"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t330016000_x6():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t330016000_x7(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

