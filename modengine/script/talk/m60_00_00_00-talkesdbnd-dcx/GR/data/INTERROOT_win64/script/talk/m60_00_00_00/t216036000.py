# -*- coding: utf-8 -*-
def t216036000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t216036000_x5(flag1=3603, flag2=3601, flag3=3602, val1=5, val2=10, val3=12, val4=100, val5=100, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6001, flag7=6001, flag8=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode1=0, mode2=0)
    Quit()

def t216036000_1000():
    """State 0,2,3"""
    assert t216036000_x36()
    """State 1"""
    c1_120(1000)
    Quit()

def t216036000_2000():
    """State 0,1,3"""
    assert t216036000_x35(z1=10, z2=12)
    """State 2"""
    c1_120(2000)
    Quit()

def t216036000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t216036000_x1():
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

def t216036000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t216036000_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t216036000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t216036000_x1()
    else:
        """State 4,7"""
        call = t216036000_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t216036000_x1()
    """State 9"""
    return 0

def t216036000_x4():
    """State 0,1"""
    assert t216036000_x1()
    """State 2"""
    return 0

def t216036000_x5(flag1=3603, flag2=3601, flag3=3602, val1=5, val2=10, val3=12, val4=100, val5=100, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6001, flag7=6001, flag8=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000, mode1=0, mode2=0):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t216036000_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z3=z3, z4=z4, z5=z5, z6=z6, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t216036000_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t216036000_x6(val1=5, val2=10, val3=12, val4=100, val5=100, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6001, flag7=6001, flag8=6000, z3=1, z4=1000000, z5=1000000, z6=1000000, mode1=0,
                  mode2=0):
    """State 0"""
    while True:
        """State 2"""
        call = t216036000_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z4=z4, z5=z5, z6=z6)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t216036000_x13(val1=val1, z3=z3)
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
        elif GetEventFlag(flag6) == 1 and not GetEventFlag(flag7) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t216036000_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t216036000_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t216036000_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t216036000_x7(val2=10, val3=12):
    """State 0,1"""
    call = t216036000_x17(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t216036000_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t216036000_x8(flag1=3603, val2=10, val3=12):
    """State 0,8"""
    assert t216036000_x34()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t216036000_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t216036000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t216036000_x9(actionbutton1=6000, flag4=6000, flag5=6001, z4=1000000, z5=1000000, z6=1000000):
    """State 0,1"""
    call = t216036000_x10(z7=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t216036000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t216036000_x10(z7=_, val6=_):
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

def t216036000_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t216036000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t216036000_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t216036000_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t216036000_x12():
    """State 0,1"""
    assert t216036000_x10(z7=1101, val6=1101)
    """State 2"""
    return 0

def t216036000_x13(val1=5, z3=1):
    """State 0,2"""
    assert t216036000_x23()
    """State 1"""
    call = t216036000_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t216036000_x25()
    """State 4"""
    return 0

def t216036000_x14():
    """State 0,1"""
    assert t216036000_x10(z7=1000, val6=1000)
    """State 2"""
    return 0

def t216036000_x15(val5=100):
    """State 0,1"""
    call = t216036000_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t216036000_x26()
    """State 3"""
    return 0

def t216036000_x16():
    """State 0,1"""
    assert t216036000_x10(z7=1100, val6=1100)
    """State 2"""
    return 0

def t216036000_x17(val2=10, val3=12):
    """State 0,5"""
    assert t216036000_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t216036000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t216036000_x28()
    """Unused"""
    """State 6"""
    return 0

def t216036000_x18():
    """State 0,2"""
    call = t216036000_x10(z7=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t216036000_x19():
    """State 0,1"""
    assert t216036000_x10(z7=1001, val6=1001)
    """State 2"""
    return 0

def t216036000_x20():
    """State 0,1"""
    assert t216036000_x10(z7=1103, val6=1103)
    """State 2"""
    return 0

def t216036000_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t216036000_x22(flag1=3603, flag2=3601, flag3=3602, val1=5, val2=10, val3=12, val4=100, val5=100,
                   actionbutton1=6000, flag4=6000, flag5=6001, flag6=6001, flag7=6001, flag8=6000, z3=1,
                   z4=1000000, z5=1000000, z6=1000000, mode1=0, mode2=0):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t216036000_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z3=z3,
                             z4=z4, z5=z5, z6=z6, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t216036000_x8(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t216036000_x7(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t216036000_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t216036000_x23():
    """State 0,1"""
    assert t216036000_x24()
    """State 2"""
    return 0

def t216036000_x24():
    """State 0,1"""
    assert t216036000_x10(z7=1104, val6=1104)
    """State 2"""
    return 0

def t216036000_x25():
    """State 0,1"""
    call = t216036000_x10(z7=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t216036000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t216036000_x26():
    """State 0,1"""
    call = t216036000_x10(z7=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t216036000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t216036000_x27():
    """State 0,1"""
    call = t216036000_x10(z7=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t216036000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t216036000_x28():
    """State 0,1"""
    call = t216036000_x10(z7=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t216036000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t216036000_x29(text2=_, mode4=1):
    """State 0,4"""
    assert t216036000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text2, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode4:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t216036000_x30(text1=21609000, mode3=1):
    """State 0,4"""
    assert t216036000_x31() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    # talk:21609000:"<howl>"
    TalkToPlayer(text1, -1, -1, 1)
    """State 3"""
    if not mode3:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t216036000_x31():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t216036000_x32():
    """State 0,1"""
    assert t216036000_x10(z7=1002, val6=1002)
    """State 2"""
    return 0

def t216036000_x33():
    """State 0,1"""
    assert t216036000_x1()
    """State 2"""
    return 0

def t216036000_x34():
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

def t216036000_x35(z1=10, z2=12):
    """State 0,1"""
    call = t216036000_x37()
    if call.Done():
        """State 3"""
        return 0
    elif GetEventFlag(1044350719) == 1:
        """State 2"""
        t216036000_x1()
        Quit()

def t216036000_x36():
    """State 0,1"""
    if not GetEventFlag(1044359255):
        """State 2,6"""
        # talk:21610000:"Oh, it's you..."
        assert t216036000_x29(text2=21610000, mode4=1)
        """State 4"""
        SetEventFlag(1044359255, 1)
        """State 5"""
        SetEventFlag(1045379208, 1)
    else:
        """State 3,7"""
        # talk:21610100:"I don't understand. Why would Iji do this..."
        assert t216036000_x29(text2=21610100, mode4=1)
    """State 8"""
    assert t216036000_x39()
    """State 9"""
    return 0

def t216036000_x37():
    """State 0"""
    while True:
        """State 3"""
        call = t216036000_x38()
        if call.Done():
            break
        elif GetEventFlag(1044359257) == 1:
            """State 1,2"""
            SetEventFlag(1044359257, 0)
            """State 4"""
            SetEventFlag(1044359258, 1)
            # talk:21609000:"<howl>"
            assert t216036000_x30(text1=21609000, mode3=1)
    """State 5"""
    return 0

def t216036000_x38():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    assert (t216036000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
            flag4=6000))
    """State 2"""
    return 0

def t216036000_x39():
    """State 0,1"""
    c1_110()
    """State 2"""
    ClearTalkListData()
    """State 3"""
    # action:22161004:"Open the evergaol"
    AddTalkListData(1, 22161004, -1)
    # action:22161005:"Don't open it"
    AddTalkListData(2, 22161005, -1)
    """State 4"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 5"""
    if GetTalkListEntryResult() == 1:
        """State 6"""
        SetEventFlag(1044359260, 1)
    else:
        pass
    """State 7"""
    return 0

