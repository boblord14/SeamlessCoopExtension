# -*- coding: utf-8 -*-
def t219016000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t219016000_x4(flag1=6000, flag2=6000, flag3=6000, val2=5, val3=10, val4=12, val5=10, val6=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode1=1, mode2=1)
    Quit()

def t219016000_2000():
    """State 0,2,3"""
    assert t219016000_x33(val1=10, z1=12, z2=1)
    """State 1"""
    c1_120(2000)
    Quit()

def t219016000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                  flag4=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag5) == 1 or GetEventFlag(flag9) == 1 or GetEventFlag(flag10) == 1 or
                GetEventFlag(flag11) == 1 or GetEventFlag(flag12) == 1)
        """State 4"""
        assert not GetEventFlag(flag4)
        """State 2"""
        if GetEventFlag(flag4) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag5) and not GetEventFlag(flag9) and not GetEventFlag(flag10) and not
              GetEventFlag(flag11) and not GetEventFlag(flag12)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t219016000_x1():
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

def t219016000_x2(val3=10, val4=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val3 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t219016000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val4 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t219016000_x1()
    else:
        """State 4,7"""
        call = t219016000_x30()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val4 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t219016000_x1()
    """State 9"""
    return 0

def t219016000_x3():
    """State 0,1"""
    assert t219016000_x1()
    """State 2"""
    return 0

def t219016000_x4(flag1=6000, flag2=6000, flag3=6000, val2=5, val3=10, val4=12, val5=10, val6=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t219016000_x21(flag1=flag1, flag2=flag2, flag3=flag3, val2=val2, val3=val3, val4=val4,
                              val5=val5, val6=val6, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z3=z3, z4=z4, z5=z5, z6=z6, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t219016000_x20()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t219016000_x5(val2=5, val3=10, val4=12, val5=10, val6=12, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z3=1, z4=1000000, z5=1000000, z6=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t219016000_x8(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z4=z4, z5=z5, z6=z6)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t219016000_x12(val2=val2, z3=z3)
            def WhilePaused():
                c5_138(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
                GiveSpEffectToPlayer(9640)
                c5_139(1 == (mode1 == 1), -1, 0)
                c5_139(1 == (mode2 == 1), 0, -1)
            def ExitPause():
                c1_138(-1)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif IsAttackedBySomeone() == 1 and not DoesSelfHaveSpEffect(9626) and not DoesSelfHaveSpEffect(9627):
            pass
        elif GetEventFlag(flag8) == 1:
            Goto('L0')
        elif GetEventFlag(flag6) == 1 and not GetEventFlag(flag7) and GetDistanceToPlayer() < val5:
            """State 5"""
            call = t219016000_x14(val6=val6)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val6 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t219016000_x25() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t219016000_x10(val3=val3, val4=val4)
    """Unused"""
    """State 7"""
    return 0

def t219016000_x6(val3=10, val4=12):
    """State 0,1"""
    call = t219016000_x16(val3=val3, val4=val4)
    assert IsPlayerDead() == 1
    """State 2"""
    t219016000_x2(val3=val3, val4=val4)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t219016000_x7(flag1=6000, val3=10, val4=12):
    """State 0,8"""
    assert t219016000_x32()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val3:
            """State 4,6"""
            call = t219016000_x19()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val4 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t219016000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t219016000_x8(actionbutton1=6000, flag4=6000, flag5=6001, z4=1000000, z5=1000000, z6=1000000):
    """State 0,1"""
    call = t219016000_x9(z7=2000, val7=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t219016000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t219016000_x9(z7=_, val7=_):
    """State 0,1"""
    if f203(z7) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z7)
        assert f202() == val7
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t219016000_x10(val3=10, val4=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t219016000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val3:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t219016000_x11()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val4 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t219016000_x26()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t219016000_x11():
    """State 0,1"""
    assert t219016000_x9(z7=1101, val7=1101)
    """State 2"""
    return 0

def t219016000_x12(val2=5, z3=1):
    """State 0,2"""
    assert t219016000_x22()
    """State 1"""
    call = t219016000_x13()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val2 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t219016000_x24()
    """State 4"""
    return 0

def t219016000_x13():
    """State 0,1"""
    assert t219016000_x9(z7=1000, val7=1000)
    """State 2"""
    return 0

def t219016000_x14(val6=12):
    """State 0,1"""
    call = t219016000_x15()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val6 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t219016000_x25()
    """State 3"""
    return 0

def t219016000_x15():
    """State 0,1"""
    assert t219016000_x9(z7=1100, val7=1100)
    """State 2"""
    return 0

def t219016000_x16(val3=10, val4=12):
    """State 0,5"""
    assert t219016000_x32()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val3
        """State 3"""
        call = t219016000_x17()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val4 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t219016000_x27()
    """Unused"""
    """State 6"""
    return 0

def t219016000_x17():
    """State 0,2"""
    call = t219016000_x9(z7=1102, val7=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t219016000_x18():
    """State 0,1"""
    assert t219016000_x9(z7=1001, val7=1001)
    """State 2"""
    return 0

def t219016000_x19():
    """State 0,1"""
    assert t219016000_x9(z7=1103, val7=1103)
    """State 2"""
    return 0

def t219016000_x20():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t219016000_x21(flag1=6000, flag2=6000, flag3=6000, val2=5, val3=10, val4=12, val5=10, val6=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z3=1, z4=1000000, z5=1000000,
                   z6=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t219016000_x5(val2=val2, val3=val3, val4=val4, val5=val5, val6=val6, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z3=z3,
                             z4=z4, z5=z5, z6=z6, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t219016000_x7(flag1=flag1, val3=val3, val4=val4)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t219016000_x6(val3=val3, val4=val4)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t219016000_x31() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t219016000_x22():
    """State 0,1"""
    assert t219016000_x23()
    """State 2"""
    return 0

def t219016000_x23():
    """State 0,1"""
    assert t219016000_x9(z7=1104, val7=1104)
    """State 2"""
    return 0

def t219016000_x24():
    """State 0,1"""
    call = t219016000_x9(z7=1201, val7=1201)
    if call.Get() == 1:
        """State 2"""
        assert t219016000_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t219016000_x25():
    """State 0,1"""
    call = t219016000_x9(z7=1300, val7=1300)
    if call.Get() == 1:
        """State 2"""
        assert t219016000_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t219016000_x26():
    """State 0,1"""
    call = t219016000_x9(z7=1301, val7=1301)
    if call.Get() == 1:
        """State 2"""
        assert t219016000_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t219016000_x27():
    """State 0,1"""
    call = t219016000_x9(z7=1302, val7=1302)
    if call.Get() == 1:
        """State 2"""
        assert t219016000_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t219016000_x28(text1=21900100, mode3=1):
    """State 0,4"""
    assert t219016000_x29() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    # talk:21900100:"Ah!"
    TalkToPlayer(text1, -1, -1, 1)
    """State 3"""
    if not mode3:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t219016000_x29():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t219016000_x30():
    """State 0,1"""
    assert t219016000_x9(z7=1002, val7=1002)
    """State 2"""
    return 0

def t219016000_x31():
    """State 0,1"""
    assert t219016000_x1()
    """State 2"""
    return 0

def t219016000_x32():
    """State 0,1"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 2"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 3"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 4"""
        ForceCloseMenu()
    else:
        pass
    """State 5"""
    return 0

def t219016000_x33(val1=10, z1=12, z2=1):
    """State 0"""
    while True:
        """State 5"""
        # actionbutton:6000:"Talk"
        call = t219016000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                             flag4=6000)
        if call.Done():
            break
        elif GetEventFlag(1035420701) == 1 and not GetEventFlag(1035429206) and GetDistanceToPlayer() < val1:
            """State 1,2"""
            SetEventFlag(1035429206, 1)
            """State 6"""
            # talk:21900100:"Ah!"
            assert t219016000_x28(text1=21900100, mode3=1) and CheckSpecificPersonTalkHasEnded(0) == 1
        elif GetEventFlag(1035429210) == 1:
            """State 3,4"""
            Quit()
    """State 7"""
    return 0

