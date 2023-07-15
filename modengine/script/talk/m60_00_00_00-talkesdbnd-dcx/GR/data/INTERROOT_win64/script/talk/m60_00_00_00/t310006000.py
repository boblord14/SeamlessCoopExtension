# -*- coding: utf-8 -*-
def t310006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t310006000_x7(flag4=3383, flag5=3381, flag6=3382, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton3=6000,
                  flag7=6000, flag8=6001, flag9=6000, flag10=6000, flag11=6000, z2=1, z3=1000000, z4=1000000,
                  z5=1000000, mode1=1, mode2=1)
    Quit()

def t310006000_1000():
    """State 0,2,3"""
    assert t310006000_x39()
    """State 1"""
    c1_120(1000)
    Quit()

def t310006000_1001():
    """State 0,2,3"""
    assert t310006000_x40()
    """State 1"""
    c1_120(1001)
    Quit()

def t310006000_1101():
    """State 0,2,3"""
    assert t310006000_x41()
    """State 1"""
    c1_120(1101)
    Quit()

def t310006000_1102():
    """State 0,2,3"""
    t310006000_x42()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t310006000_1103():
    """State 0,2,3"""
    assert t310006000_x43()
    """State 1"""
    c1_120(1103)
    Quit()

def t310006000_2000():
    """State 0,2,3"""
    assert t310006000_x44()
    """State 1"""
    c1_120(2000)
    Quit()

def t310006000_x0(actionbutton3=_, flag8=6001, flag12=6000, flag13=6000, flag14=6000, flag15=6000, flag7=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag8) == 1 or GetEventFlag(flag12) == 1 or GetEventFlag(flag13) == 1 or
                GetEventFlag(flag14) == 1 or GetEventFlag(flag15) == 1)
        """State 4"""
        assert not GetEventFlag(flag7)
        """State 2"""
        if GetEventFlag(flag7) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag8) and not GetEventFlag(flag12) and not GetEventFlag(flag13) and not
              GetEventFlag(flag14) and not GetEventFlag(flag15)):
            pass
        elif CheckActionButtonArea(actionbutton3):
            break
    """State 5"""
    return 0

def t310006000_x1():
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

def t310006000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t310006000_x3(lot1=_):
    """State 0,1"""
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t310006000_x4(action1=23101009):
    """State 0,1"""
    # action:23101009:"She's dead"
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t310006000_x5(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t310006000_x21()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t310006000_x1()
    else:
        """State 4,7"""
        call = t310006000_x36()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t310006000_x1()
    """State 9"""
    return 0

def t310006000_x6():
    """State 0,1"""
    assert t310006000_x1()
    """State 2"""
    return 0

def t310006000_x7(flag4=3383, flag5=3381, flag6=3382, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton3=6000,
                  flag7=6000, flag8=6001, flag9=6000, flag10=6000, flag11=6000, z2=1, z3=1000000, z4=1000000,
                  z5=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t310006000_x24(flag4=flag4, flag5=flag5, flag6=flag6, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton3=actionbutton3, flag7=flag7, flag8=flag8,
                              flag9=flag9, flag10=flag10, flag11=flag11, z2=z2, z3=z3, z4=z4, z5=z5,
                              mode1=mode1, mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t310006000_x23()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t310006000_x8(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton3=6000, flag7=6000, flag8=6001,
                  flag9=6000, flag10=6000, flag11=6000, z2=1, z3=1000000, z4=1000000, z5=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t310006000_x11(actionbutton3=actionbutton3, flag7=flag7, flag8=flag8, z3=z3, z4=z4, z5=z5)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t310006000_x15(val1=val1, z2=z2)
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
        elif GetEventFlag(flag11) == 1:
            Goto('L0')
        elif GetEventFlag(flag9) == 1 and not GetEventFlag(flag10) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t310006000_x17(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t310006000_x28() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t310006000_x13(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t310006000_x9(val2=10, val3=12):
    """State 0,1"""
    call = t310006000_x19(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t310006000_x5(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t310006000_x10(flag4=3383, val2=10, val3=12):
    """State 0,8"""
    assert t310006000_x38()
    """State 1"""
    if GetEventFlag(flag4) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t310006000_x22()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t310006000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t310006000_x11(actionbutton3=6000, flag7=6000, flag8=6001, z3=1000000, z4=1000000, z5=1000000):
    """State 0,1"""
    call = t310006000_x12(z7=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t310006000_x0(actionbutton3=actionbutton3, flag8=flag8, flag12=6000, flag13=6000, flag14=6000,
                flag15=6000, flag7=flag7))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t310006000_x12(z7=_, val6=_):
    """State 0,1"""
    if f203(z7) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z7)
        assert f202() == val6
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t310006000_x13(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t310006000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t310006000_x14()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t310006000_x29()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t310006000_x14():
    """State 0,1"""
    assert t310006000_x12(z7=1101, val6=1101)
    """State 2"""
    return 0

def t310006000_x15(val1=5, z2=1):
    """State 0,2"""
    assert t310006000_x25()
    """State 1"""
    call = t310006000_x16()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t310006000_x27()
    """State 4"""
    return 0

def t310006000_x16():
    """State 0,1"""
    assert t310006000_x12(z7=1000, val6=1000)
    """State 2"""
    return 0

def t310006000_x17(val5=12):
    """State 0,1"""
    call = t310006000_x18()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t310006000_x28()
    """State 3"""
    return 0

def t310006000_x18():
    """State 0,1"""
    assert t310006000_x12(z7=1100, val6=1100)
    """State 2"""
    return 0

def t310006000_x19(val2=10, val3=12):
    """State 0,5"""
    assert t310006000_x38()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t310006000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t310006000_x30()
    """Unused"""
    """State 6"""
    return 0

def t310006000_x20():
    """State 0,2"""
    call = t310006000_x12(z7=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t310006000_x21():
    """State 0,1"""
    assert t310006000_x12(z7=1001, val6=1001)
    """State 2"""
    return 0

def t310006000_x22():
    """State 0,1"""
    assert t310006000_x12(z7=1103, val6=1103)
    """State 2"""
    return 0

def t310006000_x23():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t310006000_x24(flag4=3383, flag5=3381, flag6=3382, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton3=6000,
                   flag7=6000, flag8=6001, flag9=6000, flag10=6000, flag11=6000, z2=1, z3=1000000, z4=1000000,
                   z5=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t310006000_x8(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton3=actionbutton3,
                             flag7=flag7, flag8=flag8, flag9=flag9, flag10=flag10, flag11=flag11, z2=z2,
                             z3=z3, z4=z4, z5=z5, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag4) == 1:
            """State 3"""
            Label('L0')
            call = t310006000_x10(flag4=flag4, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag4):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag5) == 1 or GetEventFlag(flag6) == 1:
            """State 2"""
            call = t310006000_x9(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag4) == 1:
                Goto('L0')
            elif not GetEventFlag(flag5) and not GetEventFlag(flag6):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t310006000_x37() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t310006000_x25():
    """State 0,1"""
    assert t310006000_x26()
    """State 2"""
    return 0

def t310006000_x26():
    """State 0,1"""
    assert t310006000_x12(z7=1104, val6=1104)
    """State 2"""
    return 0

def t310006000_x27():
    """State 0,1"""
    call = t310006000_x12(z7=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t310006000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t310006000_x28():
    """State 0,1"""
    call = t310006000_x12(z7=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t310006000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t310006000_x29():
    """State 0,1"""
    call = t310006000_x12(z7=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t310006000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t310006000_x30():
    """State 0,1"""
    call = t310006000_x12(z7=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t310006000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t310006000_x31(text4=_, z6=_, mode6=1):
    """State 0,5"""
    assert t310006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text4, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode6:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(z6, 1)
    """State 6"""
    return 0

def t310006000_x32(text1=_, mode5=1):
    """State 0,4"""
    assert t310006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text1, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode5:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t310006000_x33(text3=_, flag1=_, mode4=1):
    """State 0,5"""
    assert t310006000_x35() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(flag1, 1)
    """State 1"""
    TalkToPlayer(text3, -1, -1, 1)
    """State 4"""
    if not mode4:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t310006000_x34(text2=_, mode3=1):
    """State 0,4"""
    assert t310006000_x35() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text2, -1, -1, 1)
    """State 3"""
    if not mode3:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t310006000_x35():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t310006000_x36():
    """State 0,1"""
    assert t310006000_x12(z7=1002, val6=1002)
    """State 2"""
    return 0

def t310006000_x37():
    """State 0,1"""
    assert t310006000_x1()
    """State 2"""
    return 0

def t310006000_x38():
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

def t310006000_x39():
    """State 0,1"""
    if GetEventFlag(3385) == 1:
        """State 3"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t310006000_x46()
    elif GetEventFlag(3386) == 1:
        """State 4"""
        assert t310006000_x51()
    elif GetEventFlag(3387) == 1:
        """State 5"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t310006000_x45()
    elif GetEventFlag(3388) == 1:
        """State 6"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t310006000_x58()
    elif GetEventFlag(3389) == 1:
        """State 7"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t310006000_x61()
    elif GetEventFlag(3390) == 1:
        """State 8"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t310006000_x68()
    elif GetEventFlag(3391) == 1:
        """State 9"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t310006000_x69()
    elif GetEventFlag(3392) == 1:
        """State 10"""
        assert t310006000_x74()
    else:
        """State 2"""
        pass
    """State 11"""
    return 0

def t310006000_x40():
    """State 0,1"""
    # talk:31080300:"Oh, bless the stars."
    assert t310006000_x34(text2=31080300, mode3=1)
    """State 2"""
    return 0

def t310006000_x41():
    """State 0,1"""
    if GetEventFlag(3385) == 1:
        """State 3"""
        assert t310006000_x53(flag2=1045342700, flag3=1045342701)
    elif GetEventFlag(3387) == 1:
        """State 4"""
        assert t310006000_x53(flag2=1039402700, flag3=1039402701)
    elif GetEventFlag(3388) == 1:
        """State 5"""
        assert t310006000_x53(flag2=1038412700, flag3=1038412701)
    elif GetEventFlag(3389) == 1 or GetEventFlag(3390) == 1:
        """State 6"""
        assert t310006000_x53(flag2=1038432700, flag3=1038432701)
    elif GetEventFlag(3391) == 1:
        """State 7"""
        assert t310006000_x53(flag2=1036492700, flag3=1036492701)
    elif GetEventFlag(3392) == 1:
        """State 8"""
        assert t310006000_x53(flag2=35002700, flag3=35002701)
    else:
        """State 2"""
        pass
    """State 9"""
    return 0

def t310006000_x42():
    """State 0,3"""
    if GetEventFlag(3385) == 1:
        """State 4"""
        assert t310006000_x54(flag1=1045349202)
    elif GetEventFlag(3387) == 1:
        """State 5"""
        assert t310006000_x54(flag1=1039409202)
    elif GetEventFlag(3388) == 1:
        """State 6"""
        assert t310006000_x54(flag1=1038419202)
    elif GetEventFlag(3389) == 1 or GetEventFlag(3390) == 1:
        """State 7"""
        assert t310006000_x54(flag1=1038439202)
    elif GetEventFlag(3391) == 1:
        """State 8"""
        assert t310006000_x54(flag1=1036499202)
    elif GetEventFlag(3392) == 1:
        """State 9"""
        assert t310006000_x54(flag1=35009202)
    else:
        """State 2"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 10"""
    return 0

def t310006000_x43():
    """State 0,1"""
    if GetEventFlag(3385) == 1:
        """State 2"""
        # talk:31080400:"Father..."
        assert t310006000_x34(text2=31080400, mode3=1)
    else:
        """State 3"""
        # talk:31080500:"Ahh, the distant light...fades..."
        assert t310006000_x34(text2=31080500, mode3=1)
    """State 4"""
    return 0

def t310006000_x44():
    """State 0"""
    while True:
        """State 1"""
        call = t310006000_x67()
        if call.Done():
            break
        elif (GetEventFlag(3389) == 1 and GetEventFlag(1038439206) == 1 and not GetEventFlag(1038439207)
              and GetDistanceToPlayer() > 5):
            """State 2"""
            # talk:31001600:"..."
            assert t310006000_x33(text3=31001600, flag1=1038439207, mode4=1)
    """State 3"""
    return 0

def t310006000_x45():
    """State 0,1"""
    if GetEventFlag(1039409206) == 1:
        """State 3"""
        assert t310006000_x56()
    else:
        """State 2"""
        assert t310006000_x55()
    """State 4"""
    return 0

def t310006000_x46():
    """State 0,1"""
    if GetEventFlag(1045349205) == 1:
        """State 2"""
        if GetEventFlag(1045349207) == 1:
            """State 5"""
            assert t310006000_x49()
        else:
            """State 4"""
            assert t310006000_x48()
    else:
        """State 3"""
        assert t310006000_x47()
    """State 6"""
    return 0

def t310006000_x47():
    """State 0,1"""
    # talk:31000100:"Hello? Is somebody there?"
    assert t310006000_x31(text4=31000100, z6=1045349205, mode6=1)
    """State 2"""
    return 0

def t310006000_x48():
    """State 0,1"""
    if GetEventFlag(1045349206) == 1:
        """State 3"""
        # talk:31000300:"Hello? Is somebody there?"
        assert t310006000_x32(text1=31000300, mode5=1)
    else:
        """State 2"""
        # talk:31000600:"I...I fear for father's life."
        assert t310006000_x32(text1=31000600, mode5=1)
    """State 4"""
    assert t310006000_x50()
    """State 5"""
    return 0

def t310006000_x49():
    """State 0,1"""
    # talk:31000500:"Please, if you wouldn't mind. Deliver the letter to my father at the castle."
    assert t310006000_x32(text1=31000500, mode5=1)
    """State 2"""
    return 0

def t310006000_x50():
    """State 0,8"""
    c1_110()
    """State 6"""
    ClearTalkListData()
    """State 5"""
    # action:23101000:"Deliver the letter"
    AddTalkListData(1, 23101000, -1)
    # action:23101001:"Refuse"
    AddTalkListData(2, 23101001, -1)
    """State 4"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 7"""
    if GetTalkListEntryResult() == 1:
        """State 1,9"""
        # talk:31000400:"Thank you, dearly."
        assert t310006000_x31(text4=31000400, z6=1045349207, mode6=1)
        """State 11"""
        # lot:100800:Irina's Letter
        assert t310006000_x3(lot1=100800)
        """State 12"""
        # talk:31000450:"Deliver it to my father, who remains in the castle, if you please."
        assert t310006000_x32(text1=31000450, mode5=1)
    elif GetTalkListEntryResult() == 2:
        """State 2,10"""
        # talk:31000200:"I understand."
        assert t310006000_x31(text4=31000200, z6=1045349206, mode6=1)
    else:
        """State 3"""
        pass
    """State 13"""
    return 0

def t310006000_x51():
    """State 0,1"""
    SetEventFlag(1045349215, 1)
    """State 2"""
    # action:23101009:"She's dead"
    assert t310006000_x4(action1=23101009)
    """State 3"""
    return 0

def t310006000_x52():
    """State 0,1"""
    assert GetEventFlag(3403) == 1
    """State 2"""
    # actionbutton:6231:"Examine"
    assert (t310006000_x0(actionbutton3=6231, flag8=6001, flag12=6000, flag13=6000, flag14=6000, flag15=6000,
            flag7=6000))
    """State 3"""
    return 0

def t310006000_x53(flag2=_, flag3=_):
    """State 0,1"""
    if not GetEventFlag(flag2):
        """State 3"""
        # talk:31080000:"Agh!"
        assert t310006000_x33(text3=31080000, flag1=flag2, mode4=1)
    elif not GetEventFlag(flag3):
        """State 4"""
        # talk:31080100:"What's happened to you?"
        assert t310006000_x33(text3=31080100, flag1=flag3, mode4=1)
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t310006000_x54(flag1=_):
    """State 0,1"""
    if not GetEventFlag(flag1):
        """State 3"""
        # talk:31080200:"Ah, why on earth?"
        assert t310006000_x33(text3=31080200, flag1=flag1, mode4=1)
    else:
        """State 2"""
        pass
    """State 4"""
    return 0

def t310006000_x55():
    """State 0,1"""
    if not GetEventFlag(1039409205):
        """State 2"""
        # talk:31001000:"Hello? Is someone there?"
        assert t310006000_x31(text4=31001000, z6=1039409205, mode6=1)
    else:
        """State 3"""
        # talk:31001100:"Hello? Is someone there?"
        assert t310006000_x32(text1=31001100, mode5=1)
    """State 4"""
    # talk:31001200:"Oh, many thanks to you."
    assert t310006000_x57(z1=1039409206, text1=31001200)
    """State 5"""
    return 0

def t310006000_x56():
    """State 0,1"""
    # talk:31001900:"You are most kind, indeed."
    assert t310006000_x32(text1=31001900, mode5=1)
    """State 2"""
    return 0

def t310006000_x57(z1=_, text1=_):
    """State 0,1"""
    # goods:1240:Shabriri Grape
    if ComparePlayerInventoryNumber(3, 1240, 4, 1, 0) == 1:
        """State 2"""
        c1_110()
        """State 3"""
        ClearTalkListData()
        """State 4"""
        # action:23101004:"Give a Shabriri Grape"
        AddTalkListData(1, 23101004, -1)
        # action:23101005:"Don't give a grape"
        AddTalkListData(2, 23101005, -1)
        """State 5"""
        OpenConversationChoicesMenu(0)
        def WhilePaused():
            RequestAnimation(90310, -1)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 6"""
        if GetTalkListEntryResult() == 1:
            """State 7"""
            SetEventFlag(z1, 1)
            """State 8"""
            # goods:1240:Shabriri Grape
            PlayerEquipmentQuantityChange(3, 1240, -1)
            """State 9"""
            def WhilePaused():
                RequestAnimation(90306, -1)
            assert t310006000_x32(text1=text1, mode5=1)
            """State 10"""
            assert t310006000_x83()
            """State 11"""
            return 0
        else:
            pass
    else:
        pass
    """State 12"""
    return 1

def t310006000_x58():
    """State 0,1"""
    if GetEventFlag(1038419205) == 1:
        """State 3"""
        assert t310006000_x60()
    else:
        """State 2"""
        assert t310006000_x59()
    """State 4"""
    return 0

def t310006000_x59():
    """State 0,2"""
    # talk:31001100:"Hello? Is someone there?"
    assert t310006000_x32(text1=31001100, mode5=1)
    """State 1"""
    SetEventFlag(1038419200, 1)
    """State 3"""
    # talk:31001300:"You're not like the others who give me grapes, are you..."
    assert t310006000_x57(z1=1038419205, text1=31001300)
    """State 4"""
    return 0

def t310006000_x60():
    """State 0,1"""
    # talk:31002000:"You are most kind, indeed."
    assert t310006000_x32(text1=31002000, mode5=1)
    """State 2"""
    return 0

def t310006000_x61():
    """State 0,1"""
    if GetEventFlag(1038439206) == 1:
        """State 2"""
        assert t310006000_x63()
    else:
        """State 3"""
        assert t310006000_x62()
    """State 4"""
    return 0

def t310006000_x62():
    """State 0,1"""
    if GetEventFlag(1038439205) == 1:
        """State 3"""
        assert t310006000_x65()
    else:
        """State 2"""
        assert t310006000_x64()
    """State 4"""
    return 0

def t310006000_x63():
    """State 0,1"""
    # talk:31002200:"I apologise. You only did as I asked."
    assert t310006000_x32(text1=31002200, mode5=1)
    """State 2"""
    return 0

def t310006000_x64():
    """State 0,2"""
    # talk:31001100:"Hello? Is someone there?"
    assert t310006000_x32(text1=31001100, mode5=1)
    """State 1"""
    SetEventFlag(1038439200, 1)
    """State 3"""
    # talk:31001400:"Oh, many thanks to you."
    call = t310006000_x57(z1=1038439205, text1=31001400)
    if call.Get() == 1:
        pass
    elif call.Done():
        """State 4"""
        assert t310006000_x66()
    """State 5"""
    return 0

def t310006000_x65():
    """State 0,1"""
    # talk:31002100:"I wonder, what are Shabriri grapes?"
    assert t310006000_x32(text1=31002100, mode5=1)
    """State 2"""
    assert t310006000_x66()
    """State 3"""
    return 0

def t310006000_x66():
    """State 0,7"""
    c1_110()
    """State 1"""
    ClearTalkListData()
    """State 2"""
    # action:23101002:"They're human eyes"
    AddTalkListData(1, 23101002, -1)
    # action:23101003:"Don't say anything"
    AddTalkListData(2, 23101003, -1)
    """State 3"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 4"""
    if GetTalkListEntryResult() == 1:
        """State 5,8"""
        # talk:31001500:"N-No... That's not possible..."
        assert t310006000_x31(text4=31001500, z6=1038439206, mode6=1)
    else:
        """State 6"""
        pass
    """State 9"""
    return 0

def t310006000_x67():
    """State 0,5"""
    SetEventFlag(35009210, 0)
    while True:
        """State 3"""
        if GetEventFlag(35009209) == 1:
            break
        elif GetEventFlag(3392) == 1:
            """State 6"""
            SetEventFlag(35009210, 0)
            """State 10"""
            # actionbutton:6000:"Talk", actionbutton:6230:"Touch Hyetta"
            call = t310006000_x75(actionbutton1=6000, actionbutton2=6230)
            if call.Get() == 1:
                """State 4"""
                SetEventFlag(35009210, 1)
            elif call.Done():
                pass
            elif not GetEventFlag(3392):
                continue
        elif GetEventFlag(3386) == 1:
            """State 2,9"""
            call = t310006000_x52()
            if call.Done():
                pass
            elif not GetEventFlag(3386):
                continue
        else:
            """State 1,8"""
            # actionbutton:6000:"Talk"
            call = t310006000_x0(actionbutton3=6000, flag8=6001, flag12=6000, flag13=6000, flag14=6000,
                                 flag15=6000, flag7=6000)
            if call.Done():
                pass
            elif GetEventFlag(3386) == 1 or GetEventFlag(3392) == 1:
                continue
        """State 11"""
        return 0
    """State 7"""
    Quit()

def t310006000_x68():
    """State 0,1"""
    if not GetEventFlag(1038439209):
        """State 2"""
        # talk:31001700:"Ah, is that you over there?"
        assert t310006000_x31(text4=31001700, z6=1038439209, mode6=1)
    else:
        """State 3"""
        # talk:31002300:"I've gleaned something very important indeed, thanks to you."
        assert t310006000_x32(text1=31002300, mode5=1)
    """State 4"""
    return 0

def t310006000_x69():
    """State 0,1"""
    if GetEventFlag(1036499206) == 1:
        """State 3"""
        assert t310006000_x71()
    else:
        """State 2"""
        assert t310006000_x70()
    """State 4"""
    return 0

def t310006000_x70():
    """State 0,1"""
    if not GetEventFlag(1036499205):
        """State 2"""
        # talk:31003000:"Oh hello, is that you over there?"
        assert t310006000_x31(text4=31003000, z6=1036499205, mode6=1)
    else:
        """State 3"""
        # talk:31003300:"They're special grapes which only grow on those\nwho've been clasped by the burnt Fingers..."
        assert t310006000_x32(text1=31003300, mode5=1)
    """State 4"""
    assert t310006000_x72()
    """State 5"""
    return 0

def t310006000_x71():
    """State 0,1,3"""
    # talk:31003400:"Thank you from the bottom of my heart."
    assert t310006000_x32(text1=31003400, mode5=1)
    """State 4"""
    Label('L0')
    return 0
    """Unused"""
    """State 2"""
    assert t310006000_x73()
    Goto('L0')

def t310006000_x72():
    """State 0,1"""
    # goods:8126:Fingerprint Grape
    if ComparePlayerInventoryNumber(3, 8126, 4, 1, 0) == 1:
        """State 9"""
        c1_110()
        """State 3"""
        ClearTalkListData()
        """State 5"""
        # action:23101006:"Give a Fingerprint Grape"
        AddTalkListData(1, 23101006, -1)
        # action:23101005:"Don't give a grape"
        AddTalkListData(2, 23101005, -1)
        """State 4"""
        OpenConversationChoicesMenu(0)
        def WhilePaused():
            RequestAnimation(90310, -1)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 6"""
        if GetTalkListEntryResult() == 1:
            """State 2,7"""
            SetEventFlag(1036499206, 1)
            SetEventFlag(1036499207, 1)
            """State 8"""
            # goods:8126:Fingerprint Grape
            PlayerEquipmentQuantityChange(3, 8126, -1)
            """State 11"""
            # talk:31003100:"Oh, Oh!"
            def WhilePaused():
                RequestAnimation(90306, -1)
            assert t310006000_x32(text1=31003100, mode5=1)
        else:
            """State 10"""
            pass
    else:
        pass
    """State 12"""
    return 0

def t310006000_x73():
    """State 0,1"""
    # talk:31003200:"Oh, that's right."
    assert t310006000_x31(text4=31003200, z6=1036499207, mode6=1)
    """State 2"""
    # lot:100810:[ERROR]Rya's Necklace
    assert t310006000_x3(lot1=100810)
    """State 3"""
    # talk:31003250:"It's been so long, I don't know how I came upon it,\nbut I've been looking for its owner."
    assert t310006000_x32(text1=31003250, mode5=1)
    """State 4"""
    return 0

def t310006000_x74():
    """State 0,3"""
    if GetEventFlag(35009210) == 1:
        """State 7"""
        assert t310006000_x80()
    else:
        """State 1"""
        if GetEventFlag(35000500) == 1:
            """State 2"""
            if GetEventFlag(35000701) == 1:
                """State 6"""
                def WhilePaused():
                    RequestAnimation(90325, -1)
                assert t310006000_x78()
            else:
                """State 5"""
                def WhilePaused():
                    RequestAnimation(90315, -1)
                assert t310006000_x77()
        else:
            """State 4"""
            def WhilePaused():
                RequestAnimation(90315, -1)
            assert t310006000_x76()
    """State 8"""
    return 0

def t310006000_x75(actionbutton1=6000, actionbutton2=6230):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 6"""
        if GetEventFlag(35009206) == 1 and not GetEventFlag(35000701):
            """State 2"""
            if (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
                IsCharacterDisabled())):
                continue
            elif not GetEventFlag(35009206) or GetEventFlag(35000701) == 1:
                continue
            # actionbutton:6000:"Talk"
            elif CheckActionButtonArea(actionbutton1):
                pass
            # actionbutton:6230:"Touch Hyetta"
            elif CheckActionButtonArea(actionbutton2):
                break
        else:
            """State 5"""
            if (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
                IsCharacterDisabled())):
                continue
            elif GetEventFlag(35009206) == 1 and not GetEventFlag(35000701):
                continue
            # actionbutton:6000:"Talk"
            elif CheckActionButtonArea(actionbutton1):
                pass
        """State 3,7"""
        return 0
    """State 4,8"""
    return 1

def t310006000_x76():
    """State 0,1"""
    if not GetEventFlag(35009205):
        """State 2"""
        # talk:31004000:"Ah, so you're here as well, are you?"
        assert t310006000_x31(text4=31004000, z6=35009205, mode6=1)
    else:
        """State 3"""
        # talk:31004100:"Go to the door ahead, after divesting yourself of your possessions."
        assert t310006000_x32(text1=31004100, mode5=1)
    """State 4"""
    return 0

def t310006000_x77():
    """State 0,1,2"""
    def WhilePaused():
        RequestAnimation(90315, -1)
    assert t310006000_x79()
    """State 3"""
    return 0

def t310006000_x78():
    """State 0,1"""
    if not GetEventFlag(35009208):
        """State 3"""
        # talk:31005300:"..."
        assert t310006000_x31(text4=31005300, z6=35009208, mode6=1)
    else:
        """State 4"""
        # talk:31005400:"Those who gave me grapes howled without words."
        assert t310006000_x31(text4=31005400, z6=35009209, mode6=1)
        """State 5"""
        # talk:31005450:"..."
        assert t310006000_x34(text2=31005450, mode3=1)
        """State 2"""
        def WhilePaused():
            RequestAnimation(90210, -1)
        assert GetCurrentStateElapsedFrames() > 1
    """State 6"""
    return 0

def t310006000_x79():
    """State 0,1"""
    if not GetEventFlag(35009206):
        """State 2"""
        # talk:31005000:"Ahh, the flame of chaos has nestled within you."
        assert t310006000_x31(text4=31005000, z6=35009206, mode6=1)
    else:
        """State 3"""
        # talk:31005200:"Could you please rest your hand upon me?"
        assert t310006000_x32(text1=31005200, mode5=1)
    """State 4"""
    return 0

def t310006000_x80():
    """State 0,1"""
    SetEventFlag(35002705, 1)
    SetEventFlag(35002708, 1)
    call = t310006000_x81()
    def WhilePaused():
        RequestAnimation(90320, -1)
    def ExitPause():
        SetEventFlag(35002705, 0)
        SetEventFlag(35002708, 0)
    if call.Done():
        pass
    elif not GetEventFlag(35002705) or not GetEventFlag(35002708):
        pass
    """State 2"""
    return 0

def t310006000_x81():
    """State 0,1"""
    assert GetEventFlag(35002706) == 1 and GetEventFlag(35002709) == 1
    """State 2"""
    assert t310006000_x82()
    """State 3"""
    return 0

def t310006000_x82():
    """State 0,2"""
    assert GetCurrentStateElapsedTime() > 5
    """State 3"""
    # talk:31005100:"Oh, it burns..."
    def ExitPause():
        SetEventFlag(35000701, 1)
        RequestAnimation(90209, -1)
    assert t310006000_x34(text2=31005100, mode3=1) and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    SetEventFlag(35000701, 1)
    """State 4"""
    return 0

def t310006000_x83():
    """State 0,1"""
    if not GetEventFlag(60810):
        """State 2"""
        # gesture:10:As You Wish
        AcquireGesture(10)
        """State 3"""
        SetEventFlag(60810, 1)
    else:
        pass
    """State 4"""
    return 0

