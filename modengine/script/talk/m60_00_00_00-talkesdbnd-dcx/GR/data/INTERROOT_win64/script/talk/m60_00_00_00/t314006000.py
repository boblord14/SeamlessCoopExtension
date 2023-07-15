# -*- coding: utf-8 -*-
def t314006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t314006000_x25(flag1=3443, flag2=3441, flag3=3442, val1=5, val2=10, val3=12, val4=15, val5=15, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1)
    def WhilePaused():
        c5_121(GetEventFlag(3450) == 1, 9620)
    Quit()

def t314006000_1000():
    """State 0,2,3"""
    assert t314006000_x0()
    """State 1"""
    c1_120(1000)
    Quit()

def t314006000_1001():
    """State 0,2,3"""
    assert t314006000_x1()
    """State 1"""
    c1_120(1001)
    Quit()

def t314006000_1101():
    """State 0,2,3"""
    assert t314006000_x2()
    """State 1"""
    c1_120(1101)
    Quit()

def t314006000_1102():
    """State 0,2,3"""
    t314006000_x3()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t314006000_1103():
    """State 0,2,3"""
    assert t314006000_x4()
    """State 1"""
    c1_120(1103)
    Quit()

def t314006000_2000():
    """State 0,2,3"""
    assert t314006000_x12()
    """State 1"""
    c1_120(2000)
    Quit()

def t314006000_x0():
    """State 0,1"""
    if GetEventFlag(3445) == 1:
        """State 3"""
        assert t314006000_x5()
    elif GetEventFlag(3446) == 1:
        """State 4"""
        assert t314006000_x6()
    elif GetEventFlag(3447) == 1:
        """State 5"""
        assert t314006000_x7()
    elif GetEventFlag(3448) == 1:
        """State 6"""
        assert t314006000_x8()
    elif GetEventFlag(3449) == 1:
        """State 7"""
        assert t314006000_x9()
    elif GetEventFlag(3450) == 1:
        """State 8"""
        assert t314006000_x10()
    elif GetEventFlag(3451) == 1:
        """State 9"""
        def WhilePaused():
            RequestAnimation(90315, -1)
        assert t314006000_x11()
    else:
        """State 2"""
        pass
    """State 10"""
    return 0

def t314006000_x1():
    """State 0,1"""
    if GetEventFlag(3450) == 1:
        """State 3,5"""
        # talk:31481200:"Unharmed, thank the stars."
        assert t314006000_x51(text1=31481200, mode3=1)
    elif GetEventFlag(3451) == 1:
        """State 4"""
        pass
    else:
        """State 2,6"""
        # talk:31480200:"Lanya, your honour has been restored."
        assert t314006000_x51(text1=31480200, mode3=1)
    """State 7"""
    return 0

def t314006000_x2():
    """State 0,6"""
    if not GetEventFlag(11102732) and not GetEventFlag(3451):
        """State 1,3"""
        if not GetEventFlag(3450):
            """State 4,7"""
            if not GetEventFlag(11102731):
                """State 9"""
                # talk:31480000:"Agh!"
                assert t314006000_x50(text2=31480000, z9=11102731, mode4=1)
            else:
                """State 10"""
                # talk:31480010:"What on earth was that for!"
                assert t314006000_x50(text2=31480010, z9=11102732, mode4=1)
        else:
            """State 5,8"""
            if not GetEventFlag(11102731):
                """State 11"""
                # talk:31481000:"Ugh!"
                assert t314006000_x50(text2=31481000, z9=11102731, mode4=1)
            else:
                """State 12"""
                # talk:31481010:"What's the matter? Please, stop!"
                assert t314006000_x50(text2=31481010, z9=11102732, mode4=1)
    else:
        """State 2"""
        pass
    """State 13"""
    return 0

def t314006000_x3():
    """State 0,1"""
    if GetEventFlag(3450) == 1:
        """State 3,6"""
        assert t314006000_x18()
    elif GetEventFlag(3451) == 1:
        """State 4"""
        pass
    else:
        """State 2,5"""
        assert t314006000_x19()
    """State 7"""
    return 0

def t314006000_x4():
    """State 0,1"""
    if GetEventFlag(3450) == 1:
        """State 3,5"""
        # talk:31481300:"Ahh, just what I deserve..."
        assert t314006000_x51(text1=31481300, mode3=1)
    elif GetEventFlag(3451) == 1:
        """State 4"""
        pass
    else:
        """State 2,6"""
        # talk:31480300:"Ha ha...ha..."
        assert t314006000_x51(text1=31480300, mode3=1)
    """State 7"""
    return 0

def t314006000_x5():
    """State 0,1"""
    if not GetEventFlag(11109406):
        """State 2,5"""
        # talk:31400100:"Ah, hello. You must be new here."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t314006000_x49(text3=31400100, mode5=1)
        """State 4"""
        SetEventFlag(11109406, 1)
    else:
        """State 3,6"""
        # talk:31400200:"Be sure to tell me if you meet a young woman named Lanya."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t314006000_x49(text3=31400200, mode5=1)
    """State 7"""
    return 0

def t314006000_x6():
    """State 0,1"""
    if GetEventFlag(1037449205) == 1:
        """State 2,6"""
        # talk:31401400:"They laid hands upon my servant Lanya,\nand I refuse to let the insult stand."
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t314006000_x49(text3=31401400, mode5=1)
    elif GetEventFlag(11109406) == 1:
        """State 3,7"""
        # talk:31401100:"Hello, friend. Tell me if you know, would you."
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t314006000_x49(text3=31401100, mode5=1)
        """State 5"""
        Label('L0')
        SetEventFlag(1037449205, 1)
    else:
        """State 4,8"""
        # talk:31401300:"Who on earth are you?"
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t314006000_x49(text3=31401300, mode5=1)
        Goto('L0')
    """State 9"""
    return 0

def t314006000_x7():
    """State 0,1"""
    if not GetEventFlag(11109430):
        """State 2,5"""
        # talk:31401200:"Ah, you again, is it?"
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t314006000_x49(text3=31401200, mode5=1)
    else:
        """State 3,6"""
        # talk:31401500:"It's on Mt. Gelmir, found off the old road that leads west\nfrom the town of windmills."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t314006000_x49(text3=31401500, mode5=1)
    """State 4"""
    SetEventFlag(11109430, 1)
    """State 7"""
    return 0

def t314006000_x8():
    """State 0,1"""
    if not GetEventFlag(16009405):
        """State 2,7"""
        # talk:31402000:"Ah. Oh... I-it's you, is it?"
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t314006000_x49(text3=31402000, mode5=1)
        """State 5"""
        SetEventFlag(16009405, 1)
    elif not GetEventFlag(16009406):
        """State 4,8"""
        # talk:31402100:"I, um, I can tell... You're wondering about Lanya..."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t314006000_x49(text3=31402100, mode5=1)
        """State 6"""
        SetEventFlag(16009406, 1)
    else:
        """State 3,9"""
        # talk:31402200:"I always resented these hands."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t314006000_x49(text3=31402200, mode5=1)
    """State 10"""
    return 0

def t314006000_x9():
    """State 0,1"""
    if not GetEventFlag(16009415):
        """State 2,6"""
        # talk:31403000:"Ah, it's you, is it."
        assert t314006000_x49(text3=31403000, mode5=1)
        """State 4"""
        SetEventFlag(16009415, 1)
    else:
        """State 3,7"""
        # talk:31403200:"Perhaps I am a fool after all..."
        assert t314006000_x49(text3=31403200, mode5=1)
    """State 5"""
    SetEventFlag(16002730, 1)
    """State 8"""
    return 0

def t314006000_x10():
    """State 0,4"""
    if not GetEventFlag(1039449305):
        """State 1,5"""
        # talk:31404100:"Oh? My friend, it's been far too long."
        assert t314006000_x49(text3=31404100, mode5=1)
        """State 3"""
        SetEventFlag(1039449305, 1)
    else:
        """State 2,6"""
        # talk:31404200:"A fool I may be, but I can look after some simple jars."
        assert t314006000_x49(text3=31404200, mode5=1)
    """State 7"""
    return 0

def t314006000_x11():
    """State 0,1"""
    assert t314006000_x13()
    """State 2"""
    return 0

def t314006000_x12():
    """State 0,1"""
    if GetEventFlag(3446) == 1:
        """State 2,8"""
        assert t314006000_x14(val7=10, z8=12)
    elif GetEventFlag(3449) == 1:
        """State 3,9"""
        assert t314006000_x15(val6=10, z7=12)
    elif GetEventFlag(3450) == 1:
        """State 4,10"""
        assert t314006000_x16(z5=10, z6=12)
    elif GetEventFlag(3451) == 1:
        """State 6,11"""
        assert t314006000_x17()
    else:
        """State 5,7"""
        # actionbutton:6000:"Talk"
        assert (t314006000_x20(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=6000))
    """State 12"""
    return 0

def t314006000_x13():
    """State 0,9"""
    # talk:31405100:"...Ah, you..."
    assert t314006000_x49(text3=31405100, mode5=1)
    """State 1"""
    ClearTalkListData()
    c1_110()
    """State 3"""
    # action:23141000:"You defended them"
    AddTalkListData(1, 23141000, -1)
    # action:23141001:"I'm afraid not"
    AddTalkListData(2, 23141001, -1)
    """State 2"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 4"""
    if GetTalkListEntryResult() == 1:
        """State 5,10"""
        # talk:31405200:"Then all is well..."
        assert t314006000_x49(text3=31405200, mode5=1)
        """State 8"""
        Label('L0')
        SetEventFlag(1039449315, 1)
    elif GetTalkListEntryResult() == 2:
        """State 6,11"""
        # talk:31405300:"Ha...ha ha..."
        assert t314006000_x49(text3=31405300, mode5=1)
        Goto('L0')
    else:
        """State 7"""
        pass
    """State 12"""
    return 0

def t314006000_x14(val7=10, z8=12):
    """State 0"""
    while True:
        """State 4"""
        # actionbutton:6000:"Talk"
        call = t314006000_x20(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                              flag4=6000)
        if call.Done():
            break
        elif GetDistanceToPlayer() < val7 and not GetEventFlag(1037442700):
            pass
        """State 1,2"""
        SetEventFlag(1037442700, 1)
        """State 5"""
        # talk:31401000:"Lanya... Lanya..."
        call = t314006000_x51(text1=31401000, mode3=1)
        if call.Done():
            pass
        elif GetEventFlag(1037449205) == 1:
            """State 3"""
            pass
    """State 6"""
    return 0

def t314006000_x15(val6=10, z7=12):
    """State 0"""
    while True:
        """State 4"""
        # actionbutton:6000:"Talk"
        call = t314006000_x20(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                              flag4=6000)
        if call.Done():
            break
        elif ((GetDistanceToPlayer() < val6 and GetEventFlag(16009415) == 1 and not GetEventFlag(16002730)
              and not GetEventFlag(16009416) and GetEventFlagValue(16009260, 4) > 2) or (GetDistanceToPlayer()
              < val6 and not GetEventFlag(16009405) and not GetEventFlag(16009416))):
            """State 1,2"""
            SetEventFlag(16009416, 1)
            """State 3"""
            # talk:31403100:"It's just as my noble brother says."
            assert t314006000_x51(text1=31403100, mode3=1)
    """State 5"""
    return 0

def t314006000_x16(z5=10, z6=12):
    """State 0"""
    while True:
        """State 5"""
        # actionbutton:6000:"Talk"
        call = t314006000_x20(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                              flag4=6000)
        if call.Done():
            break
        elif (GetDistanceToPlayer() < 9 and not GetEventFlag(1039449305) and not GetEventFlag(1039442721)
              and not GetEventFlag(1039440754)):
            pass
        """State 1,2"""
        SetEventFlag(1039442721, 1)
        """State 4"""
        # talk:31404000:"Well. Aren't you full of beans."
        call = t314006000_x51(text1=31404000, mode3=1)
        if call.Done():
            pass
        elif GetEventFlag(1039449305) == 1:
            """State 3"""
            pass
    """State 6"""
    return 0

def t314006000_x17():
    """State 0,2"""
    # actionbutton:6000:"Talk"
    call = t314006000_x20(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                          flag4=6000)
    if call.Done():
        """State 3"""
        return 0
    elif GetEventFlag(1039449315) == 1:
        """State 1"""
        Quit()

def t314006000_x18():
    """State 0,2"""
    if not GetEventFlag(11109405):
        """State 3,7"""
        SetEventFlag(11109405, 1)
        """State 6"""
        SetEventFlag(11102730, 1)
        """State 9"""
        # talk:31481100:"Why on earth...?"
        assert t314006000_x51(text1=31481100, mode3=1)
    elif not GetEventFlag(11102730):
        """State 4,8"""
        SetEventFlag(11102730, 1)
    else:
        """State 5"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 10"""
    return 0

def t314006000_x19():
    """State 0,2"""
    if not GetEventFlag(11109405):
        """State 3,7"""
        SetEventFlag(11109405, 1)
        """State 6"""
        SetEventFlag(11102730, 1)
        """State 9"""
        # talk:31480100:"Now I see. You're a wretched recusant!"
        assert t314006000_x51(text1=31480100, mode3=1)
    elif not GetEventFlag(11102730):
        """State 4,8"""
        SetEventFlag(11102730, 1)
    else:
        """State 5"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 10"""
    return 0

def t314006000_x20(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t314006000_x21():
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

def t314006000_x22():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t314006000_x23(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t314006000_x39()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t314006000_x21()
    else:
        """State 4,7"""
        call = t314006000_x53()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t314006000_x21()
    """State 9"""
    return 0

def t314006000_x24():
    """State 0,1"""
    assert t314006000_x21()
    """State 2"""
    return 0

def t314006000_x25(flag1=3443, flag2=3441, flag3=3442, val1=5, val2=10, val3=12, val4=15, val5=15, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t314006000_x42(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t314006000_x41()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t314006000_x26(val1=5, val2=10, val3=12, val4=15, val5=15, actionbutton1=6000, flag4=6000, flag5=6001,
                   flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                   mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t314006000_x29(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t314006000_x33(val1=val1, z1=z1)
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
            call = t314006000_x35(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t314006000_x46() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t314006000_x31(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t314006000_x27(val2=10, val3=12):
    """State 0,1"""
    call = t314006000_x37(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t314006000_x23(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t314006000_x28(flag1=3443, val2=10, val3=12):
    """State 0,8"""
    assert t314006000_x55()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t314006000_x40()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t314006000_x21()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t314006000_x29(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t314006000_x30(z10=2000, val8=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t314006000_x20(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t314006000_x30(z10=_, val8=_):
    """State 0,1"""
    if f203(z10) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z10)
        assert f202() == val8
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t314006000_x31(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t314006000_x21()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t314006000_x32()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t314006000_x47()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t314006000_x32():
    """State 0,1"""
    assert t314006000_x30(z10=1101, val8=1101)
    """State 2"""
    return 0

def t314006000_x33(val1=5, z1=1):
    """State 0,2"""
    assert t314006000_x43()
    """State 1"""
    call = t314006000_x34()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t314006000_x45()
    """State 4"""
    return 0

def t314006000_x34():
    """State 0,1"""
    assert t314006000_x30(z10=1000, val8=1000)
    """State 2"""
    return 0

def t314006000_x35(val5=15):
    """State 0,1"""
    call = t314006000_x36()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t314006000_x46()
    """State 3"""
    return 0

def t314006000_x36():
    """State 0,1"""
    assert t314006000_x30(z10=1100, val8=1100)
    """State 2"""
    return 0

def t314006000_x37(val2=10, val3=12):
    """State 0,5"""
    assert t314006000_x55()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t314006000_x38()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t314006000_x48()
    """Unused"""
    """State 6"""
    return 0

def t314006000_x38():
    """State 0,2"""
    call = t314006000_x30(z10=1102, val8=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t314006000_x39():
    """State 0,1"""
    assert t314006000_x30(z10=1001, val8=1001)
    """State 2"""
    return 0

def t314006000_x40():
    """State 0,1"""
    assert t314006000_x30(z10=1103, val8=1103)
    """State 2"""
    return 0

def t314006000_x41():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t314006000_x42(flag1=3443, flag2=3441, flag3=3442, val1=5, val2=10, val3=12, val4=15, val5=15, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t314006000_x26(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                              flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                              z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t314006000_x28(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t314006000_x27(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t314006000_x54() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t314006000_x43():
    """State 0,1"""
    assert t314006000_x44()
    """State 2"""
    return 0

def t314006000_x44():
    """State 0,1"""
    assert t314006000_x30(z10=1104, val8=1104)
    """State 2"""
    return 0

def t314006000_x45():
    """State 0,1"""
    call = t314006000_x30(z10=1201, val8=1201)
    if call.Get() == 1:
        """State 2"""
        assert t314006000_x24()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t314006000_x46():
    """State 0,1"""
    call = t314006000_x30(z10=1300, val8=1300)
    if call.Get() == 1:
        """State 2"""
        assert t314006000_x24()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t314006000_x47():
    """State 0,1"""
    call = t314006000_x30(z10=1301, val8=1301)
    if call.Get() == 1:
        """State 2"""
        assert t314006000_x24()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t314006000_x48():
    """State 0,1"""
    call = t314006000_x30(z10=1302, val8=1302)
    if call.Get() == 1:
        """State 2"""
        assert t314006000_x24()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t314006000_x49(text3=_, mode5=1):
    """State 0,4"""
    assert t314006000_x22() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t314006000_x50(text2=_, z9=_, mode4=1):
    """State 0,5"""
    assert t314006000_x52() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(z9, 1)
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

def t314006000_x51(text1=_, mode3=1):
    """State 0,4"""
    assert t314006000_x52() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t314006000_x52():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t314006000_x53():
    """State 0,1"""
    assert t314006000_x30(z10=1002, val8=1002)
    """State 2"""
    return 0

def t314006000_x54():
    """State 0,1"""
    assert t314006000_x21()
    """State 2"""
    return 0

def t314006000_x55():
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

