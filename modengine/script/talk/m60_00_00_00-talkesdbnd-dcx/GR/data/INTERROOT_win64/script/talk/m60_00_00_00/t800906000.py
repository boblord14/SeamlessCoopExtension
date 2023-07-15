# -*- coding: utf-8 -*-
def t800906000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t800906000_x6(flag12=4963, flag13=4961, flag14=4962, val6=5, val7=10, val8=12, val9=10, val10=12,
                  actionbutton1=6000, flag15=6000, flag16=6001, flag17=6000, flag18=6000, flag19=6000,
                  z6=1, z7=1000000, z8=1000000, z9=1000000, mode3=1, mode4=1)
    Quit()

def t800906000_1000():
    """State 0,2,3"""
    assert t800906000_x37(flag6=4960, flag7=1043372700, flag8=1043379200, shop1=129050, shop2=129099)
    """State 1"""
    c1_120(1000)
    Quit()

def t800906000_1001():
    """State 0,2,3"""
    assert t800906000_x38(flag11=1043372700, z5=1043379200)
    """State 1"""
    c1_120(1001)
    Quit()

def t800906000_1100():
    """State 0,2,3"""
    assert t800906000_x39(val2=1043372700, val3=1043379200)
    """State 1"""
    c1_120(1100)
    Quit()

def t800906000_1101():
    """State 0,2,3"""
    assert t800906000_x40(flag10=1043372700, z4=1043379200)
    """State 1"""
    c1_120(1101)
    Quit()

def t800906000_1102():
    """State 0,2,3"""
    t800906000_x41(flag3=4700, flag4=1043372700, flag5=1043379200)
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t800906000_1103():
    """State 0,2,3"""
    assert t800906000_x42()
    """State 1"""
    c1_120(1103)
    Quit()

def t800906000_2000():
    """State 0,2,3"""
    assert t800906000_x43(z1=4700, flag2=1043372700, z2=1043379200)
    """State 1"""
    c1_120(2000)
    Quit()

def t800906000_80002():
    """State 0,2"""
    assert t800906000_x98()
    """State 1"""
    c1_120(80002)
    Quit()

def t800906000_80200():
    """State 0,2"""
    assert t800906000_x97(flag1=1043372700, val1=1043379200)
    """State 1"""
    c1_120(80200)
    Quit()

def t800906000_x0(actionbutton1=6000, flag16=6001, flag20=6000, flag21=6000, flag22=6000, flag23=6000,
                  flag15=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag16) == 1 or GetEventFlag(flag20) == 1 or GetEventFlag(flag21) == 1 or
                GetEventFlag(flag22) == 1 or GetEventFlag(flag23) == 1)
        """State 4"""
        assert not GetEventFlag(flag15)
        """State 2"""
        if GetEventFlag(flag15) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag16) and not GetEventFlag(flag20) and not GetEventFlag(flag21) and
              not GetEventFlag(flag22) and not GetEventFlag(flag23)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t800906000_x1():
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

def t800906000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t800906000_x3(lot1=_):
    """State 0,1"""
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t800906000_x4(val7=10, val8=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val7 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t800906000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val8 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t800906000_x1()
    else:
        """State 4,7"""
        call = t800906000_x34()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val8 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t800906000_x1()
    """State 9"""
    return 0

def t800906000_x5():
    """State 0,1"""
    assert t800906000_x1()
    """State 2"""
    return 0

def t800906000_x6(flag12=4963, flag13=4961, flag14=4962, val6=5, val7=10, val8=12, val9=10, val10=12,
                  actionbutton1=6000, flag15=6000, flag16=6001, flag17=6000, flag18=6000, flag19=6000,
                  z6=1, z7=1000000, z8=1000000, z9=1000000, mode3=1, mode4=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t800906000_x23(flag12=flag12, flag13=flag13, flag14=flag14, val6=val6, val7=val7, val8=val8,
                              val9=val9, val10=val10, actionbutton1=actionbutton1, flag15=flag15, flag16=flag16,
                              flag17=flag17, flag18=flag18, flag19=flag19, z6=z6, z7=z7, z8=z8, z9=z9,
                              mode3=mode3, mode4=mode4)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t800906000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t800906000_x7(val6=5, val7=10, val8=12, val9=10, val10=12, actionbutton1=6000, flag15=6000, flag16=6001,
                  flag17=6000, flag18=6000, flag19=6000, z6=1, z7=1000000, z8=1000000, z9=1000000, mode3=1,
                  mode4=1):
    """State 0"""
    while True:
        """State 2"""
        call = t800906000_x10(actionbutton1=actionbutton1, flag15=flag15, flag16=flag16, z7=z7, z8=z8,
                              z9=z9)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t800906000_x14(val6=val6, z6=z6)
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
        elif GetEventFlag(flag19) == 1:
            Goto('L0')
        elif GetEventFlag(flag17) == 1 and not GetEventFlag(flag18) and GetDistanceToPlayer() < val9:
            """State 5"""
            call = t800906000_x16(val10=val10)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val10 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t800906000_x27() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t800906000_x12(val7=val7, val8=val8)
    """Unused"""
    """State 7"""
    return 0

def t800906000_x8(val7=10, val8=12):
    """State 0,1"""
    call = t800906000_x18(val7=val7, val8=val8)
    assert IsPlayerDead() == 1
    """State 2"""
    t800906000_x4(val7=val7, val8=val8)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t800906000_x9(flag12=4963, val7=10, val8=12):
    """State 0,8"""
    assert t800906000_x36()
    """State 1"""
    if GetEventFlag(flag12) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val7:
            """State 4,6"""
            call = t800906000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val8 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t800906000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t800906000_x10(actionbutton1=6000, flag15=6000, flag16=6001, z7=1000000, z8=1000000, z9=1000000):
    """State 0,1"""
    call = t800906000_x11(z11=2000, val11=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t800906000_x0(actionbutton1=actionbutton1, flag16=flag16, flag20=6000, flag21=6000, flag22=6000,
                flag23=6000, flag15=flag15))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800906000_x11(z11=_, val11=_):
    """State 0,1"""
    if f203(z11) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z11)
        assert f202() == val11
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t800906000_x12(val7=10, val8=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t800906000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val7:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t800906000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val8 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t800906000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t800906000_x13():
    """State 0,1"""
    assert t800906000_x11(z11=1101, val11=1101)
    """State 2"""
    return 0

def t800906000_x14(val6=5, z6=1):
    """State 0,2"""
    assert t800906000_x24()
    """State 1"""
    call = t800906000_x15()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val6 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t800906000_x26()
    """State 4"""
    return 0

def t800906000_x15():
    """State 0,1"""
    assert t800906000_x11(z11=1000, val11=1000)
    """State 2"""
    return 0

def t800906000_x16(val10=12):
    """State 0,1"""
    call = t800906000_x17()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val10 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t800906000_x27()
    """State 3"""
    return 0

def t800906000_x17():
    """State 0,1"""
    assert t800906000_x11(z11=1100, val11=1100)
    """State 2"""
    return 0

def t800906000_x18(val7=10, val8=12):
    """State 0,5"""
    assert t800906000_x36()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val7
        """State 3"""
        call = t800906000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val8 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t800906000_x29()
    """Unused"""
    """State 6"""
    return 0

def t800906000_x19():
    """State 0,2"""
    call = t800906000_x11(z11=1102, val11=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t800906000_x20():
    """State 0,1"""
    assert t800906000_x11(z11=1001, val11=1001)
    """State 2"""
    return 0

def t800906000_x21():
    """State 0,1"""
    assert t800906000_x11(z11=1103, val11=1103)
    """State 2"""
    return 0

def t800906000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t800906000_x23(flag12=4963, flag13=4961, flag14=4962, val6=5, val7=10, val8=12, val9=10, val10=12,
                   actionbutton1=6000, flag15=6000, flag16=6001, flag17=6000, flag18=6000, flag19=6000,
                   z6=1, z7=1000000, z8=1000000, z9=1000000, mode3=1, mode4=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t800906000_x7(val6=val6, val7=val7, val8=val8, val9=val9, val10=val10, actionbutton1=actionbutton1,
                             flag15=flag15, flag16=flag16, flag17=flag17, flag18=flag18, flag19=flag19,
                             z6=z6, z7=z7, z8=z8, z9=z9, mode3=mode3, mode4=mode4)
        if CheckSelfDeath() == 1 or GetEventFlag(flag12) == 1:
            """State 3"""
            Label('L0')
            call = t800906000_x9(flag12=flag12, val7=val7, val8=val8)
            if not CheckSelfDeath() and not GetEventFlag(flag12):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag13) == 1 or GetEventFlag(flag14) == 1:
            """State 2"""
            call = t800906000_x8(val7=val7, val8=val8)
            if CheckSelfDeath() == 1 or GetEventFlag(flag12) == 1:
                Goto('L0')
            elif not GetEventFlag(flag13) and not GetEventFlag(flag14):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t800906000_x35() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t800906000_x24():
    """State 0,1"""
    assert t800906000_x25()
    """State 2"""
    return 0

def t800906000_x25():
    """State 0,1"""
    assert t800906000_x11(z11=1104, val11=1104)
    """State 2"""
    return 0

def t800906000_x26():
    """State 0,1"""
    call = t800906000_x11(z11=1201, val11=1201)
    if call.Get() == 1:
        """State 2"""
        assert t800906000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800906000_x27():
    """State 0,1"""
    call = t800906000_x11(z11=1300, val11=1300)
    if call.Get() == 1:
        """State 2"""
        assert t800906000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800906000_x28():
    """State 0,1"""
    call = t800906000_x11(z11=1301, val11=1301)
    if call.Get() == 1:
        """State 2"""
        assert t800906000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800906000_x29():
    """State 0,1"""
    call = t800906000_x11(z11=1302, val11=1302)
    if call.Get() == 1:
        """State 2"""
        assert t800906000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800906000_x30(text5=_, z10=_, mode7=1):
    """State 0,5"""
    assert t800906000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t800906000_x31(text1=_, mode6=1):
    """State 0,4"""
    assert t800906000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t800906000_x32(text4=_, mode5=1):
    """State 0,4"""
    assert t800906000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t800906000_x33():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t800906000_x34():
    """State 0,1"""
    assert t800906000_x11(z11=1002, val11=1002)
    """State 2"""
    return 0

def t800906000_x35():
    """State 0,1"""
    assert t800906000_x1()
    """State 2"""
    return 0

def t800906000_x36():
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

def t800906000_x37(flag6=4960, flag7=1043372700, flag8=1043379200, shop1=129050, shop2=129099):
    """State 0,1"""
    def WhilePaused():
        c1_121(9610)
    assert t800906000_x93(flag6=flag6, flag7=flag7, flag8=flag8, shop1=shop1, shop2=shop2)
    """State 2"""
    return 0

def t800906000_x38(flag11=1043372700, z5=1043379200):
    """State 0"""
    if GetEventFlag(6 + flag11) == 1:
        """State 1,3"""
        assert t800906000_x32(text4=95090800, mode5=1)
    else:
        """State 2,4"""
        assert t800906000_x32(text4=95090900, mode5=1)
    """State 5"""
    return 0

def t800906000_x39(val2=1043372700, val3=1043379200):
    """State 0,1"""
    assert t800906000_x92(val2=val2, val3=val3)
    """State 2"""
    return 0

def t800906000_x40(flag10=1043372700, z4=1043379200):
    """State 0"""
    if not GetEventFlag(7 + flag10):
        """State 1,3"""
        assert t800906000_x51(text2=95090000, val4=7, flag2=flag10, mode1=1)
    else:
        """State 2"""
        pass
    """State 4"""
    return 0

def t800906000_x41(flag3=4700, flag4=1043372700, flag5=1043379200):
    """State 0"""
    if not DoesSelfHaveSpEffect(9602):
        """State 1"""
        t800906000_x94(flag3=flag3, flag4=flag4, flag5=flag5)
        def WhilePaused():
            c1_121(9612)
        Quit()
    else:
        """State 2"""
        t800906000_x95(flag3=flag3, flag4=flag4, flag5=flag5)
        def ExitPause():
            c1_121(9612)
        Quit()
    """Unused"""
    """State 3"""
    return 0

def t800906000_x42():
    """State 0,1,3"""
    assert t800906000_x32(text4=95091100, mode5=1)
    """State 5"""
    Label('L0')
    return 0
    """Unused"""
    """State 2,4"""
    assert t800906000_x32(text4=95091000, mode5=1)
    Goto('L0')

def t800906000_x43(z1=4700, flag2=1043372700, z2=1043379200):
    """State 0,1"""
    assert t800906000_x96(z1=z1, flag2=flag2, z2=z2)
    """State 2"""
    return 0

def t800906000_x44(flag7=1043372700, flag8=1043379200, shop1=129050, shop2=129099):
    """State 0"""
    if GetEventFlag(4980) == 1:
        """State 1"""
        assert t800906000_x45(flag7=flag7, flag8=flag8, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4982) == 1:
        """State 2"""
        assert t800906000_x47(flag7=flag7, flag8=flag8, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4983) == 1:
        """State 3"""
        assert t800906000_x48(flag7=flag7, flag8=flag8)
    """State 5"""
    Label('L0')
    return 0
    """Unused"""
    """State 4"""
    assert t800906000_x56(flag7=flag7, flag8=flag8)
    Goto('L0')

def t800906000_x45(flag7=1043372700, flag8=1043379200, shop1=129050, shop2=129099):
    """State 0,1"""
    assert t800906000_x49(flag7=flag7, flag8=flag8)
    """State 2"""
    assert t800906000_x52(flag7=flag7, flag8=flag8, shop1=shop1, shop2=shop2)
    """State 3"""
    assert t800906000_x90()
    """State 4"""
    return 0

def t800906000_x46(flag7=1043372700, flag8=1043379200, text1=_):
    """State 0,3"""
    assert t800906000_x31(text1=text1, mode6=1)
    """State 1"""
    SetEventFlag(48 + flag8, 1)
    """State 2"""
    SetEventFlag(6 + flag7, 1)
    """State 4"""
    assert t800906000_x51(text2=95090505, val4=5, flag2=flag7, mode1=1)
    """State 5"""
    return 0

def t800906000_x47(flag7=1043372700, flag8=1043379200, shop1=129050, shop2=129099):
    """State 0,1"""
    assert t800906000_x57(flag7=flag7, flag8=flag8)
    """State 2"""
    assert t800906000_x52(flag7=flag7, flag8=flag8, shop1=shop1, shop2=shop2)
    """State 3"""
    assert t800906000_x59()
    """State 4"""
    return 0

def t800906000_x48(flag7=1043372700, flag8=1043379200):
    """State 0,1"""
    assert t800906000_x60(flag7=flag7, flag8=flag8)
    """State 2"""
    return 0

def t800906000_x49(flag7=1043372700, flag8=1043379200):
    """State 0,3"""
    call = t800906000_x11(z11=80000, val11=80000)
    if call.Get() == 1:
        """State 2,4"""
        assert t800906000_x54(flag7=flag7, flag8=flag8)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800906000_x50(text3=_, val5=_, val1=_, mode2=1):
    """State 0,5"""
    assert t800906000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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
    SetEventFlag(val5 + val1, 1)
    """State 6"""
    return 0

def t800906000_x51(text2=_, val4=_, flag2=_, mode1=1):
    """State 0,5"""
    assert t800906000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(val4 + flag2, 1)
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

def t800906000_x52(flag7=1043372700, flag8=1043379200, shop1=129050, shop2=129099):
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
            assert t800906000_x53(flag7=flag7, flag8=flag8) and CheckSpecificPersonTalkHasEnded(0) == 1
        else:
            """State 9"""
            return 0

def t800906000_x53(flag7=1043372700, flag8=1043379200):
    """State 0"""
    if GetEventFlag(4980) == 1:
        """State 1,4"""
        assert t800906000_x86(flag7=flag7, flag8=flag8)
    else:
        """State 2,3"""
        assert t800906000_x31(text1=95006500, mode6=1)
    """State 5"""
    return 0

def t800906000_x54(flag7=1043372700, flag8=1043379200):
    """State 0"""
    if not GetEventFlag(0 + flag7):
        """State 2"""
        if not GetEventFlag(4985):
            """State 3,6"""
            assert t800906000_x50(text3=95000100, val5=1, val1=flag8, mode2=1)
        else:
            """State 4,7"""
            assert t800906000_x50(text3=95000200, val5=1, val1=flag8, mode2=1)
        """State 5"""
        SetEventFlag(0 + flag7, 1)
    else:
        """State 1,8"""
        assert t800906000_x31(text1=95000300, mode6=1)
    """State 9"""
    return 0

def t800906000_x55():
    """State 0"""
    if 0 == (GetWorkValue(0) == GetEventFlagValue(1300, 8)):
        """State 1,4"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800906000_x31(text1=95008200, mode6=1)
    elif DidYouDoSomethingInTheMenu(0) == 1:
        """State 2,5"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800906000_x31(text1=95000500, mode6=1)
    else:
        """State 3,6"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800906000_x31(text1=95002400, mode6=1)
    """State 7"""
    return 0

def t800906000_x56(flag7=1043372700, flag8=1043379200):
    """State 0,1"""
    SetEventFlag(5 + flag7, 1)
    def ExitPause():
        SetEventFlag(6 + flag7, 1)
    assert t800906000_x46(flag7=flag7, flag8=flag8, text1=95090500)
    """State 2"""
    return 0

def t800906000_x57(flag7=1043372700, flag8=1043379200):
    """State 0,3"""
    call = t800906000_x11(z11=81000, val11=81000)
    if call.Get() == 1:
        """State 2,4"""
        assert t800906000_x58(flag7=flag7, flag8=flag8)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800906000_x58(flag7=1043372700, flag8=1043379200):
    """State 0"""
    if not GetEventFlag(4 + flag8):
        """State 2,4"""
        assert t800906000_x50(text3=95010000, val5=1, val1=flag8, mode2=1)
        """State 3"""
        SetEventFlag(4 + flag8, 1)
    else:
        """State 1,5"""
        assert t800906000_x31(text1=95010300, mode6=1)
    """State 6"""
    return 0

def t800906000_x59():
    """State 0,1"""
    def ExitPause():
        RequestAnimation(20012, -1)
    assert t800906000_x31(text1=95010600, mode6=1)
    """State 2"""
    return 0

def t800906000_x60(flag7=1043372700, flag8=1043379200):
    """State 0,3"""
    call = t800906000_x11(z11=82000, val11=82000)
    if call.Get() == 1:
        """State 2,4"""
        assert t800906000_x61(flag7=flag7, flag8=flag8)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800906000_x61(flag7=1043372700, flag8=1043379200):
    """State 0"""
    if not GetEventFlag(5 + flag8):
        """State 2,4"""
        assert t800906000_x50(text3=95010700, val5=1, val1=flag8, mode2=1)
        """State 3"""
        SetEventFlag(5 + flag8, 1)
    else:
        """State 1,5"""
        assert t800906000_x31(text1=95011000, mode6=1)
    """State 6"""
    return 0

def t800906000_x62(flag7=1043372700, flag8=1043379200, shop1=129050, shop2=129099):
    """State 0"""
    if GetEventFlag(4980) == 1:
        """State 1"""
        assert t800906000_x63(flag7=flag7, flag8=flag8, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4982) == 1:
        """State 3"""
        assert t800906000_x68(flag7=flag7, flag8=flag8, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4983) == 1:
        """State 4"""
        assert t800906000_x71(flag7=flag7, flag8=flag8)
    """State 5"""
    Label('L0')
    return 0
    """Unused"""
    """State 2"""
    assert t800906000_x67(flag7=flag7, flag8=flag8)
    Goto('L0')

def t800906000_x63(flag7=1043372700, flag8=1043379200, shop1=129050, shop2=129099):
    """State 0,2"""
    assert t800906000_x64(flag7=flag7, flag8=flag8)
    """State 1"""
    assert t800906000_x52(flag7=flag7, flag8=flag8, shop1=shop1, shop2=shop2)
    """State 3"""
    assert t800906000_x91()
    """State 4"""
    return 0

def t800906000_x64(flag7=1043372700, flag8=1043379200):
    """State 0,3"""
    call = t800906000_x11(z11=80100, val11=80100)
    if call.Get() == 1:
        """State 2,4"""
        assert t800906000_x65(flag7=flag7, flag8=flag8)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800906000_x65(flag7=1043372700, flag8=1043379200):
    """State 0"""
    if not GetEventFlag(0 + flag7):
        """State 2,4"""
        assert t800906000_x50(text3=95002000, val5=2, val1=flag8, mode2=1)
        """State 3"""
        SetEventFlag(0 + flag7, 1)
    else:
        """State 1,5"""
        assert t800906000_x31(text1=95002200, mode6=1)
    """State 6"""
    return 0

def t800906000_x66():
    """State 0"""
    if 0 == (GetWorkValue(0) == GetEventFlagValue(1300, 8)):
        """State 1,4"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800906000_x31(text1=95008200, mode6=1)
    elif DidYouDoSomethingInTheMenu(0) == 1:
        """State 2,5"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800906000_x31(text1=95002500, mode6=1)
    else:
        """State 3,6"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800906000_x31(text1=95002400, mode6=1)
    """State 7"""
    return 0

def t800906000_x67(flag7=1043372700, flag8=1043379200):
    """State 0,1"""
    SetEventFlag(5 + flag7, 1)
    def ExitPause():
        SetEventFlag(6 + flag7, 1)
    assert t800906000_x46(flag7=flag7, flag8=flag8, text1=95090500)
    """State 2"""
    return 0

def t800906000_x68(flag7=1043372700, flag8=1043379200, shop1=129050, shop2=129099):
    """State 0,3"""
    assert t800906000_x69(flag7=flag7, flag8=flag8)
    """State 1"""
    assert t800906000_x52(flag7=flag7, flag8=flag8, shop1=shop1, shop2=shop2)
    """State 2"""
    assert t800906000_x59()
    """State 4"""
    return 0

def t800906000_x69(flag7=1043372700, flag8=1043379200):
    """State 0,3"""
    call = t800906000_x11(z11=81100, val11=81100)
    if call.Get() == 1:
        """State 2,4"""
        assert t800906000_x70(flag7=flag7, flag8=flag8)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800906000_x70(flag7=1043372700, flag8=1043379200):
    """State 0"""
    if not GetEventFlag(4 + flag8):
        """State 2,4"""
        assert t800906000_x50(text3=95010100, val5=2, val1=flag8, mode2=1)
        """State 3"""
        SetEventFlag(4 + flag8, 1)
    else:
        """State 1,5"""
        assert t800906000_x31(text1=95010400, mode6=1)
    """State 6"""
    return 0

def t800906000_x71(flag7=1043372700, flag8=1043379200):
    """State 0,1"""
    assert t800906000_x72(flag7=flag7, flag8=flag8)
    """State 2"""
    return 0

def t800906000_x72(flag7=1043372700, flag8=1043379200):
    """State 0,3"""
    call = t800906000_x11(z11=82100, val11=82100)
    if call.Get() == 1:
        """State 2,4"""
        assert t800906000_x73(flag7=flag7, flag8=flag8)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800906000_x73(flag7=1043372700, flag8=1043379200):
    """State 0"""
    if not GetEventFlag(5 + flag8):
        """State 2,4"""
        assert t800906000_x50(text3=95010800, val5=2, val1=flag8, mode2=1)
        """State 3"""
        SetEventFlag(5 + flag8, 1)
    else:
        """State 1,5"""
        assert t800906000_x31(text1=95011000, mode6=1)
    """State 6"""
    return 0

def t800906000_x74(flag7=1043372700, flag8=1043379200, shop1=129050, shop2=129099):
    """State 0"""
    if GetEventFlag(4980) == 1:
        """State 1"""
        assert t800906000_x75(flag7=flag7, flag8=flag8, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4982) == 1:
        """State 3"""
        assert t800906000_x80(flag7=flag7, flag8=flag8, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4983) == 1:
        """State 4"""
        assert t800906000_x83(flag7=flag7, flag8=flag8)
    """State 5"""
    Label('L0')
    return 0
    """Unused"""
    """State 2"""
    assert t800906000_x79(flag7=flag7, flag8=flag8)
    Goto('L0')

def t800906000_x75(flag7=1043372700, flag8=1043379200, shop1=129050, shop2=129099):
    """State 0,2"""
    assert t800906000_x76(flag7=flag7, flag8=flag8)
    """State 1"""
    assert t800906000_x52(flag7=flag7, flag8=flag8, shop1=shop1, shop2=shop2)
    """State 3"""
    assert t800906000_x89()
    """State 4"""
    return 0

def t800906000_x76(flag7=1043372700, flag8=1043379200):
    """State 0,3"""
    call = t800906000_x11(z11=80200, val11=80200)
    if call.Get() == 1:
        """State 2,4"""
        assert t800906000_x77(flag7=flag7, flag8=flag8)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800906000_x77(flag7=1043372700, flag8=1043379200):
    """State 0"""
    if not GetEventFlag(0 + flag7):
        """State 2,4"""
        assert t800906000_x50(text3=95004000, val5=3, val1=flag8, mode2=1)
        """State 3"""
        SetEventFlag(0 + flag7, 1)
    else:
        """State 1,5"""
        assert t800906000_x31(text1=95004200, mode6=1)
    """State 6"""
    return 0

def t800906000_x78():
    """State 0"""
    if 0 == (GetWorkValue(0) == GetEventFlagValue(1300, 8)):
        """State 1,3"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800906000_x31(text1=95008200, mode6=1)
    else:
        """State 2,4"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800906000_x31(text1=95004400, mode6=1)
    """State 5"""
    return 0

def t800906000_x79(flag7=1043372700, flag8=1043379200):
    """State 0,1"""
    SetEventFlag(5 + flag7, 1)
    def ExitPause():
        SetEventFlag(6 + flag7, 1)
    assert t800906000_x46(flag7=flag7, flag8=flag8, text1=95090590)
    """State 2"""
    return 0

def t800906000_x80(flag7=1043372700, flag8=1043379200, shop1=129050, shop2=129099):
    """State 0,3"""
    assert t800906000_x81(z3=0, flag9=0)
    """State 1"""
    assert t800906000_x52(flag7=flag7, flag8=flag8, shop1=shop1, shop2=shop2)
    """State 2"""
    assert t800906000_x59()
    """State 4"""
    return 0

def t800906000_x81(z3=0, flag9=0):
    """State 0,3"""
    call = t800906000_x11(z11=81200, val11=81200)
    if call.Get() == 1:
        """State 2,4"""
        assert t800906000_x82(z3=z3, flag9=flag9)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800906000_x82(z3=0, flag9=0):
    """State 0"""
    if not GetEventFlag(4 + flag9):
        """State 2,4"""
        assert t800906000_x50(text3=95010200, val5=3, val1=flag9, mode2=1)
        """State 3"""
        SetEventFlag(4 + flag9, 1)
    else:
        """State 1,5"""
        assert t800906000_x31(text1=95010500, mode6=1)
    """State 6"""
    return 0

def t800906000_x83(flag7=1043372700, flag8=1043379200):
    """State 0,1"""
    assert t800906000_x84(flag7=flag7, flag8=flag8)
    """State 2"""
    return 0

def t800906000_x84(flag7=1043372700, flag8=1043379200):
    """State 0,3"""
    call = t800906000_x11(z11=82200, val11=82200)
    if call.Get() == 1:
        """State 2,4"""
        assert t800906000_x85(flag7=flag7, flag8=flag8)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800906000_x85(flag7=1043372700, flag8=1043379200):
    """State 0"""
    if not GetEventFlag(5 + flag8):
        """State 2,4"""
        assert t800906000_x50(text3=95010900, val5=3, val1=flag8, mode2=1)
        """State 3"""
        SetEventFlag(5 + flag8, 1)
    else:
        """State 1,5"""
        assert t800906000_x31(text1=95011000, mode6=1)
    """State 6"""
    return 0

def t800906000_x86(flag7=1043372700, flag8=1043379200):
    """State 0,1"""
    assert t800906000_x11(z11=80002, val11=80002)
    """State 2"""
    return 0

def t800906000_x87(flag4=1043372700, flag5=1043379200):
    """State 0"""
    if not GetEventFlag(5 + flag4):
        """State 2"""
        if not GetEventFlag(48 + flag5):
            """State 4,6"""
            SetEventFlag(5 + flag4, 1)
            """State 8"""
            assert t800906000_x51(text2=95090100, val4=48, flag2=flag5, mode1=1)
        else:
            """State 5,7"""
            SetEventFlag(5 + flag4, 1)
            """State 9"""
            assert t800906000_x32(text4=95090300, mode5=1)
    else:
        """State 3"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 10"""
    return 0

def t800906000_x88(flag4=1043372700, flag5=1043379200):
    """State 0"""
    if not GetEventFlag(5 + flag4):
        """State 2"""
        if not GetEventFlag(48 + flag5):
            """State 4,8"""
            assert t800906000_x51(text2=95090190, val4=48, flag2=flag5, mode1=1)
        else:
            """State 5,7"""
            SetEventFlag(5 + flag4, 1)
            """State 9"""
            assert t800906000_x32(text4=95090390, mode5=1)
    else:
        """State 3"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 6"""
    SetEventFlag(5 + flag4, 1)
    Quit()
    """State 10"""
    return 0

def t800906000_x89():
    """State 0,3"""
    call = t800906000_x11(z11=80201, val11=80201)
    if call.Get() == 1:
        """State 2,4"""
        assert t800906000_x78()
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800906000_x90():
    """State 0,3"""
    call = t800906000_x11(z11=80001, val11=80001)
    if call.Get() == 1:
        """State 2,4"""
        assert t800906000_x55()
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800906000_x91():
    """State 0,3"""
    call = t800906000_x11(z11=80101, val11=80101)
    if call.Get() == 1:
        """State 2,4"""
        assert t800906000_x66()
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800906000_x92(val2=1043372700, val3=1043379200):
    """State 0,1,2"""
    SetEventFlag(8 + val3, 1)
    """State 3"""
    assert t800906000_x51(text2=95090000, val4=8, flag2=val2, mode1=1)
    """State 4"""
    return 0

def t800906000_x93(flag6=4960, flag7=1043372700, flag8=1043379200, shop1=129050, shop2=129099):
    """State 0"""
    if GetEventFlag(5 + flag6) == 1:
        """State 1"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800906000_x44(flag7=flag7, flag8=flag8, shop1=shop1, shop2=shop2)
    elif GetEventFlag(6 + flag6) == 1:
        """State 2"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800906000_x62(flag7=flag7, flag8=flag8, shop1=shop1, shop2=shop2)
    elif GetEventFlag(7 + flag6) == 1:
        """State 3"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800906000_x74(flag7=flag7, flag8=flag8, shop1=shop1, shop2=shop2)
    """State 4"""
    return 0

def t800906000_x94(flag3=4700, flag4=1043372700, flag5=1043379200):
    """State 0"""
    if GetEventFlag(5 + flag3) == 1 or GetEventFlag(6 + flag3) == 1:
        """State 1"""
        t800906000_x87(flag4=flag4, flag5=flag5)
        Quit()
    elif GetEventFlag(7 + flag3) == 1:
        """State 2"""
        t800906000_x88(flag4=flag4, flag5=flag5)
        Quit()
    """Unused"""
    """State 3"""
    return 0

def t800906000_x95(flag3=4700, flag4=1043372700, flag5=1043379200):
    """State 0,6"""
    # actionbutton:6000:"Talk"
    call = t800906000_x0(actionbutton1=6000, flag16=6001, flag20=6000, flag21=6000, flag22=6000, flag23=6000,
                         flag15=6000)
    if call.Done():
        """State 1"""
        pass
    elif IsPlayerAttacking() == 1:
        """State 5"""
        pass
    elif GetEventFlag(8 + flag4) == 1:
        """State 2"""
        pass
    """State 3,4"""
    if GetEventFlag(5 + flag3) == 1 or GetEventFlag(6 + flag3) == 1:
        """State 7"""
        t800906000_x87(flag4=flag4, flag5=flag5)
        def WhilePaused():
            c1_121(9612)
        Quit()
    elif GetEventFlag(7 + flag3) == 1:
        """State 8"""
        t800906000_x88(flag4=flag4, flag5=flag5)
        def WhilePaused():
            c1_121(9612)
        Quit()
    """Unused"""
    """State 9"""
    return 0

def t800906000_x96(z1=4700, flag2=1043372700, z2=1043379200):
    """State 0"""
    while True:
        """State 2"""
        # actionbutton:6000:"Talk"
        call = t800906000_x0(actionbutton1=6000, flag16=6001, flag20=6000, flag21=6000, flag22=6000,
                             flag23=6000, flag15=6000)
        if call.Done():
            break
        elif GetEventFlag(8 + flag2) == 1 and not GetEventFlag(9 + flag2):
            """State 1,3"""
            assert t800906000_x51(text2=95090000, val4=9, flag2=flag2, mode1=1)
    """State 4"""
    return 0

def t800906000_x97(flag1=1043372700, val1=1043379200):
    """State 0"""
    if not GetEventFlag(1043379220):
        """State 1,10"""
        assert t800906000_x31(text1=95008000, mode6=1)
        """State 7"""
        RequestAnimation(20015, -1)
        def WhilePaused():
            c1_121(9611)
        assert GetCurrentStateElapsedTime() > 2.5
        """State 8"""
        SetEventFlag(1043379220, 1)
        """State 4"""
        SetEventFlag(3 + val1, 1)
        """State 2"""
        SetEventFlag(0 + flag1, 1)
        """State 9"""
        assert t800906000_x3(lot1=100400) and not IsMenuOpen(63)
        """State 12"""
        assert t800906000_x31(text1=95008100, mode6=1)
    elif not GetEventFlag(0 + flag1):
        """State 3,11"""
        assert t800906000_x50(text3=95004000, val5=3, val1=val1, mode2=1)
        """State 5"""
        SetEventFlag(0 + flag1, 1)
    else:
        """State 6,13"""
        assert t800906000_x31(text1=95004200, mode6=1)
    """State 14"""
    return 0

def t800906000_x98():
    """State 0"""
    if GetEventFlagValue(1300, 8) > 10 and not GetEventFlag(4986) and not GetEventFlag(1043379223):
        """State 1,4"""
        assert t800906000_x99()
    else:
        """State 2,3"""
        assert t800906000_x100()
    """State 5"""
    return 0

def t800906000_x99():
    """State 0,4"""
    assert t800906000_x31(text1=95008300, mode6=1)
    """State 1"""
    def WhilePaused():
        c1_121(9611)
    def ExitPause():
        RequestAnimation(20015, -1)
    assert GetCurrentStateElapsedTime() > 3.5
    """State 2"""
    SetEventFlag(1043379223, 1)
    """State 3"""
    # lot:100410:Perfume Bottle
    assert t800906000_x3(lot1=100410) and not IsMenuOpen(63)
    """State 5"""
    assert t800906000_x31(text1=95008400, mode6=1)
    """State 6"""
    return 0

def t800906000_x100():
    """State 0"""
    if (GetEventFlag(1043379221) == 1 and GetEventFlag(1043379222) == 1 and (GetEventFlag(1043379224)
        == 1 or not GetEventFlag(1043379220))):
        """State 2,3"""
        SetEventFlag(1043379221, 0)
        SetEventFlag(1043379222, 0)
        SetEventFlag(1043379224, 0)
    else:
        """State 1"""
        pass
    """State 4"""
    if not GetEventFlag(1043379221):
        """State 5,8"""
        assert t800906000_x30(text5=95006000, z10=1043379221, mode7=1)
    elif not GetEventFlag(1043379222):
        """State 6,9"""
        assert t800906000_x30(text5=95006100, z10=1043379222, mode7=1)
    else:
        """State 7,10"""
        assert t800906000_x30(text5=95008101, z10=1043379224, mode7=1)
    """State 11"""
    return 0

