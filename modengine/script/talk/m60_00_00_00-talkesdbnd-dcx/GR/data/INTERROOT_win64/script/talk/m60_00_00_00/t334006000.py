# -*- coding: utf-8 -*-
def t334006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t334006000_x6(flag1=4223, flag2=4221, flag3=4222, val1=5, val2=10, val3=12, val4=25, val5=25, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    def WhilePaused():
        c1_121(9620)
    Quit()

def t334006000_1000():
    """State 0,2,3"""
    assert t334006000_x37()
    """State 1"""
    c1_120(1000)
    Quit()

def t334006000_1001():
    """State 0,2,3"""
    assert t334006000_x38()
    """State 1"""
    c1_120(1001)
    Quit()

def t334006000_1101():
    """State 0,2,3"""
    assert t334006000_x39()
    """State 1"""
    c1_120(1101)
    Quit()

def t334006000_1102():
    """State 0,2,3"""
    t334006000_x40()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t334006000_1103():
    """State 0,2,3"""
    assert t334006000_x41()
    """State 1"""
    c1_120(1103)
    Quit()

def t334006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t334006000_x1():
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

def t334006000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t334006000_x3(lot1=_):
    """State 0,1"""
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t334006000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t334006000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t334006000_x1()
    else:
        """State 4,7"""
        call = t334006000_x34()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t334006000_x1()
    """State 9"""
    return 0

def t334006000_x5():
    """State 0,1"""
    assert t334006000_x1()
    """State 2"""
    return 0

def t334006000_x6(flag1=4223, flag2=4221, flag3=4222, val1=5, val2=10, val3=12, val4=25, val5=25, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t334006000_x23(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t334006000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t334006000_x7(val1=5, val2=10, val3=12, val4=25, val5=25, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t334006000_x10(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t334006000_x14(val1=val1, z1=z1)
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
            call = t334006000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t334006000_x27() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t334006000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t334006000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t334006000_x18(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t334006000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t334006000_x9(flag1=4223, val2=10, val3=12):
    """State 0,8"""
    assert t334006000_x36()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t334006000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t334006000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t334006000_x10(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t334006000_x11(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t334006000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t334006000_x11(z6=_, val6=_):
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

def t334006000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t334006000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t334006000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t334006000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t334006000_x13():
    """State 0,1"""
    assert t334006000_x11(z6=1101, val6=1101)
    """State 2"""
    return 0

def t334006000_x14(val1=5, z1=1):
    """State 0,2"""
    assert t334006000_x24()
    """State 1"""
    call = t334006000_x15()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t334006000_x26()
    """State 4"""
    return 0

def t334006000_x15():
    """State 0,1"""
    assert t334006000_x11(z6=1000, val6=1000)
    """State 2"""
    return 0

def t334006000_x16(val5=25):
    """State 0,1"""
    call = t334006000_x17()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t334006000_x27()
    """State 3"""
    return 0

def t334006000_x17():
    """State 0,1"""
    assert t334006000_x11(z6=1100, val6=1100)
    """State 2"""
    return 0

def t334006000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t334006000_x36()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t334006000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t334006000_x29()
    """Unused"""
    """State 6"""
    return 0

def t334006000_x19():
    """State 0,2"""
    call = t334006000_x11(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t334006000_x20():
    """State 0,1"""
    assert t334006000_x11(z6=1001, val6=1001)
    """State 2"""
    return 0

def t334006000_x21():
    """State 0,1"""
    assert t334006000_x11(z6=1103, val6=1103)
    """State 2"""
    return 0

def t334006000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t334006000_x23(flag1=4223, flag2=4221, flag3=4222, val1=5, val2=10, val3=12, val4=25, val5=25, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t334006000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t334006000_x9(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t334006000_x8(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t334006000_x35() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t334006000_x24():
    """State 0,1"""
    assert t334006000_x25()
    """State 2"""
    return 0

def t334006000_x25():
    """State 0,1"""
    assert t334006000_x11(z6=1104, val6=1104)
    """State 2"""
    return 0

def t334006000_x26():
    """State 0,1"""
    call = t334006000_x11(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t334006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t334006000_x27():
    """State 0,1"""
    call = t334006000_x11(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t334006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t334006000_x28():
    """State 0,1"""
    call = t334006000_x11(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t334006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t334006000_x29():
    """State 0,1"""
    call = t334006000_x11(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t334006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t334006000_x30(text3=_, mode5=1):
    """State 0,4"""
    assert t334006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t334006000_x31(text2=33480200, z5=10009703, mode4=1):
    """State 0,5"""
    assert t334006000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(z5, 1)
    """State 1"""
    # talk:33480200:"I see. You are but a simple villain."
    TalkToPlayer(text2, -1, -1, 1)
    """State 4"""
    if not mode4:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t334006000_x32(text1=_, mode3=1):
    """State 0,4"""
    assert t334006000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t334006000_x33():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t334006000_x34():
    """State 0,1"""
    assert t334006000_x11(z6=1002, val6=1002)
    """State 2"""
    return 0

def t334006000_x35():
    """State 0,1"""
    assert t334006000_x1()
    """State 2"""
    return 0

def t334006000_x36():
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

def t334006000_x37():
    """State 0,1"""
    if GetEventFlag(4225) == 1:
        """State 2"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t334006000_x42()
    elif GetEventFlag(4226) == 1:
        """State 3"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t334006000_x43()
    elif GetEventFlag(4227) == 1:
        """State 4"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t334006000_x44()
    elif GetEventFlag(4228) == 1:
        """State 5"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t334006000_x45()
    elif GetEventFlag(4229) == 1:
        """State 6"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t334006000_x46()
    """State 7"""
    return 0

def t334006000_x38():
    """State 0,1"""
    # talk:33480300:"You wouldn't even register as a threat to father."
    assert t334006000_x32(text1=33480300, mode3=1)
    """State 2"""
    return 0

def t334006000_x39():
    """State 0,1"""
    if not GetEventFlag(10002780):
        """State 5"""
        # talk:33480000:" "
        assert t334006000_x32(text1=33480000, mode3=1)
        """State 3"""
        SetEventFlag(10002780, 1)
    elif not GetEventFlag(10002781):
        """State 6"""
        # talk:33480100:"What do you intend?"
        assert t334006000_x32(text1=33480100, mode3=1)
        """State 4"""
        SetEventFlag(10002781, 1)
    else:
        """State 2"""
        pass
    """State 7"""
    return 0

def t334006000_x40():
    """State 0,2"""
    if not GetEventFlag(10009703):
        """State 3"""
        # talk:33480200:"I see. You are but a simple villain."
        assert t334006000_x31(text2=33480200, z5=10009703, mode4=1)
    else:
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 4"""
    return 0

def t334006000_x41():
    """State 0,1"""
    # talk:33480400:"Father... I am slain."
    assert t334006000_x32(text1=33480400, mode3=1)
    """State 2"""
    return 0

def t334006000_x42():
    """State 0,1"""
    assert t334006000_x47()
    """State 2"""
    return 0

def t334006000_x43():
    """State 0,1"""
    assert t334006000_x48()
    """State 2"""
    return 0

def t334006000_x44():
    """State 0,1"""
    assert t334006000_x49()
    """State 2"""
    return 0

def t334006000_x45():
    """State 0,2"""
    SetEventFlag(10009714, 1)
    """State 1"""
    if not GetEventFlag(11109916):
        """State 3"""
        assert t334006000_x50()
    elif not GetEventFlag(11109921):
        """State 4"""
        assert t334006000_x51()
    else:
        """State 5"""
        assert t334006000_x52()
    """State 6"""
    return 0

def t334006000_x46():
    """State 0,1"""
    assert t334006000_x53()
    """State 2"""
    return 0

def t334006000_x47():
    """State 0,1"""
    if not GetEventFlag(10009705):
        """State 5"""
        # talk:33400200:"Well, who do we have here?"
        assert t334006000_x30(text3=33400200, mode5=1)
        """State 3"""
        SetEventFlag(10009705, 1)
    elif not GetEventFlag(10009706):
        """State 6"""
        # talk:33400300:"If you intend to challenge Godrick,"
        assert t334006000_x30(text3=33400300, mode5=1)
        """State 2"""
        SetEventFlag(10009706, 1)
        """State 4"""
        SetEventFlag(10009709, 1)
    else:
        """State 7"""
        # talk:33400400:"Apologies, but I've idled long enough."
        assert t334006000_x30(text3=33400400, mode5=1)
    """State 8"""
    return 0

def t334006000_x48():
    """State 0,1"""
    if GetEventFlag(11109905) == 1:
        """State 2"""
        if not GetEventFlag(11109906):
            """State 13"""
            if not GetEventFlag(11109656):
                """State 18"""
                # talk:33401100:"Ah, yes."
                assert t334006000_x30(text3=33401100, mode5=1)
            else:
                """State 22"""
                # talk:33401110:"Ah, yes."
                assert t334006000_x30(text3=33401110, mode5=1)
            """State 11"""
            SetEventFlag(11109906, 1)
        else:
            """State 20"""
            # talk:33401200:"It's about time I headed off."
            assert t334006000_x30(text3=33401200, mode5=1)
            """State 12"""
            SetEventFlag(11109909, 1)
        """State 4"""
        c1_110()
        ClearTalkListData()
        """State 9"""
        # goods:8164:Seluvis's Potion
        if ComparePlayerInventoryNumber(3, 8164, 4, 1, 0) == 1 and not GetEventFlag(11109908):
            """State 5"""
            # action:23341000:"Give Seluvis's Potion"
            AddTalkListData(1, 23341000, -1)
            # action:23341003:"Leave"
            AddTalkListData(2, 23341003, -1)
            """State 6"""
            OpenConversationChoicesMenu(0)
            assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 7"""
            if GetTalkListEntryResult() == 1:
                """State 19"""
                # talk:33402000:"Is that some kind of medicine?"
                assert t334006000_x30(text3=33402000, mode5=1)
                """State 10"""
                SetEventFlag(11109908, 1)
            else:
                """State 8"""
                pass
        else:
            pass
    elif GetEventFlag(10009705) == 1 and GetEventFlag(9101) == 1 and GetEventFlag(10009707) == 1:
        """State 14"""
        # talk:33401000:"You again..."
        assert t334006000_x30(text3=33401000, mode5=1)
        """State 21"""
        Label('L0')
        # lot:104200:Arsenal Charm
        assert t334006000_x3(lot1=104200)
        """State 3"""
        Label('L1')
        SetEventFlag(11109905, 1)
    elif GetEventFlag(10009705) == 1 and GetEventFlag(9101) == 1 and not GetEventFlag(10009707):
        """State 15"""
        # talk:33401010:"You again..."
        assert t334006000_x30(text3=33401010, mode5=1)
        Goto('L0')
    elif GetEventFlag(10009705) == 1 and not GetEventFlag(9101):
        """State 16"""
        # talk:33401800:"You again..."
        assert t334006000_x30(text3=33401800, mode5=1)
        Goto('L1')
    else:
        """State 17"""
        # talk:33401900:"Oh, hello."
        assert t334006000_x30(text3=33401900, mode5=1)
        Goto('L1')
    """State 23"""
    return 0

def t334006000_x49():
    """State 0,1"""
    if not GetEventFlag(1034429205):
        """State 4"""
        # talk:33403000:"Oh, it's you..."
        assert t334006000_x30(text3=33403000, mode5=1)
        """State 2"""
        SetEventFlag(1034429205, 1)
    else:
        """State 5"""
        # talk:33403100:"But this time, I'm a woman grown."
        assert t334006000_x30(text3=33403100, mode5=1)
        """State 3"""
        SetEventFlag(1034429209, 1)
    """State 6"""
    return 0

def t334006000_x50():
    """State 0,9"""
    # talk:33404000:"Ah, you..."
    assert t334006000_x30(text3=33404000, mode5=1)
    """State 8"""
    SetEventFlag(11109923, 1)
    """State 1"""
    c1_110()
    ClearTalkListData()
    """State 6"""
    if GetEventFlag(11109678) == 1:
        """State 2"""
        # action:23341002:"I heard from Gideon"
        AddTalkListData(1, 23341002, -1)
        # action:23341003:"Leave"
        AddTalkListData(2, 23341003, -1)
        """State 3"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 10"""
            # talk:33404100:"...So you know already, do you?"
            assert t334006000_x30(text3=33404100, mode5=1)
            """State 7"""
            SetEventFlag(11109916, 1)
        else:
            """State 5"""
            pass
    else:
        pass
    """State 11"""
    return 0

def t334006000_x51():
    """State 0,8"""
    if not GetEventFlag(11109917):
        """State 13"""
        # talk:33404200:"I...can no longer trust in father..."
        assert t334006000_x30(text3=33404200, mode5=1)
        """State 9"""
        SetEventFlag(11109917, 1)
    else:
        """State 14"""
        # talk:33404300:"No, no, no..."
        assert t334006000_x30(text3=33404300, mode5=1)
        """State 1"""
        c1_110()
        ClearTalkListData()
        """State 6"""
        # goods:8164:Seluvis's Potion, goods:8194:The Stormhawk King
        if (ComparePlayerInventoryNumber(3, 8164, 4, 1, 0) == 1 or ComparePlayerInventoryNumber(3, 8194,
            4, 1, 0) == 1):
            """State 2"""
            # goods:8164:Seluvis's Potion, action:23341000:"Give Seluvis's Potion"
            AddTalkListDataIf(ComparePlayerInventoryNumber(3, 8164, 4, 1, 0) == 1 and not GetEventFlag(3569),
                              1, 23341000, -1)
            # goods:8194:The Stormhawk King, action:23341001:"Give the Stormhawk King"
            AddTalkListDataIf((ComparePlayerInventoryNumber(3, 8194, 4, 1, 0) == 1 and GetEventFlag(3708) == 1) or (ComparePlayerInventoryNumber(3, 8194, 4, 1, 0) == 1 and GetEventFlag(3709) == 1),
                              2, 23341001, -1)
            # action:23341003:"Leave"
            AddTalkListData(3, 23341003, -1)
            """State 3"""
            OpenConversationChoicesMenu(0)
            assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 4"""
            if GetTalkListEntryResult() == 1:
                """State 15"""
                # talk:33405000:"Medicine, is it?"
                assert t334006000_x30(text3=33405000, mode5=1)
                """State 7"""
                SetEventFlag(11109919, 1)
                """State 11"""
                # goods:8164:Seluvis's Potion
                PlayerEquipmentQuantityChange(3, 8164, -1)
                assert GetWhetherChrEventAnimHasEnded(11100781) == 1
                """State 17"""
                # talk:33405010:"It's very sweet...isn't it..."
                assert t334006000_x30(text3=33405010, mode5=1)
            elif GetTalkListEntryResult() == 2:
                """State 16"""
                # talk:33406000:"Is that ash?"
                assert t334006000_x30(text3=33406000, mode5=1)
                """State 10"""
                SetEventFlag(11109921, 1)
                """State 12"""
                # goods:8194:The Stormhawk King
                PlayerEquipmentQuantityChange(3, 8194, -1)
            else:
                """State 5"""
                pass
        else:
            pass
    """State 18"""
    return 0

def t334006000_x52():
    """State 0,1"""
    if not GetEventFlag(11109922):
        """State 3"""
        # talk:33406100:"I'm...not like Roderika."
        assert t334006000_x30(text3=33406100, mode5=1)
        """State 2"""
        SetEventFlag(11109922, 1)
    else:
        """State 4"""
        # talk:33406200:"In this ash, I can smell the ancient storm."
        assert t334006000_x30(text3=33406200, mode5=1)
    """State 5"""
    return 0

def t334006000_x53():
    """State 0,1"""
    if not GetEventFlag(10009715):
        """State 5"""
        # talk:33407000:"It's been some time."
        assert t334006000_x30(text3=33407000, mode5=1)
        """State 3"""
        SetEventFlag(10009715, 1)
    elif not GetEventFlag(10009716):
        """State 6"""
        # talk:33407100:"Again, I am Nepheli Loux. Warrior."
        assert t334006000_x30(text3=33407100, mode5=1)
        """State 9"""
        # lot:104220:Ancient Dragon Smithing Stone
        assert t334006000_x3(lot1=104220)
        """State 2"""
        SetEventFlag(10009716, 1)
        """State 10"""
        # talk:33407110:"Should you become Elden Lord."
        assert t334006000_x30(text3=33407110, mode5=1)
    elif not GetEventFlag(10009717):
        """State 7"""
        # talk:33407200:"Farewell, fellow warrior."
        assert t334006000_x30(text3=33407200, mode5=1)
        """State 4"""
        SetEventFlag(10009717, 1)
    else:
        """State 8"""
        # talk:33407300:"I will remain, to summon the storm."
        assert t334006000_x30(text3=33407300, mode5=1)
    """State 11"""
    return 0

