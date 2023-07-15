# -*- coding: utf-8 -*-
def t800036000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t800036000_x5(flag22=4743, flag23=4741, flag24=4742, val6=5, val7=10, val8=12, val9=10, val10=12,
                  actionbutton1=6000, flag25=6000, flag26=6001, flag27=6000, flag28=6000, flag29=6000,
                  z9=1, z10=1000000, z11=1000000, z12=1000000, mode3=1, mode4=1)
    Quit()

def t800036000_1000():
    """State 0,2,3"""
    assert t800036000_x42(flag5=4740, flag6=1041362700, flag7=1041369200, shop1=123050, shop2=123099)
    """State 1"""
    c1_120(1000)
    Quit()

def t800036000_1001():
    """State 0,2,3"""
    assert t800036000_x43(flag11=1041362700, z6=1041369200)
    """State 1"""
    c1_120(1001)
    Quit()

def t800036000_1100():
    """State 0,2,3"""
    assert t800036000_x44(val1=1041362700, val2=1041369200)
    """State 1"""
    c1_120(1100)
    Quit()

def t800036000_1101():
    """State 0,2,3"""
    assert t800036000_x45(flag9=1041362700, z4=1041369200)
    """State 1"""
    c1_120(1101)
    Quit()

def t800036000_1102():
    """State 0,1,2"""
    t800036000_x46(flag2=4740, flag3=1041362700, flag4=1041369200)
    Quit()

def t800036000_1103():
    """State 0,2,3"""
    assert t800036000_x47()
    """State 1"""
    c1_120(1103)
    Quit()

def t800036000_2000():
    """State 0,2,3"""
    assert t800036000_x48(z1=4740, flag1=1041362700, z2=1041369200)
    """State 1"""
    c1_120(2000)
    Quit()

def t800036000_80001():
    """State 0,2"""
    assert t800036000_x39(z8=1044349220, flag15=1044349223, flag16=1044349224, flag17=1044349225)
    """State 1"""
    c1_120(80001)
    Quit()

def t800036000_80002():
    """State 0,2"""
    assert t800036000_x37()
    """State 1"""
    c1_120(80002)
    Quit()

def t800036000_80101():
    """State 0,2"""
    assert t800036000_x41(z7=1044349220, flag12=1044349223, flag13=1044349224, flag14=1044349225)
    """State 1"""
    c1_120(80101)
    Quit()

def t800036000_80200():
    """State 0,2"""
    assert t800036000_x36(flag10=1041362700, val4=1041369200, z5=1044349220)
    """State 1"""
    c1_120(80200)
    Quit()

def t800036000_80201():
    """State 0,2"""
    assert t800036000_x38(flag18=1044349220, flag19=1044349223, flag20=1044349224, flag21=1044349225)
    """State 1"""
    c1_120(80201)
    Quit()

def t800036000_x0(actionbutton1=6000, flag26=6001, flag30=6000, flag31=6000, flag32=6000, flag33=6000,
                  flag25=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag26) == 1 or GetEventFlag(flag30) == 1 or GetEventFlag(flag31) == 1 or
                GetEventFlag(flag32) == 1 or GetEventFlag(flag33) == 1)
        """State 4"""
        assert not GetEventFlag(flag25)
        """State 2"""
        if GetEventFlag(flag25) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag26) and not GetEventFlag(flag30) and not GetEventFlag(flag31) and
              not GetEventFlag(flag32) and not GetEventFlag(flag33)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t800036000_x1():
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

def t800036000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t800036000_x3(val7=10, val8=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val7 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t800036000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val8 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t800036000_x1()
    else:
        """State 4,7"""
        call = t800036000_x33()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val8 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t800036000_x1()
    """State 9"""
    return 0

def t800036000_x4():
    """State 0,1"""
    assert t800036000_x1()
    """State 2"""
    return 0

def t800036000_x5(flag22=4743, flag23=4741, flag24=4742, val6=5, val7=10, val8=12, val9=10, val10=12,
                  actionbutton1=6000, flag25=6000, flag26=6001, flag27=6000, flag28=6000, flag29=6000,
                  z9=1, z10=1000000, z11=1000000, z12=1000000, mode3=1, mode4=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t800036000_x22(flag22=flag22, flag23=flag23, flag24=flag24, val6=val6, val7=val7, val8=val8,
                              val9=val9, val10=val10, actionbutton1=actionbutton1, flag25=flag25, flag26=flag26,
                              flag27=flag27, flag28=flag28, flag29=flag29, z9=z9, z10=z10, z11=z11, z12=z12,
                              mode3=mode3, mode4=mode4)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t800036000_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t800036000_x6(val6=5, val7=10, val8=12, val9=10, val10=12, actionbutton1=6000, flag25=6000, flag26=6001,
                  flag27=6000, flag28=6000, flag29=6000, z9=1, z10=1000000, z11=1000000, z12=1000000,
                  mode3=1, mode4=1):
    """State 0"""
    while True:
        """State 2"""
        call = t800036000_x9(actionbutton1=actionbutton1, flag25=flag25, flag26=flag26, z10=z10, z11=z11,
                             z12=z12)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t800036000_x13(val6=val6, z9=z9)
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
        elif GetEventFlag(flag29) == 1:
            Goto('L0')
        elif GetEventFlag(flag27) == 1 and not GetEventFlag(flag28) and GetDistanceToPlayer() < val9:
            """State 5"""
            call = t800036000_x15(val10=val10)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val10 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t800036000_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t800036000_x11(val7=val7, val8=val8)
    """Unused"""
    """State 7"""
    return 0

def t800036000_x7(val7=10, val8=12):
    """State 0,1"""
    call = t800036000_x17(val7=val7, val8=val8)
    assert IsPlayerDead() == 1
    """State 2"""
    t800036000_x3(val7=val7, val8=val8)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t800036000_x8(flag22=4743, val7=10, val8=12):
    """State 0,8"""
    assert t800036000_x35()
    """State 1"""
    if GetEventFlag(flag22) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val7:
            """State 4,6"""
            call = t800036000_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val8 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t800036000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t800036000_x9(actionbutton1=6000, flag25=6000, flag26=6001, z10=1000000, z11=1000000, z12=1000000):
    """State 0,1"""
    call = t800036000_x10(z14=2000, val11=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t800036000_x0(actionbutton1=actionbutton1, flag26=flag26, flag30=6000, flag31=6000, flag32=6000,
                flag33=6000, flag25=flag25))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800036000_x10(z14=_, val11=_):
    """State 0,1"""
    if f203(z14) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z14)
        assert f202() == val11
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t800036000_x11(val7=10, val8=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t800036000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val7:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t800036000_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val8 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t800036000_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t800036000_x12():
    """State 0,1"""
    assert t800036000_x10(z14=1101, val11=1101)
    """State 2"""
    return 0

def t800036000_x13(val6=5, z9=1):
    """State 0,2"""
    assert t800036000_x23()
    """State 1"""
    call = t800036000_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val6 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t800036000_x25()
    """State 4"""
    return 0

def t800036000_x14():
    """State 0,1"""
    assert t800036000_x10(z14=1000, val11=1000)
    """State 2"""
    return 0

def t800036000_x15(val10=12):
    """State 0,1"""
    call = t800036000_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val10 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t800036000_x26()
    """State 3"""
    return 0

def t800036000_x16():
    """State 0,1"""
    assert t800036000_x10(z14=1100, val11=1100)
    """State 2"""
    return 0

def t800036000_x17(val7=10, val8=12):
    """State 0,5"""
    assert t800036000_x35()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val7
        """State 3"""
        call = t800036000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val8 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t800036000_x28()
    """Unused"""
    """State 6"""
    return 0

def t800036000_x18():
    """State 0,2"""
    call = t800036000_x10(z14=1102, val11=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t800036000_x19():
    """State 0,1"""
    assert t800036000_x10(z14=1001, val11=1001)
    """State 2"""
    return 0

def t800036000_x20():
    """State 0,1"""
    assert t800036000_x10(z14=1103, val11=1103)
    """State 2"""
    return 0

def t800036000_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t800036000_x22(flag22=4743, flag23=4741, flag24=4742, val6=5, val7=10, val8=12, val9=10, val10=12,
                   actionbutton1=6000, flag25=6000, flag26=6001, flag27=6000, flag28=6000, flag29=6000,
                   z9=1, z10=1000000, z11=1000000, z12=1000000, mode3=1, mode4=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t800036000_x6(val6=val6, val7=val7, val8=val8, val9=val9, val10=val10, actionbutton1=actionbutton1,
                             flag25=flag25, flag26=flag26, flag27=flag27, flag28=flag28, flag29=flag29,
                             z9=z9, z10=z10, z11=z11, z12=z12, mode3=mode3, mode4=mode4)
        if CheckSelfDeath() == 1 or GetEventFlag(flag22) == 1:
            """State 3"""
            Label('L0')
            call = t800036000_x8(flag22=flag22, val7=val7, val8=val8)
            if not CheckSelfDeath() and not GetEventFlag(flag22):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag23) == 1 or GetEventFlag(flag24) == 1:
            """State 2"""
            call = t800036000_x7(val7=val7, val8=val8)
            if CheckSelfDeath() == 1 or GetEventFlag(flag22) == 1:
                Goto('L0')
            elif not GetEventFlag(flag23) and not GetEventFlag(flag24):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t800036000_x34() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t800036000_x23():
    """State 0,1"""
    assert t800036000_x24()
    """State 2"""
    return 0

def t800036000_x24():
    """State 0,1"""
    assert t800036000_x10(z14=1104, val11=1104)
    """State 2"""
    return 0

def t800036000_x25():
    """State 0,1"""
    call = t800036000_x10(z14=1201, val11=1201)
    if call.Get() == 1:
        """State 2"""
        assert t800036000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800036000_x26():
    """State 0,1"""
    call = t800036000_x10(z14=1300, val11=1300)
    if call.Get() == 1:
        """State 2"""
        assert t800036000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800036000_x27():
    """State 0,1"""
    call = t800036000_x10(z14=1301, val11=1301)
    if call.Get() == 1:
        """State 2"""
        assert t800036000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800036000_x28():
    """State 0,1"""
    call = t800036000_x10(z14=1302, val11=1302)
    if call.Get() == 1:
        """State 2"""
        assert t800036000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800036000_x29(text5=_, z13=_, mode7=1):
    """State 0,5"""
    assert t800036000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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
    SetEventFlag(z13, 1)
    """State 6"""
    return 0

def t800036000_x30(text1=_, mode6=1):
    """State 0,4"""
    assert t800036000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t800036000_x31(text4=_, mode5=1):
    """State 0,4"""
    assert t800036000_x32() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t800036000_x32():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t800036000_x33():
    """State 0,1"""
    assert t800036000_x10(z14=1002, val11=1002)
    """State 2"""
    return 0

def t800036000_x34():
    """State 0,1"""
    assert t800036000_x1()
    """State 2"""
    return 0

def t800036000_x35():
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

def t800036000_x36(flag10=1041362700, val4=1041369200, z5=1044349220):
    """State 0"""
    if not GetEventFlag(0 + flag10):
        """State 1"""
        if (not GetEventFlag(1041369224) and not GetEventFlag(1044349225) and not GetEventFlag(1045369225)
            and not GetEventFlag(1043399225)):
            """State 4,8"""
            assert t800036000_x55(text3=95004000, val5=3, flag7=val4, mode2=1)
        else:
            """State 5,10"""
            assert t800036000_x55(text3=95200000, val5=3, flag7=val4, mode2=1)
            """State 6"""
            SetEventFlag(z5, 1)
            """State 7"""
            SetEventFlag(1041369222, 0)
            SetEventFlag(1041369223, 0)
            SetEventFlag(1041369224, 0)
            SetEventFlag(1044349223, 0)
            SetEventFlag(1044349224, 0)
            SetEventFlag(1044349225, 0)
            SetEventFlag(1045369223, 0)
            SetEventFlag(1045369224, 0)
            SetEventFlag(1045369225, 0)
            SetEventFlag(1043399223, 0)
            SetEventFlag(1043399224, 0)
            SetEventFlag(1043399225, 0)
        """State 2"""
        SetEventFlag(0 + flag10, 1)
    else:
        """State 3,9"""
        assert t800036000_x30(text1=95004200, mode6=1)
    """State 11"""
    return 0

def t800036000_x37():
    """State 0"""
    if GetEventFlag(1041369220) == 1 and GetEventFlag(1041369221) == 1:
        """State 2,3"""
        SetEventFlag(1041369220, 0)
        SetEventFlag(1041369221, 0)
    else:
        """State 1"""
        pass
    """State 4"""
    if not GetEventFlag(1041369220):
        """State 5,7"""
        assert t800036000_x29(text5=95206000, z13=1041369220, mode7=1)
    elif not GetEventFlag(1041369221):
        """State 6,8"""
        assert t800036000_x29(text5=95206100, z13=1041369221, mode7=1)
    """State 9"""
    return 0

def t800036000_x38(flag18=1044349220, flag19=1044349223, flag20=1044349224, flag21=1044349225):
    """State 0"""
    if not GetEventFlag(flag18):
        """State 2,8"""
        call = t800036000_x40(flag12=flag19, flag13=flag20, flag14=flag21)
        if call.Done() and 1 == (GetWorkValue(0) == GetEventFlagValue(1300, 8)):
            """State 3,5"""
            assert t800036000_x30(text1=95004400, mode6=1)
        elif call.Done():
            """State 4,6"""
            assert t800036000_x30(text1=95008200, mode6=1)
    else:
        """State 1,7"""
        assert t800036000_x30(text1=95200100, mode6=1)
    """State 9"""
    return 0

def t800036000_x39(z8=1044349220, flag15=1044349223, flag16=1044349224, flag17=1044349225):
    """State 0,7"""
    call = t800036000_x40(flag12=flag15, flag13=flag16, flag14=flag17)
    if call.Done() and 0 == (GetWorkValue(0) == GetEventFlagValue(1300, 8)):
        """State 1,4"""
        assert t800036000_x30(text1=95008200, mode6=1)
    elif call.Done() and DidYouDoSomethingInTheMenu(0) == 1:
        """State 2,5"""
        assert t800036000_x30(text1=95002500, mode6=1)
    elif call.Done():
        """State 3,6"""
        assert t800036000_x30(text1=95002400, mode6=1)
    """State 8"""
    return 0

def t800036000_x40(flag12=1044349223, flag13=1044349224, flag14=1044349225):
    """State 0"""
    if not DidYouDoSomethingInTheMenu(0):
        """State 1"""
        pass
    elif GetEventFlag(1041362703) == 1:
        """State 2"""
        pass
    elif not GetEventFlag(flag12):
        """State 4,7"""
        SetEventFlag(flag12, 1)
        """State 10"""
        Label('L0')
        SetEventFlag(1041362703, 1)
    elif not GetEventFlag(flag13):
        """State 6,8"""
        SetEventFlag(flag13, 1)
        Goto('L0')
    elif not GetEventFlag(flag14):
        """State 5,9"""
        SetEventFlag(flag14, 1)
        Goto('L0')
    else:
        """State 3"""
        pass
    """State 11"""
    return 0

def t800036000_x41(z7=1044349220, flag12=1044349223, flag13=1044349224, flag14=1044349225):
    """State 0,7"""
    call = t800036000_x40(flag12=flag12, flag13=flag13, flag14=flag14)
    if call.Done() and 0 == (GetWorkValue(0) == GetEventFlagValue(1300, 8)):
        """State 1,4"""
        assert t800036000_x30(text1=95008200, mode6=1)
    elif call.Done() and DidYouDoSomethingInTheMenu(0) == 1:
        """State 2,5"""
        assert t800036000_x30(text1=95000500, mode6=1)
    elif call.Done():
        """State 3,6"""
        assert t800036000_x30(text1=95002400, mode6=1)
    """State 8"""
    return 0

def t800036000_x42(flag5=4740, flag6=1041362700, flag7=1041369200, shop1=123050, shop2=123099):
    """State 0,1"""
    def WhilePaused():
        c1_121(9610)
    assert t800036000_x98(flag5=flag5, flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    """State 2"""
    return 0

def t800036000_x43(flag11=1041362700, z6=1041369200):
    """State 0"""
    if GetEventFlag(6 + flag11) == 1:
        """State 1,3"""
        assert t800036000_x31(text4=95090800, mode5=1)
    else:
        """State 2,4"""
        assert t800036000_x31(text4=95090900, mode5=1)
    """State 5"""
    return 0

def t800036000_x44(val1=1041362700, val2=1041369200):
    """State 0,1"""
    assert t800036000_x97(val1=val1, val2=val2)
    """State 2"""
    return 0

def t800036000_x45(flag9=1041362700, z4=1041369200):
    """State 0"""
    if not GetEventFlag(7 + flag9):
        """State 1,3"""
        assert t800036000_x56(text2=95090000, val3=7, flag1=flag9, mode1=1)
    else:
        """State 2"""
        pass
    """State 4"""
    return 0

def t800036000_x46(flag2=4740, flag3=1041362700, flag4=1041369200):
    """State 0"""
    if not DoesSelfHaveSpEffect(9602):
        """State 1"""
        t800036000_x99(flag2=flag2, flag3=flag3, flag4=flag4)
        def WhilePaused():
            c1_121(9612)
        Quit()
    else:
        """State 2"""
        t800036000_x100(flag2=flag2, flag3=flag3, flag4=flag4)
        def ExitPause():
            c1_121(9612)
        Quit()
    """Unused"""
    """State 3"""
    return 0

def t800036000_x47():
    """State 0,1,3"""
    assert t800036000_x31(text4=95091100, mode5=1)
    """State 5"""
    Label('L0')
    return 0
    """Unused"""
    """State 2,4"""
    assert t800036000_x31(text4=95091000, mode5=1)
    Goto('L0')

def t800036000_x48(z1=4740, flag1=1041362700, z2=1041369200):
    """State 0,1"""
    assert t800036000_x101(z1=z1, flag1=flag1, z2=z2)
    """State 2"""
    return 0

def t800036000_x49(flag6=1041362700, flag7=1041369200, shop1=123050, shop2=123099):
    """State 0"""
    if GetEventFlag(4980) == 1:
        """State 1"""
        assert t800036000_x50(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4982) == 1:
        """State 2"""
        assert t800036000_x52(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4983) == 1:
        """State 3"""
        assert t800036000_x53(flag6=flag6, flag7=flag7)
    """State 5"""
    Label('L0')
    return 0
    """Unused"""
    """State 4"""
    assert t800036000_x61(flag6=flag6, flag7=flag7)
    Goto('L0')

def t800036000_x50(flag6=1041362700, flag7=1041369200, shop1=123050, shop2=123099):
    """State 0,1"""
    assert t800036000_x54(flag6=flag6, flag7=flag7)
    """State 2"""
    assert t800036000_x57(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    """State 3"""
    assert t800036000_x95()
    """State 4"""
    return 0

def t800036000_x51(flag6=1041362700, flag7=1041369200, text1=_):
    """State 0,3"""
    assert t800036000_x30(text1=text1, mode6=1)
    """State 1"""
    SetEventFlag(48 + flag7, 1)
    """State 2"""
    SetEventFlag(6 + flag6, 1)
    """State 4"""
    assert t800036000_x56(text2=95090505, val3=5, flag1=flag6, mode1=1)
    """State 5"""
    return 0

def t800036000_x52(flag6=1041362700, flag7=1041369200, shop1=123050, shop2=123099):
    """State 0,1"""
    assert t800036000_x62(flag6=flag6, flag7=flag7)
    """State 2"""
    assert t800036000_x57(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    """State 3"""
    assert t800036000_x64()
    """State 4"""
    return 0

def t800036000_x53(flag6=1041362700, flag7=1041369200):
    """State 0,1"""
    assert t800036000_x65(flag6=flag6, flag7=flag7)
    """State 2"""
    return 0

def t800036000_x54(flag6=1041362700, flag7=1041369200):
    """State 0,3"""
    call = t800036000_x10(z14=80000, val11=80000)
    if call.Get() == 1:
        """State 2,4"""
        assert t800036000_x59(flag6=flag6, flag7=flag7)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800036000_x55(text3=_, val5=_, flag7=_, mode2=1):
    """State 0,5"""
    assert t800036000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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
    SetEventFlag(val5 + flag7, 1)
    """State 6"""
    return 0

def t800036000_x56(text2=_, val3=_, flag1=_, mode1=1):
    """State 0,5"""
    assert t800036000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t800036000_x57(flag6=1041362700, flag7=1041369200, shop1=123050, shop2=123099):
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
            assert t800036000_x58(flag6=flag6, flag7=flag7) and CheckSpecificPersonTalkHasEnded(0) == 1
        else:
            """State 9"""
            return 0

def t800036000_x58(flag6=1041362700, flag7=1041369200):
    """State 0"""
    if GetEventFlag(4980) == 1:
        """State 1,4"""
        assert t800036000_x91(flag6=flag6, flag7=flag7)
    else:
        """State 2,3"""
        assert t800036000_x30(text1=95006500, mode6=1)
    """State 5"""
    return 0

def t800036000_x59(flag6=1041362700, flag7=1041369200):
    """State 0"""
    if not GetEventFlag(0 + flag6):
        """State 2"""
        if not GetEventFlag(4985):
            """State 3,6"""
            assert t800036000_x55(text3=95000100, val5=1, flag7=flag7, mode2=1)
        else:
            """State 4,7"""
            assert t800036000_x55(text3=95000200, val5=1, flag7=flag7, mode2=1)
        """State 5"""
        SetEventFlag(0 + flag6, 1)
    else:
        """State 1,8"""
        assert t800036000_x30(text1=95000300, mode6=1)
    """State 9"""
    return 0

def t800036000_x60():
    """State 0"""
    if 0 == (GetWorkValue(0) == GetEventFlagValue(1300, 8)):
        """State 1,4"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800036000_x30(text1=95008200, mode6=1)
    elif DidYouDoSomethingInTheMenu(0) == 1:
        """State 2,5"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800036000_x30(text1=95000500, mode6=1)
    else:
        """State 3,6"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800036000_x30(text1=95002400, mode6=1)
    """State 7"""
    return 0

def t800036000_x61(flag6=1041362700, flag7=1041369200):
    """State 0,1"""
    SetEventFlag(5 + flag6, 1)
    def ExitPause():
        SetEventFlag(6 + flag6, 1)
    assert t800036000_x51(flag6=flag6, flag7=flag7, text1=95090500)
    """State 2"""
    return 0

def t800036000_x62(flag6=1041362700, flag7=1041369200):
    """State 0,3"""
    call = t800036000_x10(z14=81000, val11=81000)
    if call.Get() == 1:
        """State 2,4"""
        assert t800036000_x63(flag6=flag6, flag7=flag7)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800036000_x63(flag6=1041362700, flag7=1041369200):
    """State 0"""
    if not GetEventFlag(4 + flag7):
        """State 2,4"""
        assert t800036000_x55(text3=95010000, val5=1, flag7=flag7, mode2=1)
        """State 3"""
        SetEventFlag(4 + flag7, 1)
    else:
        """State 1,5"""
        assert t800036000_x30(text1=95010300, mode6=1)
    """State 6"""
    return 0

def t800036000_x64():
    """State 0,1"""
    def ExitPause():
        RequestAnimation(20012, -1)
    assert t800036000_x30(text1=95010600, mode6=1)
    """State 2"""
    return 0

def t800036000_x65(flag6=1041362700, flag7=1041369200):
    """State 0,3"""
    call = t800036000_x10(z14=82000, val11=82000)
    if call.Get() == 1:
        """State 2,4"""
        assert t800036000_x66(flag6=flag6, flag7=flag7)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800036000_x66(flag6=1041362700, flag7=1041369200):
    """State 0"""
    if not GetEventFlag(5 + flag7):
        """State 2,4"""
        assert t800036000_x55(text3=95010700, val5=1, flag7=flag7, mode2=1)
        """State 3"""
        SetEventFlag(5 + flag7, 1)
    else:
        """State 1,5"""
        assert t800036000_x30(text1=95011000, mode6=1)
    """State 6"""
    return 0

def t800036000_x67(flag6=1041362700, flag7=1041369200, shop1=123050, shop2=123099):
    """State 0"""
    if GetEventFlag(4980) == 1:
        """State 1"""
        assert t800036000_x68(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4982) == 1:
        """State 3"""
        assert t800036000_x73(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4983) == 1:
        """State 4"""
        assert t800036000_x76(flag6=flag6, flag7=flag7)
    """State 5"""
    Label('L0')
    return 0
    """Unused"""
    """State 2"""
    assert t800036000_x72(flag6=flag6, flag7=flag7)
    Goto('L0')

def t800036000_x68(flag6=1041362700, flag7=1041369200, shop1=123050, shop2=123099):
    """State 0,2"""
    assert t800036000_x69(flag6=flag6, flag7=flag7)
    """State 1"""
    assert t800036000_x57(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    """State 3"""
    assert t800036000_x96()
    """State 4"""
    return 0

def t800036000_x69(flag6=1041362700, flag7=1041369200):
    """State 0,3"""
    call = t800036000_x10(z14=80100, val11=80100)
    if call.Get() == 1:
        """State 2,4"""
        assert t800036000_x70(flag6=flag6, flag7=flag7)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800036000_x70(flag6=1041362700, flag7=1041369200):
    """State 0"""
    if not GetEventFlag(0 + flag6):
        """State 2,4"""
        assert t800036000_x55(text3=95002000, val5=2, flag7=flag7, mode2=1)
        """State 3"""
        SetEventFlag(0 + flag6, 1)
    else:
        """State 1,5"""
        assert t800036000_x30(text1=95002200, mode6=1)
    """State 6"""
    return 0

def t800036000_x71():
    """State 0"""
    if 0 == (GetWorkValue(0) == GetEventFlagValue(1300, 8)):
        """State 1,4"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800036000_x30(text1=95008200, mode6=1)
    elif DidYouDoSomethingInTheMenu(0) == 1:
        """State 2,5"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800036000_x30(text1=95002500, mode6=1)
    else:
        """State 3,6"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800036000_x30(text1=95002400, mode6=1)
    """State 7"""
    return 0

def t800036000_x72(flag6=1041362700, flag7=1041369200):
    """State 0,1"""
    SetEventFlag(5 + flag6, 1)
    def ExitPause():
        SetEventFlag(6 + flag6, 1)
    assert t800036000_x51(flag6=flag6, flag7=flag7, text1=95090500)
    """State 2"""
    return 0

def t800036000_x73(flag6=1041362700, flag7=1041369200, shop1=123050, shop2=123099):
    """State 0,3"""
    assert t800036000_x74(flag6=flag6, flag7=flag7)
    """State 1"""
    assert t800036000_x57(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    """State 2"""
    assert t800036000_x64()
    """State 4"""
    return 0

def t800036000_x74(flag6=1041362700, flag7=1041369200):
    """State 0,3"""
    call = t800036000_x10(z14=81100, val11=81100)
    if call.Get() == 1:
        """State 2,4"""
        assert t800036000_x75(flag6=flag6, flag7=flag7)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800036000_x75(flag6=1041362700, flag7=1041369200):
    """State 0"""
    if not GetEventFlag(4 + flag7):
        """State 2,4"""
        assert t800036000_x55(text3=95010100, val5=2, flag7=flag7, mode2=1)
        """State 3"""
        SetEventFlag(4 + flag7, 1)
    else:
        """State 1,5"""
        assert t800036000_x30(text1=95010400, mode6=1)
    """State 6"""
    return 0

def t800036000_x76(flag6=1041362700, flag7=1041369200):
    """State 0,1"""
    assert t800036000_x77(flag6=flag6, flag7=flag7)
    """State 2"""
    return 0

def t800036000_x77(flag6=1041362700, flag7=1041369200):
    """State 0,3"""
    call = t800036000_x10(z14=82100, val11=82100)
    if call.Get() == 1:
        """State 2,4"""
        assert t800036000_x78(flag6=flag6, flag7=flag7)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800036000_x78(flag6=1041362700, flag7=1041369200):
    """State 0"""
    if not GetEventFlag(5 + flag7):
        """State 2,4"""
        assert t800036000_x55(text3=95010800, val5=2, flag7=flag7, mode2=1)
        """State 3"""
        SetEventFlag(5 + flag7, 1)
    else:
        """State 1,5"""
        assert t800036000_x30(text1=95011000, mode6=1)
    """State 6"""
    return 0

def t800036000_x79(flag6=1041362700, flag7=1041369200, shop1=123050, shop2=123099):
    """State 0"""
    if GetEventFlag(4980) == 1:
        """State 1"""
        assert t800036000_x80(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4982) == 1:
        """State 3"""
        assert t800036000_x85(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    elif GetEventFlag(4983) == 1:
        """State 4"""
        assert t800036000_x88(flag6=flag6, flag7=flag7)
    """State 5"""
    Label('L0')
    return 0
    """Unused"""
    """State 2"""
    assert t800036000_x84(flag6=flag6, flag7=flag7)
    Goto('L0')

def t800036000_x80(flag6=1041362700, flag7=1041369200, shop1=123050, shop2=123099):
    """State 0,2"""
    assert t800036000_x81(flag6=flag6, flag7=flag7)
    """State 1"""
    assert t800036000_x57(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    """State 3"""
    assert t800036000_x94()
    """State 4"""
    return 0

def t800036000_x81(flag6=1041362700, flag7=1041369200):
    """State 0,3"""
    call = t800036000_x10(z14=80200, val11=80200)
    if call.Get() == 1:
        """State 2,4"""
        assert t800036000_x82(flag6=flag6, flag7=flag7)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800036000_x82(flag6=1041362700, flag7=1041369200):
    """State 0"""
    if not GetEventFlag(0 + flag6):
        """State 2,4"""
        assert t800036000_x55(text3=95004000, val5=3, flag7=flag7, mode2=1)
        """State 3"""
        SetEventFlag(0 + flag6, 1)
    else:
        """State 1,5"""
        assert t800036000_x30(text1=95004200, mode6=1)
    """State 6"""
    return 0

def t800036000_x83():
    """State 0"""
    if 0 == (GetWorkValue(0) == GetEventFlagValue(1300, 8)):
        """State 1,3"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800036000_x30(text1=95008200, mode6=1)
    else:
        """State 2,4"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800036000_x30(text1=95004400, mode6=1)
    """State 5"""
    return 0

def t800036000_x84(flag6=1041362700, flag7=1041369200):
    """State 0,1"""
    SetEventFlag(5 + flag6, 1)
    def ExitPause():
        SetEventFlag(6 + flag6, 1)
    assert t800036000_x51(flag6=flag6, flag7=flag7, text1=95090590)
    """State 2"""
    return 0

def t800036000_x85(flag6=1041362700, flag7=1041369200, shop1=123050, shop2=123099):
    """State 0,3"""
    assert t800036000_x86(z3=0, flag8=0)
    """State 1"""
    assert t800036000_x57(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    """State 2"""
    assert t800036000_x64()
    """State 4"""
    return 0

def t800036000_x86(z3=0, flag8=0):
    """State 0,3"""
    call = t800036000_x10(z14=81200, val11=81200)
    if call.Get() == 1:
        """State 2,4"""
        assert t800036000_x87(z3=z3, flag8=flag8)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800036000_x87(z3=0, flag8=0):
    """State 0"""
    if not GetEventFlag(4 + flag8):
        """State 2,4"""
        assert t800036000_x55(text3=95010200, val5=3, flag7=flag8, mode2=1)
        """State 3"""
        SetEventFlag(4 + flag8, 1)
    else:
        """State 1,5"""
        assert t800036000_x30(text1=95010500, mode6=1)
    """State 6"""
    return 0

def t800036000_x88(flag6=1041362700, flag7=1041369200):
    """State 0,1"""
    assert t800036000_x89(flag6=flag6, flag7=flag7)
    """State 2"""
    return 0

def t800036000_x89(flag6=1041362700, flag7=1041369200):
    """State 0,3"""
    call = t800036000_x10(z14=82200, val11=82200)
    if call.Get() == 1:
        """State 2,4"""
        assert t800036000_x90(flag6=flag6, flag7=flag7)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800036000_x90(flag6=1041362700, flag7=1041369200):
    """State 0"""
    if not GetEventFlag(5 + flag7):
        """State 2,4"""
        assert t800036000_x55(text3=95010900, val5=3, flag7=flag7, mode2=1)
        """State 3"""
        SetEventFlag(5 + flag7, 1)
    else:
        """State 1,5"""
        assert t800036000_x30(text1=95011000, mode6=1)
    """State 6"""
    return 0

def t800036000_x91(flag6=1041362700, flag7=1041369200):
    """State 0,1"""
    assert t800036000_x10(z14=80002, val11=80002)
    """State 2"""
    return 0

def t800036000_x92(flag3=1041362700, flag4=1041369200):
    """State 0"""
    if not GetEventFlag(5 + flag3):
        """State 2"""
        if not GetEventFlag(48 + flag4):
            """State 4,6"""
            SetEventFlag(5 + flag3, 1)
            """State 8"""
            assert t800036000_x56(text2=95090100, val3=48, flag1=flag4, mode1=1)
        else:
            """State 5,7"""
            SetEventFlag(5 + flag3, 1)
            """State 9"""
            assert t800036000_x31(text4=95090300, mode5=1)
    else:
        """State 3"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 10"""
    return 0

def t800036000_x93(flag3=1041362700, flag4=1041369200):
    """State 0"""
    if not GetEventFlag(5 + flag3):
        """State 2"""
        if not GetEventFlag(48 + flag4):
            """State 4,8"""
            assert t800036000_x56(text2=95090190, val3=48, flag1=flag4, mode1=1)
        else:
            """State 5,7"""
            SetEventFlag(5 + flag3, 1)
            """State 9"""
            assert t800036000_x31(text4=95090390, mode5=1)
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

def t800036000_x94():
    """State 0,3"""
    call = t800036000_x10(z14=80201, val11=80201)
    if call.Get() == 1:
        """State 2,4"""
        assert t800036000_x83()
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800036000_x95():
    """State 0,3"""
    call = t800036000_x10(z14=80001, val11=80001)
    if call.Get() == 1:
        """State 2,4"""
        assert t800036000_x60()
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800036000_x96():
    """State 0,3"""
    call = t800036000_x10(z14=80101, val11=80101)
    if call.Get() == 1:
        """State 2,4"""
        assert t800036000_x71()
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t800036000_x97(val1=1041362700, val2=1041369200):
    """State 0,1,2"""
    SetEventFlag(8 + val2, 1)
    """State 3"""
    assert t800036000_x56(text2=95090000, val3=8, flag1=val1, mode1=1)
    """State 4"""
    return 0

def t800036000_x98(flag5=4740, flag6=1041362700, flag7=1041369200, shop1=123050, shop2=123099):
    """State 0"""
    if GetEventFlag(5 + flag5) == 1:
        """State 1"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800036000_x49(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    elif GetEventFlag(6 + flag5) == 1:
        """State 2"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800036000_x67(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    elif GetEventFlag(7 + flag5) == 1:
        """State 3"""
        def ExitPause():
            RequestAnimation(20012, -1)
        assert t800036000_x79(flag6=flag6, flag7=flag7, shop1=shop1, shop2=shop2)
    """State 4"""
    return 0

def t800036000_x99(flag2=4740, flag3=1041362700, flag4=1041369200):
    """State 0"""
    if GetEventFlag(5 + flag2) == 1 or GetEventFlag(6 + flag2) == 1:
        """State 1"""
        t800036000_x92(flag3=flag3, flag4=flag4)
        Quit()
    elif GetEventFlag(7 + flag2) == 1:
        """State 2"""
        t800036000_x93(flag3=flag3, flag4=flag4)
        Quit()
    """Unused"""
    """State 3"""
    return 0

def t800036000_x100(flag2=4740, flag3=1041362700, flag4=1041369200):
    """State 0,6"""
    # actionbutton:6000:"Talk"
    call = t800036000_x0(actionbutton1=6000, flag26=6001, flag30=6000, flag31=6000, flag32=6000, flag33=6000,
                         flag25=6000)
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
        t800036000_x92(flag3=flag3, flag4=flag4)
        def WhilePaused():
            c1_121(9612)
        Quit()
    elif GetEventFlag(7 + flag2) == 1:
        """State 8"""
        t800036000_x93(flag3=flag3, flag4=flag4)
        def WhilePaused():
            c1_121(9612)
        Quit()
    """Unused"""
    """State 9"""
    return 0

def t800036000_x101(z1=4740, flag1=1041362700, z2=1041369200):
    """State 0"""
    while True:
        """State 2"""
        # actionbutton:6000:"Talk"
        call = t800036000_x0(actionbutton1=6000, flag26=6001, flag30=6000, flag31=6000, flag32=6000,
                             flag33=6000, flag25=6000)
        if call.Done():
            break
        elif GetEventFlag(8 + flag1) == 1 and not GetEventFlag(9 + flag1):
            """State 1,3"""
            assert t800036000_x56(text2=95090000, val3=9, flag1=flag1, mode1=1)
    """State 4"""
    return 0

