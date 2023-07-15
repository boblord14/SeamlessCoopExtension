# -*- coding: utf-8 -*-
def t801186000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t801186000_x5(flag4=4758, flag5=4756, flag6=4757, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag7=6000, flag8=6001, flag9=6000, flag10=6000, flag11=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t801186000_1000():
    """State 0,2,3"""
    assert t801186000_x37(flag1=1036499250, shop1=100700, shop2=100724)
    """State 1"""
    c1_120(1000)
    Quit()

def t801186000_1001():
    """State 0,2,3"""
    assert t801186000_x38()
    """State 1"""
    c1_120(1001)
    Quit()

def t801186000_1101():
    """State 0,2"""
    assert t801186000_x39(flag3=1036492715)
    """State 1"""
    c1_120(1101)
    Quit()

def t801186000_1102():
    """State 0,2"""
    t801186000_x40(flag2=1036499255)
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t801186000_1103():
    """State 0,2"""
    assert t801186000_x41()
    """State 1"""
    c1_120(1103)
    Quit()

def t801186000_x0(actionbutton1=6000, flag8=6001, flag12=6000, flag13=6000, flag14=6000, flag15=6000,
                  flag7=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag8) == 1 or GetEventFlag(flag12) == 1 or GetEventFlag(flag13) == 1 or
                GetEventFlag(flag14) == 1 or GetEventFlag(flag15) == 1)
        """State 4"""
        assert not GetEventFlag(flag7)
        """State 2"""
        if GetEventFlag(flag7) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag8) and not GetEventFlag(flag12) and not GetEventFlag(flag13) and not
              GetEventFlag(flag14) and not GetEventFlag(flag15)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t801186000_x1():
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

def t801186000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t801186000_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t801186000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t801186000_x1()
    else:
        """State 4,7"""
        call = t801186000_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t801186000_x1()
    """State 9"""
    return 0

def t801186000_x4():
    """State 0,1"""
    assert t801186000_x1()
    """State 2"""
    return 0

def t801186000_x5(flag4=4758, flag5=4756, flag6=4757, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag7=6000, flag8=6001, flag9=6000, flag10=6000, flag11=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t801186000_x22(flag4=flag4, flag5=flag5, flag6=flag6, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag7=flag7, flag8=flag8,
                              flag9=flag9, flag10=flag10, flag11=flag11, z1=z1, z2=z2, z3=z3, z4=z4,
                              mode1=mode1, mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t801186000_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t801186000_x6(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag7=6000, flag8=6001,
                  flag9=6000, flag10=6000, flag11=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t801186000_x9(actionbutton1=actionbutton1, flag7=flag7, flag8=flag8, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t801186000_x13(val1=val1, z1=z1)
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
        elif GetEventFlag(flag11) == 1:
            Goto('L0')
        elif GetEventFlag(flag9) == 1 and not GetEventFlag(flag10) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t801186000_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t801186000_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t801186000_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t801186000_x7(val2=10, val3=12):
    """State 0,1"""
    call = t801186000_x17(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t801186000_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t801186000_x8(flag4=4758, val2=10, val3=12):
    """State 0,8"""
    assert t801186000_x36()
    """State 1"""
    if GetEventFlag(flag4) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t801186000_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t801186000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t801186000_x9(actionbutton1=6000, flag7=6000, flag8=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t801186000_x10(z5=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t801186000_x0(actionbutton1=actionbutton1, flag8=flag8, flag12=6000, flag13=6000, flag14=6000,
                flag15=6000, flag7=flag7))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t801186000_x10(z5=_, val6=_):
    """State 0,1"""
    if f203(z5) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z5)
        assert f202() == val6
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t801186000_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t801186000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t801186000_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t801186000_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t801186000_x12():
    """State 0,1"""
    assert t801186000_x10(z5=1101, val6=1101)
    """State 2"""
    return 0

def t801186000_x13(val1=5, z1=1):
    """State 0,2"""
    assert t801186000_x23()
    """State 1"""
    call = t801186000_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t801186000_x25()
    """State 4"""
    return 0

def t801186000_x14():
    """State 0,1"""
    assert t801186000_x10(z5=1000, val6=1000)
    """State 2"""
    return 0

def t801186000_x15(val5=12):
    """State 0,1"""
    call = t801186000_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t801186000_x26()
    """State 3"""
    return 0

def t801186000_x16():
    """State 0,1"""
    assert t801186000_x10(z5=1100, val6=1100)
    """State 2"""
    return 0

def t801186000_x17(val2=10, val3=12):
    """State 0,5"""
    assert t801186000_x36()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t801186000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t801186000_x28()
    """Unused"""
    """State 6"""
    return 0

def t801186000_x18():
    """State 0,2"""
    call = t801186000_x10(z5=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t801186000_x19():
    """State 0,1"""
    assert t801186000_x10(z5=1001, val6=1001)
    """State 2"""
    return 0

def t801186000_x20():
    """State 0,1"""
    assert t801186000_x10(z5=1103, val6=1103)
    """State 2"""
    return 0

def t801186000_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t801186000_x22(flag4=4758, flag5=4756, flag6=4757, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag7=6000, flag8=6001, flag9=6000, flag10=6000, flag11=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t801186000_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag7=flag7, flag8=flag8, flag9=flag9, flag10=flag10, flag11=flag11, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag4) == 1:
            """State 3"""
            Label('L0')
            call = t801186000_x8(flag4=flag4, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag4):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag5) == 1 or GetEventFlag(flag6) == 1:
            """State 2"""
            call = t801186000_x7(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag4) == 1:
                Goto('L0')
            elif not GetEventFlag(flag5) and not GetEventFlag(flag6):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t801186000_x35() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t801186000_x23():
    """State 0,1"""
    assert t801186000_x24()
    """State 2"""
    return 0

def t801186000_x24():
    """State 0,1"""
    assert t801186000_x10(z5=1104, val6=1104)
    """State 2"""
    return 0

def t801186000_x25():
    """State 0,1"""
    call = t801186000_x10(z5=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t801186000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t801186000_x26():
    """State 0,1"""
    call = t801186000_x10(z5=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t801186000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t801186000_x27():
    """State 0,1"""
    call = t801186000_x10(z5=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t801186000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t801186000_x28():
    """State 0,1"""
    call = t801186000_x10(z5=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t801186000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t801186000_x29(text4=_, mode6=1):
    """State 0,4"""
    assert t801186000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
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

def t801186000_x30(text3=_, mode5=1):
    """State 0,4"""
    assert t801186000_x31() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t801186000_x31():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t801186000_x32():
    """State 0,1"""
    assert t801186000_x10(z5=1002, val6=1002)
    """State 2"""
    return 0

def t801186000_x33(text2=80125000, flag1=1036499250, mode4=1):
    """State 0,5"""
    assert t801186000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(flag1, 1)
    """State 1"""
    # talk:80125000:"What do you need?"
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

def t801186000_x34(text1=_, flag2=_, mode3=1):
    """State 0,5"""
    assert t801186000_x31() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(flag2, 1)
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

def t801186000_x35():
    """State 0,1"""
    assert t801186000_x1()
    """State 2"""
    return 0

def t801186000_x36():
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

def t801186000_x37(flag1=1036499250, shop1=100700, shop2=100724):
    """State 0,1"""
    assert t801186000_x42(flag1=flag1)
    """State 2"""
    assert t801186000_x43(shop1=shop1, shop2=shop2)
    """State 3"""
    return 0

def t801186000_x38():
    """State 0,1"""
    # talk:80185200:"Hurry up and die! You wretched thief!"
    assert t801186000_x30(text3=80185200, mode5=1)
    """State 2"""
    return 0

def t801186000_x39(flag3=1036492715):
    """State 0,3"""
    if not GetEventFlag(flag3):
        """State 1,4"""
        # talk:80185000:"Ow!"
        assert t801186000_x34(text1=80185000, flag2=flag3, mode3=1)
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t801186000_x40(flag2=1036499255):
    """State 0,2"""
    if not GetEventFlag(flag2):
        """State 3,5"""
        # talk:80185100:"I knew it, you dirty scoundrel!"
        assert t801186000_x34(text1=80185100, flag2=flag2, mode3=1)
    else:
        """State 4"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 6"""
    return 0

def t801186000_x41():
    """State 0,1"""
    # talk:80185300:"Rotten scoundrels..."
    assert t801186000_x30(text3=80185300, mode5=1)
    """State 2"""
    return 0

def t801186000_x42(flag1=1036499250):
    """State 0,1"""
    if not GetEventFlag(flag1):
        """State 3"""
        # talk:80125000:"What do you need?"
        assert t801186000_x33(text2=80125000, flag1=flag1, mode4=1)
    else:
        """State 2"""
        # talk:80125100:"You again?"
        assert t801186000_x29(text4=80125100, mode6=1)
    """State 4"""
    return 0

def t801186000_x43(shop1=100700, shop2=100724):
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
            c1_141(5)
            """State 7"""
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 9"""
            OpenSellShop(-1, -1)
            """State 8"""
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        else:
            """State 10,11"""
            # talk:80125200:"All done?"
            assert t801186000_x29(text4=80125200, mode6=1)
            """State 12"""
            return 0

