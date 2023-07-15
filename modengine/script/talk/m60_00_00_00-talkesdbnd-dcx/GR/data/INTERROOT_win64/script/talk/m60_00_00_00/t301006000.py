# -*- coding: utf-8 -*-
def t301006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t301006000_x6(flag4=3183, flag5=3181, flag6=3182, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag7=6000, flag8=6001, flag9=6000, flag10=6000, flag11=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t301006000_1000():
    """State 0,2,3"""
    assert t301006000_x38()
    """State 1"""
    c1_120(1000)
    Quit()

def t301006000_1001():
    """State 0,2,3"""
    assert t301006000_x39()
    """State 1"""
    c1_120(1001)
    Quit()

def t301006000_1101():
    """State 0,2,3"""
    assert t301006000_x40()
    """State 1"""
    c1_120(1101)
    Quit()

def t301006000_1102():
    """State 0,2,3"""
    t301006000_x41()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t301006000_1103():
    """State 0,2,3"""
    assert t301006000_x42()
    """State 1"""
    c1_120(1103)
    Quit()

def t301006000_2000():
    """State 0,2,3"""
    assert t301006000_x43()
    """State 1"""
    c1_120(2000)
    Quit()

def t301006000_x0(actionbutton1=_, flag8=6001, flag12=6000, flag13=6000, flag14=6000, flag15=6000, flag7=6000):
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
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t301006000_x1():
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

def t301006000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t301006000_x3(lot1=_):
    """State 0,1"""
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t301006000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t301006000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t301006000_x1()
    else:
        """State 4,7"""
        call = t301006000_x35()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t301006000_x1()
    """State 9"""
    return 0

def t301006000_x5():
    """State 0,1"""
    assert t301006000_x1()
    """State 2"""
    return 0

def t301006000_x6(flag4=3183, flag5=3181, flag6=3182, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag7=6000, flag8=6001, flag9=6000, flag10=6000, flag11=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t301006000_x23(flag4=flag4, flag5=flag5, flag6=flag6, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag7=flag7, flag8=flag8,
                              flag9=flag9, flag10=flag10, flag11=flag11, z1=z1, z2=z2, z3=z3, z4=z4,
                              mode1=mode1, mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t301006000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t301006000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag7=6000, flag8=6001,
                  flag9=6000, flag10=6000, flag11=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t301006000_x10(actionbutton1=actionbutton1, flag7=flag7, flag8=flag8, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t301006000_x14(val1=val1, z1=z1)
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
            call = t301006000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t301006000_x27() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t301006000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t301006000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t301006000_x18(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t301006000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t301006000_x9(flag4=3183, val2=10, val3=12):
    """State 0,8"""
    assert t301006000_x37()
    """State 1"""
    if GetEventFlag(flag4) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t301006000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t301006000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t301006000_x10(actionbutton1=6000, flag7=6000, flag8=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t301006000_x11(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t301006000_x0(actionbutton1=actionbutton1, flag8=flag8, flag12=6000, flag13=6000, flag14=6000,
                flag15=6000, flag7=flag7))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t301006000_x11(z6=_, val6=_):
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

def t301006000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t301006000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t301006000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t301006000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t301006000_x13():
    """State 0,1"""
    assert t301006000_x11(z6=1101, val6=1101)
    """State 2"""
    return 0

def t301006000_x14(val1=5, z1=1):
    """State 0,2"""
    assert t301006000_x24()
    """State 1"""
    call = t301006000_x15()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t301006000_x26()
    """State 4"""
    return 0

def t301006000_x15():
    """State 0,1"""
    assert t301006000_x11(z6=1000, val6=1000)
    """State 2"""
    return 0

def t301006000_x16(val5=12):
    """State 0,1"""
    call = t301006000_x17()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t301006000_x27()
    """State 3"""
    return 0

def t301006000_x17():
    """State 0,1"""
    assert t301006000_x11(z6=1100, val6=1100)
    """State 2"""
    return 0

def t301006000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t301006000_x37()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t301006000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t301006000_x29()
    """Unused"""
    """State 6"""
    return 0

def t301006000_x19():
    """State 0,2"""
    call = t301006000_x11(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t301006000_x20():
    """State 0,1"""
    assert t301006000_x11(z6=1001, val6=1001)
    """State 2"""
    return 0

def t301006000_x21():
    """State 0,1"""
    assert t301006000_x11(z6=1103, val6=1103)
    """State 2"""
    return 0

def t301006000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t301006000_x23(flag4=3183, flag5=3181, flag6=3182, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag7=6000, flag8=6001, flag9=6000, flag10=6000, flag11=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t301006000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag7=flag7, flag8=flag8, flag9=flag9, flag10=flag10, flag11=flag11, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag4) == 1:
            """State 3"""
            Label('L0')
            call = t301006000_x9(flag4=flag4, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag4):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag5) == 1 or GetEventFlag(flag6) == 1:
            """State 2"""
            call = t301006000_x8(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag4) == 1:
                Goto('L0')
            elif not GetEventFlag(flag5) and not GetEventFlag(flag6):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t301006000_x36() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t301006000_x24():
    """State 0,1"""
    assert t301006000_x25()
    """State 2"""
    return 0

def t301006000_x25():
    """State 0,1"""
    assert t301006000_x11(z6=1104, val6=1104)
    """State 2"""
    return 0

def t301006000_x26():
    """State 0,1"""
    call = t301006000_x11(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t301006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t301006000_x27():
    """State 0,1"""
    call = t301006000_x11(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t301006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t301006000_x28():
    """State 0,1"""
    call = t301006000_x11(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t301006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t301006000_x29():
    """State 0,1"""
    call = t301006000_x11(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t301006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t301006000_x30(text4=_, z5=_, mode6=1):
    """State 0,5"""
    assert t301006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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
    SetEventFlag(z5, 1)
    """State 6"""
    return 0

def t301006000_x31(text3=_, mode5=1):
    """State 0,4"""
    assert t301006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text3, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode5:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t301006000_x32(text1=_, flag1=_, mode4=1):
    """State 0,5"""
    assert t301006000_x34() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(flag1, 1)
    """State 1"""
    TalkToPlayer(text1, -1, -1, 1)
    """State 4"""
    if not mode4:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t301006000_x33(text2=_, mode3=1):
    """State 0,4"""
    assert t301006000_x34() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t301006000_x34():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t301006000_x35():
    """State 0,1"""
    assert t301006000_x11(z6=1002, val6=1002)
    """State 2"""
    return 0

def t301006000_x36():
    """State 0,1"""
    assert t301006000_x1()
    """State 2"""
    return 0

def t301006000_x37():
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

def t301006000_x38():
    """State 0,1"""
    if GetEventFlag(3185) == 1:
        """State 3"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t301006000_x44()
    elif GetEventFlag(3187) == 1:
        """State 4"""
        assert t301006000_x45()
    elif GetEventFlag(3191) == 1:
        """State 8"""
        assert t301006000_x58()
    elif GetEventFlag(3188) == 1:
        """State 5"""
        assert t301006000_x46()
    elif GetEventFlag(3189) == 1:
        """State 6"""
        assert t301006000_x47()
    elif GetEventFlag(3190) == 1:
        """State 7"""
        assert t301006000_x48()
    else:
        """State 2"""
        pass
    """State 9"""
    return 0

def t301006000_x39():
    """State 0,1"""
    if not GetEventFlag(1035449235):
        """State 2,4"""
        # talk:30180400:"You will die nameless, without ceremony."
        assert t301006000_x33(text2=30180400, mode3=1)
    else:
        """State 3,5"""
        # talk:30180500:"How does it feel to die a failure?"
        assert t301006000_x33(text2=30180500, mode3=1)
    """State 6"""
    return 0

def t301006000_x40():
    """State 0,1,2"""
    assert t301006000_x56(flag2=1042362700, flag3=1042362701)
    """State 3"""
    return 0

def t301006000_x41():
    """State 0,2"""
    if not GetEventFlag(1035449235):
        """State 4"""
        # talk:30180200:"Very well."
        assert t301006000_x57(text1=30180200, flag1=1042369205)
    elif True:
        """State 5"""
        # talk:30180300:"You disappoint me."
        assert t301006000_x57(text1=30180300, flag1=1042369205)
    else:
        """State 3"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 6"""
    return 0

def t301006000_x42():
    """State 0,1"""
    if not GetEventFlag(1035449235):
        """State 2,4"""
        # talk:30180600:"You maidenless runt..."
        assert t301006000_x33(text2=30180600, mode3=1)
    else:
        """State 3,5"""
        # talk:30180700:"Luminary Mohg..."
        assert t301006000_x33(text2=30180700, mode3=1)
    """State 6"""
    return 0

def t301006000_x43():
    """State 0,1"""
    if GetEventFlag(3190) == 1 and GetEventFlag(1035449225) == 1 and not GetEventFlag(1035449227):
        """State 2,4"""
        # actionbutton:6470:"Offer finger"
        assert (t301006000_x0(actionbutton1=6470, flag8=6001, flag12=6000, flag13=6000, flag14=6000,
                flag15=6000, flag7=6000))
    else:
        """State 3,5"""
        # actionbutton:6000:"Talk"
        assert (t301006000_x0(actionbutton1=6000, flag8=6001, flag12=6000, flag13=6000, flag14=6000,
                flag15=6000, flag7=6000))
    """State 6"""
    return 0

def t301006000_x44():
    """State 0,1"""
    if GetEventFlag(1042369206) == 1:
        """State 2"""
        if GetEventFlag(1042369207) == 1:
            """State 3"""
            if not GetEventFlag(1042369208):
                """State 6"""
                # talk:30101300:"Grace's guidance will reveal the path forward, most certainly."
                assert t301006000_x30(text4=30101300, z5=1042369208, mode6=1)
            else:
                """State 7"""
                # talk:30101400:"It's time you set off, I should think."
                assert t301006000_x31(text3=30101400, mode5=1)
        else:
            """State 5"""
            # talk:30101200:"Luckily for you, however, there is one shining ray of hope for even the maidenless."
            assert t301006000_x30(text4=30101200, z5=1042369207, mode6=1)
    else:
        """State 4"""
        # talk:30101100:"Oh, yes... Tarnished, are we?"
        assert t301006000_x30(text4=30101100, z5=1042369206, mode6=1)
    """State 8"""
    return 0

def t301006000_x45():
    """State 0,1"""
    if not GetEventFlag(1042369226):
        """State 3,4"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t301006000_x49()
    else:
        """State 2,5"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t301006000_x51()
    """State 6"""
    return 0

def t301006000_x46():
    """State 0,1"""
    if not GetEventFlag(1035449206):
        """State 2"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t301006000_x52()
    else:
        """State 3"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t301006000_x53()
    """State 4"""
    return 0

def t301006000_x47():
    """State 0,1"""
    if not GetEventFlag(1035449216):
        """State 4"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t301006000_x54()
    else:
        """State 2,3"""
        # talk:30105800:"The cloth is your final trial. Soak it with the blood of a maiden."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t301006000_x31(text3=30105800, mode5=1)
    """State 5"""
    return 0

def t301006000_x48():
    """State 0,1"""
    if not GetEventFlag(1035449225):
        """State 2,9"""
        # talk:30105400:"Ahh, my lambkin."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t301006000_x31(text3=30105400, mode5=1)
        """State 6"""
        SetEventFlag(1035449225, 1)
    elif not GetEventFlag(1035449227):
        """State 3,10"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t301006000_x60()
    elif not GetEventFlag(1035449226):
        """State 5,7"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t301006000_x55()
    else:
        """State 4,8"""
        # talk:30105700:"Ahh, it is trying, but we must be patient."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t301006000_x31(text3=30105700, mode5=1)
    """State 11"""
    return 0

def t301006000_x49():
    """State 0,1"""
    if not GetEventFlag(1042369225):
        """State 2,4"""
        # talk:30102000:"Ohh, well done, well done indeed."
        assert t301006000_x31(text3=30102000, mode5=1)
    else:
        """State 3,5"""
        # talk:30102400:"Oh, have you decided to have a go after all? At joining the Roundtable proper?"
        assert t301006000_x31(text3=30102400, mode5=1)
    """State 6"""
    assert t301006000_x50()
    """State 7"""
    return 0

def t301006000_x50():
    """State 0,1"""
    ClearTalkListData()
    c1_110()
    """State 2"""
    # action:23011000:"I'll fly straight and true!"
    AddTalkListData(1, 23011000, -1)
    # action:23011001:"I don't need a seat"
    AddTalkListData(2, 23011001, -1)
    """State 3"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 4"""
    if GetTalkListEntryResult() == 1:
        """State 5,10"""
        # talk:30102100:"Ahh, then you're interested? A wise choice indeed."
        assert t301006000_x31(text3=30102100, mode5=1)
        """State 7"""
        SetEventFlag(1042369226, 1)
    elif GetTalkListEntryResult() == 2:
        """State 6,11"""
        # talk:30102300:"..."
        assert t301006000_x31(text3=30102300, mode5=1)
        """State 9"""
        SetEventFlag(1042369225, 1)
    else:
        """State 8"""
        pass
    """State 12"""
    return 0

def t301006000_x51():
    """State 0,1"""
    if not GetEventFlag(1042369227):
        """State 2,5"""
        # talk:30102200:"Challenge Godrick the Grafted, lord of Stormveil, to acquire a Great Rune."
        assert t301006000_x31(text3=30102200, mode5=1)
        """State 4"""
        SetEventFlag(1042369227, 1)
    else:
        """State 3,6"""
        # talk:30102500:"What's the matter?"
        assert t301006000_x31(text3=30102500, mode5=1)
    """State 7"""
    return 0

def t301006000_x52():
    """State 0,1"""
    if not GetEventFlag(1035449205) and not GetEventFlag(1042369235):
        """State 2,16"""
        # talk:30103000:"Ah, there you are."
        assert t301006000_x31(text3=30103000, mode5=1)
        """State 4"""
        Label('L0')
        ClearTalkListData()
        c1_110()
        """State 5"""
        # action:23011002:"They didn't seem right"
        AddTalkListData(1, 23011002, -1)
        # action:23011003:"They were magnificent"
        AddTalkListData(2, 23011003, -1)
    elif not GetEventFlag(1035449205) and GetEventFlag(1042369235) == 1:
        """State 15,20"""
        # talk:30103010:"Ah, there you are."
        assert t301006000_x31(text3=30103010, mode5=1)
        Goto('L0')
    else:
        """State 3,17"""
        # talk:30103500:"Oh? Is something wrong?"
        assert t301006000_x31(text3=30103500, mode5=1)
        """State 13"""
        ClearTalkListData()
        c1_110()
        """State 14"""
        # action:23011006:"Two Fingers seemed off"
        AddTalkListData(1, 23011006, -1)
        # action:23011007:"They were magnificent"
        AddTalkListData(2, 23011007, -1)
    """State 6"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 7"""
    if GetTalkListEntryResult() == 1:
        """State 8,18"""
        # talk:30103100:"Ah-ha, your intuition serves you well."
        assert t301006000_x31(text3=30103100, mode5=1)
        """State 10"""
        SetEventFlag(1035449206, 1)
    elif GetTalkListEntryResult() == 2:
        """State 9,19"""
        # talk:30103400:"You don't say. Well, what a relief that must be."
        assert t301006000_x31(text3=30103400, mode5=1)
        """State 12"""
        SetEventFlag(1035449205, 1)
    else:
        """State 11"""
        pass
    """State 21"""
    return 0

def t301006000_x53():
    """State 0,1"""
    if not GetEventFlag(1035449207):
        """State 2,7"""
        # talk:30103200:"Oh, I have a gift for you, something fit only for the wise."
        assert t301006000_x31(text3=30103200, mode5=1)
        """State 4"""
        SetEventFlag(1035449207, 1)
        """State 9"""
        # lot:100300:Festering Bloody Finger
        assert t301006000_x3(lot1=100300)
        """State 10"""
        # talk:30103300:"A means for circumventing the draw of the Two Fingers."
        assert t301006000_x31(text3=30103300, mode5=1)
    elif not GetEventFlag(1035449208):
        """State 3,8"""
        # talk:30103600:"Be sure to try that finger I gave you."
        assert t301006000_x31(text3=30103600, mode5=1)
        """State 6"""
        SetEventFlag(1035449208, 1)
    else:
        """State 5,11"""
        # talk:30103700:"Be sure to try that finger I gave you."
        assert t301006000_x31(text3=30103700, mode5=1)
    """State 12"""
    return 0

def t301006000_x54():
    """State 0,9"""
    if not GetEventFlag(1035449215):
        """State 10,17"""
        # talk:30105000:"Oh, lambkin, so pleased you're here."
        assert t301006000_x31(text3=30105000, mode5=1)
    else:
        """State 11,18"""
        # talk:30105300:"Oh, it's you."
        assert t301006000_x31(text3=30105300, mode5=1)
    """State 1"""
    ClearTalkListData()
    c1_110()
    """State 2"""
    # action:23011004:"Anoint me"
    AddTalkListData(1, 23011004, -1)
    # action:23011005:"I refuse"
    AddTalkListData(2, 23011005, -1)
    """State 3"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 4"""
    if GetTalkListEntryResult() == 1:
        """State 5,13"""
        # talk:30105100:"Mm, yes, who would have it any other way?"
        assert t301006000_x31(text3=30105100, mode5=1)
        """State 7"""
        SetEventFlag(1035449216, 1)
        """State 15"""
        # lot:100310:Lord of Blood's Favor
        assert t301006000_x3(lot1=100310)
        """State 16"""
        # talk:30105105:"For your final trial. Soak the cloth with a maiden's blood."
        assert t301006000_x31(text3=30105105, mode5=1)
    elif GetTalkListEntryResult() == 2:
        """State 6,14"""
        # talk:30105200:"Oh my, perhaps you misheard me."
        assert t301006000_x31(text3=30105200, mode5=1)
        """State 12"""
        SetEventFlag(1035449215, 1)
    else:
        """State 8"""
        pass
    """State 19"""
    return 0

def t301006000_x55():
    """State 0,2"""
    # talk:30105500:"Oh, another thing. You should have this."
    assert t301006000_x31(text3=30105500, mode5=1)
    """State 1"""
    SetEventFlag(1035449226, 1)
    """State 3"""
    # lot:100320:Pureblood Knight's Medal
    assert t301006000_x3(lot1=100320)
    """State 4"""
    # talk:30105600:"A medal granted by the new Mohgwyn dynasty."
    assert t301006000_x31(text3=30105600, mode5=1)
    """State 5"""
    return 0

def t301006000_x56(flag2=1042362700, flag3=1042362701):
    """State 0,1"""
    if not GetEventFlag(flag2):
        """State 3"""
        # talk:30180000:"Oh?"
        assert t301006000_x32(text1=30180000, flag1=flag2, mode4=1)
    elif not GetEventFlag(flag3):
        """State 4"""
        # talk:30180100:"Do you even comprehend?"
        assert t301006000_x32(text1=30180100, flag1=flag3, mode4=1)
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t301006000_x57(text1=_, flag1=1042369205):
    """State 0,1"""
    if not GetEventFlag(flag1):
        """State 4"""
        assert t301006000_x32(text1=text1, flag1=flag1, mode4=1)
    else:
        """State 2"""
        pass
    """State 3"""
    Quit()
    """Unused"""
    """State 5"""
    return 0

def t301006000_x58():
    """State 0,5"""
    if not GetEventFlag(1042369235) and GetEventFlag(9101) == 1:
        """State 1,6"""
        # talk:30102600:"Ohh, well done, well done indeed."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t301006000_x31(text3=30102600, mode5=1)
        """State 4"""
        Label('L0')
        SetEventFlag(1042369235, 1)
    elif not GetEventFlag(1042369235):
        """State 2,7"""
        # talk:30102610:"Ohh, well done, well done indeed."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t301006000_x31(text3=30102610, mode5=1)
        Goto('L0')
    else:
        """State 3,8"""
        # talk:30102700:"Go to the Roundtable Hold."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t301006000_x31(text3=30102700, mode5=1)
    """State 9"""
    return 0

def t301006000_x59():
    """State 0,3"""
    assert GetEventFlag(1035442706) == 1 and GetEventFlag(1035442709) == 1
    """State 4"""
    assert GetCurrentStateElapsedTime() > 11.5
    """State 9"""
    # talk:30105410:"Oh, good heavens. Clench your teeth, or something."
    assert t301006000_x33(text2=30105410, mode3=1) and GetCurrentStateElapsedTime() > 9
    """State 1"""
    SetEventFlag(1035449227, 1)
    """State 2"""
    SetEventFlag(9432, 1)
    """State 5"""
    # eventflag:60270:lot:100340:Bloody Finger
    if not GetEventFlag(60270):
        """State 6,8"""
        # lot:100340:Bloody Finger
        assert t301006000_x3(lot1=100340)
    else:
        """State 7"""
        assert GetCurrentStateElapsedTime() > 4
    """State 10"""
    return 0

def t301006000_x60():
    """State 0,5"""
    SetEventFlag(1035442705, 1)
    SetEventFlag(1035442708, 1)
    call = t301006000_x59()
    def ExitPause():
        SetEventFlag(1035442705, 0)
        SetEventFlag(1035442708, 0)
    if call.Done():
        pass
    elif not GetEventFlag(1035442705) or not GetEventFlag(1035442708):
        pass
    """State 1"""
    if GetEventFlag(1035449227) == 1:
        """State 2"""
        assert not IsMenuOpen(63)
        """State 4"""
        # talk:30105415:"Never forget that feeling of agony."
        assert t301006000_x31(text3=30105415, mode5=1)
    else:
        """State 3"""
        pass
    """State 6"""
    return 0

