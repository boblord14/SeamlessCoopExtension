# -*- coding: utf-8 -*-
def t226006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t226006000_x5(flag1=3823, flag2=3821, flag3=3822, val1=5, val2=10, val3=10, val4=10, val5=10, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    def WhilePaused():
        c5_121(GetEventFlag(3827) == 1 and not GetEventFlag(1039449270), 9620)
    Quit()

def t226006000_1000():
    """State 0,2,3"""
    assert t226006000_x36()
    """State 1"""
    c1_120(1000)
    Quit()

def t226006000_1101():
    """State 0,2,3"""
    assert t226006000_x37()
    """State 1"""
    c1_120(1101)
    Quit()

def t226006000_1102():
    """State 0,2,3"""
    t226006000_x38()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t226006000_2000():
    """State 0,2,3"""
    assert t226006000_x39()
    """State 1"""
    c1_120(2000)
    Quit()

def t226006000_x0(actionbutton1=_, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag4=6000):
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

def t226006000_x1():
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

def t226006000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t226006000_x3(val2=10, val3=10):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t226006000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t226006000_x1()
    else:
        """State 4,7"""
        call = t226006000_x33()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t226006000_x1()
    """State 9"""
    return 0

def t226006000_x4():
    """State 0,1"""
    assert t226006000_x1()
    """State 2"""
    return 0

def t226006000_x5(flag1=3823, flag2=3821, flag3=3822, val1=5, val2=10, val3=10, val4=10, val5=10, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t226006000_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t226006000_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t226006000_x6(val1=5, val2=10, val3=10, val4=10, val5=10, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t226006000_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t226006000_x13(val1=val1, z1=z1)
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
            call = t226006000_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t226006000_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t226006000_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t226006000_x7(val2=10, val3=10):
    """State 0,1"""
    call = t226006000_x17(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t226006000_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t226006000_x8(flag1=3823, val2=10, val3=10):
    """State 0,8"""
    assert t226006000_x35()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t226006000_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t226006000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t226006000_x9(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t226006000_x10(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t226006000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t226006000_x10(z6=_, val6=_):
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

def t226006000_x11(val2=10, val3=10):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t226006000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t226006000_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t226006000_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t226006000_x12():
    """State 0,1"""
    assert t226006000_x10(z6=1101, val6=1101)
    """State 2"""
    return 0

def t226006000_x13(val1=5, z1=1):
    """State 0,2"""
    assert t226006000_x23()
    """State 1"""
    call = t226006000_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t226006000_x25()
    """State 4"""
    return 0

def t226006000_x14():
    """State 0,1"""
    assert t226006000_x10(z6=1000, val6=1000)
    """State 2"""
    return 0

def t226006000_x15(val5=10):
    """State 0,1"""
    call = t226006000_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t226006000_x26()
    """State 3"""
    return 0

def t226006000_x16():
    """State 0,1"""
    assert t226006000_x10(z6=1100, val6=1100)
    """State 2"""
    return 0

def t226006000_x17(val2=10, val3=10):
    """State 0,5"""
    assert t226006000_x35()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t226006000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t226006000_x28()
    """Unused"""
    """State 6"""
    return 0

def t226006000_x18():
    """State 0,2"""
    call = t226006000_x10(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t226006000_x19():
    """State 0,1"""
    assert t226006000_x10(z6=1001, val6=1001)
    """State 2"""
    return 0

def t226006000_x20():
    """State 0,1"""
    assert t226006000_x10(z6=1103, val6=1103)
    """State 2"""
    return 0

def t226006000_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t226006000_x22(flag1=3823, flag2=3821, flag3=3822, val1=5, val2=10, val3=10, val4=10, val5=10, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t226006000_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t226006000_x8(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t226006000_x7(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t226006000_x34() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t226006000_x23():
    """State 0,1"""
    assert t226006000_x24()
    """State 2"""
    return 0

def t226006000_x24():
    """State 0,1"""
    assert t226006000_x10(z6=1104, val6=1104)
    """State 2"""
    return 0

def t226006000_x25():
    """State 0,1"""
    call = t226006000_x10(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t226006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t226006000_x26():
    """State 0,1"""
    call = t226006000_x10(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t226006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t226006000_x27():
    """State 0,1"""
    call = t226006000_x10(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t226006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t226006000_x28():
    """State 0,1"""
    call = t226006000_x10(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t226006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t226006000_x29(text3=_, mode5=1):
    """State 0,4"""
    assert t226006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t226006000_x30(text2=_, z5=_, mode4=1):
    """State 0,5"""
    assert t226006000_x32() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t226006000_x31(text1=_, mode3=1):
    """State 0,4"""
    assert t226006000_x32() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t226006000_x32():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t226006000_x33():
    """State 0,1"""
    assert t226006000_x10(z6=1002, val6=1002)
    """State 2"""
    return 0

def t226006000_x34():
    """State 0,1"""
    assert t226006000_x1()
    """State 2"""
    return 0

def t226006000_x35():
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

def t226006000_x36():
    """State 0,7"""
    call = t226006000_x53()
    def WhilePaused():
        RequestAnimationIf(GetEventFlag(3825) == 1 or GetEventFlag(3826) == 1, 20025, -1)
        RequestAnimationIf(GetEventFlag(3827) == 1 or GetEventFlag(3828) == 1, 20028, -1)
    if call.Get() == 0:
        """State 1"""
        if GetEventFlag(3825) == 1:
            """State 3"""
            def WhilePaused():
                RequestAnimation(20025, -1)
            assert t226006000_x40()
        elif GetEventFlag(3826) == 1:
            """State 4"""
            def WhilePaused():
                RequestAnimation(20025, -1)
            assert t226006000_x42()
        elif GetEventFlag(3827) == 1:
            """State 5"""
            def WhilePaused():
                RequestAnimation(20028, -1)
            assert t226006000_x46()
        elif GetEventFlag(3828) == 1:
            """State 6"""
            assert t226006000_x48()
        else:
            """State 2"""
            pass
    elif call.Get() == 1:
        pass
    """State 8"""
    return 0

def t226006000_x37():
    """State 0,1"""
    if not GetEventFlag(1039442710):
        """State 3"""
        SetEventFlag(1039442716, 0)
        """State 5"""
        RequestAnimation(20054, -1)
        # talk:22680000:"Oh?"
        assert t226006000_x30(text2=22680000, z5=1039442710, mode4=1)
    elif not GetEventFlag(1039442711):
        """State 4"""
        # talk:22680100:"What's the matter, coz?"
        assert t226006000_x30(text2=22680100, z5=1039442711, mode4=1)
    else:
        """State 2"""
        pass
    """State 6"""
    return 0

def t226006000_x38():
    """State 0,2"""
    if not GetEventFlag(1039449253):
        """State 5"""
        SetEventFlag(1039449253, 1)
        """State 4"""
        if not GetEventFlag(1039449263):
            """State 6"""
            # talk:22680200:"Is this who you are, coz?"
            assert t226006000_x31(text1=22680200, mode3=1)
        elif not GetEventFlag(3827) and not GetEventFlag(3828):
            """State 7"""
            # talk:22680300:"You were a poacher, all along."
            assert t226006000_x31(text1=22680300, mode3=1)
        else:
            """State 8"""
            # talk:22680400:"So, you were a poacher, too."
            assert t226006000_x31(text1=22680400, mode3=1)
    else:
        """State 3"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 9"""
    return 0

def t226006000_x39():
    """State 0,1"""
    if not GetEventFlag(3828) or (GetEventFlag(3828) == 1 and GetEventFlag(1039449296) == 1):
        """State 2"""
        # actionbutton:6260:"Talk"
        assert (t226006000_x0(actionbutton1=6260, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                flag4=6000))
    else:
        """State 3"""
        # actionbutton:6000:"Talk"
        assert (t226006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                flag4=6000))
    """State 4"""
    return 0

def t226006000_x40():
    """State 0,1"""
    if not GetEventFlag(1039449255) or GetEventFlag(1039442712) == 1:
        """State 2"""
        assert t226006000_x41()
    else:
        """State 3"""
        assert t226006000_x51()
    """State 4"""
    return 0

def t226006000_x41():
    """State 0,10"""
    SetEventFlag(1039442712, 1)
    """State 9"""
    if not GetEventFlag(1039449255) and not GetEventFlag(1039449256):
        """State 11"""
        # talk:22600100:"Hallo coz, what are you doing here?"
        assert t226006000_x29(text3=22600100, mode5=1)
        """State 1"""
        Label('L0')
        ClearTalkListData()
        c1_110()
        """State 2"""
        # action:22261000:"I'll be your Potentate"
        AddTalkListData(1, 22261000, -1)
        # action:22261001:"I'm no Potentate"
        AddTalkListData(2, 22261001, -1)
        """State 3"""
        OpenConversationChoicesMenu(0)
        """State 4"""
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 12"""
            # talk:22600200:"Gosh, truly? That's wonderful news!"
            assert t226006000_x29(text3=22600200, mode5=1)
            """State 6"""
            SetEventFlag(1039449255, 1)
            """State 17"""
            call = t226006000_x56()
            if call.Done():
                pass
            elif GetCurrentStateElapsedTime() > 10:
                pass
            """State 13"""
            # talk:22600300:"Hmm."
            assert t226006000_x29(text3=22600300, mode5=1)
        elif GetTalkListEntryResult() == 2:
            """State 14"""
            # talk:22600600:"Oh, well, I'm sorry."
            assert t226006000_x29(text3=22600600, mode5=1)
            """State 7"""
            SetEventFlag(1039449256, 1)
        else:
            """State 8"""
            pass
    elif not GetEventFlag(1039449255):
        """State 15"""
        # talk:22600700:"Coz. You'll be our Potentate after all, then?"
        assert t226006000_x29(text3=22600700, mode5=1)
        Goto('L0')
    else:
        """State 16"""
        # talk:22600800:"Don't look so glum, coz."
        assert t226006000_x29(text3=22600800, mode5=1)
    """State 18"""
    return 0

def t226006000_x42():
    """State 0,1"""
    if ((GetEventFlag(1039449261) == 1 and GetEventFlag(11109430) == 1 and not GetEventFlag(1039442712))
        or (GetEventFlag(1039449261) == 1 and GetEventFlag(3443) == 1 and GetEventFlag(3063) == 1 and
        not GetEventFlag(1039442712))):
        """State 2"""
        if not GetEventFlag(3450):
            """State 6"""
            assert t226006000_x44()
        else:
            """State 4"""
            assert t226006000_x52()
    else:
        """State 3"""
        if GetEventFlag(1043399313) == 1:
            """State 8"""
            assert t226006000_x43()
        else:
            """State 7"""
            assert t226006000_x54()
    """State 5"""
    assert t226006000_x45()
    """State 9"""
    return 0

def t226006000_x43():
    """State 0,5"""
    if not GetEventFlag(1039442716):
        """State 1"""
        if not GetEventFlag(1039449260):
            """State 6"""
            # talk:22603000:"Ah, hallo again."
            assert t226006000_x29(text3=22603000, mode5=1)
            """State 2"""
            SetEventFlag(1039449260, 1)
        elif not GetEventFlag(1039449261):
            """State 7"""
            # talk:22603100:"Uncle Alexander said he won't be back again."
            assert t226006000_x29(text3=22603100, mode5=1)
            """State 4"""
            SetEventFlag(1039449261, 1)
        else:
            """State 8"""
            # talk:22603200:"Uncle Alexander won't come back here again."
            assert t226006000_x29(text3=22603200, mode5=1)
        """State 3"""
        SetEventFlag(1039442712, 1)
    else:
        """State 9"""
        # talk:22608400:"..."
        assert t226006000_x29(text3=22608400, mode5=1)
    """State 10"""
    return 0

def t226006000_x44():
    """State 0,4"""
    if not GetEventFlag(1039442716):
        """State 3"""
        SetEventFlag(1039442713, 1)
        """State 1"""
        if not GetEventFlag(1039449263):
            """State 5"""
            # talk:22604000:"Ah, hallo again."
            assert t226006000_x29(text3=22604000, mode5=1)
            """State 2"""
            SetEventFlag(1039449263, 1)
        else:
            """State 6"""
            # talk:22604100:"Those awful poachers. I hope uncle Alexander beats them all up."
            assert t226006000_x29(text3=22604100, mode5=1)
    else:
        """State 7"""
        # talk:22608500:"..."
        assert t226006000_x29(text3=22608500, mode5=1)
    """State 8"""
    return 0

def t226006000_x45():
    """State 0,2"""
    if GetEventFlag(3443) == 1:
        """State 1"""
        # goods:8222:Alexander's Innards
        if ComparePlayerInventoryNumber(3, 8222, 0, 1, 0) == 1:
            """State 3"""
            ClearTalkListData()
            c1_110()
            """State 4"""
            # action:22261002:"Give Alexander's Insides"
            AddTalkListData(1, 22261002, -1)
            # action:22261003:"Don't give"
            AddTalkListData(2, 22261003, -1)
            """State 5"""
            OpenConversationChoicesMenu(0)
            """State 6"""
            assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 7"""
            if GetTalkListEntryResult() == 1:
                """State 11"""
                # talk:22607100:"Wow, coz, are these..."
                assert t226006000_x29(text3=22607100, mode5=1)
                """State 10"""
                # goods:8222:Alexander's Innards
                PlayerEquipmentQuantityChange(3, 8222, -1)
                """State 8"""
                SetEventFlag(1039449289, 1)
            else:
                """State 9"""
                pass
        else:
            pass
    else:
        pass
    """State 12"""
    return 0

def t226006000_x46():
    """State 0,1"""
    assert t226006000_x47()
    """State 2"""
    return 0

def t226006000_x47():
    """State 0,1"""
    if not GetEventFlag(1039449270):
        """State 3"""
        # talk:22606000:"O-oh! Coz!"
        assert t226006000_x29(text3=22606000, mode5=1)
        """State 2"""
        SetEventFlag(1039449270, 1)
    else:
        """State 4"""
        # talk:22606100:""The tale of House Hoslow is told in blood.""
        assert t226006000_x29(text3=22606100, mode5=1)
    """State 5"""
    return 0

def t226006000_x48():
    """State 0,1"""
    if not GetEventFlag(1039449285) or GetEventFlag(1039442712) == 1:
        """State 3"""
        def WhilePaused():
            RequestAnimation(20031, -1)
        assert t226006000_x55()
    elif not GetEventFlag(1039449280) or GetEventFlag(1039442713) == 1:
        """State 4"""
        def WhilePaused():
            RequestAnimation(20025, -1)
        assert t226006000_x49()
        """State 2"""
        Label('L0')
        assert t226006000_x45()
    else:
        """State 5"""
        def WhilePaused():
            RequestAnimation(20025, -1)
        assert t226006000_x50()
        Goto('L0')
    """State 6"""
    return 0

def t226006000_x49():
    """State 0,1"""
    if not GetEventFlag(1039449280):
        """State 4"""
        # talk:22607000:"Thanks for coming back, coz."
        assert t226006000_x29(text3=22607000, mode5=1)
        """State 2"""
        SetEventFlag(1039449280, 1)
    else:
        """State 5"""
        # talk:22607200:"I'm about to go on a journey."
        assert t226006000_x29(text3=22607200, mode5=1)
    """State 3"""
    SetEventFlag(1039442713, 1)
    """State 6"""
    return 0

def t226006000_x50():
    """State 0,3"""
    if not GetEventFlag(1039442716):
        """State 1"""
        if not GetEventFlag(1039449282):
            """State 4"""
            # talk:22607300:"Oh, hallo again, coz."
            assert t226006000_x29(text3=22607300, mode5=1)
            """State 2"""
            SetEventFlag(1039449282, 1)
        else:
            """State 5"""
            # talk:22607400:"I'll begin my journey once I'm ready to go."
            assert t226006000_x29(text3=22607400, mode5=1)
    else:
        """State 6"""
        # talk:22608700:"..."
        assert t226006000_x29(text3=22608700, mode5=1)
    """State 7"""
    return 0

def t226006000_x51():
    """State 0,4"""
    if not GetEventFlag(1039442716):
        """State 1"""
        if not GetEventFlag(1039449258):
            """State 5"""
            # talk:22600400:"Oh, hallo again, coz."
            assert t226006000_x29(text3=22600400, mode5=1)
            """State 2"""
            SetEventFlag(1039449258, -1)
        elif not GetEventFlag(1039442713):
            """State 7"""
            # talk:22600410:"Oh, hallo again, coz."
            assert t226006000_x29(text3=22600410, mode5=1)
        else:
            """State 6"""
            # talk:22600900:"Go on, coz, you really should pick some of our flowers."
            assert t226006000_x29(text3=22600900, mode5=1)
            Goto('L0')
        """State 3"""
        SetEventFlag(1039442713, 1)
    else:
        """State 8"""
        # talk:22608300:"..."
        assert t226006000_x29(text3=22608300, mode5=1)
    """State 9"""
    Label('L0')
    return 0

def t226006000_x52():
    """State 0,4"""
    if not GetEventFlag(1039442716):
        """State 1"""
        if not GetEventFlag(1039449265):
            """State 5"""
            # talk:22605000:"Oh, hallo again, coz."
            assert t226006000_x29(text3=22605000, mode5=1)
            """State 2"""
            SetEventFlag(1039449265, 1)
        elif not GetEventFlag(1039449266):
            """State 6"""
            # talk:22605100:"I don't know, I'm a little disappointed actually."
            assert t226006000_x29(text3=22605100, mode5=1)
            """State 3"""
            SetEventFlag(1039449266, 1)
        else:
            """State 7"""
            # talk:22605200:"Diallos' smooth and silky hands feel nice when he pats us..."
            assert t226006000_x29(text3=22605200, mode5=1)
    else:
        """State 8"""
        # talk:22608600:"..."
        assert t226006000_x29(text3=22608600, mode5=1)
    """State 9"""
    return 0

def t226006000_x53():
    """State 0,3"""
    if GetEventFlag(1039449289) == 1:
        pass
    else:
        Goto('L0')
    """State 1"""
    if GetEventFlag(3826) == 1 and not GetEventFlag(1039449290):
        """State 5"""
        # talk:22607110:"I'll begin my journey once I'm ready to go."
        assert t226006000_x29(text3=22607110, mode5=1)
        """State 2"""
        SetEventFlag(1039449290, 1)
    elif not GetEventFlag(1039449291):
        """State 6"""
        # talk:22608000:"I don't think I'll see you again, when I set out."
        assert t226006000_x29(text3=22608000, mode5=1)
        """State 4"""
        SetEventFlag(1039449291, 1)
    else:
        """State 7"""
        # talk:22608100:"I'll never forget you, coz."
        assert t226006000_x29(text3=22608100, mode5=1)
    """State 9"""
    return 1
    """State 8"""
    Label('L0')
    return 0

def t226006000_x54():
    """State 0,4"""
    if not GetEventFlag(1039442716):
        """State 1"""
        if not GetEventFlag(1039442712):
            """State 6"""
            # talk:22600410:"Oh, hallo again, coz."
            assert t226006000_x29(text3=22600410, mode5=1)
            """State 2"""
            SetEventFlag(1039449261, 1)
        else:
            """State 5"""
            # talk:22600900:"Go on, coz, you really should pick some of our flowers."
            assert t226006000_x29(text3=22600900, mode5=1)
        """State 3"""
        SetEventFlag(1039442712, 1)
    else:
        """State 7"""
        # talk:22608300:"..."
        assert t226006000_x29(text3=22608300, mode5=1)
    """State 8"""
    return 0

def t226006000_x55():
    """State 0,3"""
    # talk:22606200:""The tale of House Hoslow is told in blood.""
    assert t226006000_x29(text3=22606200, mode5=1)
    """State 1"""
    SetEventFlag(1039442712, 1)
    """State 2"""
    SetEventFlag(1039449285, 1)
    """State 4"""
    return 0

def t226006000_x56():
    """State 0,1"""
    TurnCharacterToFaceEntity(-1, 10000, -1, -1)
    assert GetWhetherChrEventAnimHasEnded(10000) == 1 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    TurnCharacterToFaceEntity(60010, 10000, -1, -1)
    assert GetWhetherChrEventAnimHasEnded(10000) == 1 and GetCurrentStateElapsedFrames() > 1
    """State 3"""
    return 0

