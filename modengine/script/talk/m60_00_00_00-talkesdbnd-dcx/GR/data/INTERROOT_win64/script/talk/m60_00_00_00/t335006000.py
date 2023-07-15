# -*- coding: utf-8 -*-
def t335006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t335006000_x6(flag4=3923, flag5=3921, flag6=3922, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag7=6000, flag8=6001, flag9=6000, flag10=6000, flag11=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode2=1, mode3=1)
    Quit()

def t335006000_1000():
    """State 0,2,3"""
    assert t335006000_x38()
    """State 1"""
    c1_120(1000)
    Quit()

def t335006000_1001():
    """State 0,2,1"""
    c1_120(1001)
    Quit()

def t335006000_1101():
    """State 0,2,3"""
    assert t335006000_x39()
    """State 1"""
    c1_120(1101)
    Quit()

def t335006000_1102():
    """State 0,2,3"""
    t335006000_x40()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t335006000_1103():
    """State 0,2,3"""
    assert t335006000_x41()
    """State 1"""
    c1_120(1103)
    Quit()

def t335006000_2000():
    """State 0,2,3"""
    assert t335006000_x42()
    """State 1"""
    c1_120(2000)
    Quit()

def t335006000_x0(actionbutton1=6000, flag8=6001, flag12=6000, flag13=6000, flag14=6000, flag15=6000,
                  flag7=6000):
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
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t335006000_x1():
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

def t335006000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t335006000_x3(lot1=_):
    """State 0,1"""
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t335006000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t335006000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t335006000_x1()
    else:
        """State 4,7"""
        call = t335006000_x35()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t335006000_x1()
    """State 9"""
    return 0

def t335006000_x5():
    """State 0,1"""
    assert t335006000_x1()
    """State 2"""
    return 0

def t335006000_x6(flag4=3923, flag5=3921, flag6=3922, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag7=6000, flag8=6001, flag9=6000, flag10=6000, flag11=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode2=1, mode3=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t335006000_x23(flag4=flag4, flag5=flag5, flag6=flag6, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag7=flag7, flag8=flag8,
                              flag9=flag9, flag10=flag10, flag11=flag11, z1=z1, z2=z2, z3=z3, z4=z4,
                              mode2=mode2, mode3=mode3)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t335006000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t335006000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag7=6000, flag8=6001,
                  flag9=6000, flag10=6000, flag11=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode2=1,
                  mode3=1):
    """State 0"""
    while True:
        """State 2"""
        call = t335006000_x10(actionbutton1=actionbutton1, flag7=flag7, flag8=flag8, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t335006000_x14(val1=val1, z1=z1)
            def WhilePaused():
                c5_138(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
                GiveSpEffectToPlayer(9640)
                c5_139(1 == (mode2 == 1), -1, 0)
                c5_139(1 == (mode3 == 1), 0, -1)
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
            call = t335006000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t335006000_x27() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t335006000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t335006000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t335006000_x18(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t335006000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t335006000_x9(flag4=3923, val2=10, val3=12):
    """State 0,8"""
    assert t335006000_x37()
    """State 1"""
    if GetEventFlag(flag4) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t335006000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t335006000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t335006000_x10(actionbutton1=6000, flag7=6000, flag8=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t335006000_x11(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t335006000_x0(actionbutton1=actionbutton1, flag8=flag8, flag12=6000, flag13=6000, flag14=6000,
                flag15=6000, flag7=flag7))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t335006000_x11(z6=_, val6=_):
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

def t335006000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t335006000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t335006000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t335006000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t335006000_x13():
    """State 0,1"""
    assert t335006000_x11(z6=1101, val6=1101)
    """State 2"""
    return 0

def t335006000_x14(val1=5, z1=1):
    """State 0,2"""
    assert t335006000_x24()
    """State 1"""
    call = t335006000_x15()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t335006000_x26()
    """State 4"""
    return 0

def t335006000_x15():
    """State 0,1"""
    assert t335006000_x11(z6=1000, val6=1000)
    """State 2"""
    return 0

def t335006000_x16(val5=12):
    """State 0,1"""
    call = t335006000_x17()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t335006000_x27()
    """State 3"""
    return 0

def t335006000_x17():
    """State 0,1"""
    assert t335006000_x11(z6=1100, val6=1100)
    """State 2"""
    return 0

def t335006000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t335006000_x37()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t335006000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t335006000_x29()
    """Unused"""
    """State 6"""
    return 0

def t335006000_x19():
    """State 0,2"""
    call = t335006000_x11(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t335006000_x20():
    """State 0,1"""
    assert t335006000_x11(z6=1001, val6=1001)
    """State 2"""
    return 0

def t335006000_x21():
    """State 0,1"""
    assert t335006000_x11(z6=1103, val6=1103)
    """State 2"""
    return 0

def t335006000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t335006000_x23(flag4=3923, flag5=3921, flag6=3922, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag7=6000, flag8=6001, flag9=6000, flag10=6000, flag11=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t335006000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag7=flag7, flag8=flag8, flag9=flag9, flag10=flag10, flag11=flag11, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode2=mode2, mode3=mode3)
        if CheckSelfDeath() == 1 or GetEventFlag(flag4) == 1:
            """State 3"""
            Label('L0')
            call = t335006000_x9(flag4=flag4, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag4):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag5) == 1 or GetEventFlag(flag6) == 1:
            """State 2"""
            call = t335006000_x8(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag4) == 1:
                Goto('L0')
            elif not GetEventFlag(flag5) and not GetEventFlag(flag6):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t335006000_x36() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t335006000_x24():
    """State 0,1"""
    assert t335006000_x25()
    """State 2"""
    return 0

def t335006000_x25():
    """State 0,1"""
    assert t335006000_x11(z6=1104, val6=1104)
    """State 2"""
    return 0

def t335006000_x26():
    """State 0,1"""
    call = t335006000_x11(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t335006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t335006000_x27():
    """State 0,1"""
    call = t335006000_x11(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t335006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t335006000_x28():
    """State 0,1"""
    call = t335006000_x11(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t335006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t335006000_x29():
    """State 0,1"""
    call = t335006000_x11(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t335006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t335006000_x30(text4=_, z5=_, mode7=1):
    """State 0,5"""
    assert t335006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text4, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode7:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(z5, 1)
    """State 6"""
    return 0

def t335006000_x31(text3=_, mode6=1):
    """State 0,4"""
    assert t335006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text3, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode6:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t335006000_x32(text2=_, flag1=_, mode5=1):
    """State 0,5"""
    assert t335006000_x34() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(flag1, 1)
    """State 1"""
    TalkToPlayer(text2, -1, -1, 1)
    """State 4"""
    if not mode5:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t335006000_x33(text1=33580300, mode4=1):
    """State 0,4"""
    assert t335006000_x34() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    # talk:33580300:"You base, facile, uncharitable bastard…"
    TalkToPlayer(text1, -1, -1, 1)
    """State 3"""
    if not mode4:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t335006000_x34():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t335006000_x35():
    """State 0,1"""
    assert t335006000_x11(z6=1002, val6=1002)
    """State 2"""
    return 0

def t335006000_x36():
    """State 0,1"""
    assert t335006000_x1()
    """State 2"""
    return 0

def t335006000_x37():
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

def t335006000_x38():
    """State 0,1"""
    if GetEventFlag(3925) == 1:
        """State 3"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t335006000_x43()
    elif GetEventFlag(3926) == 1:
        """State 4"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t335006000_x44()
    elif GetEventFlag(3928) == 1:
        """State 5"""
        assert t335006000_x73()
    elif GetEventFlag(3929) == 1:
        """State 6"""
        assert t335006000_x74()
    else:
        """State 2"""
        pass
    """State 7"""
    return 0

def t335006000_x39():
    """State 0,1"""
    if GetEventFlag(3925) == 1:
        """State 3"""
        assert t335006000_x71(flag2=1041382740, flag3=1041382741)
    elif GetEventFlag(3926) == 1:
        """State 4"""
        assert t335006000_x71(flag2=1049552700, flag3=1049552701)
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t335006000_x40():
    """State 0,2"""
    if GetEventFlag(3925) == 1:
        """State 4"""
        assert t335006000_x72(flag1=1041389452)
    elif GetEventFlag(3926) == 1:
        """State 5"""
        assert t335006000_x72(flag1=1049549002)
    else:
        """State 3"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 6"""
    return 0

def t335006000_x41():
    """State 0,1"""
    # talk:33580300:"You base, facile, uncharitable bastard…"
    assert t335006000_x33(text1=33580300, mode4=1)
    """State 2"""
    return 0

def t335006000_x42():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    assert (t335006000_x0(actionbutton1=6000, flag8=6001, flag12=6000, flag13=6000, flag14=6000, flag15=6000,
            flag7=6000))
    """State 2"""
    return 0

def t335006000_x43():
    """State 0,3,1"""
    if GetEventFlag(1041389456) == 1:
        """State 2"""
        if GetEventFlag(1041389457) == 1:
            """State 6"""
            assert t335006000_x47()
        else:
            """State 5"""
            assert t335006000_x46()
    else:
        """State 4"""
        assert t335006000_x45()
    """State 8"""
    Label('L0')
    return 0
    """Unused"""
    """State 7"""
    assert t335006000_x61()
    Goto('L0')

def t335006000_x44():
    """State 0,1,3"""
    assert t335006000_x63()
    """State 4"""
    Label('L0')
    return 0
    """Unused"""
    """State 2"""
    assert t335006000_x62()
    Goto('L0')

def t335006000_x45():
    """State 0,1"""
    if GetEventFlag(1041389455) == 1:
        """State 3"""
        # talk:33500500:"What? Taken an interest in the finer things, after all?"
        assert t335006000_x31(text3=33500500, mode6=1)
    else:
        """State 2"""
        # talk:33500100:"Hm."
        assert t335006000_x31(text3=33500100, mode6=1)
    """State 4"""
    assert t335006000_x49()
    """State 5"""
    return 0

def t335006000_x46():
    """State 0,1"""
    if ComparePlayerInventoryNumber(3, 22000, 4, 1, 0) == 1:
        """State 3"""
        assert t335006000_x48()
    else:
        """State 2"""
        # talk:33500300:"Go ahead and bring me some slumber fog, my compeer."
        assert t335006000_x31(text3=33500300, mode6=1)
    """State 4"""
    return 0

def t335006000_x47():
    """State 0,2"""
    if not GetEventFlag(1041389463):
        """State 5"""
        # talk:33501300:"Bring me more slumber fog, my compeer."
        assert t335006000_x30(text4=33501300, z5=1041389463, mode7=1)
        """State 1"""
        Label('L0')
        SetEventFlag(1041382742, 1)
    else:
        """State 3"""
        if not GetEventFlag(1041382742):
            """State 6"""
            # talk:33501600:"Oh, hello there."
            assert t335006000_x31(text3=33501600, mode6=1)
            """State 4"""
            SetEventFlag(1041380741, 1)
            Goto('L0')
        else:
            """State 7"""
            # talk:33501500:"Did you forget something?"
            assert t335006000_x31(text3=33501500, mode6=1)
    """State 8"""
    assert t335006000_x50(mode1=0)
    """State 9"""
    return 0

def t335006000_x48():
    """State 0,6"""
    # talk:33501000:"Ah, I've been eagerly awaiting your return."
    assert t335006000_x31(text3=33501000, mode6=1)
    """State 5"""
    c1_110()
    """State 2"""
    ClearTalkListData()
    """State 3"""
    AddTalkListData(1, 23351002, -1)
    """State 4"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 1"""
    if ComparePlayerInventoryNumber(3, 22000, 4, 2, 0) == 1:
        """State 7"""
        # talk:33501200:"I see, I see. You have what I asked."
        assert t335006000_x30(text4=33501200, z5=1041389457, mode7=1)
        """State 9"""
        assert t335006000_x3(lot1=102510)
    else:
        """State 8"""
        # talk:33501100:"Hmm, not quite enough."
        assert t335006000_x31(text3=33501100, mode6=1)
    """State 10"""
    return 0

def t335006000_x49():
    """State 0,5"""
    c1_110()
    """State 1"""
    ClearTalkListData()
    """State 2"""
    AddTalkListData(1, 23350000, -1)
    # action:23351001:""
    AddTalkListData(2, 23351001, -1)
    """State 3"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 4"""
    if GetTalkListEntryResult() == 1:
        """State 6"""
        if GetEventFlag(400250) == 1:
            """State 11"""
            # talk:33500250:"You'll help me then?"
            assert t335006000_x30(text4=33500250, z5=1041389456, mode7=1)
        else:
            """State 7"""
            # talk:33500200:"You'll help me then?"
            assert t335006000_x30(text4=33500200, z5=1041389456, mode7=1)
            """State 9"""
            assert t335006000_x3(lot1=102500)
            """State 10"""
            # talk:33500210:"That, is St. Trina's Crystal Ball."
            assert t335006000_x31(text3=33500210, mode6=1)
    elif GetTalkListEntryResult() == 2:
        """State 8"""
        # talk:33500400:"You what? You hardly know what you're missing out on."
        assert t335006000_x30(text4=33500400, z5=1041389455, mode7=1)
    else:
        pass
    """State 12"""
    return 0

def t335006000_x50(mode1=_):
    """State 0"""
    while Loop('mainloop'):
        """State 2"""
        c1_110()
        while True:
            """State 1"""
            Label('L0')
            ClearTalkListData()
            if mode1 == 1:
                """State 10"""
                assert t335006000_x64()
            else:
                """State 6"""
                assert t335006000_x51()
            """State 3"""
            ShowShopMessage(1)
            assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 4"""
            if GetTalkListEntryResult() == 1:
                Break('mainloop')
            elif GetTalkListEntryResult() == 2:
                """State 7"""
                assert t335006000_x52()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 3:
                """State 8"""
                assert t335006000_x59()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 4:
                """State 12"""
                assert t335006000_x69()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 5:
                """State 13"""
                assert t335006000_x70()
                Continue('mainloop')
            else:
                """State 5"""
                if not GetEventFlag(1041389462) and GetEventFlagValue(1041389470, 10) > 5:
                    """State 11"""
                    # talk:33501700:"You certainly have a taste for spirits."
                    assert t335006000_x30(text4=33501700, z5=1041389462, mode7=1)
                else:
                    pass
                """State 14"""
                return 0
    """State 9"""
    assert t335006000_x60()
    Goto('L0')

def t335006000_x51():
    """State 0,1"""
    AddTalkListData(1, 23350001, -1)
    """State 3"""
    assert t335006000_x53()
    """State 2"""
    # action:20000009:"Leave"
    AddTalkListData(99, 20000009, -1)
    """State 4"""
    return 0

def t335006000_x52():
    """State 0,1"""
    # talk:33501400:"Allow me a little advice, my compeer."
    assert t335006000_x30(text4=33501400, z5=1041389459, mode7=1)
    """State 2"""
    return 0

def t335006000_x53():
    """State 0,1"""
    assert t335006000_x54()
    """State 2"""
    assert t335006000_x55()
    """State 3"""
    assert t335006000_x56()
    """State 4"""
    return 0

def t335006000_x54():
    """State 0,1"""
    SetEventFlag(1041389458, 0)
    SetEventFlag(1041389460, 0)
    """State 2"""
    assert t335006000_x57()
    """State 3"""
    assert t335006000_x58()
    """State 4"""
    return 0

def t335006000_x55():
    """State 0,1"""
    return 0

def t335006000_x56():
    """State 0,1"""
    AddTalkListDataIf(GetEventFlag(1049549006) == 1, 4, 23351003, -1)
    AddTalkListDataIf(GetEventFlag(1041389458) == 1, 2, 23351000, -1)
    AddTalkListDataIf(GetEventFlag(1041389460) == 1, 3, 23351002, -1)
    AddTalkListDataIf(GetEventFlag(1049549008) == 1, 5, 23351004, -1)
    """State 2"""
    return 0

def t335006000_x57():
    """State 0,1"""
    SetEventFlagIf(not GetEventFlag(1041389459), 1041389458, 1)
    """State 2"""
    return 0

def t335006000_x58():
    """State 0,1"""
    SetEventFlagIf(not GetEventFlag(1041389461), 1041389460, 1)
    """State 2"""
    return 0

def t335006000_x59():
    """State 0,1"""
    # talk:33502000:"As you surely know, my compeer, I am but a humble man of the cloth."
    assert t335006000_x30(text4=33502000, z5=1041389461, mode7=1)
    """State 2"""
    return 0

def t335006000_x60():
    """State 0,1"""
    while True:
        """State 2"""
        ClearTalkActionState()
        if not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            break
        elif not GetEventFlagValue(1041389470, 10) > 5 and DidYouDoSomethingInTheMenu(0) == 1:
            """State 3"""
            SetEventFlagValue(1041389470, 10, GetEventFlagValue(1041389470, 10) + 1)
    """State 4"""
    return 0

def t335006000_x61():
    """State 0,1"""
    # talk:33501900:"..."
    assert t335006000_x31(text3=33501900, mode6=1)
    """State 2"""
    return 0

def t335006000_x62():
    """State 0,1"""
    # talk:33503400:"..."
    assert t335006000_x31(text3=33503400, mode6=1)
    """State 2"""
    return 0

def t335006000_x63():
    """State 0,1"""
    if not GetEventFlag(1049549005):
        """State 4"""
        # talk:33503000:"Ah, good to see you."
        assert t335006000_x30(text4=33503000, z5=1049549005, mode7=1)
        """State 3"""
        Label('L0')
        SetEventFlag(1049552702, 1)
    else:
        """State 2"""
        if not GetEventFlag(1049552702):
            """State 5"""
            # talk:33503200:"Oh it's, good, good to see you."
            assert t335006000_x31(text3=33503200, mode6=1)
            Goto('L0')
        else:
            """State 6"""
            # talk:33503100:"Did you need something else?"
            assert t335006000_x31(text3=33503100, mode6=1)
    """State 7"""
    assert t335006000_x50(mode1=1)
    """State 8"""
    return 0

def t335006000_x64():
    """State 0,1"""
    AddTalkListData(1, 23350001, -1)
    """State 3"""
    assert t335006000_x65()
    """State 2"""
    # action:20000009:"Leave"
    AddTalkListData(99, 20000009, -1)
    """State 4"""
    return 0

def t335006000_x65():
    """State 0,1"""
    assert t335006000_x66()
    """State 2"""
    assert t335006000_x67()
    """State 3"""
    assert t335006000_x56()
    """State 4"""
    return 0

def t335006000_x66():
    """State 0,1"""
    SetEventFlag(1041389458, 0)
    SetEventFlag(1041389460, 0)
    SetEventFlag(1049549006, 0)
    SetEventFlag(1049549008, 0)
    """State 2"""
    assert t335006000_x57()
    """State 3"""
    assert t335006000_x58()
    """State 4"""
    assert t335006000_x68()
    """State 5"""
    return 0

def t335006000_x67():
    """State 0,1"""
    return 0

def t335006000_x68():
    """State 0,1"""
    SetEventFlagIf(not GetEventFlag(1049549007), 1049549006, 1)
    SetEventFlagIf(GetEventFlag(1049549007) == 1, 1049549008, 1)
    """State 2"""
    return 0

def t335006000_x69():
    """State 0,1"""
    # talk:33504000:"You know, a holy personage was once abducted from these lands."
    assert t335006000_x30(text4=33504000, z5=1049549007, mode7=1)
    """State 2"""
    return 0

def t335006000_x70():
    """State 0,1"""
    # talk:33504100:"You know, a holy personage was once abducted from these lands."
    assert t335006000_x31(text3=33504100, mode6=1)
    """State 2"""
    return 0

def t335006000_x71(flag2=_, flag3=_):
    """State 0,1"""
    if not GetEventFlag(flag2):
        """State 3"""
        # talk:33580000:"..."
        assert t335006000_x32(text2=33580000, flag1=flag2, mode5=1)
    elif not GetEventFlag(flag3):
        """State 4"""
        # talk:33580010:"Have you lost your marbles?"
        assert t335006000_x32(text2=33580010, flag1=flag3, mode5=1)
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t335006000_x72(flag1=_):
    """State 0,1"""
    if not GetEventFlag(flag1):
        """State 3"""
        # talk:33580100:"Haven't you Tarnished any respect?"
        t335006000_x32(text2=33580100, flag1=flag1, mode5=1)
        Quit()
    else:
        """State 2"""
        Quit()
    """Unused"""
    """State 4"""
    return 0

def t335006000_x73():
    """State 0,1"""
    if GetEventFlag(12059055) == 1:
        """State 2"""
        # talk:33505100:"I have partaken of untold secrets."
        assert t335006000_x31(text3=33505100, mode6=1)
    else:
        """State 3"""
        # talk:33505000:"Finally, I have found it!"
        assert t335006000_x30(text4=33505000, z5=12059055, mode7=1)
    """State 4"""
    return 0

def t335006000_x74():
    """State 0,1"""
    # talk:33506000:"..."
    assert t335006000_x31(text3=33506000, mode6=1)
    """State 2"""
    return 0

