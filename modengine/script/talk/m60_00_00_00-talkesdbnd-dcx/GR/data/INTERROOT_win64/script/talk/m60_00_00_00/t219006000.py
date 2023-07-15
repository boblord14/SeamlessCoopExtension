# -*- coding: utf-8 -*-
def t219006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t219006000_x14(flag1=3543, flag2=3541, flag3=3542, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1)
    Quit()

def t219006000_1000():
    """State 0,2,3"""
    assert t219006000_x0()
    """State 1"""
    c1_120(1000)
    Quit()

def t219006000_1001():
    """State 0,2,3"""
    assert t219006000_x1()
    """State 1"""
    c1_120(1001)
    Quit()

def t219006000_1101():
    """State 0,2,3"""
    assert t219006000_x2()
    """State 1"""
    c1_120(1101)
    Quit()

def t219006000_1102():
    """State 0,2,3"""
    t219006000_x3()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t219006000_1103():
    """State 0,2,3"""
    assert t219006000_x4()
    """State 1"""
    c1_120(1103)
    Quit()

def t219006000_2000():
    """State 0,2,3"""
    assert t219006000_x5(val6=10, z5=12, z6=1)
    """State 1"""
    c1_120(2000)
    Quit()

def t219006000_x0():
    """State 0,1"""
    if GetEventFlag(3545) == 1:
        """State 3"""
        assert t219006000_x6()
    else:
        """State 2"""
        pass
    """State 4"""
    return 0

def t219006000_x1():
    """State 0,1"""
    # talk:21980300:"I will never give this up."
    assert t219006000_x39(text1=21980300, mode3=1)
    """State 2"""
    return 0

def t219006000_x2():
    """State 0"""
    if not GetEventFlag(1035422701) and not GetEventFlag(1035429210):
        """State 2,1"""
        SetEventFlag(1035422701, 1)
        """State 4"""
        # talk:21980000:"Ngh!"
        assert t219006000_x39(text1=21980000, mode3=1)
    else:
        """State 3"""
        pass
    """State 5"""
    return 0

def t219006000_x3():
    """State 0,2"""
    if not GetEventFlag(1035429205) and not GetEventFlag(1035429210):
        """State 3,7"""
        SetEventFlag(1035429205, 1)
        """State 6"""
        SetEventFlag(1035422700, 1)
        """State 8"""
        # talk:21980100:"We are Albinaurics."
        assert t219006000_x39(text1=21980100, mode3=1)
    elif not GetEventFlag(1035422700):
        """State 4"""
        pass
    else:
        """State 5"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 9"""
    return 0

def t219006000_x4():
    """State 0,1"""
    if not GetEventFlag(1035429210):
        """State 2,5"""
        # talk:21980200:"You merciless brutes."
        assert t219006000_x39(text1=21980200, mode3=1)
    else:
        """State 3"""
        """State 4"""
        pass
    """State 6"""
    return 0

def t219006000_x5(val6=10, z5=12, z6=1):
    """State 0"""
    while True:
        """State 5"""
        # actionbutton:6000:"Talk"
        call = t219006000_x8(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                             flag4=6000)
        if call.Done():
            break
        elif GetEventFlag(1035420701) == 1 and not GetEventFlag(1035429206) and GetDistanceToPlayer() < val6:
            """State 1,2"""
            SetEventFlag(1035429206, 1)
            """State 6"""
            # talk:21900100:"Ah!"
            assert t219006000_x39(text1=21900100, mode3=1) and CheckSpecificPersonTalkHasEnded(0) == 1
        elif GetEventFlag(1035429210) == 1:
            """State 3,4"""
            Quit()
    """State 7"""
    return 0

def t219006000_x6():
    """State 0,1"""
    if not GetEventFlag(1035429209):
        """State 2,4"""
        SetEventFlag(1035429207, 1)
        """State 8"""
        def WhilePaused():
            RequestAnimation(20040, -1)
        assert t219006000_x7()
    elif not GetEventFlag(1035429212):
        """State 3,9"""
        # talk:21900300:"A chosen land awaits us Albinaurics."
        def WhilePaused():
            RequestAnimation(20040, -1)
        assert t219006000_x38(text2=21900300, mode4=1)
        """State 5"""
        SetEventFlag(1035429212, 1)
    else:
        """State 6,10"""
        # talk:21900400:"My legs will soon fade, and with them, my life."
        def WhilePaused():
            RequestAnimation(20040, -1)
        assert t219006000_x38(text2=21900400, mode4=1)
        """State 7"""
        SetEventFlag(1035429210, 1)
    """State 11"""
    return 0

def t219006000_x7():
    """State 0,4"""
    # talk:21900200:"Wait, then, you're not one of them?"
    assert t219006000_x38(text2=21900200, mode4=1)
    """State 1"""
    SetEventFlag(1035429209, 1)
    """State 2"""
    # lot:101300:Haligtree Secret Medallion (Right)
    assert t219006000_x11(lot1=101300)
    """State 3"""
    # talk:21900210:"And if you should meet the young Albinauric Latenna,"
    assert t219006000_x38(text2=21900210, mode4=1)
    """State 5"""
    return 0

def t219006000_x8(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t219006000_x9():
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

def t219006000_x10():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t219006000_x11(lot1=101300):
    """State 0,1"""
    # lot:101300:Haligtree Secret Medallion (Right)
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t219006000_x12(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t219006000_x28()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t219006000_x9()
    else:
        """State 4,7"""
        call = t219006000_x41()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t219006000_x9()
    """State 9"""
    return 0

def t219006000_x13():
    """State 0,1"""
    assert t219006000_x9()
    """State 2"""
    return 0

def t219006000_x14(flag1=3543, flag2=3541, flag3=3542, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t219006000_x31(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t219006000_x30()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t219006000_x15(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                   flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                   mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t219006000_x18(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t219006000_x22(val1=val1, z1=z1)
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
            call = t219006000_x24(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t219006000_x35() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t219006000_x20(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t219006000_x16(val2=10, val3=12):
    """State 0,1"""
    call = t219006000_x26(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t219006000_x12(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t219006000_x17(flag1=3543, val2=10, val3=12):
    """State 0,8"""
    assert t219006000_x43()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t219006000_x29()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t219006000_x9()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t219006000_x18(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t219006000_x19(z7=2000, val7=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t219006000_x8(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t219006000_x19(z7=_, val7=_):
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

def t219006000_x20(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t219006000_x9()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t219006000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t219006000_x36()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t219006000_x21():
    """State 0,1"""
    assert t219006000_x19(z7=1101, val7=1101)
    """State 2"""
    return 0

def t219006000_x22(val1=5, z1=1):
    """State 0,2"""
    assert t219006000_x32()
    """State 1"""
    call = t219006000_x23()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t219006000_x34()
    """State 4"""
    return 0

def t219006000_x23():
    """State 0,1"""
    assert t219006000_x19(z7=1000, val7=1000)
    """State 2"""
    return 0

def t219006000_x24(val5=12):
    """State 0,1"""
    call = t219006000_x25()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t219006000_x35()
    """State 3"""
    return 0

def t219006000_x25():
    """State 0,1"""
    assert t219006000_x19(z7=1100, val7=1100)
    """State 2"""
    return 0

def t219006000_x26(val2=10, val3=12):
    """State 0,5"""
    assert t219006000_x43()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t219006000_x27()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t219006000_x37()
    """Unused"""
    """State 6"""
    return 0

def t219006000_x27():
    """State 0,2"""
    call = t219006000_x19(z7=1102, val7=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t219006000_x28():
    """State 0,1"""
    assert t219006000_x19(z7=1001, val7=1001)
    """State 2"""
    return 0

def t219006000_x29():
    """State 0,1"""
    assert t219006000_x19(z7=1103, val7=1103)
    """State 2"""
    return 0

def t219006000_x30():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t219006000_x31(flag1=3543, flag2=3541, flag3=3542, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t219006000_x15(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                              flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                              z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t219006000_x17(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t219006000_x16(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t219006000_x42() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t219006000_x32():
    """State 0,1"""
    assert t219006000_x33()
    """State 2"""
    return 0

def t219006000_x33():
    """State 0,1"""
    assert t219006000_x19(z7=1104, val7=1104)
    """State 2"""
    return 0

def t219006000_x34():
    """State 0,1"""
    call = t219006000_x19(z7=1201, val7=1201)
    if call.Get() == 1:
        """State 2"""
        assert t219006000_x13()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t219006000_x35():
    """State 0,1"""
    call = t219006000_x19(z7=1300, val7=1300)
    if call.Get() == 1:
        """State 2"""
        assert t219006000_x13()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t219006000_x36():
    """State 0,1"""
    call = t219006000_x19(z7=1301, val7=1301)
    if call.Get() == 1:
        """State 2"""
        assert t219006000_x13()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t219006000_x37():
    """State 0,1"""
    call = t219006000_x19(z7=1302, val7=1302)
    if call.Get() == 1:
        """State 2"""
        assert t219006000_x13()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t219006000_x38(text2=_, mode4=1):
    """State 0,4"""
    assert t219006000_x10() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t219006000_x39(text1=_, mode3=1):
    """State 0,4"""
    assert t219006000_x40() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t219006000_x40():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t219006000_x41():
    """State 0,1"""
    assert t219006000_x19(z7=1002, val7=1002)
    """State 2"""
    return 0

def t219006000_x42():
    """State 0,1"""
    assert t219006000_x9()
    """State 2"""
    return 0

def t219006000_x43():
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

