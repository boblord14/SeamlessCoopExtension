# -*- coding: utf-8 -*-
def t316006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t316006000_x6(flag1=3463, flag2=3461, flag3=3462, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t316006000_1000():
    """State 0,2,3"""
    assert t316006000_x38()
    """State 1"""
    c1_120(1000)
    Quit()

def t316006000_1101():
    """State 0,2,3"""
    assert t316006000_x39()
    """State 1"""
    c1_120(1101)
    Quit()

def t316006000_1102():
    """State 0,2"""
    t316006000_x40()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t316006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t316006000_x1():
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

def t316006000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t316006000_x3(lot1=_):
    """State 0,1"""
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t316006000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t316006000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t316006000_x1()
    else:
        """State 4,7"""
        call = t316006000_x35()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t316006000_x1()
    """State 9"""
    return 0

def t316006000_x5():
    """State 0,1"""
    assert t316006000_x1()
    """State 2"""
    return 0

def t316006000_x6(flag1=3463, flag2=3461, flag3=3462, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t316006000_x23(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t316006000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t316006000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t316006000_x10(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t316006000_x14(val1=val1, z1=z1)
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
            call = t316006000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t316006000_x27() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t316006000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t316006000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t316006000_x18(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t316006000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t316006000_x9(flag1=3463, val2=10, val3=12):
    """State 0,8"""
    assert t316006000_x37()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t316006000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t316006000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t316006000_x10(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t316006000_x11(z7=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t316006000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t316006000_x11(z7=_, val6=_):
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

def t316006000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t316006000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t316006000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t316006000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t316006000_x13():
    """State 0,1"""
    assert t316006000_x11(z7=1101, val6=1101)
    """State 2"""
    return 0

def t316006000_x14(val1=5, z1=1):
    """State 0,2"""
    assert t316006000_x24()
    """State 1"""
    call = t316006000_x15()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t316006000_x26()
    """State 4"""
    return 0

def t316006000_x15():
    """State 0,1"""
    assert t316006000_x11(z7=1000, val6=1000)
    """State 2"""
    return 0

def t316006000_x16(val5=12):
    """State 0,1"""
    call = t316006000_x17()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t316006000_x27()
    """State 3"""
    return 0

def t316006000_x17():
    """State 0,1"""
    assert t316006000_x11(z7=1100, val6=1100)
    """State 2"""
    return 0

def t316006000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t316006000_x37()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t316006000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t316006000_x29()
    """Unused"""
    """State 6"""
    return 0

def t316006000_x19():
    """State 0,2"""
    call = t316006000_x11(z7=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t316006000_x20():
    """State 0,1"""
    assert t316006000_x11(z7=1001, val6=1001)
    """State 2"""
    return 0

def t316006000_x21():
    """State 0,1"""
    assert t316006000_x11(z7=1103, val6=1103)
    """State 2"""
    return 0

def t316006000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t316006000_x23(flag1=3463, flag2=3461, flag3=3462, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t316006000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t316006000_x9(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t316006000_x8(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t316006000_x36() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t316006000_x24():
    """State 0,1"""
    assert t316006000_x25()
    """State 2"""
    return 0

def t316006000_x25():
    """State 0,1"""
    assert t316006000_x11(z7=1104, val6=1104)
    """State 2"""
    return 0

def t316006000_x26():
    """State 0,1"""
    call = t316006000_x11(z7=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t316006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t316006000_x27():
    """State 0,1"""
    call = t316006000_x11(z7=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t316006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t316006000_x28():
    """State 0,1"""
    call = t316006000_x11(z7=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t316006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t316006000_x29():
    """State 0,1"""
    call = t316006000_x11(z7=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t316006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t316006000_x30(text4=31602100, z6=1044369236, mode6=1):
    """State 0,5"""
    assert t316006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    # talk:31602100:"Your appetite for learning is impressive."
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

def t316006000_x31(text3=_, mode5=1):
    """State 0,4"""
    assert t316006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t316006000_x32(text2=31680000, z5=1044362701, mode4=1):
    """State 0,5"""
    assert t316006000_x34() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(z5, 1)
    """State 1"""
    # talk:31680000:"What's the meaning of this?"
    TalkToPlayer(text2, -1, -1, 1)
    """State 4"""
    if not mode4:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t316006000_x33(text1=_, mode3=1):
    """State 0,4"""
    assert t316006000_x34() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t316006000_x34():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t316006000_x35():
    """State 0,1"""
    assert t316006000_x11(z7=1002, val6=1002)
    """State 2"""
    return 0

def t316006000_x36():
    """State 0,1"""
    assert t316006000_x1()
    """State 2"""
    return 0

def t316006000_x37():
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

def t316006000_x38():
    """State 0,1"""
    if GetEventFlag(3465) == 1:
        """State 3"""
        SetEventFlag(1044369202, 1)
        assert t316006000_x41()
    else:
        """State 2"""
        pass
    """State 4"""
    return 0

def t316006000_x39():
    """State 0,3"""
    if not GetEventFlag(1044362701):
        """State 1,4"""
        # talk:31680000:"What's the meaning of this?"
        assert t316006000_x32(text2=31680000, z5=1044362701, mode4=1)
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t316006000_x40():
    """State 0,2"""
    if not GetEventFlag(1044369234):
        """State 3,5"""
        SetEventFlag(1044369234, 1)
        """State 6"""
        if GetEventFlag(1044369209) == 1:
            """State 7"""
            # talk:31680100:"How unfortunate."
            assert t316006000_x33(text1=31680100, mode3=1) and CheckSpecificPersonTalkHasEnded(0) == 1
        else:
            """State 8"""
            # talk:31680110:"How unfortunate."
            assert t316006000_x33(text1=31680110, mode3=1)
    else:
        """State 4"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 9"""
    return 0

def t316006000_x41():
    """State 0,1"""
    if not GetEventFlag(1044369209):
        """State 2"""
        def WhilePaused():
            RequestAnimation(90315, -1)
        assert t316006000_x42()
    elif not GetEventFlag(1044369229) and not GetEventFlag(1044369225):
        """State 3"""
        def WhilePaused():
            RequestAnimation(90315, -1)
        assert t316006000_x43()
    else:
        """State 4"""
        def WhilePaused():
            RequestAnimation(90315, -1)
        assert t316006000_x59()
    """State 5"""
    return 0

def t316006000_x42():
    """State 0,16"""
    if not GetEventFlag(1044369208):
        """State 1"""
        if not GetEventFlag(1044369207):
            """State 26"""
            # talk:31600100:"Tarnished, are we? A wonder you should turn up here."
            assert t316006000_x31(text3=31600100, mode5=1)
            """State 2"""
            SetEventFlag(1044369206, 1)
        else:
            """State 27"""
            # talk:31600500:"What is it now? Why are you here again?"
            assert t316006000_x31(text3=31600500, mode5=1)
    else:
        """State 33"""
        # talk:31600900:"Well? Have you made up your mind?"
        assert t316006000_x31(text3=31600900, mode5=1)
    """State 17,20"""
    if GetEventFlag(1044369208) == 1:
        """State 9"""
        Label('L0')
        ClearTalkListData()
        c1_110()
        """State 10"""
        # action:23161002:"I still want to learn"
        AddTalkListDataIf(not GetEventFlag(1044369208), 1, 23161002, -1)
        # action:23161010:"I still want to learn sorcery"
        AddTalkListDataIf(GetEventFlag(1044369208) == 1, 1, 23161010, -1)
        # action:23161003:"Let me reconsider"
        AddTalkListDataIf(not GetEventFlag(1044369208), 2, 23161003, -1)
        # action:23161011:"I need a bit more time to think"
        AddTalkListDataIf(GetEventFlag(1044369208) == 1, 2, 23161011, -1)
        """State 11"""
        OpenConversationChoicesMenu(0)
        """State 14"""
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 12"""
        if GetTalkListEntryResult() == 1:
            """State 32"""
            # talk:31600300:"Well, you are a piece of work."
            assert t316006000_x31(text3=31600300, mode5=1)
            """State 13"""
            SetEventFlag(1044369209, 1)
            """State 24"""
            if not GetEventFlag(60817):
                """State 23"""
                # gesture:30:Nod In Thought
                AcquireGesture(30)
                SetEventFlag(60817, 1)
            else:
                """State 25"""
                pass
            """State 35"""
            assert t316006000_x47()
        elif GetTalkListEntryResult() == 2:
            """State 30"""
            # talk:31600800:"Yes, I think that would be wise."
            assert t316006000_x31(text3=31600800, mode5=1)
            """State 21"""
            SetEventFlag(1044369208, 1)
        else:
            """State 22"""
            pass
    else:
        """State 3"""
        ClearTalkListData()
        c1_110()
        """State 4"""
        # action:23161000:"I want to learn sorcery"
        AddTalkListData(1, 23161000, -1)
        # action:23161001:"Never mind"
        AddTalkListData(2, 23161001, -1)
        """State 5"""
        OpenConversationChoicesMenu(0)
        """State 7"""
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 6"""
        if GetTalkListEntryResult() == 1:
            """State 15"""
            if ComparePlayerStat(5, 4, 15) == 1:
                """State 31"""
                # talk:31600200:"Ahh, a yen for glintstone sorceries?"
                assert t316006000_x31(text3=31600200, mode5=1)
                Goto('L0')
            else:
                """State 28"""
                # talk:31600700:"Ahh, a yen for glintstone sorceries?"
                assert t316006000_x31(text3=31600700, mode5=1)
                Goto('L0')
        elif GetTalkListEntryResult() == 2:
            """State 18"""
            if not GetEventFlag(1044369207):
                """State 29"""
                # talk:31600400:"Really."
                assert t316006000_x31(text3=31600400, mode5=1)
                """State 19"""
                SetEventFlag(1044369207, 1)
            else:
                """State 34"""
                # talk:31600600:"..."
                assert t316006000_x31(text3=31600600, mode5=1)
        else:
            """State 8"""
            pass
    """State 36"""
    return 0

def t316006000_x43():
    """State 0,1"""
    if not GetEventFlag(1044369210):
        """State 6"""
        # talk:31601000:"Young apprentice. First things first."
        assert t316006000_x31(text3=31601000, mode5=1)
        """State 2"""
        SetEventFlag(1044369210, 1)
        """State 3"""
        Label('L0')
        SetEventFlag(1044362705, 1)
    else:
        """State 4"""
        if not GetEventFlag(1044362705):
            """State 7"""
            # talk:31601100:"There you are, my apprentice."
            assert t316006000_x31(text3=31601100, mode5=1)
            Goto('L0')
        else:
            """State 8"""
            # talk:31601200:"You wish to continue the lesson?"
            assert t316006000_x31(text3=31601200, mode5=1)
    """State 5"""
    assert t316006000_x47()
    """State 9"""
    return 0

def t316006000_x44():
    """State 0,2"""
    # talk:31605000:"What's this sorcery, my apprentice?"
    assert t316006000_x31(text3=31605000, mode5=1)
    """State 1"""
    SetEventFlag(1044369224, 1)
    """State 3"""
    return 0

def t316006000_x45():
    """State 0,3"""
    # talk:31608000:"Who could've guessed. What a place to find Master Lusat..."
    assert t316006000_x31(text3=31608000, mode5=1)
    """State 2"""
    RequestAnimation(90200, -1)
    assert GetCurrentStateElapsedTime() > 1
    """State 1"""
    SetEventFlag(1044369228, 1)
    """State 5"""
    # lot:101030:Starlight Shards
    assert t316006000_x3(lot1=101030)
    """State 4"""
    # talk:31608100:"This brings us a full step closer."
    assert t316006000_x31(text3=31608100, mode5=1)
    """State 6"""
    return 0

def t316006000_x46():
    """State 0,2"""
    if not GetEventFlag(9130):
        """State 3"""
        # talk:31603100:"Well, well..."
        assert t316006000_x31(text3=31603100, mode5=1)
    else:
        """State 4"""
        # talk:31603110:"Well, well..."
        assert t316006000_x31(text3=31603110, mode5=1)
    """State 1"""
    SetEventFlag(1044369223, 1)
    """State 5"""
    return 0

def t316006000_x47():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        c1_110()
        """State 14"""
        assert t316006000_x50()
        """State 20"""
        assert t316006000_x61()
        """State 8"""
        if GetEventFlag(3465) == 1:
            """State 13"""
            assert t316006000_x48()
            """State 19"""
            assert t316006000_x62()
        else:
            """State 10"""
            pass
        """State 2"""
        # action:23160003:"Study sorcery"
        AddTalkListData(1, 23160003, -1)
        # action:23160007:"About the request"
        AddTalkListDataIf(GetEventFlag(1044369212) == 1, 50, 23160007, -1)
        # action:23160009:"Show letter of introduction"
        AddTalkListDataIf(GetEventFlag(1044369214) == 1, 50, 23160009, -1)
        # action:23160010:"Show Azur's sorcery"
        AddTalkListDataIf(GetEventFlag(1044369215) == 1, 50, 23160010, -1)
        # action:23160011:"Tell me your story"
        AddTalkListDataIf(GetEventFlag(1044369216) == 1, 50, 23160011, -1)
        # action:23160012:"I'll help restore the primeval current"
        AddTalkListDataIf(GetEventFlag(1044369217) == 1, 50, 23160012, -1)
        # action:23160013:"I have a favor to ask"
        AddTalkListDataIf(GetEventFlag(1044369218) == 1, 50, 23160013, -1)
        # action:23160014:"Lusat's location"
        AddTalkListDataIf(GetEventFlag(1044369219) == 1, 50, 23160014, -1)
        # action:23160015:"About glintstone sorcery"
        AddTalkListDataIf(GetEventFlag(1044369220) == 1, 50, 23160015, -1)
        # action:23160016:"Talk"
        AddTalkListDataIf(GetEventFlag(14009256) == 1, 50, 23160016, -1)
        # action:23160017:"Talk"
        AddTalkListDataIf(GetEventFlag(14009257) == 1, 50, 23160017, -1)
        # action:23160018:"About Lusat"
        AddTalkListDataIf(GetEventFlag(14009258) == 1, 50, 23160018, -1)
        # action:23160019:"Lusat's location"
        AddTalkListDataIf(GetEventFlag(14009259) == 1, 50, 23160019, -1)
        # action:23160008:"About the request"
        AddTalkListDataIf(GetEventFlag(1044369213) == 1, 60, 23160008, -1)
        # action:23160027:"Lead on Lusat"
        AddTalkListDataIf(GetEventFlag(1044369249) == 1, 61, 23160027, -1)
        # action:23160020:"Give a scroll"
        AddTalkListDataIf(GetEventFlag(1044369238) == 1, 70, 23160020, -1)
        # action:20000009:"Leave"
        AddTalkListData(99, 20000009, -1)
        """State 3"""
        ShowShopMessage(1)
        """State 4"""
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 6"""
            OpenRegularShop(100050, 100074)
            c1_141(5)
            """State 7"""
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            continue
        elif GetTalkListEntryResult() == 50:
            """State 15"""
            assert t316006000_x49()
        elif GetTalkListEntryResult() == 60:
            """State 16"""
            assert t316006000_x53()
        elif GetTalkListEntryResult() == 61:
            """State 18"""
            assert t316006000_x60()
        elif GetTalkListEntryResult() == 70:
            """State 11"""
            SetEventFlag(1044362707, 0)
            """State 21"""
            assert t316006000_x63()
            """State 12"""
            assert CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        else:
            """State 17"""
            assert t316006000_x58()
            """State 22"""
            return 0
        """State 9"""
        assert CheckSpecificPersonTalkHasEnded(0) == 1

def t316006000_x48():
    """State 0,8"""
    if GetEventFlag(1044369221) == 1 and not GetEventFlag(1044369222):
        """State 1"""
        SetEventFlag(1044369212, 1)
    # goods:8143:Seluvis's Introduction
    elif not GetEventFlag(1044369223) and ComparePlayerInventoryNumber(3, 8143, 4, 1, 0) == 1:
        """State 2"""
        SetEventFlag(1044369214, 1)
    # eventflag:400440:lot:104400:Comet Azur
    elif GetEventFlag(400440) == 1 and not GetEventFlag(1044369224):
        """State 3"""
        SetEventFlag(1044369215, 1)
    elif GetEventFlag(1044369224) == 1 and not GetEventFlag(1044369225) and not GetEventFlag(1044369226):
        """State 4"""
        SetEventFlag(1044369216, 1)
    elif not GetEventFlag(1044369225) and GetEventFlag(1044369226) == 1 and not GetEventFlag(1044369229):
        """State 5"""
        SetEventFlag(1044369217, 1)
    elif ((GetEventFlag(1044369225) == 1 and not GetEventFlag(1044369227)) or (GetEventFlag(1044369229)
          == 1 and not GetEventFlag(1044369227))):
        """State 6"""
        SetEventFlag(1044369218, 1)
    # eventflag:400430:lot:104300:Stars of Ruin
    elif GetEventFlag(1044369227) == 1 and GetEventFlag(400430) == 1 and not GetEventFlag(1044369228):
        """State 7"""
        SetEventFlag(1044369219, 1)
    elif not GetEventFlag(1044369230) and GetEventFlag(1044369237) == 1:
        """State 9"""
        SetEventFlag(1044369220, 1)
    else:
        """State 10"""
        pass
    """State 11"""
    if GetEventFlag(1044369222) == 1 and not GetEventFlag(1044369231):
        """State 12"""
        SetEventFlag(1044369213, 1)
    else:
        """State 13"""
        pass
    """State 14"""
    # eventflag:400430:lot:104300:Stars of Ruin
    if GetEventFlag(1044369227) == 1 and not GetEventFlag(400430):
        """State 15"""
        SetEventFlag(1044369249, 1)
    else:
        """State 16"""
        pass
    """State 17"""
    return 0

def t316006000_x49():
    """State 0,1"""
    if GetEventFlag(1044369211) == 1:
        """State 3"""
        assert t316006000_x51()
    elif GetEventFlag(1044369212) == 1:
        """State 4"""
        assert t316006000_x52()
    elif GetEventFlag(1044369214) == 1:
        """State 5"""
        assert t316006000_x46()
    elif GetEventFlag(1044369215) == 1:
        """State 6"""
        assert t316006000_x44()
    elif GetEventFlag(1044369216) == 1:
        """State 7"""
        assert t316006000_x54()
    elif GetEventFlag(1044369218) == 1:
        """State 10"""
        assert t316006000_x55()
    elif GetEventFlag(1044369219) == 1:
        """State 11"""
        assert t316006000_x45()
    elif GetEventFlag(1044369217) == 1:
        """State 8"""
        assert t316006000_x56()
    elif GetEventFlag(1044369220) == 1:
        """State 9"""
        assert t316006000_x57()
    else:
        """State 2"""
        pass
    """State 12"""
    return 0

def t316006000_x50():
    """State 0,1"""
    SetEventFlag(1044369211, 0)
    SetEventFlag(1044369212, 0)
    SetEventFlag(1044369213, 0)
    SetEventFlag(1044369214, 0)
    SetEventFlag(1044369215, 0)
    SetEventFlag(1044369216, 0)
    SetEventFlag(1044369218, 0)
    SetEventFlag(1044369219, 0)
    SetEventFlag(1044369217, 0)
    SetEventFlag(1044369220, 0)
    SetEventFlag(1044369249, 0)
    """State 2"""
    return 0

def t316006000_x51():
    """State 0,2"""
    # talk:31609000:"My apprentice. Give me a moment later."
    assert t316006000_x31(text3=31609000, mode5=1)
    """State 1"""
    SetEventFlag(1044369221, 1)
    """State 3"""
    return 0

def t316006000_x52():
    """State 0,1"""
    SetEventFlag(1044369222, 1)
    """State 2"""
    # talk:31609010:"The form you see before you is merely a projection."
    assert t316006000_x31(text3=31609010, mode5=1)
    """State 3"""
    return 0

def t316006000_x53():
    """State 0,1"""
    # talk:31609200:"My body is on the Weeping Peninsula, at the southern tip of the Lands Between,"
    assert t316006000_x31(text3=31609200, mode5=1)
    """State 2"""
    return 0

def t316006000_x54():
    """State 0,11"""
    # talk:31606000:"If you recall, I was exiled from the Academy of Raya Lucaria."
    assert t316006000_x31(text3=31606000, mode5=1)
    """State 2"""
    ClearTalkListData()
    c1_110()
    """State 3"""
    # action:23161006:"Let us journey together"
    AddTalkListData(1, 23161006, -1)
    # action:23161007:"Let me think about it"
    AddTalkListData(2, 23161007, -1)
    """State 4"""
    OpenConversationChoicesMenu(0)
    """State 5"""
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 6"""
    if GetTalkListEntryResult() == 1:
        """State 9"""
        # talk:31606100:"Splendid. I thank you."
        assert t316006000_x31(text3=31606100, mode5=1)
        """State 1"""
        SetEventFlag(1044369225, 1)
    elif GetTalkListEntryResult() == 2:
        """State 10"""
        # talk:31606200:"Forgive me, it was an outlandish idea to begin with."
        assert t316006000_x31(text3=31606200, mode5=1)
        """State 7"""
        SetEventFlag(1044369226, 1)
    else:
        """State 8"""
        pass
    """State 12"""
    return 0

def t316006000_x55():
    """State 0,2"""
    # talk:31607000:"I need your help, my apprentice."
    assert t316006000_x31(text3=31607000, mode5=1)
    """State 1"""
    SetEventFlag(1044369227, 1)
    """State 4"""
    # lot:101020:Sellian Sealbreaker
    assert t316006000_x3(lot1=101020)
    """State 3"""
    # talk:31607100:"I need him to restore the primeval current of glintstone sorcery."
    assert t316006000_x31(text3=31607100, mode5=1)
    """State 5"""
    return 0

def t316006000_x56():
    """State 0,2"""
    # talk:31606300:"Really? My apprentice."
    assert t316006000_x31(text3=31606300, mode5=1)
    """State 1"""
    SetEventFlag(1044369229, 1)
    """State 3"""
    return 0

def t316006000_x57():
    """State 0,2"""
    # talk:31602000:"Our art draws upon the powers embedded in glintstone."
    assert t316006000_x31(text3=31602000, mode5=1)
    """State 1"""
    SetEventFlag(1044369230, 1)
    """State 3"""
    return 0

def t316006000_x58():
    """State 0,1"""
    if GetEventFlag(1044369235) == 1 and not GetEventFlag(1044369236):
        """State 2"""
        # talk:31602100:"Your appetite for learning is impressive."
        assert t316006000_x30(text4=31602100, z6=1044369236, mode6=1)
    else:
        pass
    """State 3"""
    return 0

def t316006000_x59():
    """State 0,3"""
    if (GetEventFlag(1044369227) == 1 and GetEventFlag(9130) == 1 and not GetEventFlag(1044362705) and
        not GetEventFlag(1044369222)):
        """State 8"""
        # talk:31609000:"My apprentice. Give me a moment later."
        assert t316006000_x31(text3=31609000, mode5=1)
        """State 4"""
        SetEventFlag(1044369221, 1)
        """State 2"""
        Label('L0')
        SetEventFlag(1044362705, 1)
    else:
        """State 1"""
        if not GetEventFlag(1044362705):
            """State 6"""
            # talk:31606400:"There you are, my apprentice."
            assert t316006000_x31(text3=31606400, mode5=1)
            Goto('L0')
        else:
            """State 7"""
            # talk:31606500:"You wish to resume the lesson?"
            assert t316006000_x31(text3=31606500, mode5=1)
    """State 5"""
    assert t316006000_x47()
    """State 9"""
    return 0

def t316006000_x60():
    """State 0,1"""
    # talk:31607200:"After his expulsion from the academy, I heard that Master Lusat returned to his home."
    assert t316006000_x31(text3=31607200, mode5=1)
    """State 2"""
    return 0

def t316006000_x61():
    """State 0,1"""
    SetEventFlag(1044369238, 0)
    SetEventFlag(1044369239, 0)
    SetEventFlag(1044369240, 0)
    SetEventFlag(1044369243, 0)
    """State 2"""
    return 0

def t316006000_x62():
    """State 0"""
    while True:
        """State 1"""
        # goods:8850:Conspectus Scroll
        if (ComparePlayerInventoryNumber(3, 8850, 4, 1, 0) == 1 and not GetEventFlag(1044369239) and
            not GetEventFlag(1044369244)):
            """State 2"""
            SetEventFlag(1044369239, 1)
        # goods:8866:Academy Scroll
        elif (ComparePlayerInventoryNumber(3, 8866, 4, 1, 0) == 1 and not GetEventFlag(1044369243) and
              not GetEventFlag(1044369250)):
            """State 6"""
            SetEventFlag(1044369243, 1)
        # goods:8851:Royal House Scroll
        elif (ComparePlayerInventoryNumber(3, 8851, 4, 1, 0) == 1 and not GetEventFlag(1044369240) and
              not GetEventFlag(1044369245)):
            """State 3"""
            SetEventFlag(1044369240, 1)
        else:
            """State 5,7"""
            return 0
        """State 4"""
        SetEventFlag(1044369238, 1)

def t316006000_x63():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        c1_110()
        """State 16"""
        assert t316006000_x50()
        """State 15"""
        assert t316006000_x61()
        """State 17"""
        assert t316006000_x62()
        """State 8"""
        if GetEventFlag(1044369238) == 1:
            """State 2"""
            # action:23160021:"Give the Conspectus Scroll"
            AddTalkListDataIf(GetEventFlag(1044369239) == 1, 1, 23160021, -1)
            # action:23160028:"Give the Academy Scroll"
            AddTalkListDataIf(GetEventFlag(1044369243) == 1, 2, 23160028, -1)
            # action:23160022:"Give the Royal House Scroll"
            AddTalkListDataIf(GetEventFlag(1044369240) == 1, 3, 23160022, -1)
            # action:23160026:"Don't give a scroll"
            AddTalkListData(99, 23160026, -1)
            """State 3"""
            ShowShopMessage(1)
            assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 6"""
            if GetTalkListEntryResult() == 1:
                """State 10"""
                # goods:8850:Conspectus Scroll
                PlayerEquipmentQuantityChange(3, 8850, -1)
                """State 11"""
                SetEventFlag(1044369244, 1)
            elif GetTalkListEntryResult() == 2:
                """State 13"""
                # goods:8866:Academy Scroll
                PlayerEquipmentQuantityChange(3, 8866, -1)
                """State 12"""
                SetEventFlag(1044369250, 1)
            elif GetTalkListEntryResult() == 3:
                """State 4"""
                # goods:8851:Royal House Scroll
                PlayerEquipmentQuantityChange(3, 8851, -1)
                """State 5"""
                SetEventFlag(1044369245, 1)
            else:
                """State 7"""
                Goto('L0')
            """State 9,14"""
            # talk:31615000:"Oh, is that a scroll? Takes me back to my academy days."
            assert t316006000_x31(text3=31615000, mode5=1) and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        else:
            pass
        """State 18"""
        Label('L0')
        return 0

