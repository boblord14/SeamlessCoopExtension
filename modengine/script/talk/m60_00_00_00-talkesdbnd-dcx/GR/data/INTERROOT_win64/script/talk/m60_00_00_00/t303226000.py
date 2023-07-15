# -*- coding: utf-8 -*-
def t303226000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t303226000_x4(flag2=3283, flag3=3281, flag4=3282, val1=5, val2=100, val3=150, val4=10, val5=12, actionbutton1=6000,
                  flag5=6001, flag6=6000, flag7=6000, flag8=6000, flag9=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t303226000_1001():
    """State 0,2,3"""
    assert t303226000_x34()
    """State 1"""
    c1_120(1001)
    Quit()

def t303226000_1102():
    """State 0,2,3"""
    t303226000_x35(flag1=1041382710)
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t303226000_1103():
    """State 0,2,3"""
    assert t303226000_x36()
    """State 1"""
    c1_120(1103)
    Quit()

def t303226000_x0(actionbutton1=6000, flag6=6000, flag10=6000, flag11=6000, flag12=6000, flag13=6000,
                  flag5=6001):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag6) == 1 or GetEventFlag(flag10) == 1 or GetEventFlag(flag11) == 1 or
                GetEventFlag(flag12) == 1 or GetEventFlag(flag13) == 1)
        """State 4"""
        assert not GetEventFlag(flag5)
        """State 2"""
        if GetEventFlag(flag5) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag6) and not GetEventFlag(flag10) and not GetEventFlag(flag11) and not
              GetEventFlag(flag12) and not GetEventFlag(flag13)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t303226000_x1():
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

def t303226000_x2(val2=100, val3=150):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t303226000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t303226000_x1()
    else:
        """State 4,7"""
        call = t303226000_x31()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t303226000_x1()
    """State 9"""
    return 0

def t303226000_x3():
    """State 0,1"""
    assert t303226000_x1()
    """State 2"""
    return 0

def t303226000_x4(flag2=3283, flag3=3281, flag4=3282, val1=5, val2=100, val3=150, val4=10, val5=12, actionbutton1=6000,
                  flag5=6001, flag6=6000, flag7=6000, flag8=6000, flag9=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t303226000_x21(flag2=flag2, flag3=flag3, flag4=flag4, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag5=flag5, flag6=flag6,
                              flag7=flag7, flag8=flag8, flag9=flag9, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t303226000_x20()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t303226000_x5(val1=5, val2=100, val3=150, val4=10, val5=12, actionbutton1=6000, flag5=6001, flag6=6000,
                  flag7=6000, flag8=6000, flag9=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t303226000_x8(actionbutton1=actionbutton1, flag5=flag5, flag6=flag6, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t303226000_x12(val1=val1, z1=z1)
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
        elif GetEventFlag(flag9) == 1:
            Goto('L0')
        elif GetEventFlag(flag7) == 1 and not GetEventFlag(flag8) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t303226000_x14(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t303226000_x25() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t303226000_x10(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t303226000_x6(val2=100, val3=150):
    """State 0,1"""
    call = t303226000_x16(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t303226000_x2(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t303226000_x7(flag2=3283, val2=100, val3=150):
    """State 0,8"""
    assert t303226000_x33()
    """State 1"""
    if GetEventFlag(flag2) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t303226000_x19()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t303226000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t303226000_x8(actionbutton1=6000, flag5=6001, flag6=6000, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t303226000_x9(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t303226000_x0(actionbutton1=actionbutton1, flag6=flag6, flag10=6000, flag11=6000, flag12=6000,
                flag13=6000, flag5=flag5))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t303226000_x9(z6=_, val6=_):
    """State 0,1"""
    if f203(z6) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z6)
        assert f202() == val6
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t303226000_x10(val2=100, val3=150):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t303226000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t303226000_x11()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t303226000_x26()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t303226000_x11():
    """State 0,1"""
    assert t303226000_x9(z6=1101, val6=1101)
    """State 2"""
    return 0

def t303226000_x12(val1=5, z1=1):
    """State 0,2"""
    assert t303226000_x22()
    """State 1"""
    call = t303226000_x13()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t303226000_x24()
    """State 4"""
    return 0

def t303226000_x13():
    """State 0,1"""
    assert t303226000_x9(z6=1000, val6=1000)
    """State 2"""
    return 0

def t303226000_x14(val5=12):
    """State 0,1"""
    call = t303226000_x15()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t303226000_x25()
    """State 3"""
    return 0

def t303226000_x15():
    """State 0,1"""
    assert t303226000_x9(z6=1100, val6=1100)
    """State 2"""
    return 0

def t303226000_x16(val2=100, val3=150):
    """State 0,5"""
    assert t303226000_x33()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t303226000_x17()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t303226000_x27()
    """Unused"""
    """State 6"""
    return 0

def t303226000_x17():
    """State 0,2"""
    call = t303226000_x9(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t303226000_x18():
    """State 0,1"""
    assert t303226000_x9(z6=1001, val6=1001)
    """State 2"""
    return 0

def t303226000_x19():
    """State 0,1"""
    assert t303226000_x9(z6=1103, val6=1103)
    """State 2"""
    return 0

def t303226000_x20():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t303226000_x21(flag2=3283, flag3=3281, flag4=3282, val1=5, val2=100, val3=150, val4=10, val5=12,
                   actionbutton1=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, flag9=6000, z1=1,
                   z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t303226000_x5(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, flag9=flag9, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag2) == 1:
            """State 3"""
            Label('L0')
            call = t303226000_x7(flag2=flag2, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag2):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag3) == 1 or GetEventFlag(flag4) == 1:
            """State 2"""
            call = t303226000_x6(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag2) == 1:
                Goto('L0')
            elif not GetEventFlag(flag3) and not GetEventFlag(flag4):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t303226000_x32() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t303226000_x22():
    """State 0,1"""
    assert t303226000_x23()
    """State 2"""
    return 0

def t303226000_x23():
    """State 0,1"""
    assert t303226000_x9(z6=1104, val6=1104)
    """State 2"""
    return 0

def t303226000_x24():
    """State 0,1"""
    call = t303226000_x9(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t303226000_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t303226000_x25():
    """State 0,1"""
    call = t303226000_x9(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t303226000_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t303226000_x26():
    """State 0,1"""
    call = t303226000_x9(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t303226000_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t303226000_x27():
    """State 0,1"""
    call = t303226000_x9(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t303226000_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t303226000_x28(text2=_, z5=_, mode4=1):
    """State 0,5"""
    assert t303226000_x30() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(z5, 1)
    """State 1"""
    TalkToPlayer(text2, -1, -1, 1)
    """State 4"""
    if not mode4:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t303226000_x29(text1=_, mode3=1):
    """State 0,4"""
    assert t303226000_x30() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text1, -1, -1, 1)
    """State 3"""
    if not mode3:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t303226000_x30():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t303226000_x31():
    """State 0,1"""
    assert t303226000_x9(z6=1002, val6=1002)
    """State 2"""
    return 0

def t303226000_x32():
    """State 0,1"""
    assert t303226000_x1()
    """State 2"""
    return 0

def t303226000_x33():
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

def t303226000_x34():
    """State 0,1"""
    # talk:30390800:"Don't you see now?"
    assert t303226000_x29(text1=30390800, mode3=1)
    """State 2"""
    return 0

def t303226000_x35(flag1=1041382710):
    """State 0"""
    if GetEventFlag(3295) == 1:
        """State 2"""
        t303226000_x37(flag1=flag1)
        Quit()
    else:
        """State 1"""
        Quit()
    """Unused"""
    """State 3"""
    return 0

def t303226000_x36():
    """State 0,1"""
    # talk:30390600:"Let it be known."
    assert t303226000_x29(text1=30390600, mode3=1)
    """State 2"""
    return 0

def t303226000_x37(flag1=1041382710):
    """State 0"""
    while True:
        """State 1"""
        assert GetEventFlag(flag1) == 1
        """State 9"""
        if GetEventFlag(1043352702) == 1:
            """State 2"""
            pass
        else:
            """State 7"""
            SetEventFlag(1043352702, 1)
            if not GetEventFlag(1043359220) and not GetEventFlag(1043359221):
                """State 4"""
                if not GetEventFlag(1043359201):
                    """State 5,10"""
                    # talk:30390100:"Hello there, I don't believe we've met."
                    assert t303226000_x28(text2=30390100, z5=1043359220, mode4=1)
                else:
                    """State 6,11"""
                    # talk:30390000:"Well, well, you've made yourself a target of vengeance."
                    assert t303226000_x28(text2=30390000, z5=1043359221, mode4=1)
            else:
                """State 8,12"""
                # talk:30391000:"Didn't I tell you before?"
                assert t303226000_x29(text1=30391000, mode3=1)
        """State 3"""
        assert not GetEventFlag(flag1)
    """Unused"""
    """State 13"""
    return 0

