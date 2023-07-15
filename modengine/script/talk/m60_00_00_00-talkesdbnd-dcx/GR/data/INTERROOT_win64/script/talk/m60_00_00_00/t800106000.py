# -*- coding: utf-8 -*-
def t800106000_1():
    """State 0"""
    while True:
        """State 2"""
        # actionbutton:6000:"Talk"
        call = t800106000_x5(flag31=4743, flag32=4741, flag33=4742, val2=5, val3=10, val4=12, val5=10,
                             val6=12, actionbutton1=6000, flag34=6000, flag35=6001, flag36=6000, flag37=6000,
                             flag38=6000, z9=1, z10=1000000, z11=1000000, z12=1000000, mode1=1, mode2=1)
        assert not GetEventFlag(4745)
        """State 1"""
        assert GetEventFlag(4745) == 1

def t800106000_1000():
    """State 0,2,3"""
    assert (t800106000_x38(val1=802, flag1=1050309251, flag2=1050309252, z1=1050309254, flag3=1050309255,
            z2=1050309256, flag4=1050309290, shop1=600501, shop2=600550, z3=1050309297, z4=1050302710,
            z5=1050309298, flag5=1050309294, flag6=1050309295, flag7=1050302715, flag8=1050302716, flag9=1050309260,
            flag10=1050309261, z6=1050309265, flag11=1050309266, flag12=1050302718, flag13=1050309270,
            flag14=1050309271, flag15=1050309272, flag16=1050309275, flag17=1050309276, flag18=1050309277,
            flag19=1050302719, flag20=1042399243, flag21=1050302717))
    """State 1"""
    c1_120(1000)
    Quit()

def t800106000_1001():
    """State 0,2,3"""
    assert t800106000_x39()
    """State 1"""
    c1_120(1001)
    Quit()

def t800106000_1101():
    """State 0,2,3"""
    assert t800106000_x40(flag30=1050309291, z7=4741, z8=1050309297)
    """State 1"""
    c1_120(1101)
    Quit()

def t800106000_1102():
    """State 0,2,3"""
    t800106000_x41(flag27=1050302710, flag28=1050309298, flag29=1050309297)
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t800106000_1103():
    """State 0,2,3"""
    assert t800106000_x42()
    """State 1"""
    c1_120(1103)
    Quit()

def t800106000_x0(actionbutton1=6000, flag35=6001, flag39=6000, flag40=6000, flag41=6000, flag42=6000,
                  flag34=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag35) == 1 or GetEventFlag(flag39) == 1 or GetEventFlag(flag40) == 1 or
                GetEventFlag(flag41) == 1 or GetEventFlag(flag42) == 1)
        """State 4"""
        assert not GetEventFlag(flag34)
        """State 2"""
        if GetEventFlag(flag34) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag35) and not GetEventFlag(flag39) and not GetEventFlag(flag40) and
              not GetEventFlag(flag41) and not GetEventFlag(flag42)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t800106000_x1():
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

def t800106000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t800106000_x3(val3=10, val4=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val3 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t800106000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val4 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t800106000_x1()
    else:
        """State 4,7"""
        call = t800106000_x35()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val4 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t800106000_x1()
    """State 9"""
    return 0

def t800106000_x4():
    """State 0,1"""
    assert t800106000_x1()
    """State 2"""
    return 0

def t800106000_x5(flag31=4743, flag32=4741, flag33=4742, val2=5, val3=10, val4=12, val5=10, val6=12,
                  actionbutton1=6000, flag34=6000, flag35=6001, flag36=6000, flag37=6000, flag38=6000,
                  z9=1, z10=1000000, z11=1000000, z12=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t800106000_x22(flag31=flag31, flag32=flag32, flag33=flag33, val2=val2, val3=val3, val4=val4,
                              val5=val5, val6=val6, actionbutton1=actionbutton1, flag34=flag34, flag35=flag35,
                              flag36=flag36, flag37=flag37, flag38=flag38, z9=z9, z10=z10, z11=z11, z12=z12,
                              mode1=mode1, mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t800106000_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t800106000_x6(val2=5, val3=10, val4=12, val5=10, val6=12, actionbutton1=6000, flag34=6000, flag35=6001,
                  flag36=6000, flag37=6000, flag38=6000, z9=1, z10=1000000, z11=1000000, z12=1000000,
                  mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t800106000_x9(actionbutton1=actionbutton1, flag34=flag34, flag35=flag35, z10=z10, z11=z11,
                             z12=z12)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t800106000_x13(val2=val2, z9=z9)
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
        elif GetEventFlag(flag38) == 1:
            Goto('L0')
        elif GetEventFlag(flag36) == 1 and not GetEventFlag(flag37) and GetDistanceToPlayer() < val5:
            """State 5"""
            call = t800106000_x15(val6=val6)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val6 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t800106000_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t800106000_x11(val3=val3, val4=val4)
    """Unused"""
    """State 7"""
    return 0

def t800106000_x7(val3=10, val4=12):
    """State 0,1"""
    call = t800106000_x17(val3=val3, val4=val4)
    assert IsPlayerDead() == 1
    """State 2"""
    t800106000_x3(val3=val3, val4=val4)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t800106000_x8(flag31=4743, val3=10, val4=12):
    """State 0,8"""
    assert t800106000_x37()
    """State 1"""
    if GetEventFlag(flag31) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val3:
            """State 4,6"""
            call = t800106000_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val4 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t800106000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t800106000_x9(actionbutton1=6000, flag34=6000, flag35=6001, z10=1000000, z11=1000000, z12=1000000):
    """State 0,1"""
    call = t800106000_x10(z13=2000, val7=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t800106000_x0(actionbutton1=actionbutton1, flag35=flag35, flag39=6000, flag40=6000, flag41=6000,
                flag42=6000, flag34=flag34))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800106000_x10(z13=_, val7=_):
    """State 0,1"""
    if f203(z13) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z13)
        assert f202() == val7
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t800106000_x11(val3=10, val4=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t800106000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val3:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t800106000_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val4 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t800106000_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t800106000_x12():
    """State 0,1"""
    assert t800106000_x10(z13=1101, val7=1101)
    """State 2"""
    return 0

def t800106000_x13(val2=5, z9=1):
    """State 0,2"""
    assert t800106000_x23()
    """State 1"""
    call = t800106000_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val2 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t800106000_x25()
    """State 4"""
    return 0

def t800106000_x14():
    """State 0,1"""
    assert t800106000_x10(z13=1000, val7=1000)
    """State 2"""
    return 0

def t800106000_x15(val6=12):
    """State 0,1"""
    call = t800106000_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val6 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t800106000_x26()
    """State 3"""
    return 0

def t800106000_x16():
    """State 0,1"""
    assert t800106000_x10(z13=1100, val7=1100)
    """State 2"""
    return 0

def t800106000_x17(val3=10, val4=12):
    """State 0,5"""
    assert t800106000_x37()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val3
        """State 3"""
        call = t800106000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val4 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t800106000_x28()
    """Unused"""
    """State 6"""
    return 0

def t800106000_x18():
    """State 0,2"""
    call = t800106000_x10(z13=1102, val7=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t800106000_x19():
    """State 0,1"""
    assert t800106000_x10(z13=1001, val7=1001)
    """State 2"""
    return 0

def t800106000_x20():
    """State 0,1"""
    assert t800106000_x10(z13=1103, val7=1103)
    """State 2"""
    return 0

def t800106000_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t800106000_x22(flag31=4743, flag32=4741, flag33=4742, val2=5, val3=10, val4=12, val5=10, val6=12,
                   actionbutton1=6000, flag34=6000, flag35=6001, flag36=6000, flag37=6000, flag38=6000,
                   z9=1, z10=1000000, z11=1000000, z12=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t800106000_x6(val2=val2, val3=val3, val4=val4, val5=val5, val6=val6, actionbutton1=actionbutton1,
                             flag34=flag34, flag35=flag35, flag36=flag36, flag37=flag37, flag38=flag38,
                             z9=z9, z10=z10, z11=z11, z12=z12, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag31) == 1:
            """State 3"""
            Label('L0')
            call = t800106000_x8(flag31=flag31, val3=val3, val4=val4)
            if not CheckSelfDeath() and not GetEventFlag(flag31):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag32) == 1 or GetEventFlag(flag33) == 1:
            """State 2"""
            call = t800106000_x7(val3=val3, val4=val4)
            if CheckSelfDeath() == 1 or GetEventFlag(flag31) == 1:
                Goto('L0')
            elif not GetEventFlag(flag32) and not GetEventFlag(flag33):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t800106000_x36() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t800106000_x23():
    """State 0,1"""
    assert t800106000_x24()
    """State 2"""
    return 0

def t800106000_x24():
    """State 0,1"""
    assert t800106000_x10(z13=1104, val7=1104)
    """State 2"""
    return 0

def t800106000_x25():
    """State 0,1"""
    call = t800106000_x10(z13=1201, val7=1201)
    if call.Get() == 1:
        """State 2"""
        assert t800106000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800106000_x26():
    """State 0,1"""
    call = t800106000_x10(z13=1300, val7=1300)
    if call.Get() == 1:
        """State 2"""
        assert t800106000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800106000_x27():
    """State 0,1"""
    call = t800106000_x10(z13=1301, val7=1301)
    if call.Get() == 1:
        """State 2"""
        assert t800106000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800106000_x28():
    """State 0,1"""
    call = t800106000_x10(z13=1302, val7=1302)
    if call.Get() == 1:
        """State 2"""
        assert t800106000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800106000_x29(text5=_, flag16=_, mode7=1):
    """State 0,5"""
    assert t800106000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(flag16, 1)
    """State 1"""
    TalkToPlayer(text5, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode7:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t800106000_x30(text4=80003300, z4=1050302710, mode6=1):
    """State 0,5"""
    assert t800106000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    # talk:80003300:"My thanks. I've been wanting to get my hands on this."
    TalkToPlayer(text4, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode6:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(z4, 1)
    """State 6"""
    return 0

def t800106000_x31(text3=_, mode5=1):
    """State 0,4"""
    assert t800106000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t800106000_x32(text2=_, flag27=_, mode4=1):
    """State 0,5"""
    assert t800106000_x34() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(flag27, 1)
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

def t800106000_x33(text1=_, mode3=1):
    """State 0,4"""
    assert t800106000_x34() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t800106000_x34():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t800106000_x35():
    """State 0,1"""
    assert t800106000_x10(z13=1002, val7=1002)
    """State 2"""
    return 0

def t800106000_x36():
    """State 0,1"""
    assert t800106000_x1()
    """State 2"""
    return 0

def t800106000_x37():
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

def t800106000_x38(val1=802, flag1=1050309251, flag2=1050309252, z1=1050309254, flag3=1050309255, z2=1050309256,
                   flag4=1050309290, shop1=600501, shop2=600550, z3=1050309297, z4=1050302710, z5=1050309298,
                   flag5=1050309294, flag6=1050309295, flag7=1050302715, flag8=1050302716, flag9=1050309260,
                   flag10=1050309261, z6=1050309265, flag11=1050309266, flag12=1050302718, flag13=1050309270,
                   flag14=1050309271, flag15=1050309272, flag16=1050309275, flag17=1050309276, flag18=1050309277,
                   flag19=1050302719, flag20=1042399243, flag21=1050302717):
    """State 0,1"""
    if not GetEventFlag(4980):
        """State 8"""
        if not GetEventFlag(4981) and not GetEventFlag(4982):
            """State 2"""
            if not GetEventFlag(flag1) or GetEventFlag(flag7) == 1:
                """State 3"""
                SetEventFlag(flag7, 1)
                """State 13"""
                assert t800106000_x43(flag1=flag1, flag2=flag2, z1=z1, flag4=flag4)
            else:
                """State 6"""
                SetEventFlag(flag5, 1)
                """State 5"""
                if not GetEventFlag(flag9) or GetEventFlag(flag8) == 1:
                    """State 4"""
                    SetEventFlag(flag8, 1)
                    """State 15"""
                    assert t800106000_x49(flag9=flag9, flag10=flag10, z1=z1, flag4=flag4)
                else:
                    """State 7"""
                    SetEventFlag(flag6, 1)
                    """State 10"""
                    if not GetEventFlag(flag20) and val1 == 800:
                        """State 17"""
                        assert t800106000_x57(flag20=flag20)
                    else:
                        """State 14"""
                        assert t800106000_x50(z6=z6, flag11=flag11, z1=z1, flag4=flag4, flag21=flag21)
        else:
            """State 16"""
            assert (t800106000_x55(flag12=flag12, flag13=flag13, flag14=flag14, flag15=flag15, flag16=flag16,
                    flag17=flag17, flag18=flag18, flag19=flag19, flag1=flag1, flag9=flag9, flag22=6000,
                    flag23=6000, flag24=6000, flag25=flag1, flag26=flag9))
            """State 9"""
            if not GetEventFlag(4982):
                pass
            else:
                Goto('L0')
        """State 11"""
        assert (t800106000_x44(val1=val1, flag3=flag3, z2=z2, shop1=shop1, shop2=shop2, flag5=flag5,
                flag6=flag6))
    else:
        """State 12"""
        def ExitPause():
            SetEventFlag(z3, 1)
            SetEventFlag(z4, 1)
            SetEventFlag(z5, 1)
        assert t800106000_x47(z3=z3, z4=z4, z5=z5)
    """State 18"""
    Label('L0')
    return 0

def t800106000_x39():
    """State 0,1"""
    assert t800106000_x33(text1=80003700, mode3=1)
    """State 2"""
    return 0

def t800106000_x40(flag30=1050309291, z7=4741, z8=1050309297):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        """State 4"""
        if not GetEventFlag(4980):
            """State 2"""
            if not GetEventFlag(flag30):
                """State 3"""
                SetEventFlag(flag30, 1)
                """State 7"""
                call = t800106000_x33(text1=80090000, mode3=1)
                if call.Done():
                    break
                elif GetCurrentStateElapsedFrames() > 1 and IsPlayerAttacking() == 1:
                    pass
            else:
                """State 6"""
                call = t800106000_x33(text1=80003420, mode3=1)
                if call.Done():
                    break
                elif GetCurrentStateElapsedFrames() > 1 and IsPlayerAttacking() == 1:
                    pass
        else:
            """State 5"""
            SetEventFlag(z8, 1)
            break
    """State 8"""
    return 0

def t800106000_x41(flag27=1050302710, flag28=1050309298, flag29=1050309297):
    """State 0,1"""
    SetEventFlag(4980, 1)
    t800106000_x48(flag27=flag27, flag28=flag28, flag29=flag29)
    def WhilePaused():
        c1_121(11020)
    Quit()
    """Unused"""
    """State 2"""
    return 0

def t800106000_x42():
    """State 0,1"""
    # talk:80003500:"Once I decipher that cryptogram, I'll be packing up shop again."
    assert t800106000_x33(text1=80003500, mode3=1)
    """State 2"""
    return 0

def t800106000_x43(flag1=1050309251, flag2=1050309252, z1=1050309254, flag4=1050309290):
    """State 0,1"""
    if not GetEventFlag(flag1):
        """State 3"""
        if not GetEventFlag(4985):
            """State 6,2"""
            SetEventFlag(4985, 1)
            """State 11"""
            # talk:80000100:"You're a Tarnished, I can see it."
            assert t800106000_x29(text5=80000100, flag16=flag1, mode7=1)
        else:
            """State 7,8"""
            # talk:80000200:"What is it? Still going to purchase something?"
            assert t800106000_x29(text5=80000200, flag16=flag1, mode7=1)
    elif GetEventFlag(flag4) == 1 and not GetEventFlag(flag2):
        """State 4,9"""
        # talk:80000800:"You know, if you can spare the runes,"
        assert t800106000_x29(text5=80000800, flag16=z1, mode7=1)
    else:
        """State 5,10"""
        # talk:80000300:"Wait, weren't you...?"
        assert t800106000_x29(text5=80000300, flag16=flag2, mode7=1)
    """State 12"""
    return 0

def t800106000_x44(val1=802, flag3=1050309255, z2=1050309256, shop1=600501, shop2=600550, flag5=1050309294,
                   flag6=1050309295):
    """State 0,7"""
    c1_110()
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
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 6"""
            OpenRegularShop(shop1, shop2)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 5"""
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 9"""
            assert t800106000_x46(val1=val1, flag3=flag3, z2=z2)
        else:
            """State 8"""
            assert t800106000_x51(flag5=flag5, flag6=flag6)
            """State 10"""
            return 0

def t800106000_x45(flag3=1050309255, z2=1050309256):
    """State 0,1"""
    if not GetEventFlag(flag3):
        """State 3,5"""
        assert t800106000_x29(text5=80006000, flag16=flag3, mode7=1)
    else:
        """State 4,6"""
        assert t800106000_x29(text5=80006100, flag16=z2, mode7=1)
        """State 2"""
        SetEventFlag(flag3, 0)
        SetEventFlag(z2, 0)
    """State 7"""
    return 0

def t800106000_x46(val1=802, flag3=1050309255, z2=1050309256):
    """State 0,6"""
    if not GetEventFlag(4981) and not GetEventFlag(4982):
        """State 1"""
        if val1 == 800:
            """State 2,7"""
            assert t800106000_x45(flag3=flag3, z2=z2)
        elif val1 == 801:
            """State 3,8"""
            assert t800106000_x52(flag3=flag3, z2=z2)
        elif val1 == 802:
            """State 4,9"""
            assert t800106000_x53(flag3=flag3, z2=z2)
        else:
            """State 5"""
            pass
    else:
        """State 10"""
        assert t800106000_x31(text3=80006500, mode5=1)
    """State 11"""
    return 0

def t800106000_x47(z3=1050309297, z4=1050302710, z5=1050309298):
    """State 0,2"""
    # talk:80003300:"My thanks. I've been wanting to get my hands on this."
    assert t800106000_x30(text4=80003300, z4=z4, mode6=1)
    """State 3"""
    assert t800106000_x32(text2=80003310, flag27=z3, mode4=1) and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    return 0
    """Unused"""
    """State 1"""
    SetEventFlag(z5, 1)
    Quit()

def t800106000_x48(flag27=1050302710, flag28=1050309298, flag29=1050309297):
    """State 0,2"""
    if not GetEventFlag(flag27):
        """State 3"""
        if not GetEventFlag(flag28):
            """State 4"""
            SetEventFlag(flag28, 1)
            """State 5"""
            if not GetEventFlag(flag29):
                """State 7"""
                assert t800106000_x32(text2=80090100, flag27=flag27, mode4=1)
            else:
                """State 9"""
                assert t800106000_x32(text2=80090100, flag27=flag27, mode4=1)
        else:
            """State 6,8"""
            assert t800106000_x32(text2=80090300, flag27=flag27, mode4=1)
    else:
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 10"""
    return 0

def t800106000_x49(flag9=1050309260, flag10=1050309261, z1=1050309254, flag4=1050309290):
    """State 0,1"""
    if not GetEventFlag(flag9):
        """State 4,7"""
        assert t800106000_x29(text5=80002000, flag16=flag9, mode7=1)
    elif GetEventFlag(flag4) == 1 and not GetEventFlag(flag10):
        """State 2,5"""
        # talk:80000800:"You know, if you can spare the runes,"
        assert t800106000_x29(text5=80000800, flag16=z1, mode7=1)
    else:
        """State 3,6"""
        assert t800106000_x29(text5=80002200, flag16=flag10, mode7=1)
    """State 8"""
    return 0

def t800106000_x50(z6=1050309265, flag11=1050309266, z1=1050309254, flag4=1050309290, flag21=1050302717):
    """State 0,1"""
    if not GetEventFlag(flag21):
        """State 2,7"""
        assert t800106000_x29(text5=80004000, flag16=flag21, mode7=1)
    elif GetEventFlag(flag4) == 1 and not GetEventFlag(flag11):
        """State 3,5"""
        # talk:80000800:"You know, if you can spare the runes,"
        assert t800106000_x29(text5=80000800, flag16=z1, mode7=1)
    else:
        """State 4,6"""
        assert t800106000_x29(text5=80004200, flag16=flag11, mode7=1)
    """State 8"""
    return 0

def t800106000_x51(flag5=1050309294, flag6=1050309295):
    """State 0,3"""
    if not GetEventFlag(4981):
        """State 2"""
        if not GetEventFlag(flag5):
            """State 1"""
            if not DidYouDoSomethingInTheMenu(0):
                """State 5"""
                # talk:80000400:"Ah, it's you again."
                assert t800106000_x31(text3=80000400, mode5=1)
            else:
                """State 6"""
                # talk:80000500:"Good-bye for now."
                assert t800106000_x31(text3=80000500, mode5=1)
        elif not GetEventFlag(flag6):
            """State 4"""
            if not DidYouDoSomethingInTheMenu(0):
                """State 7"""
                assert t800106000_x31(text3=80002400, mode5=1)
            else:
                """State 8"""
                assert t800106000_x31(text3=80002500, mode5=1)
        else:
            """State 9"""
            assert t800106000_x31(text3=80004400, mode5=1)
    else:
        """State 10"""
        assert t800106000_x31(text3=80010600, mode5=1)
    """State 11"""
    return 0

def t800106000_x52(flag3=1050309255, z2=1050309256):
    """State 0,1"""
    if not GetEventFlag(flag3):
        """State 3,5"""
        assert t800106000_x29(text5=80106000, flag16=flag3, mode7=1)
    else:
        """State 4,6"""
        assert t800106000_x29(text5=80106100, flag16=z2, mode7=1)
        """State 2"""
        SetEventFlag(flag3, 0)
        SetEventFlag(z2, 0)
    """State 7"""
    return 0

def t800106000_x53(flag3=1050309255, z2=1050309256):
    """State 0,1"""
    if not GetEventFlag(flag3):
        """State 3,5"""
        assert t800106000_x29(text5=80206000, flag16=flag3, mode7=1)
    else:
        """State 4,6"""
        assert t800106000_x29(text5=80206100, flag16=z2, mode7=1)
        """State 2"""
        SetEventFlag(flag3, 0)
        SetEventFlag(z2, 0)
    """State 7"""
    return 0

def t800106000_x54(flag12=1050302718, flag13=1050309270, flag14=1050309271, flag15=1050309272, flag1=1050309251,
                   flag9=1050309260, flag19=1050302719, flag22=6000, flag23=6000):
    """State 0,5"""
    if ((not GetEventFlag(flag13) and not GetEventFlag(flag14) and not GetEventFlag(flag15)) or GetEventFlag(flag12)
        == 1):
        """State 11"""
        SetEventFlag(flag12, 1)
        """State 1"""
        if not GetEventFlag(flag1):
            """State 2"""
            if not GetEventFlag(flag13):
                """State 12"""
                assert t800106000_x29(text5=80010000, flag16=flag13, mode7=1)
            else:
                """State 13"""
                assert t800106000_x31(text3=80010500, mode5=1)
        elif not GetEventFlag(flag9):
            """State 3"""
            if not GetEventFlag(flag14):
                """State 14"""
                assert t800106000_x29(text5=80010100, flag16=flag14, mode7=1)
            else:
                """State 15"""
                assert t800106000_x31(text3=80010500, mode5=1)
        else:
            """State 4"""
            if not GetEventFlag(flag15):
                """State 16"""
                assert t800106000_x29(text5=80010200, flag16=flag15, mode7=1)
            else:
                """State 17"""
                assert t800106000_x31(text3=80010500, mode5=1)
    elif not GetEventFlag(flag22) or GetEventFlag(flag19) == 1:
        """State 6,9"""
        SetEventFlag(flag19, 1)
        """State 8"""
        if not GetEventFlag(flag22):
            """State 18"""
            assert t800106000_x29(text5=80010300, flag16=flag22, mode7=1)
        else:
            """State 19"""
            assert t800106000_x31(text3=80010500, mode5=1)
    else:
        """State 7,10"""
        if not GetEventFlag(flag23):
            """State 20"""
            assert t800106000_x29(text5=80010400, flag16=flag23, mode7=1)
        else:
            """State 21"""
            assert t800106000_x31(text3=80010500, mode5=1)
    """State 22"""
    return 0

def t800106000_x55(flag12=1050302718, flag13=1050309270, flag14=1050309271, flag15=1050309272, flag16=1050309275,
                   flag17=1050309276, flag18=1050309277, flag19=1050302719, flag1=1050309251, flag9=1050309260,
                   flag22=6000, flag23=6000, flag24=6000, flag25=1050309251, flag26=1050309260):
    """State 0,1"""
    if GetEventFlag(4981) == 1 and not GetEventFlag(4982):
        """State 2,4"""
        assert (t800106000_x54(flag12=flag12, flag13=flag13, flag14=flag14, flag15=flag15, flag1=flag1,
                flag9=flag9, flag19=flag19, flag22=flag22, flag23=flag23))
    else:
        """State 3"""
        assert (t800106000_x56(flag24=flag24, flag16=flag16, flag17=flag17, flag18=flag18, flag1=flag25,
                flag9=flag26))
    """State 5"""
    return 0

def t800106000_x56(flag24=6000, flag16=1050309275, flag17=1050309276, flag18=1050309277, flag1=1050309251,
                   flag9=1050309260):
    """State 0,5"""
    if ((not GetEventFlag(flag16) and not GetEventFlag(flag17) and not GetEventFlag(flag18)) or GetEventFlag(flag24)
        == 1):
        """State 6"""
        SetEventFlag(flag24, 1)
        """State 1"""
        if not GetEventFlag(flag1):
            """State 2"""
            if not GetEventFlag(flag16):
                """State 8"""
                assert t800106000_x29(text5=80010700, flag16=flag16, mode7=1)
            else:
                """State 9"""
                assert t800106000_x31(text3=80011000, mode5=1)
        elif not GetEventFlag(flag1):
            """State 3"""
            if not GetEventFlag(flag17):
                """State 10"""
                assert t800106000_x29(text5=80010800, flag16=flag17, mode7=1)
            else:
                """State 11"""
                assert t800106000_x31(text3=80011000, mode5=1)
        else:
            """State 4"""
            if not GetEventFlag(flag18):
                """State 12"""
                assert t800106000_x29(text5=80010900, flag16=flag18, mode7=1)
            else:
                """State 13"""
                assert t800106000_x31(text3=80011000, mode5=1)
    else:
        """State 7,14"""
        assert t800106000_x31(text3=80011000, mode5=1)
    """State 15"""
    return 0

def t800106000_x57(flag20=1042399243):
    """State 0,2"""
    assert t800106000_x31(text3=80008000, mode5=1)
    """State 1"""
    AwardItemLot(60400)
    SetEventFlag(flag20, 1)
    assert not IsMenuOpen(63)
    """State 3"""
    assert t800106000_x31(text3=80008100, mode5=1)
    """State 4"""
    return 0

