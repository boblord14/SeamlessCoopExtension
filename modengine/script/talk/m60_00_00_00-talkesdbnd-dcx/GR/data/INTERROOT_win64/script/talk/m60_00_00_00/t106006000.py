# -*- coding: utf-8 -*-
def t106006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t106006000_x6(flag3=6000, flag4=6000, flag5=6000, val1=5, val2=10, val3=12, val4=22, val5=25, actionbutton1=6000,
                  flag6=6000, flag7=6001, flag8=6000, flag9=6000, flag10=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t106006000_1000():
    """State 0,2,3"""
    assert t106006000_x37()
    """State 1"""
    c1_120(1000)
    Quit()

def t106006000_1101():
    """State 0,2,3"""
    assert t106006000_x38()
    """State 1"""
    c1_120(1101)
    Quit()

def t106006000_2000():
    """State 0,2,3"""
    assert t106006000_x39()
    """State 1"""
    c1_120(2000)
    Quit()

def t106006000_x0(actionbutton1=_, flag7=_, flag11=6000, flag12=6000, flag13=6000, flag14=6000, flag6=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag7) == 1 or GetEventFlag(flag11) == 1 or GetEventFlag(flag12) == 1 or
                GetEventFlag(flag13) == 1 or GetEventFlag(flag14) == 1)
        """State 4"""
        assert not GetEventFlag(flag6)
        """State 2"""
        if GetEventFlag(flag6) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag7) and not GetEventFlag(flag11) and not GetEventFlag(flag12) and not
              GetEventFlag(flag13) and not GetEventFlag(flag14)):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t106006000_x1():
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

def t106006000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t106006000_x3(lot1=103900):
    """State 0,1"""
    # lot:103900:Spirit Calling Bell
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t106006000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t106006000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t106006000_x1()
    else:
        """State 4,7"""
        call = t106006000_x34()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t106006000_x1()
    """State 9"""
    return 0

def t106006000_x5():
    """State 0,1"""
    assert t106006000_x1()
    """State 2"""
    return 0

def t106006000_x6(flag3=6000, flag4=6000, flag5=6000, val1=5, val2=10, val3=12, val4=22, val5=25, actionbutton1=6000,
                  flag6=6000, flag7=6001, flag8=6000, flag9=6000, flag10=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t106006000_x23(flag3=flag3, flag4=flag4, flag5=flag5, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag6=flag6, flag7=flag7,
                              flag8=flag8, flag9=flag9, flag10=flag10, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t106006000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t106006000_x7(val1=5, val2=10, val3=12, val4=22, val5=25, actionbutton1=6000, flag6=6000, flag7=6001,
                  flag8=6000, flag9=6000, flag10=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t106006000_x10(actionbutton1=actionbutton1, flag6=flag6, flag7=flag7, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t106006000_x14(val1=val1, z1=z1)
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
        elif GetEventFlag(flag10) == 1:
            Goto('L0')
        elif GetEventFlag(flag8) == 1 and not GetEventFlag(flag9) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t106006000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t106006000_x27() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t106006000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t106006000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t106006000_x18(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t106006000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t106006000_x9(flag3=6000, val2=10, val3=12):
    """State 0,8"""
    assert t106006000_x36()
    """State 1"""
    if GetEventFlag(flag3) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t106006000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t106006000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t106006000_x10(actionbutton1=6000, flag6=6000, flag7=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t106006000_x11(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t106006000_x0(actionbutton1=actionbutton1, flag7=flag7, flag11=6000, flag12=6000, flag13=6000,
                flag14=6000, flag6=flag6))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t106006000_x11(z6=_, val6=_):
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

def t106006000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t106006000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t106006000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t106006000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t106006000_x13():
    """State 0,1"""
    assert t106006000_x11(z6=1101, val6=1101)
    """State 2"""
    return 0

def t106006000_x14(val1=5, z1=1):
    """State 0,2"""
    assert t106006000_x24()
    """State 1"""
    call = t106006000_x15()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t106006000_x26()
    """State 4"""
    return 0

def t106006000_x15():
    """State 0,1"""
    assert t106006000_x11(z6=1000, val6=1000)
    """State 2"""
    return 0

def t106006000_x16(val5=25):
    """State 0,1"""
    call = t106006000_x17()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t106006000_x27()
    """State 3"""
    return 0

def t106006000_x17():
    """State 0,1"""
    assert t106006000_x11(z6=1100, val6=1100)
    """State 2"""
    return 0

def t106006000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t106006000_x36()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t106006000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t106006000_x29()
    """Unused"""
    """State 6"""
    return 0

def t106006000_x19():
    """State 0,2"""
    call = t106006000_x11(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t106006000_x20():
    """State 0,1"""
    assert t106006000_x11(z6=1001, val6=1001)
    """State 2"""
    return 0

def t106006000_x21():
    """State 0,1"""
    assert t106006000_x11(z6=1103, val6=1103)
    """State 2"""
    return 0

def t106006000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t106006000_x23(flag3=6000, flag4=6000, flag5=6000, val1=5, val2=10, val3=12, val4=22, val5=25, actionbutton1=6000,
                   flag6=6000, flag7=6001, flag8=6000, flag9=6000, flag10=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t106006000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag6=flag6, flag7=flag7, flag8=flag8, flag9=flag9, flag10=flag10, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag3) == 1:
            """State 3"""
            Label('L0')
            call = t106006000_x9(flag3=flag3, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag4) == 1 or GetEventFlag(flag5) == 1:
            """State 2"""
            call = t106006000_x8(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag3) == 1:
                Goto('L0')
            elif not GetEventFlag(flag4) and not GetEventFlag(flag5):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t106006000_x35() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t106006000_x24():
    """State 0,1"""
    assert t106006000_x25()
    """State 2"""
    return 0

def t106006000_x25():
    """State 0,1"""
    assert t106006000_x11(z6=1104, val6=1104)
    """State 2"""
    return 0

def t106006000_x26():
    """State 0,1"""
    call = t106006000_x11(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t106006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t106006000_x27():
    """State 0,1"""
    call = t106006000_x11(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t106006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t106006000_x28():
    """State 0,1"""
    call = t106006000_x11(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t106006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t106006000_x29():
    """State 0,1"""
    call = t106006000_x11(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t106006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t106006000_x30(text3=_, z5=_, mode5=1):
    """State 0,5"""
    assert t106006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text3, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode5:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(z5, 1)
    """State 6"""
    return 0

def t106006000_x31(text2=_, mode4=1):
    """State 0,4"""
    assert t106006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t106006000_x32(text1=_, flag1=_, mode3=1):
    """State 0,5"""
    assert t106006000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(flag1, 1)
    """State 1"""
    TalkToPlayer(text1, -1, -1, 1)
    """State 4"""
    if not mode3:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t106006000_x33():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t106006000_x34():
    """State 0,1"""
    assert t106006000_x11(z6=1002, val6=1002)
    """State 2"""
    return 0

def t106006000_x35():
    """State 0,1"""
    assert t106006000_x1()
    """State 2"""
    return 0

def t106006000_x36():
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

def t106006000_x37():
    """State 0,2"""
    if GetEventFlag(3746) == 1:
        """State 3"""
        def WhilePaused():
            RequestAnimation(20010, -1)
        assert t106006000_x41()
    else:
        """State 1"""
        pass
    """State 4"""
    return 0

def t106006000_x38():
    """State 0,1"""
    if GetEventFlag(1042369401) == 1:
        """State 2"""
        assert not GetEventFlag(1042362734)
        """State 5"""
        SetEventFlag(1042362733, 1)
        # talk:10602020:"No sense in arguing, I see."
        def WhilePaused():
            RequestAnimation(20010, -1)
        def ExitPause():
            SetEventFlag(1042362733, 0)
        assert (t106006000_x32(text1=10602020, flag1=1042369410, mode3=1) and CheckSpecificPersonTalkHasEnded(0)
                == 1)
        """State 3"""
        def WhilePaused():
            RequestAnimation(20010, -1)
        Quit()
    else:
        """State 4"""
        assert t106006000_x46(flag1=1042362730, flag2=1042362731)
        """State 6"""
        return 0

def t106006000_x39():
    """State 0,1"""
    assert GetEventFlag(3746) == 1
    """State 2"""
    assert t106006000_x40()
    """State 3"""
    return 0

def t106006000_x40():
    """State 0,1"""
    if GetEventFlag(1042369410) == 1:
        """State 2"""
        Quit()
    else:
        pass
    while True:
        """State 6"""
        # actionbutton:6414:"Talk"
        call = t106006000_x0(actionbutton1=6414, flag7=1042369415, flag11=6000, flag12=6000, flag13=6000,
                             flag14=6000, flag6=6000)
        if call.Done():
            break
        elif not GetEventFlag(1042369415):
            """State 5"""
            assert GetEventFlag(1042369415) == 1
        elif not GetEventFlag(1042369412) and not GetEventFlag(9000) and GetDistanceToPlayer() < 20:
            """State 3"""
            SetEventFlag(1042369406, 1)
            """State 7"""
            # talk:10600400:"This way, Tarnished."
            assert t106006000_x32(text1=10600400, flag1=1042369412, mode3=1)
        elif GetEventFlag(1042369407) == 1 and GetDistanceToPlayer() > 9 and not GetEventFlag(1042369410):
            """State 8"""
            SetEventFlag(1042362733, 1)
            SetEventFlag(1042369410, 1)
            SetEventFlag(1042369415, 0)
            # talk:10600300:"Forgive mine intrusion, Tarnished."
            def WhilePaused():
                RequestAnimation(20010, -1)
            def ExitPause():
                SetEventFlag(1042362732, 1)
                SetEventFlag(1042362733, 0)
            assert (t106006000_x32(text1=10600300, flag1=1042369409, mode3=1) and CheckSpecificPersonTalkHasEnded(0)
                    == 1)
            """State 4"""
            def WhilePaused():
                RequestAnimation(20010, -1)
            Quit()
    """State 9"""
    return 0

def t106006000_x41():
    """State 0,1"""
    if GetEventFlag(1042369407) == 1:
        """State 3,5"""
        assert t106006000_x44()
    elif GetEventFlag(1042369408) == 1:
        """State 2,6"""
        assert t106006000_x45()
    else:
        """State 4"""
        assert t106006000_x43()
    """State 7"""
    return 0

def t106006000_x42(action1=_, action2=_):
    """State 0,1"""
    c1_110()
    """State 2"""
    ClearTalkListData()
    """State 3"""
    AddTalkListData(1, action1, -1)
    AddTalkListData(2, action2, -1)
    """State 4"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 5"""
    if GetTalkListEntryResult() == 1:
        """State 6"""
        return 0
    elif GetTalkListEntryResult() == 2:
        """State 7"""
        return 1
    else:
        """State 8"""
        return 2

def t106006000_x43():
    """State 0,2"""
    # talk:10600100:"A pleasure to meet thee, Tarnished."
    assert t106006000_x31(text2=10600100, mode4=1)
    """State 3"""
    # action:21061000:"I can call the spectral steed", action:21061001:"I cannot call the spectral steed"
    call = t106006000_x42(action1=21061000, action2=21061001)
    if call.Get() == 0:
        """State 4"""
        # talk:10600200:"Ah. As I had hoped."
        assert t106006000_x30(text3=10600200, z5=1042369407, mode5=1)
        """State 6"""
        # lot:103900:Spirit Calling Bell
        assert t106006000_x3(lot1=103900)
        """State 5"""
        # talk:10600210:"Tis a bell for calling forth spirits."
        assert t106006000_x31(text2=10600210, mode4=1)
        """State 1"""
        Label('L0')
        SetEventFlag(1042369405, 1)
        SetEventFlag(1042369406, 1)
    elif call.Get() == 1:
        """State 7"""
        # talk:10601000:"Trifle not with me, Tarnished."
        assert t106006000_x30(text3=10601000, z5=1042369408, mode5=1)
        Goto('L0')
    elif call.Done():
        pass
    """State 8"""
    return 0

def t106006000_x44():
    """State 0,2"""
    # talk:10600300:"Forgive mine intrusion, Tarnished."
    assert t106006000_x30(text3=10600300, z5=1042369409, mode5=1)
    """State 1"""
    SetEventFlag(1042362732, 1)
    SetEventFlag(1042369410, 1)
    """State 3"""
    return 0

def t106006000_x45():
    """State 0,2"""
    # talk:10601100:"I will ask thee again."
    assert t106006000_x31(text2=10601100, mode4=1)
    """State 3"""
    # action:21061002:"I can call the spectral steed", action:21061003:"I cannot call the spectral steed"
    call = t106006000_x42(action1=21061002, action2=21061003)
    if call.Get() == 0:
        """State 4"""
        # talk:10600200:"Ah. As I had hoped."
        assert t106006000_x30(text3=10600200, z5=1042369407, mode5=1)
        """State 6"""
        # lot:103900:Spirit Calling Bell
        assert t106006000_x3(lot1=103900)
        """State 5"""
        # talk:10600210:"Tis a bell for calling forth spirits."
        assert t106006000_x31(text2=10600210, mode4=1)
    elif call.Get() == 1:
        """State 7"""
        # talk:10601200:"Quite the stubborn one, aren't we?"
        assert t106006000_x31(text2=10601200, mode4=1)
        """State 1"""
        SetEventFlag(1042362732, 1)
        SetEventFlag(1042369410, 1)
    elif call.Done():
        pass
    """State 8"""
    return 0

def t106006000_x46(flag1=1042362730, flag2=1042362731):
    """State 0,1"""
    if not GetEventFlag(flag1):
        """State 3"""
        # talk:10602000:"What hopest thou to profit?"
        assert t106006000_x32(text1=10602000, flag1=flag1, mode3=1)
    elif not GetEventFlag(flag2):
        """State 4"""
        # talk:10602010:"..."
        assert t106006000_x32(text1=10602010, flag1=flag2, mode3=1)
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

