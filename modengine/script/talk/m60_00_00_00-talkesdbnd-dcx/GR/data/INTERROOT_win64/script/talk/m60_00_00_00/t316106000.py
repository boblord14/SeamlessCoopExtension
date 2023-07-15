# -*- coding: utf-8 -*-
def t316106000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t316106000_x6(flag1=1041339259, flag2=3461, flag3=3462, val1=5, val2=10, val3=12, val4=10, val5=12,
                  actionbutton1=6000, flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1,
                  z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1)
    def WhilePaused():
        c5_121(not GetEventFlag(1044369222), 9620)
    Quit()

def t316106000_1000():
    """State 0,2,3"""
    assert t316106000_x38()
    """State 1"""
    c1_120(1000)
    Quit()

def t316106000_1101():
    """State 0,2,3"""
    assert t316106000_x39()
    """State 1"""
    c1_120(1101)
    Quit()

def t316106000_1102():
    """State 0,2,3"""
    t316106000_x40()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t316106000_2000():
    """State 0,2,3"""
    assert t316106000_x41()
    """State 1"""
    c1_120(2000)
    Quit()

def t316106000_x0(actionbutton1=_, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag4=6000):
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
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t316106000_x1():
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

def t316106000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t316106000_x3(lot1=101000):
    """State 0,1"""
    # lot:101000:Sellen's Primal Glintstone
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t316106000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t316106000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t316106000_x1()
    else:
        """State 4,7"""
        call = t316106000_x35()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t316106000_x1()
    """State 9"""
    return 0

def t316106000_x5():
    """State 0,1"""
    assert t316106000_x1()
    """State 2"""
    return 0

def t316106000_x6(flag1=1041339259, flag2=3461, flag3=3462, val1=5, val2=10, val3=12, val4=10, val5=12,
                  actionbutton1=6000, flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1,
                  z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t316106000_x23(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t316106000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t316106000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t316106000_x10(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t316106000_x14(val1=val1, z1=z1)
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
            call = t316106000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t316106000_x27() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t316106000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t316106000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t316106000_x18(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t316106000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t316106000_x9(flag1=1041339259, val2=10, val3=12):
    """State 0,8"""
    assert t316106000_x37()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t316106000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t316106000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t316106000_x10(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t316106000_x11(z7=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t316106000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t316106000_x11(z7=_, val6=_):
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

def t316106000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t316106000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t316106000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t316106000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t316106000_x13():
    """State 0,1"""
    assert t316106000_x11(z7=1101, val6=1101)
    """State 2"""
    return 0

def t316106000_x14(val1=5, z1=1):
    """State 0,2"""
    assert t316106000_x24()
    """State 1"""
    call = t316106000_x15()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t316106000_x26()
    """State 4"""
    return 0

def t316106000_x15():
    """State 0,1"""
    assert t316106000_x11(z7=1000, val6=1000)
    """State 2"""
    return 0

def t316106000_x16(val5=12):
    """State 0,1"""
    call = t316106000_x17()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t316106000_x27()
    """State 3"""
    return 0

def t316106000_x17():
    """State 0,1"""
    assert t316106000_x11(z7=1100, val6=1100)
    """State 2"""
    return 0

def t316106000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t316106000_x37()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t316106000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t316106000_x29()
    """Unused"""
    """State 6"""
    return 0

def t316106000_x19():
    """State 0,2"""
    call = t316106000_x11(z7=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t316106000_x20():
    """State 0,1"""
    assert t316106000_x11(z7=1001, val6=1001)
    """State 2"""
    return 0

def t316106000_x21():
    """State 0,1"""
    assert t316106000_x11(z7=1103, val6=1103)
    """State 2"""
    return 0

def t316106000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t316106000_x23(flag1=1041339259, flag2=3461, flag3=3462, val1=5, val2=10, val3=12, val4=10, val5=12,
                   actionbutton1=6000, flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1,
                   z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t316106000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t316106000_x9(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t316106000_x8(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t316106000_x36() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t316106000_x24():
    """State 0,1"""
    assert t316106000_x25()
    """State 2"""
    return 0

def t316106000_x25():
    """State 0,1"""
    assert t316106000_x11(z7=1104, val6=1104)
    """State 2"""
    return 0

def t316106000_x26():
    """State 0,1"""
    call = t316106000_x11(z7=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t316106000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t316106000_x27():
    """State 0,1"""
    call = t316106000_x11(z7=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t316106000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t316106000_x28():
    """State 0,1"""
    call = t316106000_x11(z7=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t316106000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t316106000_x29():
    """State 0,1"""
    call = t316106000_x11(z7=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t316106000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t316106000_x30(text4=31610300, z6=1044369232, mode6=1):
    """State 0,5"""
    assert t316106000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    # talk:31610300:"<panting>"
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

def t316106000_x31(text3=_, mode5=1):
    """State 0,4"""
    assert t316106000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t316106000_x32(text2=_, z5=_, mode4=1):
    """State 0,5"""
    assert t316106000_x34() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t316106000_x33(text1=_, mode3=1):
    """State 0,4"""
    assert t316106000_x34() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t316106000_x34():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t316106000_x35():
    """State 0,1"""
    assert t316106000_x11(z7=1002, val6=1002)
    """State 2"""
    return 0

def t316106000_x36():
    """State 0,1"""
    assert t316106000_x1()
    """State 2"""
    return 0

def t316106000_x37():
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

def t316106000_x38():
    """State 0,1,2"""
    assert t316106000_x42()
    """State 3"""
    return 0

def t316106000_x39():
    """State 0,1"""
    if not GetEventFlag(1041332700):
        """State 3"""
        # talk:31680200:"Ngh!"
        assert t316106000_x32(text2=31680200, z5=1041332700, mode4=1)
    elif not GetEventFlag(1041332701):
        """State 4"""
        # talk:31680300:"Why, you. Are you mad?"
        assert t316106000_x32(text2=31680300, z5=1041332701, mode4=1)
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t316106000_x40():
    """State 0,2"""
    if not GetEventFlag(1044369234):
        """State 3,5"""
        SetEventFlag(1044369234, 1)
        """State 6"""
        # talk:31680400:"My death would only be temporary."
        assert t316106000_x33(text1=31680400, mode3=1)
    else:
        """State 4"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 7"""
    return 0

def t316106000_x41():
    """State 0,1"""
    assert t316106000_x44()
    """State 2"""
    return 0

def t316106000_x42():
    """State 0,1"""
    def WhilePaused():
        RequestAnimationIf(GetEventFlag(1044369222) == 1, 90310, -1)
    assert t316106000_x43()
    """State 2"""
    return 0

def t316106000_x43():
    """State 0,5"""
    SetEventFlag(1041339206, 1)
    """State 4"""
    if GetEventFlag(1044369222) == 1:
        """State 2"""
        if not GetEventFlag(1044369233):
            """State 6"""
            # talk:31610000:"My apprentice, thank you for coming."
            assert t316106000_x31(text3=31610000, mode5=1)
            """State 8"""
            assert t316106000_x31(text3=31610100, mode5=1)
            """State 3"""
            SetEventFlag(1044369233, 1)
        else:
            """State 1"""
            if not GetEventFlag(1044369231):
                """State 11"""
                assert t316106000_x46()
            elif not GetEventFlag(1044369232):
                """State 10"""
                # talk:31610300:"<panting>"
                assert t316106000_x30(text4=31610300, z6=1044369232, mode6=1)
            else:
                """State 7"""
                # talk:31610500:"Treat it with care, my apprentice..."
                assert t316106000_x31(text3=31610500, mode5=1)
    else:
        """State 9"""
        # talk:31610400:"<shivering moans>"
        assert t316106000_x31(text3=31610400, mode5=1)
    """State 12"""
    return 0

def t316106000_x44():
    """State 0"""
    while True:
        """State 1"""
        # actionbutton:6000:"Talk"
        call = t316106000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                             flag4=6000)
        if call.Done():
            break
        elif GetEventFlag(1044369233) == 1 and not GetEventFlag(1044369231):
            """State 2"""
            # actionbutton:6290:"Accept primal glintstone"
            call = t316106000_x0(actionbutton1=6290, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                                 flag12=6000, flag4=6000)
            if call.Done():
                break
            elif GetEventFlag(1044369231) == 1:
                pass
    """State 3"""
    return 0

def t316106000_x45():
    """State 0,2"""
    assert GetEventFlag(1044362703) == 1 and GetEventFlag(1044362709) == 1
    """State 3"""
    assert GetCurrentStateElapsedTime() > 4.7
    """State 5"""
    # talk:31610200:"<groaning in pain>"
    assert t316106000_x33(text1=31610200, mode3=1) and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    SetEventFlag(1044369231, 1)
    """State 4"""
    # lot:101000:Sellen's Primal Glintstone
    assert t316106000_x3(lot1=101000)
    """State 6"""
    return 0

def t316106000_x46():
    """State 0,1"""
    SetEventFlag(1044362702, 1)
    SetEventFlag(1044362708, 1)
    call = t316106000_x45()
    def ExitPause():
        SetEventFlag(1044362702, 0)
        SetEventFlag(1044362708, 0)
    if call.Done():
        pass
    elif not GetEventFlag(1044362702) or not GetEventFlag(1044362708):
        pass
    """State 2"""
    return 0

