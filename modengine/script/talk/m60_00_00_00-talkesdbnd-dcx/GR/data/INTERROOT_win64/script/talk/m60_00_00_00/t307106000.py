# -*- coding: utf-8 -*-
def t307106000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t307106000_x11(flag1=3563, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1)
    Quit()

def t307106000_1000():
    """State 0,2,3"""
    assert t307106000_x0()
    """State 1"""
    c1_120(1000)
    Quit()

def t307106000_2000():
    """State 0,2,3"""
    assert t307106000_x1()
    """State 1"""
    c1_120(2000)
    Quit()

def t307106000_x0():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(20044, -1)
    assert t307106000_x2()
    """State 2"""
    return 0

def t307106000_x1():
    """State 0"""
    while True:
        """State 1"""
        if (GetEventFlag(3565) == 1 or GetEventFlag(3566) == 1 or GetEventFlag(3567) == 1 or GetEventFlag(3568)
            == 1):
            """State 2"""
            # actionbutton:6000:"Talk"
            call = t307106000_x6(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                                 flag12=6000, flag4=6000)
            if call.Done():
                break
            elif (call.Done() and (not GetEventFlag(3565) and not GetEventFlag(3566) and not GetEventFlag(3567)
                  and not GetEventFlag(3568))):
                pass
        elif GetEventFlag(3569) == 1:
            """State 3"""
            assert t307106000_x5() and not GetEventFlag(3569)
    """State 4"""
    return 0

def t307106000_x2():
    """State 0,1"""
    if GetEventFlag(1035509205) == 1:
        """State 2"""
        if GetEventFlag(1035509206) == 1:
            """State 3"""
            if GetEventFlag(1035509208) == 1:
                """State 5"""
                assert t307106000_x4()
                Goto('L0')
            else:
                """State 8"""
                # talk:30720200:"Ah, a fine day to your worship."
                assert t307106000_x36(text2=30720200, mode4=1)
        else:
            """State 6"""
            # talk:30720100:"Ahh, your worship, allow me to be of use."
            assert t307106000_x35(text3=30720100, z6=1035509206, mode5=1)
        """State 7"""
        def WhilePaused():
            RequestAnimation(20045, -1)
        assert t307106000_x3()
    else:
        """State 4"""
        # talk:30720000:"O-oh!"
        assert t307106000_x35(text3=30720000, z6=1035509205, mode5=1)
    """State 9"""
    Label('L0')
    return 0

def t307106000_x3():
    """State 0,1"""
    c1_110()
    while True:
        """State 2"""
        ClearTalkListData()
        """State 3"""
        # action:23070020:"Purchase"
        AddTalkListData(1, 23070020, -1)
        # action:20000009:"Leave"
        AddTalkListData(99, 20000009, -1)
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 6"""
            OpenRegularShop(100325, 100349)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 7"""
            if GetEventFlag(1035509208) == 1:
                break
            else:
                continue
        else:
            pass
        """State 9"""
        Label('L0')
        return 0
    """State 8"""
    # talk:30720300:"Ah, I'm sorry your worship, but poor Pidia has given all he has."
    assert t307106000_x35(text3=30720300, z6=1035502703, mode5=1)
    Goto('L0')

def t307106000_x4():
    """State 0,1"""
    if not GetEventFlag(1035502703):
        """State 2"""
        # talk:30720300:"Ah, I'm sorry your worship, but poor Pidia has given all he has."
        assert t307106000_x35(text3=30720300, z6=1035502703, mode5=1)
    else:
        """State 3"""
        # talk:30720400:"Please, find it in your heart... Forgive me..."
        assert t307106000_x36(text2=30720400, mode4=1)
    """State 4"""
    return 0

def t307106000_x5():
    """State 0"""
    while True:
        """State 1"""
        if (not GetEventFlag(1035509210) and not GetEventFlag(1035509211) and GetEventFlag(1035502705)
            == 1 and GetDistanceToPlayer() < 80):
            """State 3"""
            # talk:30720500:"Argh!"
            call = t307106000_x37(text1=30720500, z5=1035509210, mode3=1)
            def WhilePaused():
                c5_121(not CheckSpecificPersonTalkHasEnded(0), 9625)
            if call.Done() and CheckSpecificPersonTalkHasEnded(0) == 1:
                continue
            elif GetDistanceToPlayer() > 90:
                """State 4"""
                assert t307106000_x7()
                continue
            elif not GetEventFlag(1035509211) and GetEventFlag(1035502706) == 1:
                pass
        elif not GetEventFlag(1035509211) and GetEventFlag(1035502706) == 1 and GetDistanceToPlayer() < 30:
            pass
        """State 5"""
        # talk:30720550:"Eeek"
        call = t307106000_x37(text1=30720550, z5=1035509211, mode3=1)
        def WhilePaused():
            c5_121(not CheckSpecificPersonTalkHasEnded(0), 9625)
        if call.Done() and CheckSpecificPersonTalkHasEnded(0) == 1:
            pass
        elif GetDistanceToPlayer() > 40:
            """State 6"""
            assert t307106000_x7()
        """State 2"""
        Quit()
    """Unused"""
    """State 7"""
    return 0

def t307106000_x6(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t307106000_x7():
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

def t307106000_x8():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t307106000_x9(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t307106000_x25()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t307106000_x7()
    else:
        """State 4,7"""
        call = t307106000_x39()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t307106000_x7()
    """State 9"""
    return 0

def t307106000_x10():
    """State 0,1"""
    assert t307106000_x7()
    """State 2"""
    return 0

def t307106000_x11(flag1=3563, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t307106000_x28(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t307106000_x27()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t307106000_x12(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                   flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                   mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t307106000_x15(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t307106000_x19(val1=val1, z1=z1)
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
            call = t307106000_x21(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t307106000_x32() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t307106000_x17(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t307106000_x13(val2=10, val3=12):
    """State 0,1"""
    call = t307106000_x23(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t307106000_x9(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t307106000_x14(flag1=3563, val2=10, val3=12):
    """State 0,8"""
    assert t307106000_x41()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t307106000_x26()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t307106000_x7()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t307106000_x15(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t307106000_x16(z7=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t307106000_x6(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t307106000_x16(z7=_, val6=_):
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

def t307106000_x17(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t307106000_x7()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t307106000_x18()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t307106000_x33()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t307106000_x18():
    """State 0,1"""
    assert t307106000_x16(z7=1101, val6=1101)
    """State 2"""
    return 0

def t307106000_x19(val1=5, z1=1):
    """State 0,2"""
    assert t307106000_x29()
    """State 1"""
    call = t307106000_x20()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t307106000_x31()
    """State 4"""
    return 0

def t307106000_x20():
    """State 0,1"""
    assert t307106000_x16(z7=1000, val6=1000)
    """State 2"""
    return 0

def t307106000_x21(val5=12):
    """State 0,1"""
    call = t307106000_x22()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t307106000_x32()
    """State 3"""
    return 0

def t307106000_x22():
    """State 0,1"""
    assert t307106000_x16(z7=1100, val6=1100)
    """State 2"""
    return 0

def t307106000_x23(val2=10, val3=12):
    """State 0,5"""
    assert t307106000_x41()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t307106000_x24()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t307106000_x34()
    """Unused"""
    """State 6"""
    return 0

def t307106000_x24():
    """State 0,2"""
    call = t307106000_x16(z7=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t307106000_x25():
    """State 0,1"""
    assert t307106000_x16(z7=1001, val6=1001)
    """State 2"""
    return 0

def t307106000_x26():
    """State 0,1"""
    assert t307106000_x16(z7=1103, val6=1103)
    """State 2"""
    return 0

def t307106000_x27():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t307106000_x28(flag1=3563, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t307106000_x12(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                              flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                              z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t307106000_x14(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t307106000_x13(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t307106000_x40() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t307106000_x29():
    """State 0,1"""
    assert t307106000_x30()
    """State 2"""
    return 0

def t307106000_x30():
    """State 0,1"""
    assert t307106000_x16(z7=1104, val6=1104)
    """State 2"""
    return 0

def t307106000_x31():
    """State 0,1"""
    call = t307106000_x16(z7=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t307106000_x10()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t307106000_x32():
    """State 0,1"""
    call = t307106000_x16(z7=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t307106000_x10()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t307106000_x33():
    """State 0,1"""
    call = t307106000_x16(z7=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t307106000_x10()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t307106000_x34():
    """State 0,1"""
    call = t307106000_x16(z7=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t307106000_x10()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t307106000_x35(text3=_, z6=_, mode5=1):
    """State 0,5"""
    assert t307106000_x8() and CheckSpecificPersonTalkHasEnded(0) == 1
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
    SetEventFlag(z6, 1)
    """State 6"""
    return 0

def t307106000_x36(text2=_, mode4=1):
    """State 0,4"""
    assert t307106000_x8() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t307106000_x37(text1=_, z5=_, mode3=1):
    """State 0,5"""
    assert t307106000_x38() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(z5, 1)
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

def t307106000_x38():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t307106000_x39():
    """State 0,1"""
    assert t307106000_x16(z7=1002, val6=1002)
    """State 2"""
    return 0

def t307106000_x40():
    """State 0,1"""
    assert t307106000_x7()
    """State 2"""
    return 0

def t307106000_x41():
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

