# -*- coding: utf-8 -*-
def t331006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t331006000_x5(flag1=4143, flag2=4141, flag3=4142, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z2=1, z3=1000000, z4=1000000,
                  z5=1000000, mode1=1, mode2=1)
    Quit()

def t331006000_1000():
    """State 0,2,3"""
    assert t331006000_x35()
    """State 1"""
    c1_120(1000)
    Quit()

def t331006000_1001():
    """State 0,2,3"""
    assert t331006000_x36()
    """State 1"""
    c1_120(1001)
    Quit()

def t331006000_1101():
    """State 0,2,3"""
    assert t331006000_x37()
    """State 1"""
    c1_120(1101)
    Quit()

def t331006000_1102():
    """State 0,2,3"""
    t331006000_x38()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t331006000_1103():
    """State 0,2,3"""
    assert t331006000_x39()
    """State 1"""
    c1_120(1103)
    Quit()

def t331006000_2000():
    """State 0,2,3"""
    # actionbutton:6000:"Talk"
    assert (t331006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
            flag4=6000))
    """State 1"""
    c1_120(2000)
    Quit()

def t331006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t331006000_x1():
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

def t331006000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t331006000_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t331006000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t331006000_x1()
    else:
        """State 4,7"""
        call = t331006000_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t331006000_x1()
    """State 9"""
    return 0

def t331006000_x4():
    """State 0,1"""
    assert t331006000_x1()
    """State 2"""
    return 0

def t331006000_x5(flag1=4143, flag2=4141, flag3=4142, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z2=1, z3=1000000, z4=1000000,
                  z5=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t331006000_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z2=z2, z3=z3, z4=z4, z5=z5, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t331006000_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t331006000_x6(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z2=1, z3=1000000, z4=1000000, z5=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t331006000_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z3=z3, z4=z4, z5=z5)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t331006000_x13(val1=val1, z2=z2)
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
            call = t331006000_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t331006000_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t331006000_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t331006000_x7(val2=10, val3=12):
    """State 0,1"""
    call = t331006000_x17(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t331006000_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t331006000_x8(flag1=4143, val2=10, val3=12):
    """State 0,8"""
    assert t331006000_x34()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t331006000_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t331006000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t331006000_x9(actionbutton1=6000, flag4=6000, flag5=6001, z3=1000000, z4=1000000, z5=1000000):
    """State 0,1"""
    call = t331006000_x10(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t331006000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t331006000_x10(z6=_, val6=_):
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

def t331006000_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t331006000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t331006000_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t331006000_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t331006000_x12():
    """State 0,1"""
    assert t331006000_x10(z6=1101, val6=1101)
    """State 2"""
    return 0

def t331006000_x13(val1=5, z2=1):
    """State 0,2"""
    assert t331006000_x23()
    """State 1"""
    call = t331006000_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t331006000_x25()
    """State 4"""
    return 0

def t331006000_x14():
    """State 0,1"""
    assert t331006000_x10(z6=1000, val6=1000)
    """State 2"""
    return 0

def t331006000_x15(val5=12):
    """State 0,1"""
    call = t331006000_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t331006000_x26()
    """State 3"""
    return 0

def t331006000_x16():
    """State 0,1"""
    assert t331006000_x10(z6=1100, val6=1100)
    """State 2"""
    return 0

def t331006000_x17(val2=10, val3=12):
    """State 0,5"""
    assert t331006000_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t331006000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t331006000_x28()
    """Unused"""
    """State 6"""
    return 0

def t331006000_x18():
    """State 0,2"""
    call = t331006000_x10(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t331006000_x19():
    """State 0,1"""
    assert t331006000_x10(z6=1001, val6=1001)
    """State 2"""
    return 0

def t331006000_x20():
    """State 0,1"""
    assert t331006000_x10(z6=1103, val6=1103)
    """State 2"""
    return 0

def t331006000_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t331006000_x22(flag1=4143, flag2=4141, flag3=4142, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z2=1, z3=1000000, z4=1000000,
                   z5=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t331006000_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z2=z2,
                             z3=z3, z4=z4, z5=z5, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t331006000_x8(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t331006000_x7(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t331006000_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t331006000_x23():
    """State 0,1"""
    assert t331006000_x24()
    """State 2"""
    return 0

def t331006000_x24():
    """State 0,1"""
    assert t331006000_x10(z6=1104, val6=1104)
    """State 2"""
    return 0

def t331006000_x25():
    """State 0,1"""
    call = t331006000_x10(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t331006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t331006000_x26():
    """State 0,1"""
    call = t331006000_x10(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t331006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t331006000_x27():
    """State 0,1"""
    call = t331006000_x10(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t331006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t331006000_x28():
    """State 0,1"""
    call = t331006000_x10(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t331006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t331006000_x29(text2=_, mode4=1):
    """State 0,4"""
    assert t331006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t331006000_x30(text1=_, mode3=1):
    """State 0,4"""
    assert t331006000_x31() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t331006000_x31():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t331006000_x32():
    """State 0,1"""
    assert t331006000_x10(z6=1002, val6=1002)
    """State 2"""
    return 0

def t331006000_x33():
    """State 0,1"""
    assert t331006000_x1()
    """State 2"""
    return 0

def t331006000_x34():
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

def t331006000_x35():
    """State 0,1"""
    if GetEventFlag(4145) == 1:
        """State 3"""
        assert t331006000_x40()
    elif GetEventFlag(4146) == 1:
        """State 4"""
        assert t331006000_x41()
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t331006000_x36():
    """State 0,1"""
    # talk:33180400:"You feel that, eh?"
    assert t331006000_x30(text1=33180400, mode3=1)
    """State 2"""
    return 0

def t331006000_x37():
    """State 0"""
    if not GetEventFlag(1036432701):
        """State 2,1"""
        SetEventFlag(1036432701, 1)
        """State 6"""
        # talk:33180000:"Oof!"
        assert t331006000_x30(text1=33180000, mode3=1)
    elif not GetEventFlag(1036432703):
        """State 4,5"""
        SetEventFlag(1036432703, 1)
        """State 7"""
        # talk:33180100:"What's your blinkin' problem!"
        assert t331006000_x30(text1=33180100, mode3=1)
    else:
        """State 3"""
        pass
    """State 8"""
    return 0

def t331006000_x38():
    """State 0,2"""
    if not GetEventFlag(1036439203):
        """State 3,6"""
        SetEventFlag(1036439203, 1)
        """State 5"""
        SetEventFlag(1036432700, 1)
        if not GetEventFlag(1036439210):
            """State 7,9"""
            # talk:33180200:"That bitch put you up to this, eh."
            assert t331006000_x30(text1=33180200, mode3=1)
        else:
            """State 8,10"""
            # talk:33180300:"Not scared, are ya."
            t331006000_x30(text1=33180300, mode3=1)
            Quit()
    else:
        """State 4"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 11"""
    return 0

def t331006000_x39():
    """State 0,1"""
    # talk:33180500:"Goddamn it."
    assert t331006000_x30(text1=33180500, mode3=1)
    """State 2"""
    return 0

def t331006000_x40():
    """State 0"""
    while True:
        """State 1"""
        if not GetEventFlag(1036439210):
            """State 2"""
            # eventflag:400300:shop:100150:Rya's Necklace, goods:8136:Rya's Necklace
            if not GetEventFlag(400300) and ComparePlayerInventoryNumber(3, 8136, 1, 1, 0) == 1:
                break
            else:
                """State 4,5"""
                SetEventFlag(1036439210, 1)
                continue
        else:
            """State 3,7"""
            def WhilePaused():
                RequestAnimation(90300, -1)
            assert t331006000_x43()
        """State 8"""
        Label('L0')
        return 0
    """State 6"""
    def WhilePaused():
        RequestAnimation(90300, -1)
    assert t331006000_x42()
    Goto('L0')

def t331006000_x41():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(90300, -1)
    assert t331006000_x49()
    """State 2"""
    return 0

def t331006000_x42():
    """State 0,1"""
    if not GetEventFlag(1036439205):
        """State 4,5"""
        call = t331006000_x44()
        if call.Get() == 1:
            """State 6"""
            Label('L0')
            call = t331006000_x45()
            if call.Get() == 1:
                """State 7"""
                Label('L1')
                assert t331006000_x47()
            elif call.Done():
                pass
        elif call.Done():
            pass
    elif not GetEventFlag(1036439207):
        """State 2"""
        Goto('L0')
    else:
        """State 3"""
        Goto('L1')
    """State 8"""
    return 0

def t331006000_x43():
    """State 0,1"""
    if not GetEventFlag(1036439209):
        """State 2,7"""
        # talk:33100400:"Oh piss off, what is it now?"
        assert t331006000_x29(text2=33100400, mode4=1)
        """State 5"""
        SetEventFlag(1036439209, 1)
        """State 6"""
        Label('L0')
        SetEventFlag(1036432702, 1)
    elif GetEventFlag(1036439209) == 1 and not GetEventFlag(1036432702):
        """State 3,8"""
        # talk:33101100:"Alright mate. Want some more prawn, do ya?"
        assert t331006000_x29(text2=33101100, mode4=1)
        Goto('L0')
    else:
        """State 4,9"""
        # talk:33101000:"Marika's tits, you must be 'ungry."
        assert t331006000_x29(text2=33101000, mode4=1)
    """State 10"""
    assert t331006000_x48()
    """State 11"""
    return 0

def t331006000_x44():
    """State 0,1"""
    if not GetEventFlag(1036439205) and not GetEventFlag(1036439206):
        """State 2,12"""
        # talk:33100100:"What are you lookin' at?"
        assert t331006000_x29(text2=33100100, mode4=1)
    else:
        """State 3,13"""
        # talk:33100500:"What the hell is wrong with you."
        assert t331006000_x29(text2=33100500, mode4=1)
    """State 4"""
    ClearTalkListData()
    c1_110()
    """State 5"""
    # action:23311000:"Give me the necklace"
    AddTalkListDataIf(GetEventFlag(1037429209) == 1, 1, 23311000, -1)
    # action:23311001:"Leave"
    AddTalkListData(2, 23311001, -1)
    """State 6"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 7"""
    if GetTalkListEntryResult() == 1:
        """State 8,15"""
        return 1
    elif GetTalkListEntryResult() == 2:
        """State 9,10"""
        SetEventFlag(1036439206, 1)
    else:
        """State 11"""
        pass
    """State 14"""
    return 0

def t331006000_x45():
    """State 0,1"""
    if not GetEventFlag(1036439205) and not GetEventFlag(1036439207):
        """State 2,13"""
        # talk:33100200:"Oh, that necklace what you're after, is it?"
        assert t331006000_x29(text2=33100200, mode4=1)
        """State 4"""
        SetEventFlag(1036439205, 1)
    else:
        """State 3,14"""
        # talk:33100600:"This bloody swine..."
        assert t331006000_x29(text2=33100600, mode4=1)
    """State 5"""
    ClearTalkListData()
    c1_110()
    """State 6"""
    # action:23311002:"Deal"
    AddTalkListData(1, 23311002, -1)
    # action:23311003:"Refuse"
    AddTalkListData(2, 23311003, -1)
    """State 7"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 8"""
    if GetTalkListEntryResult() == 1:
        """State 9,17"""
        return 1
    elif GetTalkListEntryResult() == 2:
        """State 10,15"""
        # talk:33100700:"Think you're bloody clever, do ya?"
        assert t331006000_x29(text2=33100700, mode4=1)
        """State 11"""
        SetEventFlag(1036439208, 1)
    else:
        """State 12"""
        pass
    """State 16"""
    return 0

def t331006000_x46(z1=_):
    """State 0,1"""
    assert DidYouDoSomethingInTheMenu(0) == 1
    """State 2"""
    SetEventFlag(z1, 1)
    """State 3"""
    Quit()
    """Unused"""
    """State 4"""
    return 0

def t331006000_x47():
    """State 0,1"""
    if not GetEventFlag(1036439207):
        """State 2,15"""
        # talk:33100300:"You're a shrewd one, chief."
        assert t331006000_x29(text2=33100300, mode4=1)
        """State 4"""
        SetEventFlag(1036439207, 1)
    else:
        """State 3,16"""
        # talk:33100600:"This bloody swine..."
        assert t331006000_x29(text2=33100600, mode4=1)
    """State 5"""
    ClearTalkActionState()
    c1_110()
    while True:
        """State 6"""
        ClearTalkListData()
        """State 7"""
        # action:20000010:"Purchase"
        AddTalkListData(1, 20000010, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 8"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 9"""
        if GetTalkListEntryResult() == 1:
            """State 10,12"""
            OpenRegularShop(100150, 100174)
            """State 17"""
            call = t331006000_x46(z1=1036439210)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        else:
            """State 11"""
            if GetEventFlag(1036439210) == 1:
                """State 13,18"""
                # talk:33100305:"Hmm..."
                assert t331006000_x29(text2=33100305, mode4=1)
            else:
                """State 14"""
                pass
            """State 19"""
            return 0

def t331006000_x48():
    """State 0,1"""
    ClearTalkActionState()
    c1_110()
    while True:
        """State 2"""
        ClearTalkListData()
        """State 3"""
        # action:20000010:"Purchase"
        AddTalkListData(1, 20000010, -1)
        # action:20000011:"Sell"
        AddTalkListData(2, 20000011, -1)
        # action:23310000:"About Rya"
        AddTalkListDataIf(not GetEventFlag(1036439211), 3, 23310000, -1)
        # action:23310001:"Talk"
        AddTalkListDataIf(not GetEventFlag(1036439212) and GetEventFlag(1036439213) == 1, 4, 23310001,
                          -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 6,10"""
            OpenRegularShop(100150, 100174)
            """State 18"""
            call = t331006000_x46(z1=1036439213)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 16,17"""
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 7,19"""
            # talk:33101500:"Oh, so you met the girl, did ya?"
            assert t331006000_x29(text2=33101500, mode4=1)
            """State 11"""
            SetEventFlag(1036439211, 1)
        elif GetTalkListEntryResult() == 4:
            """State 8,20"""
            # talk:33101600:"You're Tarnished too, ain'tcha?"
            assert t331006000_x29(text2=33101600, mode4=1)
            """State 12"""
            SetEventFlag(1036439212, 1)
        else:
            """State 9"""
            if GetEventFlag(1036439213) == 1 and not GetEventFlag(1036439214):
                """State 13,21"""
                # talk:33101200:"Never met someone with a taste for prawn I couldn't trust."
                assert t331006000_x29(text2=33101200, mode4=1)
                """State 22"""
                assert t331006000_x53()
                """State 15"""
                SetEventFlag(1036439214, 1)
            else:
                """State 14"""
                pass
            """State 23"""
            return 0

def t331006000_x49():
    """State 0,1"""
    if not GetEventFlag(1044529256):
        """State 2,7"""
        # talk:33102000:"What are you lookin' at?"
        assert t331006000_x29(text2=33102000, mode4=1)
        """State 5"""
        SetEventFlag(1044529256, -1)
        """State 6"""
        Label('L0')
        SetEventFlag(1044522700, 1)
    elif not GetEventFlag(1044522700):
        """State 3,8"""
        # talk:33102200:"Alright mate. Want some more crab, do ya?"
        assert t331006000_x29(text2=33102200, mode4=1)
        Goto('L0')
    else:
        """State 4,9"""
        # talk:33102100:"Marika's tits, you must be 'ungry."
        assert t331006000_x29(text2=33102100, mode4=1)
    """State 10"""
    assert t331006000_x50()
    """State 11"""
    return 0

def t331006000_x50():
    """State 0,1"""
    ClearTalkActionState()
    c1_110()
    while True:
        """State 2"""
        ClearTalkListData()
        """State 15"""
        assert t331006000_x51()
        """State 3"""
        # action:20000010:"Purchase"
        AddTalkListData(1, 20000010, -1)
        # action:20000011:"Sell"
        AddTalkListData(2, 20000011, -1)
        # action:23310002:"You should probably know... "
        AddTalkListDataIf(GetEventFlag(1044529262) == 1, 3, 23310002, -1)
        # action:23310003:"About the Dung Eater"
        AddTalkListDataIf(GetEventFlag(1044529263) == 1, 3, 23310003, -1)
        # action:23310004:"About the Dung Eater"
        AddTalkListDataIf(GetEventFlag(1044529264) == 1, 3, 23310004, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 8"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 5,9"""
            OpenRegularShop(100150, 100174)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 6,10"""
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 7,16"""
            assert t331006000_x52()
        else:
            """State 11"""
            # eventflag:110550:shop:100155:Boiled Crab
            if not GetEventFlag(1044529261) and GetEventFlagValue(110550, 10) > 1:
                """State 12,17"""
                # talk:33102300:"Never met someone with a taste for crab I couldn't trust."
                assert t331006000_x29(text2=33102300, mode4=1)
                """State 14"""
                SetEventFlag(1044529261, 1)
            else:
                """State 13"""
                pass
            """State 18"""
            return 0

def t331006000_x51():
    """State 0,1"""
    SetEventFlag(1044529262, 0)
    SetEventFlag(1044529263, 0)
    SetEventFlag(1044529264, 0)
    """State 2"""
    if not GetEventFlag(1044529257):
        """State 3"""
        SetEventFlag(1044529262, 1)
    elif GetEventFlag(1044529257) == 1 and not GetEventFlag(1044529258):
        """State 4"""
        SetEventFlag(1044529263, 1)
    elif (GetEventFlag(1044529258) == 1 and not GetEventFlag(1044529259) and GetEventFlag(35009306) ==
          1 and not GetEventFlag(1045520180) and not GetEventFlag(4243)):
        """State 5"""
        SetEventFlag(1044529264, 1)
    else:
        """State 6"""
        pass
    """State 7"""
    return 0

def t331006000_x52():
    """State 0,1"""
    if GetEventFlag(1044529262) == 1:
        """State 2,8"""
        # talk:33102500:"Mate, there's somethin' I should probably tell ya."
        assert t331006000_x29(text2=33102500, mode4=1)
        """State 5"""
        SetEventFlag(1044529257, 1)
    elif GetEventFlag(1044529263) == 1:
        """State 3,9"""
        # talk:33102600:"E's a killer. Kills people and curses their souls..."
        assert t331006000_x29(text2=33102600, mode4=1)
        """State 6"""
        SetEventFlag(1044529258, 1)
    else:
        """State 4,10"""
        # talk:33102700:"Yeah...and now I seen it 'ere, again."
        assert t331006000_x29(text2=33102700, mode4=1)
        """State 7"""
        SetEventFlag(1044529259, 1)
    """State 11"""
    return 0

def t331006000_x53():
    """State 0,3"""
    if not GetEventFlag(60837):
        """State 4,1"""
        SetEventFlag(60837, 1)
        """State 2"""
        # gesture:95:Spread Out
        AcquireGesture(95)
    else:
        """State 5"""
        pass
    """State 6"""
    return 0

