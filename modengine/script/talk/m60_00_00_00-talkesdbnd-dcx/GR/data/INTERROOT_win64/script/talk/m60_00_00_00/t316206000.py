# -*- coding: utf-8 -*-
def t316206000_1():
    """State 0,1"""
    assert GetEventFlag(3466) == 1
    """State 2"""
    # actionbutton:6000:"Talk"
    t316206000_x6(flag1=3463, flag2=3461, flag3=3462, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t316206000_1000():
    """State 0,2,3"""
    assert t316206000_x37()
    """State 1"""
    c1_120(1000)
    Quit()

def t316206000_1001():
    """State 0,2,3"""
    assert t316206000_x38()
    """State 1"""
    c1_120(1001)
    Quit()

def t316206000_1101():
    """State 0,2,3"""
    assert t316206000_x39()
    """State 1"""
    c1_120(1101)
    Quit()

def t316206000_1102():
    """State 0,2,3"""
    t316206000_x40()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t316206000_1103():
    """State 0,2,3"""
    assert t316206000_x41()
    """State 1"""
    c1_120(1103)
    Quit()

def t316206000_2000():
    """State 0,2,3"""
    assert t316206000_x42()
    """State 1"""
    c1_120(2000)
    Quit()

def t316206000_x0(actionbutton1=_, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag4=6000):
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

def t316206000_x1():
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

def t316206000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t316206000_x3(lot1=_):
    """State 0,1"""
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t316206000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t316206000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t316206000_x1()
    else:
        """State 4,7"""
        call = t316206000_x34()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t316206000_x1()
    """State 9"""
    return 0

def t316206000_x5():
    """State 0,1"""
    assert t316206000_x1()
    """State 2"""
    return 0

def t316206000_x6(flag1=3463, flag2=3461, flag3=3462, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t316206000_x23(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t316206000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t316206000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t316206000_x10(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t316206000_x14(val1=val1, z1=z1)
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
            call = t316206000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t316206000_x27() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t316206000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t316206000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t316206000_x18(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t316206000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t316206000_x9(flag1=3463, val2=10, val3=12):
    """State 0,8"""
    assert t316206000_x36()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t316206000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t316206000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t316206000_x10(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t316206000_x11(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t316206000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t316206000_x11(z6=_, val6=_):
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

def t316206000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t316206000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t316206000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t316206000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t316206000_x13():
    """State 0,1"""
    assert t316206000_x11(z6=1101, val6=1101)
    """State 2"""
    return 0

def t316206000_x14(val1=5, z1=1):
    """State 0,2"""
    assert t316206000_x24()
    """State 1"""
    call = t316206000_x15()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t316206000_x26()
    """State 4"""
    return 0

def t316206000_x15():
    """State 0,1"""
    assert t316206000_x11(z6=1000, val6=1000)
    """State 2"""
    return 0

def t316206000_x16(val5=12):
    """State 0,1"""
    call = t316206000_x17()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t316206000_x27()
    """State 3"""
    return 0

def t316206000_x17():
    """State 0,1"""
    assert t316206000_x11(z6=1100, val6=1100)
    """State 2"""
    return 0

def t316206000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t316206000_x36()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t316206000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t316206000_x29()
    """Unused"""
    """State 6"""
    return 0

def t316206000_x19():
    """State 0,2"""
    call = t316206000_x11(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t316206000_x20():
    """State 0,1"""
    assert t316206000_x11(z6=1001, val6=1001)
    """State 2"""
    return 0

def t316206000_x21():
    """State 0,1"""
    assert t316206000_x11(z6=1103, val6=1103)
    """State 2"""
    return 0

def t316206000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t316206000_x23(flag1=3463, flag2=3461, flag3=3462, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t316206000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t316206000_x9(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t316206000_x8(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t316206000_x35() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t316206000_x24():
    """State 0,1"""
    assert t316206000_x25()
    """State 2"""
    return 0

def t316206000_x25():
    """State 0,1"""
    assert t316206000_x11(z6=1104, val6=1104)
    """State 2"""
    return 0

def t316206000_x26():
    """State 0,1"""
    call = t316206000_x11(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t316206000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t316206000_x27():
    """State 0,1"""
    call = t316206000_x11(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t316206000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t316206000_x28():
    """State 0,1"""
    call = t316206000_x11(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t316206000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t316206000_x29():
    """State 0,1"""
    call = t316206000_x11(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t316206000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t316206000_x30(text3=_, mode5=1):
    """State 0,4"""
    assert t316206000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t316206000_x31(text2=_, z5=_, mode4=1):
    """State 0,5"""
    assert t316206000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t316206000_x32(text1=_, mode3=1):
    """State 0,4"""
    assert t316206000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t316206000_x33():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t316206000_x34():
    """State 0,1"""
    assert t316206000_x11(z6=1002, val6=1002)
    """State 2"""
    return 0

def t316206000_x35():
    """State 0,1"""
    assert t316206000_x1()
    """State 2"""
    return 0

def t316206000_x36():
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

def t316206000_x37():
    """State 0,1"""
    if GetEventFlag(3466) == 1:
        """State 4"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t316206000_x43()
    elif GetEventFlag(3468) == 1:
        """State 3"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t316206000_x44()
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t316206000_x38():
    """State 0,1"""
    # talk:31680900:"For a time, I believed us kindred spirits."
    assert t316206000_x32(text1=31680900, mode3=1)
    """State 2"""
    return 0

def t316206000_x39():
    """State 0,3"""
    if not GetEventFlag(14002711):
        """State 1,5"""
        # talk:31680500:"Agh!"
        assert t316206000_x31(text2=31680500, z5=14002711, mode4=1)
    elif not GetEventFlag(14002712):
        """State 4,6"""
        # talk:31680600:"Why, you. Are you mad?"
        assert t316206000_x31(text2=31680600, z5=14002712, mode4=1)
    else:
        """State 2"""
        pass
    """State 7"""
    return 0

def t316206000_x40():
    """State 0,2"""
    if not GetEventFlag(1034509253):
        """State 3,5"""
        SetEventFlag(1034509253, 1)
        """State 6"""
        # talk:31680700:"You sadden me, my apprentice."
        assert t316206000_x32(text1=31680700, mode3=1)
    else:
        """State 4"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 7"""
    return 0

def t316206000_x41():
    """State 0,1"""
    # talk:31680800:"Ahh, how can this be..."
    assert t316206000_x32(text1=31680800, mode3=1)
    """State 2"""
    return 0

def t316206000_x42():
    """State 0,1"""
    if GetEventFlag(3466) == 1:
        """State 3"""
        assert t316206000_x53()
    else:
        """State 2"""
        # actionbutton:6000:"Talk"
        assert (t316206000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                flag4=6000))
    """State 4"""
    return 0

def t316206000_x43():
    """State 0,1"""
    assert t316206000_x47()
    """State 2"""
    return 0

def t316206000_x44():
    """State 0,1"""
    assert t316206000_x48()
    """State 2"""
    return 0

def t316206000_x45():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        c1_110()
        """State 14"""
        assert t316206000_x46()
        """State 19"""
        assert t316206000_x54()
        """State 9"""
        if GetEventFlag(3468) == 1:
            """State 15"""
            assert t316206000_x49()
        else:
            """State 11"""
            pass
        """State 20"""
        assert t316206000_x58()
        """State 18"""
        assert t316206000_x55()
        """State 2"""
        # action:23160003:"Study sorcery"
        AddTalkListData(1, 23160003, -1)
        # action:23160009:"Show letter of introduction"
        AddTalkListDataIf(GetEventFlag(1044369214) == 1, 25, 23160009, -1)
        # action:23160018:"About Lusat"
        AddTalkListDataIf(GetEventFlag(14009258) == 1, 50, 23160018, -1)
        # action:23160019:"Lusat's location"
        AddTalkListDataIf(GetEventFlag(14009259) == 1, 50, 23160019, -1)
        # action:23160020:"Give a scroll"
        AddTalkListDataIf(GetEventFlag(1044369238) == 1, 60, 23160020, -1)
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
            """State 8"""
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 25:
            """State 21"""
            assert t316206000_x57()
            """State 13"""
            assert CheckSpecificPersonTalkHasEnded(0) == 1
        elif GetTalkListEntryResult() == 50:
            """State 16"""
            assert t316206000_x50()
            """State 10"""
            assert CheckSpecificPersonTalkHasEnded(0) == 1
        elif GetTalkListEntryResult() == 60:
            """State 12"""
            SetEventFlag(1044362707, 0)
            """State 17"""
            assert t316206000_x56()
        else:
            """State 7,22"""
            return 0

def t316206000_x46():
    """State 0,1"""
    SetEventFlag(14009256, 0)
    SetEventFlag(14009257, 0)
    SetEventFlag(14009258, 0)
    SetEventFlag(14009259, 0)
    SetEventFlag(1044369214, 0)
    """State 2"""
    return 0

def t316206000_x47():
    """State 0,4"""
    if not GetEventFlag(1034509257):
        """State 1"""
        if not GetEventFlag(1034509255):
            """State 8"""
            # talk:31611000:"My apprentice, just how long has it been?"
            assert t316206000_x30(text3=31611000, mode5=1)
            """State 2"""
            SetEventFlag(1034509255, 1)
            """State 7"""
            SetEventFlag(1034509259, 1)
        else:
            """State 9"""
            # talk:31611100:"Finally, I can return to the academy."
            assert t316206000_x30(text3=31611100, mode5=1)
            """State 3"""
            SetEventFlag(1034509257, 1)
    else:
        """State 5"""
        if not GetEventFlag(1044362705):
            """State 12"""
            # talk:31611200:"My apprentice, shall we commence the lesson?"
            assert t316206000_x30(text3=31611200, mode5=1)
            """State 6"""
            SetEventFlag(1044362705, 1)
        else:
            """State 11"""
            # talk:31611300:"You wish to resume the lesson?"
            assert t316206000_x30(text3=31611300, mode5=1)
        """State 10"""
        assert t316206000_x45()
    """State 13"""
    return 0

def t316206000_x48():
    """State 0,2"""
    if not GetEventFlag(14009255):
        """State 1"""
        if not GetEventFlag(1044369228):
            """State 11"""
            # talk:31612400:"Ahh, my apprentice."
            assert t316206000_x30(text3=31612400, mode5=1)
        else:
            """State 12"""
            # talk:31612000:"Ahh, my apprentice."
            assert t316206000_x30(text3=31612000, mode5=1)
        """State 4"""
        SetEventFlag(14009255, 1)
    elif not GetEventFlag(14009266):
        """State 17"""
        # talk:31612100:"Hmm, perhaps I'm jumping ahead,"
        assert t316206000_x30(text3=31612100, mode5=1)
        """State 9"""
        SetEventFlag(14009266, 1)
        """State 19"""
        # lot:101010:Glintstone Kris
        assert t316206000_x3(lot1=101010) and not IsMenuOpen(63)
        """State 18"""
        # talk:31612200:"Do you recall what once I told you?"
        assert t316206000_x30(text3=31612200, mode5=1)
    elif not GetEventFlag(14009265):
        """State 20"""
        # talk:31612300:"Oh, one last thing."
        assert t316206000_x30(text3=31612300, mode5=1)
        """State 10"""
        SetEventFlag(14009265, 1)
        """State 14"""
        Label('L0')
        assert t316206000_x45()
    else:
        """State 6"""
        if not GetEventFlag(14009264) or GetEventFlag(1044362706) == 1:
            """State 15"""
            # talk:31612500:"What is it? My apprentice."
            assert t316206000_x30(text3=31612500, mode5=1)
            """State 5"""
            SetEventFlag(14009264, 1)
            """State 8"""
            SetEventFlag(1044362706, 1)
            Goto('L0')
        else:
            """State 7"""
            if not GetEventFlag(1044362705):
                """State 16"""
                # talk:31612600:"Ahh, I am glad to see you. My apprentice."
                assert t316206000_x30(text3=31612600, mode5=1)
            else:
                """State 13"""
                # talk:31612900:"You wish to resume the lesson?"
                assert t316206000_x30(text3=31612900, mode5=1)
            """State 3"""
            SetEventFlag(1044362705, 1)
            Goto('L0')
    """State 21"""
    return 0

def t316206000_x49():
    """State 0,3"""
    if not GetEventFlag(1044369228) and not GetEventFlag(14009262):
        """State 1"""
        SetEventFlag(14009258, 1)
    # eventflag:400430:lot:104300:Stars of Ruin
    elif GetEventFlag(14009262) == 1 and GetEventFlag(400430) == 1 and not GetEventFlag(14009263):
        """State 2"""
        SetEventFlag(14009259, 1)
    else:
        """State 4"""
        pass
    """State 5"""
    return 0

def t316206000_x50():
    """State 0,1"""
    if GetEventFlag(14009258) == 1:
        """State 3"""
        assert t316206000_x51()
    elif GetEventFlag(14009259) == 1:
        """State 4"""
        assert t316206000_x52()
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t316206000_x51():
    """State 0,2"""
    # talk:31612700:"It warms my heart. That you still think of me."
    assert t316206000_x30(text3=31612700, mode5=1)
    """State 1"""
    SetEventFlag(14009262, 1)
    """State 3"""
    return 0

def t316206000_x52():
    """State 0,2"""
    # talk:31612800:"Who could've guessed. What a place to find Master Lusat..."
    assert t316206000_x30(text3=31612800, mode5=1)
    """State 1"""
    SetEventFlag(14009263, 1)
    """State 3"""
    # lot:101030:Starlight Shards
    assert t316206000_x3(lot1=101030)
    """State 4"""
    return 0

def t316206000_x53():
    """State 0,6"""
    # actionbutton:6000:"Talk"
    call = t316206000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                         flag4=6000)
    if call.Done():
        pass
    elif not GetEventFlag(1034509256):
        """State 7"""
        # actionbutton:6292:"Transplant primal glintstone"
        assert (t316206000_x0(actionbutton1=6292, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                flag4=6000))
        """State 2"""
        SetEventFlag(1034509258, 0)
        """State 1"""
        def WhilePaused():
            RequestAnimation(90203, -1)
        """State 4"""
        # goods:8144:Sellen's Primal Glintstone
        PlayerEquipmentQuantityChange(3, 8144, -1)
        """State 3"""
        SetEventFlag(1034509256, 1)
        """State 5"""
        SetEventFlag(1034509254, 0)
        assert GetCurrentStateElapsedTime() > 7
    """State 8"""
    return 0

def t316206000_x54():
    """State 0,1"""
    SetEventFlag(1044369238, 0)
    SetEventFlag(1044369239, 0)
    SetEventFlag(1044369240, 0)
    SetEventFlag(1044369243, 0)
    """State 2"""
    return 0

def t316206000_x55():
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

def t316206000_x56():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        c1_110()
        """State 15"""
        assert t316206000_x46()
        """State 16"""
        assert t316206000_x54()
        """State 17"""
        assert t316206000_x55()
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
            assert t316206000_x30(text3=31615000, mode5=1) and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        else:
            pass
        """State 18"""
        Label('L0')
        return 0

def t316206000_x57():
    """State 0,2"""
    # talk:31603110:"Well, well..."
    assert t316206000_x30(text3=31603110, mode5=1)
    """State 1"""
    SetEventFlag(1044369223, 1)
    """State 3"""
    return 0

def t316206000_x58():
    """State 0,2"""
    # goods:8143:Seluvis's Introduction
    if not GetEventFlag(1044369223) and ComparePlayerInventoryNumber(3, 8143, 4, 1, 0) == 1:
        """State 1"""
        SetEventFlag(1044369214, 1)
    else:
        """State 3"""
        pass
    """State 4"""
    return 0

