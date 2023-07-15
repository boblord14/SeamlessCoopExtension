# -*- coding: utf-8 -*-
def t321006000_1():
    """State 0,1"""
    SetUpdateDistance(100)
    """State 2"""
    # actionbutton:6000:"Talk"
    t321006000_x6(flag1=3583, flag2=3581, flag3=3582, val1=5, val2=10, val3=12, val4=75, val5=75, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t321006000_1000():
    """State 0,2,3"""
    assert t321006000_x38()
    """State 1"""
    c1_120(1000)
    Quit()

def t321006000_1001():
    """State 0,2,3"""
    assert t321006000_x39()
    """State 1"""
    c1_120(1001)
    Quit()

def t321006000_1101():
    """State 0,2,3"""
    assert t321006000_x40()
    """State 1"""
    c1_120(1101)
    Quit()

def t321006000_1102():
    """State 0,2,3"""
    t321006000_x41()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t321006000_1103():
    """State 0,2,3"""
    assert t321006000_x42()
    """State 1"""
    c1_120(1103)
    Quit()

def t321006000_2000():
    """State 0,2,3"""
    assert t321006000_x43()
    """State 1"""
    c1_120(2000)
    Quit()

def t321006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t321006000_x1():
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

def t321006000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t321006000_x3(lot1=102200):
    """State 0,1"""
    # lot:102200:Erdsteel Dagger
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t321006000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t321006000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t321006000_x1()
    else:
        """State 4,7"""
        call = t321006000_x35()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t321006000_x1()
    """State 9"""
    return 0

def t321006000_x5():
    """State 0,1"""
    assert t321006000_x1()
    """State 2"""
    return 0

def t321006000_x6(flag1=3583, flag2=3581, flag3=3582, val1=5, val2=10, val3=12, val4=75, val5=75, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t321006000_x23(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t321006000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t321006000_x7(val1=5, val2=10, val3=12, val4=75, val5=75, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t321006000_x10(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t321006000_x14(val1=val1, z1=z1)
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
            call = t321006000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t321006000_x27() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t321006000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t321006000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t321006000_x18(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t321006000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t321006000_x9(flag1=3583, val2=10, val3=12):
    """State 0,8"""
    assert t321006000_x37()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t321006000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t321006000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t321006000_x10(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t321006000_x11(z7=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t321006000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t321006000_x11(z7=_, val6=_):
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

def t321006000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t321006000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t321006000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t321006000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t321006000_x13():
    """State 0,1"""
    assert t321006000_x11(z7=1101, val6=1101)
    """State 2"""
    return 0

def t321006000_x14(val1=5, z1=1):
    """State 0,2"""
    assert t321006000_x24()
    """State 1"""
    call = t321006000_x15()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t321006000_x26()
    """State 4"""
    return 0

def t321006000_x15():
    """State 0,1"""
    assert t321006000_x11(z7=1000, val6=1000)
    """State 2"""
    return 0

def t321006000_x16(val5=75):
    """State 0,1"""
    call = t321006000_x17()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t321006000_x27()
    """State 3"""
    return 0

def t321006000_x17():
    """State 0,1"""
    assert t321006000_x11(z7=1100, val6=1100)
    """State 2"""
    return 0

def t321006000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t321006000_x37()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t321006000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t321006000_x29()
    """Unused"""
    """State 6"""
    return 0

def t321006000_x19():
    """State 0,2"""
    call = t321006000_x11(z7=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t321006000_x20():
    """State 0,1"""
    assert t321006000_x11(z7=1001, val6=1001)
    """State 2"""
    return 0

def t321006000_x21():
    """State 0,1"""
    assert t321006000_x11(z7=1103, val6=1103)
    """State 2"""
    return 0

def t321006000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t321006000_x23(flag1=3583, flag2=3581, flag3=3582, val1=5, val2=10, val3=12, val4=75, val5=75, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t321006000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t321006000_x9(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t321006000_x8(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t321006000_x36() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t321006000_x24():
    """State 0,1"""
    assert t321006000_x25()
    """State 2"""
    return 0

def t321006000_x25():
    """State 0,1"""
    assert t321006000_x11(z7=1104, val6=1104)
    """State 2"""
    return 0

def t321006000_x26():
    """State 0,1"""
    call = t321006000_x11(z7=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t321006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t321006000_x27():
    """State 0,1"""
    call = t321006000_x11(z7=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t321006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t321006000_x28():
    """State 0,1"""
    call = t321006000_x11(z7=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t321006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t321006000_x29():
    """State 0,1"""
    call = t321006000_x11(z7=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t321006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t321006000_x30(text4=_, z6=_, mode6=1):
    """State 0,5"""
    assert t321006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t321006000_x31(text3=_, mode5=1):
    """State 0,4"""
    assert t321006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t321006000_x32(text2=_, z5=_, mode4=1):
    """State 0,5"""
    assert t321006000_x34() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t321006000_x33(text1=_, mode3=1):
    """State 0,4"""
    assert t321006000_x34() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t321006000_x34():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t321006000_x35():
    """State 0,1"""
    assert t321006000_x11(z7=1002, val6=1002)
    """State 2"""
    return 0

def t321006000_x36():
    """State 0,1"""
    assert t321006000_x1()
    """State 2"""
    return 0

def t321006000_x37():
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

def t321006000_x38():
    """State 0,1"""
    if GetEventFlag(3585) == 1:
        """State 3"""
        assert t321006000_x44()
    elif GetEventFlag(3586) == 1:
        """State 4"""
        assert t321006000_x48()
    elif GetEventFlag(3587) == 1:
        """State 5"""
        assert t321006000_x51()
    else:
        """State 2"""
        pass
    """State 6"""
    return 0

def t321006000_x39():
    """State 0,1"""
    # talk:32180300:"I fear for the integrity of the Order..."
    assert t321006000_x33(text1=32180300, mode3=1)
    """State 2"""
    return 0

def t321006000_x40():
    """State 0,3"""
    if not GetEventFlag(1045382701):
        """State 1,4"""
        # talk:32180000:"Oof!"
        assert t321006000_x32(text2=32180000, z5=1045382701, mode4=1)
    else:
        """State 2,5"""
        # talk:32180100:"Goodness gracious!"
        assert t321006000_x33(text1=32180100, mode3=1)
    """State 6"""
    return 0

def t321006000_x41():
    """State 0,2"""
    if not GetEventFlag(1045389203):
        """State 3,6"""
        # talk:32180200:"Blast! You wretched Tarnished!"
        assert t321006000_x32(text2=32180200, z5=1045389203, mode4=1)
    elif not GetEventFlag(1045382700):
        """State 4"""
        pass
    else:
        """State 5"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 7"""
    return 0

def t321006000_x42():
    """State 0,1"""
    # talk:32180400:"Where are my...men...?"
    assert t321006000_x33(text1=32180400, mode3=1)
    """State 2"""
    return 0

def t321006000_x43():
    """State 0,1"""
    if GetEventFlag(3585) == 1:
        """State 3"""
        Label('L0')
        """State 5"""
        assert t321006000_x46()
    else:
        """State 2,4"""
        # actionbutton:6000:"Talk"
        call = t321006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                             flag4=6000)
        if call.Done():
            pass
        elif GetEventFlag(3585) == 1:
            Goto('L0')
    """State 6"""
    return 0

def t321006000_x44():
    """State 0,1"""
    if not GetEventFlag(1045389205):
        """State 2"""
        pass
    else:
        """State 3"""
        pass
    """State 4"""
    def WhilePaused():
        RequestAnimation(90300, -1)
    assert t321006000_x45()
    """State 5"""
    return 0

def t321006000_x45():
    """State 0,1"""
    if not GetEventFlag(1045389205):
        """State 5"""
        SetEventFlag(1045382705, 1)
        """State 6"""
        # talk:32101000:"Ah, you've come to lend me your aid, have you?"
        assert t321006000_x31(text3=32101000, mode5=1)
        """State 2"""
        SetEventFlag(1045389205, 1)
    else:
        """State 3"""
        if not GetEventFlag(1046360705):
            """State 4"""
            SetEventFlag(1045382705, 1)
            """State 7"""
            assert t321006000_x49()
        else:
            """State 8"""
            assert t321006000_x50()
    """State 9"""
    return 0

def t321006000_x46():
    """State 0"""
    while True:
        """State 3"""
        # actionbutton:6000:"Talk"
        call = t321006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                             flag4=6000)
        if call.Done():
            break
        elif (not GetEventFlag(1045389205) and GetDistanceToPlayer() < 50 and not GetEventFlag(1045382705)
              and not GetEventFlag(1045382701)):
            """State 2"""
            # talk:32100100:"Hello? Is anybody there?"
            call = t321006000_x32(text2=32100100, z5=1045382704, mode4=1)
            if call.Done():
                """State 4"""
                # actionbutton:6000:"Talk"
                call = t321006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                                     flag12=6000, flag4=6000)
                if call.Done():
                    break
                elif (CheckSpecificPersonTalkHasEnded(0) == 1 and not GetEventFlag(1045389205) and GetCurrentStateElapsedTime()
                      > 25):
                    pass
            elif (GetEventFlag(1045389205) == 1 or GetEventFlag(1045382705) == 1 or GetEventFlag(1045382701)
                  == 1 or GetDistanceToPlayer() > 75):
                """State 1"""
                pass
    """State 5"""
    return 0

def t321006000_x47():
    """State 0,1"""
    if not GetEventFlag(1046369205):
        """State 2"""
        # talk:32105000:"Ah, you, is it?"
        assert t321006000_x30(text4=32105000, z6=1046369205, mode6=1)
    elif not GetEventFlag(1046369206):
        """State 3"""
        # talk:32105100:"I am sorry to have lifted your hopes..."
        assert t321006000_x30(text4=32105100, z6=1046369206, mode6=1)
    else:
        """State 4"""
        # talk:32105200:"I must begin my search post-haste."
        assert t321006000_x30(text4=32105200, z6=1046369207, mode6=1)
    """State 5"""
    return 0

def t321006000_x48():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(90300, -1)
    assert t321006000_x47()
    """State 2"""
    return 0

def t321006000_x49():
    """State 0,1"""
    if not GetEventFlag(1045389206):
        """State 6"""
        # talk:32101100:"What are you waiting for? A kiss goodbye?"
        assert t321006000_x31(text3=32101100, mode5=1)
        """State 3"""
        SetEventFlag(1045389206, 1)
    elif not GetEventFlag(1045389207):
        """State 5"""
        # talk:32101200:"Hmph, yes, now allow me to furnish you with a little advice."
        assert t321006000_x31(text3=32101200, mode5=1)
        """State 2"""
        SetEventFlag(1045389207, 1)
    else:
        """State 7"""
        # talk:32101300:"What are you waiting for? A kiss goodbye?"
        assert t321006000_x31(text3=32101300, mode5=1)
        """State 4"""
        SetEventFlag(1045389208, 1)
    """State 8"""
    return 0

def t321006000_x50():
    """State 0,1"""
    if GetEventFlag(1045389220) == 1:
        """State 16"""
        if GetEventFlag(1045389221) == 1:
            """State 4"""
            if GetEventFlag(1045389222) == 1:
                """State 18"""
                # talk:32102110:"Right then. Time for me to head to the fort."
                assert t321006000_x31(text3=32102110, mode5=1)
                Goto('L1')
            else:
                """State 5"""
                if not GetEventFlag(1045389223):
                    """State 22"""
                    # talk:32102200:"Ah, yes. I've been meaning to ask."
                    assert t321006000_x31(text3=32102200, mode5=1)
                    """State 6"""
                    SetEventFlag(1045389223, 1)
                else:
                    """State 23"""
                    # talk:32102500:"What is it? Have you put your misgivings to rest?"
                    assert t321006000_x31(text3=32102500, mode5=1)
                """State 7"""
                ClearTalkListData()
                c1_110()
                """State 8"""
                # action:23211000:"Pledge service"
                AddTalkListData(1, 23211000, -1)
                # action:23211001:"Do not pledge service"
                AddTalkListData(2, 23211001, -1)
                """State 9"""
                OpenConversationChoicesMenu(0)
                """State 10"""
                assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                """State 11"""
                if GetTalkListEntryResult() == 1:
                    """State 24"""
                    # talk:32102300:"Very well. Very well, indeed."
                    assert t321006000_x31(text3=32102300, mode5=1)
                    """State 13"""
                    SetEventFlag(1045389222, 1)
                    """State 17"""
                    SetEventFlag(1046360706, 1)
                    Goto('L1')
                elif GetTalkListEntryResult() == 2:
                    """State 12"""
                    if not GetEventFlag(1045389224):
                        """State 25"""
                        # talk:32102400:"Excuse me?"
                        assert t321006000_x31(text3=32102400, mode5=1)
                        """State 14"""
                        SetEventFlag(1045389224, 1)
                        Goto('L1')
                    else:
                        """State 26"""
                        # talk:32102600:"Well...not that I can't sympathise with your choice."
                        assert t321006000_x31(text3=32102600, mode5=1)
                        Goto('L1')
        else:
            """State 27"""
            # talk:32102100:"Right then. Time for me to head to the fort."
            assert t321006000_x31(text3=32102100, mode5=1)
            """State 15"""
            SetEventFlag(1045389221, 1)
            Goto('L1')
        """State 3"""
        Label('L0')
        SetEventFlag(1045389220, 1)
        """State 21"""
        # lot:102200:Erdsteel Dagger
        assert t321006000_x3(lot1=102200)
    else:
        """State 2"""
        if not GetEventFlag(1045382705):
            """State 19"""
            # talk:32102000:"Ah-ha! I've been waiting for you with baited breath!"
            assert t321006000_x31(text3=32102000, mode5=1)
            Goto('L0')
        else:
            """State 20"""
            # talk:32101400:"Hm? What's this, kind sir?"
            assert t321006000_x31(text3=32101400, mode5=1)
            Goto('L0')
    """State 28"""
    Label('L1')
    return 0

def t321006000_x51():
    """State 0,1"""
    if not GetEventFlag(10009755):
        """State 2"""
        # talk:32106000:"Ah, nice to see you after so long."
        assert t321006000_x30(text4=32106000, z6=10009755, mode6=1)
    else:
        """State 3"""
        # talk:32106100:"For the time being, I share command of the castle with my Lady, but I plan on returning to my fort afterwards."
        assert t321006000_x30(text4=32106100, z6=10009756, mode6=1)
    """State 4"""
    return 0

