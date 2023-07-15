# -*- coding: utf-8 -*-
def t801226000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t801226000_x5(flag8=4778, flag9=4776, flag10=4777, val3=5, val4=10, val5=12, val6=10, val7=12, actionbutton1=6000,
                  flag11=6000, flag12=6001, flag13=6000, flag14=6000, flag15=6000, z1=1, z2=1000000,
                  z3=1000000, z4=1000000, mode1=1, mode2=1)
    Quit()

def t801226000_1000():
    """State 0,2,3"""
    assert t801226000_x37(flag5=1048389200, shop1=100800, shop2=100824)
    """State 1"""
    c1_120(1000)
    Quit()

def t801226000_1001():
    """State 0,2,3"""
    assert t801226000_x38()
    """State 1"""
    c1_120(1001)
    Quit()

def t801226000_1101():
    """State 0,2"""
    assert t801226000_x39(flag7=1048382705)
    """State 1"""
    c1_120(1101)
    Quit()

def t801226000_1102():
    """State 0,2"""
    t801226000_x40(flag6=1048389205)
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t801226000_1103():
    """State 0,2"""
    assert t801226000_x41()
    """State 1"""
    c1_120(1103)
    Quit()

def t801226000_2000():
    """State 0,2,3"""
    assert t801226000_x42(flag1=1048382702, flag2=1048382706, flag3=1048382707, val1=37, val2=27, flag4=1048389200)
    """State 1"""
    c1_120(2000)
    Quit()

def t801226000_x0(actionbutton1=6000, flag12=6001, flag16=6000, flag17=6000, flag18=6000, flag19=6000,
                  flag11=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag12) == 1 or GetEventFlag(flag16) == 1 or GetEventFlag(flag17) == 1 or
                GetEventFlag(flag18) == 1 or GetEventFlag(flag19) == 1)
        """State 4"""
        assert not GetEventFlag(flag11)
        """State 2"""
        if GetEventFlag(flag11) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag12) and not GetEventFlag(flag16) and not GetEventFlag(flag17) and
              not GetEventFlag(flag18) and not GetEventFlag(flag19)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t801226000_x1():
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

def t801226000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t801226000_x3(val4=10, val5=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val4 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t801226000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t801226000_x1()
    else:
        """State 4,7"""
        call = t801226000_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t801226000_x1()
    """State 9"""
    return 0

def t801226000_x4():
    """State 0,1"""
    assert t801226000_x1()
    """State 2"""
    return 0

def t801226000_x5(flag8=4778, flag9=4776, flag10=4777, val3=5, val4=10, val5=12, val6=10, val7=12, actionbutton1=6000,
                  flag11=6000, flag12=6001, flag13=6000, flag14=6000, flag15=6000, z1=1, z2=1000000,
                  z3=1000000, z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t801226000_x22(flag8=flag8, flag9=flag9, flag10=flag10, val3=val3, val4=val4, val5=val5,
                              val6=val6, val7=val7, actionbutton1=actionbutton1, flag11=flag11, flag12=flag12,
                              flag13=flag13, flag14=flag14, flag15=flag15, z1=z1, z2=z2, z3=z3, z4=z4,
                              mode1=mode1, mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t801226000_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t801226000_x6(val3=5, val4=10, val5=12, val6=10, val7=12, actionbutton1=6000, flag11=6000, flag12=6001,
                  flag13=6000, flag14=6000, flag15=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t801226000_x9(actionbutton1=actionbutton1, flag11=flag11, flag12=flag12, z2=z2, z3=z3,
                             z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t801226000_x13(val3=val3, z1=z1)
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
        elif GetEventFlag(flag15) == 1:
            Goto('L0')
        elif GetEventFlag(flag13) == 1 and not GetEventFlag(flag14) and GetDistanceToPlayer() < val6:
            """State 5"""
            call = t801226000_x15(val7=val7)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val7 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t801226000_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t801226000_x11(val4=val4, val5=val5)
    """Unused"""
    """State 7"""
    return 0

def t801226000_x7(val4=10, val5=12):
    """State 0,1"""
    call = t801226000_x17(val4=val4, val5=val5)
    assert IsPlayerDead() == 1
    """State 2"""
    t801226000_x3(val4=val4, val5=val5)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t801226000_x8(flag8=4778, val4=10, val5=12):
    """State 0,8"""
    assert t801226000_x36()
    """State 1"""
    if GetEventFlag(flag8) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val4:
            """State 4,6"""
            call = t801226000_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t801226000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t801226000_x9(actionbutton1=6000, flag11=6000, flag12=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t801226000_x10(z5=2000, val8=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t801226000_x0(actionbutton1=actionbutton1, flag12=flag12, flag16=6000, flag17=6000, flag18=6000,
                flag19=6000, flag11=flag11))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t801226000_x10(z5=_, val8=_):
    """State 0,1"""
    if f203(z5) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z5)
        assert f202() == val8
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t801226000_x11(val4=10, val5=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t801226000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val4:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t801226000_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t801226000_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t801226000_x12():
    """State 0,1"""
    assert t801226000_x10(z5=1101, val8=1101)
    """State 2"""
    return 0

def t801226000_x13(val3=5, z1=1):
    """State 0,2"""
    assert t801226000_x23()
    """State 1"""
    call = t801226000_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t801226000_x25()
    """State 4"""
    return 0

def t801226000_x14():
    """State 0,1"""
    assert t801226000_x10(z5=1000, val8=1000)
    """State 2"""
    return 0

def t801226000_x15(val7=12):
    """State 0,1"""
    call = t801226000_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val7 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t801226000_x26()
    """State 3"""
    return 0

def t801226000_x16():
    """State 0,1"""
    assert t801226000_x10(z5=1100, val8=1100)
    """State 2"""
    return 0

def t801226000_x17(val4=10, val5=12):
    """State 0,5"""
    assert t801226000_x36()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val4
        """State 3"""
        call = t801226000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t801226000_x28()
    """Unused"""
    """State 6"""
    return 0

def t801226000_x18():
    """State 0,2"""
    call = t801226000_x10(z5=1102, val8=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t801226000_x19():
    """State 0,1"""
    assert t801226000_x10(z5=1001, val8=1001)
    """State 2"""
    return 0

def t801226000_x20():
    """State 0,1"""
    assert t801226000_x10(z5=1103, val8=1103)
    """State 2"""
    return 0

def t801226000_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t801226000_x22(flag8=4778, flag9=4776, flag10=4777, val3=5, val4=10, val5=12, val6=10, val7=12, actionbutton1=6000,
                   flag11=6000, flag12=6001, flag13=6000, flag14=6000, flag15=6000, z1=1, z2=1000000,
                   z3=1000000, z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t801226000_x6(val3=val3, val4=val4, val5=val5, val6=val6, val7=val7, actionbutton1=actionbutton1,
                             flag11=flag11, flag12=flag12, flag13=flag13, flag14=flag14, flag15=flag15,
                             z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag8) == 1:
            """State 3"""
            Label('L0')
            call = t801226000_x8(flag8=flag8, val4=val4, val5=val5)
            if not CheckSelfDeath() and not GetEventFlag(flag8):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag9) == 1 or GetEventFlag(flag10) == 1:
            """State 2"""
            call = t801226000_x7(val4=val4, val5=val5)
            if CheckSelfDeath() == 1 or GetEventFlag(flag8) == 1:
                Goto('L0')
            elif not GetEventFlag(flag9) and not GetEventFlag(flag10):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t801226000_x35() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t801226000_x23():
    """State 0,1"""
    assert t801226000_x24()
    """State 2"""
    return 0

def t801226000_x24():
    """State 0,1"""
    assert t801226000_x10(z5=1104, val8=1104)
    """State 2"""
    return 0

def t801226000_x25():
    """State 0,1"""
    call = t801226000_x10(z5=1201, val8=1201)
    if call.Get() == 1:
        """State 2"""
        assert t801226000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t801226000_x26():
    """State 0,1"""
    call = t801226000_x10(z5=1300, val8=1300)
    if call.Get() == 1:
        """State 2"""
        assert t801226000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t801226000_x27():
    """State 0,1"""
    call = t801226000_x10(z5=1301, val8=1301)
    if call.Get() == 1:
        """State 2"""
        assert t801226000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t801226000_x28():
    """State 0,1"""
    call = t801226000_x10(z5=1302, val8=1302)
    if call.Get() == 1:
        """State 2"""
        assert t801226000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t801226000_x29(text4=80100300, mode6=1):
    """State 0,4"""
    assert t801226000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    # talk:80100300:"Ahh, hello."
    TalkToPlayer(text4, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode6:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t801226000_x30(text3=_, mode5=1):
    """State 0,4"""
    assert t801226000_x31() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text3, -1, -1, 1)
    """State 3"""
    if not mode5:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t801226000_x31():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t801226000_x32():
    """State 0,1"""
    assert t801226000_x10(z5=1002, val8=1002)
    """State 2"""
    return 0

def t801226000_x33(text2=80100200, flag5=1048389200, mode4=1):
    """State 0,5"""
    assert t801226000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(flag5, 1)
    """State 1"""
    # talk:80100200:"Welcome..."
    TalkToPlayer(text2, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode4:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t801226000_x34(text1=_, flag1=_, mode3=1):
    """State 0,5"""
    assert t801226000_x31() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t801226000_x35():
    """State 0,1"""
    assert t801226000_x1()
    """State 2"""
    return 0

def t801226000_x36():
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

def t801226000_x37(flag5=1048389200, shop1=100800, shop2=100824):
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(20008, -1)
    assert t801226000_x43(flag5=flag5)
    """State 2"""
    def WhilePaused():
        RequestAnimation(20008, -1)
    assert t801226000_x44(shop1=shop1, shop2=shop2)
    """State 3"""
    return 0

def t801226000_x38():
    """State 0,1"""
    # talk:80180200:"Dirty little thief..."
    assert t801226000_x30(text3=80180200, mode5=1)
    """State 2"""
    return 0

def t801226000_x39(flag7=1048382705):
    """State 0,2"""
    if not GetEventFlag(flag7):
        """State 1,4"""
        # talk:80180000:"Agh! "
        assert t801226000_x34(text1=80180000, flag1=flag7, mode3=1)
    else:
        """State 3,5"""
        # talk:80180010:"Please! Stop this, good customer!"
        assert t801226000_x34(text1=80180010, flag1=flag7, mode3=1)
    """State 6"""
    return 0

def t801226000_x40(flag6=1048389205):
    """State 0,2"""
    if not GetEventFlag(flag6):
        """State 3,5"""
        # talk:80180100:"Bollocks! What the devil's wrong with you!"
        assert t801226000_x34(text1=80180100, flag1=flag6, mode3=1)
    else:
        """State 4"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 6"""
    return 0

def t801226000_x41():
    """State 0,1"""
    # talk:80180300:"You dirty little thief..."
    assert t801226000_x30(text3=80180300, mode5=1)
    """State 2"""
    return 0

def t801226000_x42(flag1=1048382702, flag2=1048382706, flag3=1048382707, val1=37, val2=27, flag4=1048389200):
    """State 0,1"""
    def WhilePaused():
        c1_121(9625)
    assert t801226000_x45(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, flag4=flag4)
    """State 2"""
    return 0

def t801226000_x43(flag5=1048389200):
    """State 0,1"""
    if not GetEventFlag(flag5):
        """State 3"""
        # talk:80100200:"Welcome..."
        assert t801226000_x33(text2=80100200, flag5=flag5, mode4=1)
    else:
        """State 2"""
        # talk:80100300:"Ahh, hello."
        assert t801226000_x29(text4=80100300, mode6=1)
    """State 4"""
    return 0

def t801226000_x44(shop1=100800, shop2=100824):
    """State 0"""
    while True:
        """State 1"""
        c1_110()
        ClearTalkActionState()
        ClearTalkListData()
        """State 2"""
        # action:20000010:"Purchase"
        AddTalkListData(1, 20000010, -1)
        # action:20000011:"Sell"
        AddTalkListData(2, 20000011, -1)
        # action:20000009:"Leave"
        AddTalkListData(99, 20000009, -1)
        """State 3"""
        ShowShopMessage(1)
        """State 4"""
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 6"""
            OpenRegularShop(shop1, shop2)
            """State 7"""
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 9"""
            OpenSellShop(-1, -1)
            """State 8"""
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        else:
            """State 10,11"""
            return 0

def t801226000_x45(flag1=1048382702, flag2=1048382706, flag3=1048382707, val1=37, val2=27, flag4=1048389200):
    """State 0"""
    while True:
        """State 1"""
        # actionbutton:6000:"Talk"
        call = t801226000_x0(actionbutton1=6000, flag12=6001, flag16=6000, flag17=6000, flag18=6000,
                             flag19=6000, flag11=6000)
        if call.Done():
            break
        elif GetDistanceToPlayer() < val2 and not GetEventFlag(flag1) and not GetEventFlag(flag4):
            """State 2"""
            # talk:80100100:"Ahh, welcome...dear customer."
            assert t801226000_x34(text1=80100100, flag1=flag1, mode3=1)
        elif GetEventFlag(flag2) == 1 and not GetEventFlag(flag3) and GetDistanceToPlayer() < 10:
            """State 3"""
            # talk:80180010:"Please! Stop this, good customer!"
            assert t801226000_x34(text1=80180010, flag1=flag3, mode3=1)
        elif GetDistanceToPlayer() > val1 and not CheckSpecificPersonTalkHasEnded(0):
            """State 4"""
            assert t801226000_x2()
    """State 5"""
    return 0

