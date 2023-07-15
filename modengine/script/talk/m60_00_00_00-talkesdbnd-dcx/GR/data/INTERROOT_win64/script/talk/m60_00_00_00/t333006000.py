# -*- coding: utf-8 -*-
def t333006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t333006000_x6(flag1=3803, flag2=3801, flag3=3802, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    def WhilePaused():
        c1_121(9620)
    Quit()

def t333006000_1000():
    """State 0,2,3"""
    assert t333006000_x37()
    """State 1"""
    c1_120(1000)
    Quit()

def t333006000_1001():
    """State 0,2,3"""
    assert t333006000_x38()
    """State 1"""
    c1_120(1001)
    Quit()

def t333006000_1101():
    """State 0,2,3"""
    assert t333006000_x39()
    """State 1"""
    c1_120(1101)
    Quit()

def t333006000_1102():
    """State 0,2,3"""
    t333006000_x40()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t333006000_1103():
    """State 0,2,3"""
    assert t333006000_x41()
    """State 1"""
    c1_120(1103)
    Quit()

def t333006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t333006000_x1():
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

def t333006000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t333006000_x3(action1=23331003):
    """State 0,1"""
    # action:23331003:"Not enough runes to donate"
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t333006000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t333006000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t333006000_x1()
    else:
        """State 4,7"""
        call = t333006000_x34()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t333006000_x1()
    """State 9"""
    return 0

def t333006000_x5():
    """State 0,1"""
    assert t333006000_x1()
    """State 2"""
    return 0

def t333006000_x6(flag1=3803, flag2=3801, flag3=3802, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t333006000_x23(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t333006000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t333006000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t333006000_x10(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t333006000_x14(val1=val1, z1=z1)
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
            call = t333006000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t333006000_x27() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t333006000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t333006000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t333006000_x18(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t333006000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t333006000_x9(flag1=3803, val2=10, val3=12):
    """State 0,8"""
    assert t333006000_x36()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t333006000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t333006000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t333006000_x10(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t333006000_x11(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t333006000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t333006000_x11(z6=_, val6=_):
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

def t333006000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t333006000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t333006000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t333006000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t333006000_x13():
    """State 0,1"""
    assert t333006000_x11(z6=1101, val6=1101)
    """State 2"""
    return 0

def t333006000_x14(val1=5, z1=1):
    """State 0,2"""
    assert t333006000_x24()
    """State 1"""
    call = t333006000_x15()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t333006000_x26()
    """State 4"""
    return 0

def t333006000_x15():
    """State 0,1"""
    assert t333006000_x11(z6=1000, val6=1000)
    """State 2"""
    return 0

def t333006000_x16(val5=12):
    """State 0,1"""
    call = t333006000_x17()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t333006000_x27()
    """State 3"""
    return 0

def t333006000_x17():
    """State 0,1"""
    assert t333006000_x11(z6=1100, val6=1100)
    """State 2"""
    return 0

def t333006000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t333006000_x36()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t333006000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t333006000_x29()
    """Unused"""
    """State 6"""
    return 0

def t333006000_x19():
    """State 0,2"""
    call = t333006000_x11(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t333006000_x20():
    """State 0,1"""
    assert t333006000_x11(z6=1001, val6=1001)
    """State 2"""
    return 0

def t333006000_x21():
    """State 0,1"""
    assert t333006000_x11(z6=1103, val6=1103)
    """State 2"""
    return 0

def t333006000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t333006000_x23(flag1=3803, flag2=3801, flag3=3802, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t333006000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t333006000_x9(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t333006000_x8(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t333006000_x35() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t333006000_x24():
    """State 0,1"""
    assert t333006000_x25()
    """State 2"""
    return 0

def t333006000_x25():
    """State 0,1"""
    assert t333006000_x11(z6=1104, val6=1104)
    """State 2"""
    return 0

def t333006000_x26():
    """State 0,1"""
    call = t333006000_x11(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t333006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t333006000_x27():
    """State 0,1"""
    call = t333006000_x11(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t333006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t333006000_x28():
    """State 0,1"""
    call = t333006000_x11(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t333006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t333006000_x29():
    """State 0,1"""
    call = t333006000_x11(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t333006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t333006000_x30(text3=_, mode5=1):
    """State 0,4"""
    assert t333006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t333006000_x31(text2=_, z5=_, mode4=1):
    """State 0,5"""
    assert t333006000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t333006000_x32(text1=_, mode3=1):
    """State 0,4"""
    assert t333006000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t333006000_x33():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t333006000_x34():
    """State 0,1"""
    assert t333006000_x11(z6=1002, val6=1002)
    """State 2"""
    return 0

def t333006000_x35():
    """State 0,1"""
    assert t333006000_x1()
    """State 2"""
    return 0

def t333006000_x36():
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

def t333006000_x37():
    """State 0,1"""
    if GetEventFlag(3805) == 1:
        """State 4"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t333006000_x42()
    elif GetEventFlag(3806) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        pass
    """State 5"""
    return 0

def t333006000_x38():
    """State 0,1"""
    # talk:33380300:"..."
    assert t333006000_x32(text1=33380300, mode3=1)
    """State 2"""
    return 0

def t333006000_x39():
    """State 0,1"""
    if not GetEventFlag(1039392701):
        """State 3"""
        # talk:33380000:"Ow!"
        assert t333006000_x31(text2=33380000, z5=1039392701, mode4=1)
    elif not GetEventFlag(1039392703):
        """State 4"""
        # talk:33380100:"What's wrong with you?"
        assert t333006000_x31(text2=33380100, z5=1039392703, mode4=1)
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t333006000_x40():
    """State 0,2"""
    if not GetEventFlag(1039399203):
        """State 3,5"""
        # talk:33380200:"There's no getting through to you, is there."
        assert t333006000_x31(text2=33380200, z5=1039399203, mode4=1)
    else:
        """State 4"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 6"""
    return 0

def t333006000_x41():
    """State 0,1"""
    # talk:33380400:"Oh, Raya... Lucaria..."
    assert t333006000_x32(text1=33380400, mode3=1)
    """State 2"""
    return 0

def t333006000_x42():
    """State 0,2"""
    SetEventFlag(1039392704, 0)
    """State 1"""
    if not GetEventFlag(1039399206):
        """State 3"""
        assert t333006000_x43()
    else:
        """State 4"""
        assert t333006000_x44()
    """State 5"""
    return 0

def t333006000_x43():
    """State 0,1"""
    if not GetEventFlag(1039399205):
        """State 15"""
        # talk:33300100:"You're Tarnished, aren't you?"
        assert t333006000_x30(text3=33300100, mode5=1)
    else:
        """State 16"""
        # talk:33300600:"Oh, there you are."
        assert t333006000_x30(text3=33300600, mode5=1)
    """State 2"""
    ClearTalkListData()
    c1_110()
    """State 14"""
    SetMessageTagValue(0, 10)
    """State 3"""
    # action:23331000:"Donate <?evntAcquittalPrice?> runes"
    AddTalkListData(1, 23331000, -1)
    # action:23331001:"Don't donate runes"
    AddTalkListData(2, 23331001, -1)
    """State 4"""
    OpenConversationChoicesMenu(0)
    """State 5"""
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 6"""
    if GetTalkListEntryResult() == 1:
        """State 12"""
        if ComparePlayerStat(8, 4, 10) == 1:
            """State 17"""
            # talk:33300200:"Well, bless you, bless you."
            assert t333006000_x30(text3=33300200, mode5=1)
            """State 11"""
            SetEventFlag(1039399205, 1)
            """State 7"""
            SetEventFlag(1039399206, 1)
            """State 8"""
            SetEventFlag(1039392702, 1)
            """State 10"""
            ChangePlayerStat(8, 1, 10)
            """State 19"""
            assert t333006000_x52()
        else:
            """State 20"""
            # action:23331003:"Not enough runes to donate"
            assert t333006000_x3(action1=23331003)
            """State 13"""
            Label('L0')
            SetEventFlag(1039399205, 1)
    elif GetTalkListEntryResult() == 2:
        """State 18"""
        # talk:33300500:"Well, I can't blame you, I suppose."
        assert t333006000_x30(text3=33300500, mode5=1)
        Goto('L0')
    else:
        """State 9"""
        pass
    """State 21"""
    return 0

def t333006000_x44():
    """State 0,1"""
    if not GetEventFlag(1039399207) and not GetEventFlag(1039392702):
        """State 5"""
        # talk:33300300:"Back to learn another?"
        assert t333006000_x30(text3=33300300, mode5=1)
        """State 2"""
        SetEventFlag(1039399207, 1)
        """State 3"""
        SetEventFlag(1039392702, 1)
    else:
        """State 6"""
        # talk:33300400:"Back to learn another?"
        assert t333006000_x30(text3=33300400, mode5=1)
    """State 4"""
    assert t333006000_x52()
    """State 7"""
    return 0

def t333006000_x45():
    """State 0,1"""
    if GetEventFlag(1039399218) == 1 and not GetEventFlag(1039399213):
        """State 2"""
        SetEventFlag(1039399208, 1)
    elif not GetEventFlag(1039399214):
        """State 3"""
        SetEventFlag(1039399209, 1)
    elif GetEventFlag(1044369209) == 1 and not GetEventFlag(1039399221):
        """State 10"""
        SetEventFlag(1039399223, 1)
    else:
        """State 6"""
        pass
    """State 7"""
    # goods:8174:Academy Glintstone Key
    if (GetEventFlag(1039399215) == 1 and ComparePlayerInventoryNumber(3, 8174, 0, 1, 0) == 1 and not
        GetEventFlag(1039399220)):
        """State 9"""
        SetEventFlag(1039399211, 1)
    # goods:8109:Academy Glintstone Key
    elif (GetEventFlag(1039399215) == 1 and ComparePlayerInventoryNumber(3, 8109, 0, 1, 0) == 1 and not
          GetEventFlag(1039399216) and not GetEventFlag(1039399220)):
        """State 4"""
        SetEventFlag(1039399211, 1)
    elif GetEventFlag(1039399214) == 1 and not GetEventFlag(1039399211):
        """State 5"""
        SetEventFlag(1039399210, 1)
    else:
        """State 8"""
        pass
    """State 11"""
    if not GetEventFlag(1039399225) and GetEventFlag(1039399213) == 1:
        """State 14"""
        # goods:8850:Conspectus Scroll, goods:8851:Royal House Scroll
        if (ComparePlayerInventoryNumber(3, 8850, 4, 1, 0) == 1 or ComparePlayerInventoryNumber(3, 8851,
            4, 1, 0) == 1):
            """State 13"""
            SetEventFlag(1039399226, 1)
        else:
            """State 12"""
            Label('L0')
    else:
        Goto('L0')
    """State 15"""
    return 0

def t333006000_x46():
    """State 0,2"""
    # talk:33302300:"Thank you, kind soul."
    assert t333006000_x30(text3=33302300, mode5=1)
    """State 1"""
    SetEventFlag(1039399213, 1)
    """State 3"""
    return 0

def t333006000_x47():
    """State 0,1"""
    if GetEventFlag(1039399208) == 1:
        """State 3"""
        assert t333006000_x46()
    elif GetEventFlag(1039399209) == 1:
        """State 4"""
        assert t333006000_x48()
    elif GetEventFlag(1039399223) == 1:
        """State 5"""
        assert t333006000_x53()
    else:
        """State 2"""
        pass
    """State 6"""
    return 0

def t333006000_x48():
    """State 0,2"""
    # talk:33302000:"Apologies, friend."
    assert t333006000_x30(text3=33302000, mode5=1)
    """State 1"""
    SetEventFlag(1039399214, 1)
    """State 3"""
    return 0

def t333006000_x49():
    """State 0,2"""
    if not GetEventFlag(1039399215):
        """State 4"""
        # talk:33302100:"Why not find yourself a glintstone key?"
        assert t333006000_x30(text3=33302100, mode5=1)
        """State 1"""
        SetEventFlag(1039399215, 1)
    elif not GetEventFlag(1039399216) and not GetEventFlag(1039399220):
        """State 5"""
        # talk:33302600:"Find yourself a glintstone key."
        assert t333006000_x30(text3=33302600, mode5=1)
    else:
        """State 3"""
        if not GetEventFlag(1039399220) and GetEventFlag(1039399216) == 1:
            """State 8"""
            # talk:33304100:"Head to the Academy of Raya Lucaria."
            assert t333006000_x30(text3=33304100, mode5=1)
        else:
            """State 9"""
            # talk:33305100:"Thank you dearly."
            assert t333006000_x30(text3=33305100, mode5=1)
    """State 10"""
    return 0
    """Unused"""
    """State 6"""
    # talk:33302600:"Find yourself a glintstone key."
    t333006000_x30(text3=33302600, mode5=1)
    Quit()
    """State 7"""
    # talk:33302100:"Why not find yourself a glintstone key?"
    t333006000_x30(text3=33302100, mode5=1)
    Quit()

def t333006000_x50():
    """State 0,3"""
    # goods:8109:Academy Glintstone Key, goods:8174:Academy Glintstone Key
    if (ComparePlayerInventoryNumber(3, 8109, 0, 1, 0) == 1 and ComparePlayerInventoryNumber(3, 8174,
        0, 0, 0) == 1):
        pass
    else:
        Goto('L0')
    """State 10"""
    # talk:33304000:"So, you've found yourself a glintstone key."
    assert t333006000_x30(text3=33304000, mode5=1)
    """State 4"""
    SetEventFlag(1039399216, 1)
    """State 11"""
    return 0
    """State 8"""
    Label('L0')
    SetEventFlag(1039392704, 1)
    """State 9"""
    # talk:33302400:"Are you certain?"
    assert t333006000_x30(text3=33302400, mode5=1)
    """State 2"""
    # goods:8174:Academy Glintstone Key
    PlayerEquipmentQuantityChange(3, 8174, -1)
    """State 6"""
    if not GetEventFlag(60845):
        """State 5"""
        # gesture:103:Erudition
        AcquireGesture(103)
        SetEventFlag(60845, 1)
    else:
        """State 7"""
        pass
    """State 1"""
    SetEventFlag(1039399220, 1)
    """State 12"""
    return 1

def t333006000_x51():
    """State 0,1"""
    SetEventFlag(1039399208, 0)
    SetEventFlag(1039399209, 0)
    SetEventFlag(1039399210, 0)
    SetEventFlag(1039399211, 0)
    SetEventFlag(1039399223, 0)
    SetEventFlag(1039399226, 0)
    """State 2"""
    return 0

def t333006000_x52():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        c1_110()
        """State 13"""
        assert t333006000_x51()
        """State 2"""
        if GetEventFlag(3805) == 1:
            """State 12"""
            assert t333006000_x45()
        else:
            """State 3"""
            pass
        """State 4"""
        # action:23330000:"Study sorcery"
        AddTalkListData(1, 23330000, -1)
        # action:23330002:"About the glintstone key"
        AddTalkListDataIf(GetEventFlag(1039399210) == 1, 40, 23330002, -1)
        # action:23330005:"Give the Academy Glintstone Key"
        AddTalkListDataIf(GetEventFlag(1039399211) == 1, 40, 23330005, -1)
        # action:23330004:"Talk"
        AddTalkListDataIf(GetEventFlag(1039399208) == 1, 50, 23330004, -1)
        # action:23330001:"Talk"
        AddTalkListDataIf(GetEventFlag(1039399209) == 1, 50, 23330001, -1)
        # action:23330003:""
        AddTalkListDataIf(GetEventFlag(1039399212) == 1, 50, 23330003, -1)
        # action:23330006:"About Sellen"
        AddTalkListDataIf(GetEventFlag(1039399223) == 1, 50, 23330006, -1)
        # action:23330009:"Give a scroll"
        AddTalkListDataIf(GetEventFlag(1039399226) == 1, 55, 23330009, -1)
        # action:20000009:"Leave"
        AddTalkListData(99, 20000009, -1)
        """State 5"""
        ShowShopMessage(1)
        """State 6"""
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 7"""
        if GetTalkListEntryResult() == 1:
            """State 8"""
            OpenRegularShop(100250, 100274)
            """State 9"""
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            continue
        elif GetTalkListEntryResult() == 40:
            """State 15"""
            call = t333006000_x55()
            if call.Get() == 0:
                pass
            elif call.Get() == 1:
                """State 17"""
                Label('L0')
                return 0
        elif GetTalkListEntryResult() == 50:
            """State 14"""
            assert t333006000_x47()
        elif GetTalkListEntryResult() == 55:
            """State 16"""
            assert t333006000_x56()
        else:
            """State 11"""
            Goto('L0')
        """State 10"""
        assert CheckSpecificPersonTalkHasEnded(0) == 1

def t333006000_x53():
    """State 0,2"""
    # talk:33302500:"You've taken an apprenticeship with Sellen?"
    assert t333006000_x30(text3=33302500, mode5=1)
    """State 1"""
    SetEventFlag(1039399221, 1)
    """State 3"""
    return 0

def t333006000_x54():
    """State 0,2"""
    # talk:33310000:"Oh, did I not mention?"
    assert t333006000_x30(text3=33310000, mode5=1)
    """State 1"""
    SetEventFlag(1039399225, 1)
    """State 3"""
    return 0

def t333006000_x55():
    """State 0,1"""
    if GetEventFlag(1039399211) == 1:
        """State 2"""
        call = t333006000_x50()
        if call.Get() == 0:
            pass
        elif call.Get() == 1:
            """State 5"""
            return 1
    elif GetEventFlag(1039399210) == 1:
        """State 3"""
        assert t333006000_x49()
    """State 4"""
    return 0

def t333006000_x56():
    """State 0,1"""
    assert t333006000_x54()
    """State 2"""
    return 0

