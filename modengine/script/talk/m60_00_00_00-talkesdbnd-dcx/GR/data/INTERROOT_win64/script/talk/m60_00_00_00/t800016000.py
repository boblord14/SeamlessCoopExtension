# -*- coding: utf-8 -*-
def t800016000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t800016000_x5(flag11=4723, flag12=4721, flag13=4722, val5=5, val6=10, val7=12, val8=10, val9=12,
                  actionbutton1=6000, flag14=6000, flag15=6001, flag16=6000, flag17=6000, flag18=6000,
                  z6=1, z7=1000000, z8=1000000, z9=1000000, mode3=1, mode4=1)
    Quit()

def t800016000_1000():
    """State 0,2,3"""
    assert t800016000_x36(flag5=4720, flag6=1042382700, flag7=1042389200, shop1=123000, shop2=123049)
    """State 1"""
    c1_120(1000)
    Quit()

def t800016000_1001():
    """State 0,2,3"""
    assert t800016000_x37(flag10=1042382700, z5=1042389200)
    """State 1"""
    c1_120(1001)
    Quit()

def t800016000_1100():
    """State 0,2,3"""
    assert t800016000_x38(val1=1042382700, val2=1042389200)
    """State 1"""
    c1_120(1100)
    Quit()

def t800016000_1101():
    """State 0,2,3"""
    assert t800016000_x39(flag9=1042382700, z4=1042389200)
    """State 1"""
    c1_120(1101)
    Quit()

def t800016000_1102():
    """State 0,2,3"""
    t800016000_x40(flag2=4720, flag3=1042382700, flag4=1042389200)
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t800016000_1103():
    """State 0,2,3"""
    assert t800016000_x41()
    """State 1"""
    c1_120(1103)
    Quit()

def t800016000_2000():
    """State 0,2,3"""
    assert t800016000_x42(z1=4720, flag1=1042382700, z2=1042389200)
    """State 1"""
    c1_120(2000)
    Quit()

def t800016000_80002():
    """State 0,2"""
    assert t800016000_x96()
    """State 1"""
    c1_120(80002)
    Quit()

def t800016000_x0(actionbutton1=6000, flag15=6001, flag19=6000, flag20=6000, flag21=6000, flag22=6000,
                  flag14=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag15) == 1 or GetEventFlag(flag19) == 1 or GetEventFlag(flag20) == 1 or
                GetEventFlag(flag21) == 1 or GetEventFlag(flag22) == 1)
        """State 4"""
        assert not GetEventFlag(flag14)
        """State 2"""
        if GetEventFlag(flag14) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag15) and not GetEventFlag(flag19) and not GetEventFlag(flag20) and
              not GetEventFlag(flag21) and not GetEventFlag(flag22)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t800016000_x1():
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

def t800016000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t800016000_x3(val6=10, val7=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val6 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t800016000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val7 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t800016000_x1()
    else:
        """State 4,7"""
        call = t800016000_x33()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val7 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t800016000_x1()
    """State 9"""
    return 0

def t800016000_x4():
    """State 0,1"""
    assert t800016000_x1()
    """State 2"""
    return 0

def t800016000_x5(flag11=4723, flag12=4721, flag13=4722, val5=5, val6=10, val7=12, val8=10, val9=12,
                  actionbutton1=6000, flag14=6000, flag15=6001, flag16=6000, flag17=6000, flag18=6000,
                  z6=1, z7=1000000, z8=1000000, z9=1000000, mode3=1, mode4=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t800016000_x22(flag11=flag11, flag12=flag12, flag13=flag13, val5=val5, val6=val6, val7=val7,
                              val8=val8, val9=val9, actionbutton1=actionbutton1, flag14=flag14, flag15=flag15,
                              flag16=flag16, flag17=flag17, flag18=flag18, z6=z6, z7=z7, z8=z8, z9=z9,
                              mode3=mode3, mode4=mode4)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t800016000_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t800016000_x6(val5=5, val6=10, val7=12, val8=10, val9=12, actionbutton1=6000, flag14=6000, flag15=6001,
                  flag16=6000, flag17=6000, flag18=6000, z6=1, z7=1000000, z8=1000000, z9=1000000, mode3=1,
                  mode4=1):
    """State 0"""
    while True:
        """State 2"""
        call = t800016000_x9(actionbutton1=actionbutton1, flag14=flag14, flag15=flag15, z7=z7, z8=z8,
                             z9=z9)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t800016000_x13(val5=val5, z6=z6)
            def WhilePaused():
                c5_138(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
                GiveSpEffectToPlayer(9640)
                c5_139(1 == (mode3 == 1), -1, 0)
                c5_139(1 == (mode4 == 1), 0, -1)
            def ExitPause():
                c1_138(-1)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif IsAttackedBySomeone() == 1 and not DoesSelfHaveSpEffect(9626) and not DoesSelfHaveSpEffect(9627):
            pass
        elif GetEventFlag(flag18) == 1:
            Goto('L0')
        elif GetEventFlag(flag16) == 1 and not GetEventFlag(flag17) and GetDistanceToPlayer() < val8:
            """State 5"""
            call = t800016000_x15(val9=val9)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val9 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t800016000_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t800016000_x11(val6=val6, val7=val7)
    """Unused"""
    """State 7"""
    return 0

def t800016000_x7(val6=10, val7=12):
    """State 0,1"""
    call = t800016000_x17(val6=val6, val7=val7)
    assert IsPlayerDead() == 1
    """State 2"""
    t800016000_x3(val6=val6, val7=val7)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t800016000_x8(flag11=4723, val6=10, val7=12):
    """State 0,8"""
    assert t800016000_x35()
    """State 1"""
    if GetEventFlag(flag11) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val6:
            """State 4,6"""
            call = t800016000_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val7 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t800016000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t800016000_x9(actionbutton1=6000, flag14=6000, flag15=6001, z7=1000000, z8=1000000, z9=1000000):
    """State 0,1"""
    call = t800016000_x10(z11=2000, val10=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t800016000_x0(actionbutton1=actionbutton1, flag15=flag15, flag19=6000, flag20=6000, flag21=6000,
                flag22=6000, flag14=flag14))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800016000_x10(z11=_, val10=_):
    """State 0,1"""
    if f203(z11) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z11)
        assert f202() == val10
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t800016000_x11(val6=10, val7=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t800016000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val6:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t800016000_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val7 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t800016000_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t800016000_x12():
    """State 0,1"""
    assert t800016000_x10(z11=1101, val10=1101)
    """State 2"""
    return 0

def t800016000_x13(val5=5, z6=1):
    """State 0,2"""
    assert t800016000_x23()
    """State 1"""
    call = t800016000_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t800016000_x25()
    """State 4"""
    return 0

def t800016000_x14():
    """State 0,1"""
    assert t800016000_x10(z11=1000, val10=1000)
    """State 2"""
    return 0

def t800016000_x15(val9=12):
    """State 0,1"""
    call = t800016000_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val9 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t800016000_x26()
    """State 3"""
    return 0

def t800016000_x16():
    """State 0,1"""
    assert t800016000_x10(z11=1100, val10=1100)
    """State 2"""
    return 0

def t800016000_x17(val6=10, val7=12):
    """State 0,5"""
    assert t800016000_x35()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val6
        """State 3"""
        call = t800016000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val7 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t800016000_x28()
    """Unused"""
    """State 6"""
    return 0

def t800016000_x18():
    """State 0,2"""
    call = t800016000_x10(z11=1102, val10=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t800016000_x19():
    """State 0,1"""
    assert t800016000_x10(z11=1001, val10=1001)
    """State 2"""
    return 0

def t800016000_x20():
    """State 0,1"""
    assert t800016000_x10(z11=1103, val10=1103)
    """State 2"""
    return 0

def t800016000_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t800016000_x22(flag11=4723, flag12=4721, flag13=4722, val5=5, val6=10, val7=12, val8=10, val9=12,
                   actionbutton1=6000, flag14=6000, flag15=6001, flag16=6000, flag17=6000, flag18=6000,
                   z6=1, z7=1000000, z8=1000000, z9=1000000, mode3=1, mode4=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t800016000_x6(val5=val5, val6=val6, val7=val7, val8=val8, val9=val9, actionbutton1=actionbutton1,
                             flag14=flag14, flag15=flag15, flag16=flag16, flag17=flag17, flag18=flag18,
                             z6=z6, z7=z7, z8=z8, z9=z9, mode3=mode3, mode4=mode4)
        if CheckSelfDeath() == 1 or GetEventFlag(flag11) == 1:
            """State 3"""
            Label('L0')
            call = t800016000_x8(flag11=flag11, val6=val6, val7=val7)
            if not CheckSelfDeath() and not GetEventFlag(flag11):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag12) == 1 or GetEventFlag(flag13) == 1:
            """State 2"""
            call = t800016000_x7(val6=val6, val7=val7)
            if CheckSelfDeath() == 1 or GetEventFlag(flag11) == 1:
                Goto('L0')
            elif not GetEventFlag(flag12) and not GetEventFlag(flag13):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t800016000_x34() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t800016000_x23():
    """State 0,1"""
    assert t800016000_x24()
    """State 2"""
    return 0

def t800016000_x24():
    """State 0,1"""
    assert t800016000_x10(z11=1104, val10=1104)
    """State 2"""
    return 0

def t800016000_x25():
    """State 0,1"""
    call = t800016000_x10(z11=1201, val10=1201)
    if call.Get() == 1:
        """State 2"""
        assert t800016000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800016000_x26():
    """State 0,1"""
    call = t800016000_x10(z11=1300, val10=1300)
    if call.Get() == 1:
        """State 2"""
        assert t800016000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800016000_x27():
    """State 0,1"""
    call = t800016000_x10(z11=1301, val10=1301)
    if call.Get() == 1:
        """State 2"""
        assert t800016000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800016000_x28():
    """State 0,1"""
    call = t800016000_x10(z11=1302, val10=1302)
    if call.Get() == 1:
        """State 2"""
        assert t800016000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800016000_x29(text5=_, z10=_, mode7=1):
    """State 0,5"""
    assert t800016000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text5, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode7:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(z10, 1)
    """State 6"""
    return 0

def t800016000_x30(text1=_, mode6=1):
    """State 0,4"""
    assert t800016000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text1, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode6:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t800016000_x31(text4=_, mode5=1):
    """State 0,4"""
    assert t800016000_x32() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text4, -1, -1, 1)
    """State 3"""
    if not mode5:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t800016000_x32():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t800016000_x33():
    """State 0,1"""
    assert t800016000_x10(z11=1002, val10=1002)
    """State 2"""
    return 0

def t800016000_x34():
    """State 0,1"""
    assert t800016000_x1()
    """State 2"""
    return 0

def t800016000_x35():
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

def t800016000_x36(flag5=4720, flag6=1042382700, flag7=1042389200, shop1=123000, shop2=123049):
    """State 0,1"""
    def WhilePaused():
        c1_121(9610)
    assert t800016000_x92(flag5=flag5, flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    """State 2"""
    return 0

def t800016000_x37(flag10=1042382700, z5=1042389200):
    """State 0"""
    if GetEventFlag(6 + flag10) == 1:
        """State 1,3"""
        assert t800016000_x31(text4=95090800, mode5=1)
    else:
        """State 2,4"""
        assert t800016000_x31(text4=95090900, mode5=1)
    """State 5"""
    return 0

def t800016000_x38(val1=1042382700, val2=1042389200):
    """State 0,1"""
    assert t800016000_x91(val1=val1, val2=val2)
    """State 2"""
    return 0

def t800016000_x39(flag9=1042382700, z4=1042389200):
    """State 0"""
    if not GetEventFlag(7 + flag9):
        """State 1,3"""
        assert t800016000_x50(text2=95090000, val3=7, flag1=flag9, mode1=1)
    else:
        """State 2"""
        pass
    """State 4"""
    return 0

def t800016000_x40(flag2=4720, flag3=1042382700, flag4=1042389200):
    """State 0"""
    if not DoesSelfHaveSpEffect(9602):
        """State 1"""
        t800016000_x93(flag2=flag2, flag3=flag3, flag4=flag4)
        def WhilePaused():
            c1_121(9612)
        Quit()
    else:
        """State 2"""
        t800016000_x94(flag2=flag2, flag3=flag3, flag4=flag4)
        def ExitPause():
            c1_121(9612)
        Quit()
    """Unused"""
    """State 3"""
    return 0

def t800016000_x41():
    """State 0,1,3"""
    assert t800016000_x31(text4=95091100, mode5=1)
    """State 5"""
    Label('L0')
    return 0
    """Unused"""
    """State 2,4"""
    assert t800016000_x31(text4=95091000, mode5=1)
    Goto('L0')

def t800016000_x42(z1=4720, flag1=1042382700, z2=1042389200):
    """State 0,1"""
    assert t800016000_x95(z1=z1, flag1=flag1, z2=z2)
    """State 2"""
    return 0

def t800016000_x43(flag6=1042382700, flag7=1042389200, shop1=123000, shop2=123049):
    """State 0"""
    if GetEventFlag(4980) == 1:
        """State 1"""
        assert t800016000_x44(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4982) == 1:
        """State 2"""
        assert t800016000_x46(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4983) == 1:
        """State 3"""
        assert t800016000_x47(flag6=flag6, flag7=flag7)
    """State 5"""
    Label('L0')
    return 0
    """Unused"""
    """State 4"""
    assert t800016000_x55(flag6=flag6, flag7=flag7)
    Goto('L0')

def t800016000_x44(flag6=1042382700, flag7=1042389200, shop1=123000, shop2=123049):
    """State 0,1"""
    assert t800016000_x48(flag6=flag6, flag7=flag7)
    """State 2"""
    assert t800016000_x51(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    """State 3"""
    assert t800016000_x89()
    """State 4"""
    return 0

def t800016000_x45(flag6=1042382700, flag7=1042389200, text1=_):
    """State 0,3"""
    assert t800016000_x30(text1=text1, mode6=1)
    """State 1"""
    SetEventFlag(48 + flag7, 1)
    """State 2"""
    SetEventFlag(6 + flag6, 1)
    """State 4"""
    assert t800016000_x50(text2=95090505, val3=5, flag1=flag6, mode1=1)
    """State 5"""
    return 0

def t800016000_x46(flag6=1042382700, flag7=1042389200, shop1=123000, shop2=123049):
    """State 0,1"""
    assert t800016000_x56(flag6=flag6, flag7=flag7)
    """State 2"""
    assert t800016000_x51(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    """State 3"""
    assert t800016000_x58()
    """State 4"""
    return 0

def t800016000_x47(flag6=1042382700, flag7=1042389200):
    """State 0,1"""
    assert t800016000_x59(flag6=flag6, flag7=flag7)
    """State 2"""
    return 0

def t800016000_x48(flag6=1042382700, flag7=1042389200):
    """State 0,3"""
    call = t800016000_x10(z11=80000, val10=80000)
    if call.Get() == 1:
        """State 2,4"""
        assert t800016000_x53(flag6=flag6, flag7=flag7)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800016000_x49(text3=_, val4=_, flag7=_, mode2=1):
    """State 0,5"""
    assert t800016000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text3, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode2:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(val4 + flag7, 1)
    """State 6"""
    return 0

def t800016000_x50(text2=_, val3=_, flag1=_, mode1=1):
    """State 0,5"""
    assert t800016000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(val3 + flag1, 1)
    """State 1"""
    TalkToPlayer(text2, -1, -1, 1)
    """State 4"""
    if not mode1:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t800016000_x51(flag6=1042382700, flag7=1042389200, shop1=123000, shop2=123049):
    """State 0,3"""
    c1_110()
    ClearTalkActionState()
    SetWorkValue(0, GetEventFlagValue(1300, 8))
    while True:
        """State 1"""
        ClearTalkListData()
        """State 2"""
        # action:20000010:"Purchase"
        AddTalkListData(1, 20000010, -1)
        # action:20000011:"Sell"
        AddTalkListData(2, 20000011, -1)
        # action:20000000:"Talk"
        AddTalkListData(3, 20000000, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 6"""
            OpenRegularShop(shop1, shop2)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 7"""
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 8"""
            assert t800016000_x52(flag6=flag6, flag7=flag7) and CheckSpecificPersonTalkHasEnded(0) == 1
        else:
            """State 9"""
            return 0

def t800016000_x52(flag6=1042382700, flag7=1042389200):
    """State 0"""
    if GetEventFlag(4980) == 1:
        """State 1,4"""
        assert t800016000_x85(flag6=flag6, flag7=flag7)
    else:
        """State 2,3"""
        assert t800016000_x30(text1=95006500, mode6=1)
    """State 5"""
    return 0

def t800016000_x53(flag6=1042382700, flag7=1042389200):
    """State 0"""
    if not GetEventFlag(0 + flag6):
        """State 2"""
        if not GetEventFlag(4985):
            """State 3,6"""
            assert t800016000_x49(text3=95000100, val4=1, flag7=flag7, mode2=1)
        else:
            """State 4,7"""
            assert t800016000_x49(text3=95000200, val4=1, flag7=flag7, mode2=1)
        """State 5"""
        SetEventFlag(0 + flag6, 1)
    else:
        """State 1,8"""
        assert t800016000_x30(text1=95000300, mode6=1)
    """State 9"""
    return 0

def t800016000_x54():
    """State 0"""
    if 0 == (GetWorkValue(0) == GetEventFlagValue(1300, 8)):
        """State 1,4"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800016000_x30(text1=95008200, mode6=1)
    elif DidYouDoSomethingInTheMenu(0) == 1:
        """State 2,5"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800016000_x30(text1=95000500, mode6=1)
    else:
        """State 3,6"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800016000_x30(text1=95002400, mode6=1)
    """State 7"""
    return 0

def t800016000_x55(flag6=1042382700, flag7=1042389200):
    """State 0,1"""
    SetEventFlag(5 + flag6, 1)
    def ExitPause():
        SetEventFlag(6 + flag6, 1)
    assert t800016000_x45(flag6=flag6, flag7=flag7, text1=95090500)
    """State 2"""
    return 0

def t800016000_x56(flag6=1042382700, flag7=1042389200):
    """State 0,3"""
    call = t800016000_x10(z11=81000, val10=81000)
    if call.Get() == 1:
        """State 2,4"""
        assert t800016000_x57(flag6=flag6, flag7=flag7)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800016000_x57(flag6=1042382700, flag7=1042389200):
    """State 0"""
    if not GetEventFlag(4 + flag7):
        """State 2,4"""
        assert t800016000_x49(text3=95010000, val4=1, flag7=flag7, mode2=1)
        """State 3"""
        SetEventFlag(4 + flag7, 1)
    else:
        """State 1,5"""
        assert t800016000_x30(text1=95010300, mode6=1)
    """State 6"""
    return 0

def t800016000_x58():
    """State 0,1"""
    def ExitPause():
        RequestAnimation(20012, -1)
    assert t800016000_x30(text1=95010600, mode6=1)
    """State 2"""
    return 0

def t800016000_x59(flag6=1042382700, flag7=1042389200):
    """State 0,3"""
    call = t800016000_x10(z11=82000, val10=82000)
    if call.Get() == 1:
        """State 2,4"""
        assert t800016000_x60(flag6=flag6, flag7=flag7)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800016000_x60(flag6=1042382700, flag7=1042389200):
    """State 0"""
    if not GetEventFlag(5 + flag7):
        """State 2,4"""
        assert t800016000_x49(text3=95010700, val4=1, flag7=flag7, mode2=1)
        """State 3"""
        SetEventFlag(5 + flag7, 1)
    else:
        """State 1,5"""
        assert t800016000_x30(text1=95011000, mode6=1)
    """State 6"""
    return 0

def t800016000_x61(flag6=1042382700, flag7=1042389200, shop1=123000, shop2=123049):
    """State 0"""
    if GetEventFlag(4980) == 1:
        """State 1"""
        assert t800016000_x62(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4982) == 1:
        """State 3"""
        assert t800016000_x67(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4983) == 1:
        """State 4"""
        assert t800016000_x70(flag6=flag6, flag7=flag7)
    """State 5"""
    Label('L0')
    return 0
    """Unused"""
    """State 2"""
    assert t800016000_x66(flag6=flag6, flag7=flag7)
    Goto('L0')

def t800016000_x62(flag6=1042382700, flag7=1042389200, shop1=123000, shop2=123049):
    """State 0,2"""
    assert t800016000_x63(flag6=flag6, flag7=flag7)
    """State 1"""
    assert t800016000_x51(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    """State 3"""
    assert t800016000_x90()
    """State 4"""
    return 0

def t800016000_x63(flag6=1042382700, flag7=1042389200):
    """State 0,3"""
    call = t800016000_x10(z11=80100, val10=80100)
    if call.Get() == 1:
        """State 2,4"""
        assert t800016000_x64(flag6=flag6, flag7=flag7)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800016000_x64(flag6=1042382700, flag7=1042389200):
    """State 0"""
    if not GetEventFlag(0 + flag6):
        """State 2,4"""
        assert t800016000_x49(text3=95002000, val4=2, flag7=flag7, mode2=1)
        """State 3"""
        SetEventFlag(0 + flag6, 1)
    else:
        """State 1,5"""
        assert t800016000_x30(text1=95002200, mode6=1)
    """State 6"""
    return 0

def t800016000_x65():
    """State 0"""
    if 0 == (GetWorkValue(0) == GetEventFlagValue(1300, 8)):
        """State 1,4"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800016000_x30(text1=95008200, mode6=1)
    elif DidYouDoSomethingInTheMenu(0) == 1:
        """State 2,5"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800016000_x30(text1=95002500, mode6=1)
    else:
        """State 3,6"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800016000_x30(text1=95002400, mode6=1)
    """State 7"""
    return 0

def t800016000_x66(flag6=1042382700, flag7=1042389200):
    """State 0,1"""
    SetEventFlag(5 + flag6, 1)
    def ExitPause():
        SetEventFlag(6 + flag6, 1)
    assert t800016000_x45(flag6=flag6, flag7=flag7, text1=95090500)
    """State 2"""
    return 0

def t800016000_x67(flag6=1042382700, flag7=1042389200, shop1=123000, shop2=123049):
    """State 0,3"""
    assert t800016000_x68(flag6=flag6, flag7=flag7)
    """State 1"""
    assert t800016000_x51(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    """State 2"""
    assert t800016000_x58()
    """State 4"""
    return 0

def t800016000_x68(flag6=1042382700, flag7=1042389200):
    """State 0,3"""
    call = t800016000_x10(z11=81100, val10=81100)
    if call.Get() == 1:
        """State 2,4"""
        assert t800016000_x69(flag6=flag6, flag7=flag7)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800016000_x69(flag6=1042382700, flag7=1042389200):
    """State 0"""
    if not GetEventFlag(4 + flag7):
        """State 2,4"""
        assert t800016000_x49(text3=95010100, val4=2, flag7=flag7, mode2=1)
        """State 3"""
        SetEventFlag(4 + flag7, 1)
    else:
        """State 1,5"""
        assert t800016000_x30(text1=95010400, mode6=1)
    """State 6"""
    return 0

def t800016000_x70(flag6=1042382700, flag7=1042389200):
    """State 0,1"""
    assert t800016000_x71(flag6=flag6, flag7=flag7)
    """State 2"""
    return 0

def t800016000_x71(flag6=1042382700, flag7=1042389200):
    """State 0,3"""
    call = t800016000_x10(z11=82100, val10=82100)
    if call.Get() == 1:
        """State 2,4"""
        assert t800016000_x72(flag6=flag6, flag7=flag7)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800016000_x72(flag6=1042382700, flag7=1042389200):
    """State 0"""
    if not GetEventFlag(5 + flag7):
        """State 2,4"""
        assert t800016000_x49(text3=95010800, val4=2, flag7=flag7, mode2=1)
        """State 3"""
        SetEventFlag(5 + flag7, 1)
    else:
        """State 1,5"""
        assert t800016000_x30(text1=95011000, mode6=1)
    """State 6"""
    return 0

def t800016000_x73(flag6=1042382700, flag7=1042389200, shop1=123000, shop2=123049):
    """State 0"""
    if GetEventFlag(4980) == 1:
        """State 1"""
        assert t800016000_x74(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4982) == 1:
        """State 3"""
        assert t800016000_x79(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4983) == 1:
        """State 4"""
        assert t800016000_x82(flag6=flag6, flag7=flag7)
    """State 5"""
    Label('L0')
    return 0
    """Unused"""
    """State 2"""
    assert t800016000_x78(flag6=flag6, flag7=flag7)
    Goto('L0')

def t800016000_x74(flag6=1042382700, flag7=1042389200, shop1=123000, shop2=123049):
    """State 0,2"""
    assert t800016000_x75(flag6=flag6, flag7=flag7)
    """State 1"""
    assert t800016000_x51(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    """State 3"""
    assert t800016000_x88()
    """State 4"""
    return 0

def t800016000_x75(flag6=1042382700, flag7=1042389200):
    """State 0,3"""
    call = t800016000_x10(z11=80200, val10=80200)
    if call.Get() == 1:
        """State 2,4"""
        assert t800016000_x76(flag6=flag6, flag7=flag7)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800016000_x76(flag6=1042382700, flag7=1042389200):
    """State 0"""
    if not GetEventFlag(0 + flag6):
        """State 2,4"""
        assert t800016000_x49(text3=95004000, val4=3, flag7=flag7, mode2=1)
        """State 3"""
        SetEventFlag(0 + flag6, 1)
    else:
        """State 1,5"""
        assert t800016000_x30(text1=95004200, mode6=1)
    """State 6"""
    return 0

def t800016000_x77():
    """State 0"""
    if 0 == (GetWorkValue(0) == GetEventFlagValue(1300, 8)):
        """State 1,3"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800016000_x30(text1=95008200, mode6=1)
    else:
        """State 2,4"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800016000_x30(text1=95004400, mode6=1)
    """State 5"""
    return 0

def t800016000_x78(flag6=1042382700, flag7=1042389200):
    """State 0,1"""
    SetEventFlag(5 + flag6, 1)
    def ExitPause():
        SetEventFlag(6 + flag6, 1)
    assert t800016000_x45(flag6=flag6, flag7=flag7, text1=95090590)
    """State 2"""
    return 0

def t800016000_x79(flag6=1042382700, flag7=1042389200, shop1=123000, shop2=123049):
    """State 0,3"""
    assert t800016000_x80(z3=0, flag8=0)
    """State 1"""
    assert t800016000_x51(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    """State 2"""
    assert t800016000_x58()
    """State 4"""
    return 0

def t800016000_x80(z3=0, flag8=0):
    """State 0,3"""
    call = t800016000_x10(z11=81200, val10=81200)
    if call.Get() == 1:
        """State 2,4"""
        assert t800016000_x81(z3=z3, flag8=flag8)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800016000_x81(z3=0, flag8=0):
    """State 0"""
    if not GetEventFlag(4 + flag8):
        """State 2,4"""
        assert t800016000_x49(text3=95010200, val4=3, flag7=flag8, mode2=1)
        """State 3"""
        SetEventFlag(4 + flag8, 1)
    else:
        """State 1,5"""
        assert t800016000_x30(text1=95010500, mode6=1)
    """State 6"""
    return 0

def t800016000_x82(flag6=1042382700, flag7=1042389200):
    """State 0,1"""
    assert t800016000_x83(flag6=flag6, flag7=flag7)
    """State 2"""
    return 0

def t800016000_x83(flag6=1042382700, flag7=1042389200):
    """State 0,3"""
    call = t800016000_x10(z11=82200, val10=82200)
    if call.Get() == 1:
        """State 2,4"""
        assert t800016000_x84(flag6=flag6, flag7=flag7)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800016000_x84(flag6=1042382700, flag7=1042389200):
    """State 0"""
    if not GetEventFlag(5 + flag7):
        """State 2,4"""
        assert t800016000_x49(text3=95010900, val4=3, flag7=flag7, mode2=1)
        """State 3"""
        SetEventFlag(5 + flag7, 1)
    else:
        """State 1,5"""
        assert t800016000_x30(text1=95011000, mode6=1)
    """State 6"""
    return 0

def t800016000_x85(flag6=1042382700, flag7=1042389200):
    """State 0,1"""
    assert t800016000_x10(z11=80002, val10=80002)
    """State 2"""
    return 0

def t800016000_x86(flag3=1042382700, flag4=1042389200):
    """State 0"""
    if not GetEventFlag(5 + flag3):
        """State 2"""
        if not GetEventFlag(48 + flag4):
            """State 4,6"""
            SetEventFlag(5 + flag3, 1)
            """State 8"""
            assert t800016000_x50(text2=95090100, val3=48, flag1=flag4, mode1=1)
        else:
            """State 5,7"""
            SetEventFlag(5 + flag3, 1)
            """State 9"""
            assert t800016000_x31(text4=95090300, mode5=1)
    else:
        """State 3"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 10"""
    return 0

def t800016000_x87(flag3=1042382700, flag4=1042389200):
    """State 0"""
    if not GetEventFlag(5 + flag3):
        """State 2"""
        if not GetEventFlag(48 + flag4):
            """State 4,8"""
            assert t800016000_x50(text2=95090190, val3=48, flag1=flag4, mode1=1)
        else:
            """State 5,7"""
            SetEventFlag(5 + flag3, 1)
            """State 9"""
            assert t800016000_x31(text4=95090390, mode5=1)
    else:
        """State 3"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 6"""
    SetEventFlag(5 + flag3, 1)
    Quit()
    """State 10"""
    return 0

def t800016000_x88():
    """State 0,3"""
    call = t800016000_x10(z11=80201, val10=80201)
    if call.Get() == 1:
        """State 2,4"""
        assert t800016000_x77()
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800016000_x89():
    """State 0,3"""
    call = t800016000_x10(z11=80001, val10=80001)
    if call.Get() == 1:
        """State 2,4"""
        assert t800016000_x54()
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800016000_x90():
    """State 0,3"""
    call = t800016000_x10(z11=80101, val10=80101)
    if call.Get() == 1:
        """State 2,4"""
        assert t800016000_x65()
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800016000_x91(val1=1042382700, val2=1042389200):
    """State 0,1,2"""
    SetEventFlag(8 + val2, 1)
    """State 3"""
    assert t800016000_x50(text2=95090000, val3=8, flag1=val1, mode1=1)
    """State 4"""
    return 0

def t800016000_x92(flag5=4720, flag6=1042382700, flag7=1042389200, shop1=123000, shop2=123049):
    """State 0"""
    if GetEventFlag(5 + flag5) == 1:
        """State 1"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800016000_x43(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    elif GetEventFlag(6 + flag5) == 1:
        """State 2"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800016000_x61(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    elif GetEventFlag(7 + flag5) == 1:
        """State 3"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800016000_x73(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    """State 4"""
    return 0

def t800016000_x93(flag2=4720, flag3=1042382700, flag4=1042389200):
    """State 0"""
    if GetEventFlag(5 + flag2) == 1 or GetEventFlag(6 + flag2) == 1:
        """State 1"""
        t800016000_x86(flag3=flag3, flag4=flag4)
        Quit()
    elif GetEventFlag(7 + flag2) == 1:
        """State 2"""
        t800016000_x87(flag3=flag3, flag4=flag4)
        Quit()
    """Unused"""
    """State 3"""
    return 0

def t800016000_x94(flag2=4720, flag3=1042382700, flag4=1042389200):
    """State 0,6"""
    # actionbutton:6000:"Talk"
    call = t800016000_x0(actionbutton1=6000, flag15=6001, flag19=6000, flag20=6000, flag21=6000, flag22=6000,
                         flag14=6000)
    if call.Done():
        """State 1"""
        pass
    elif IsPlayerAttacking() == 1:
        """State 5"""
        pass
    elif GetEventFlag(8 + flag3) == 1:
        """State 2"""
        pass
    """State 3,4"""
    if GetEventFlag(5 + flag2) == 1 or GetEventFlag(6 + flag2) == 1:
        """State 7"""
        t800016000_x86(flag3=flag3, flag4=flag4)
        def WhilePaused():
            c1_121(9612)
        Quit()
    elif GetEventFlag(7 + flag2) == 1:
        """State 8"""
        t800016000_x87(flag3=flag3, flag4=flag4)
        def WhilePaused():
            c1_121(9612)
        Quit()
    """Unused"""
    """State 9"""
    return 0

def t800016000_x95(z1=4720, flag1=1042382700, z2=1042389200):
    """State 0"""
    while True:
        """State 2"""
        # actionbutton:6000:"Talk"
        call = t800016000_x0(actionbutton1=6000, flag15=6001, flag19=6000, flag20=6000, flag21=6000,
                             flag22=6000, flag14=6000)
        if call.Done():
            break
        elif GetEventFlag(8 + flag1) == 1 and not GetEventFlag(9 + flag1):
            """State 1,3"""
            assert t800016000_x50(text2=95090000, val3=9, flag1=flag1, mode1=1)
    """State 4"""
    return 0

def t800016000_x96():
    """State 0"""
    if GetEventFlag(1042389220) == 1 and GetEventFlag(1042389221) == 1:
        """State 2,3"""
        SetEventFlag(1042389220, 0)
        SetEventFlag(1042389221, 0)
    else:
        """State 1"""
        pass
    """State 4"""
    if not GetEventFlag(1042389220):
        """State 5,7"""
        assert t800016000_x29(text5=95106000, z10=1042389220, mode7=1)
    elif not GetEventFlag(1042389221):
        """State 6,8"""
        assert t800016000_x29(text5=95106100, z10=1042389221, mode7=1)
    """State 9"""
    return 0

