# -*- coding: utf-8 -*-
def t312026000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t312026000_x6(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t312026000_1000():
    """State 0,2,3"""
    assert t312026000_x35()
    """State 1"""
    c1_120(1000)
    Quit()

def t312026000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t312026000_x1():
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

def t312026000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t312026000_x3(lot1=104000):
    """State 0,1"""
    # lot:104000:Ancient Dragon Smithing Stone
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t312026000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t312026000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t312026000_x1()
    else:
        """State 4,7"""
        call = t312026000_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t312026000_x1()
    """State 9"""
    return 0

def t312026000_x5():
    """State 0,1"""
    assert t312026000_x1()
    """State 2"""
    return 0

def t312026000_x6(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t312026000_x23(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t312026000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t312026000_x7(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t312026000_x10(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t312026000_x14(val1=val1, z1=z1)
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
            call = t312026000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t312026000_x27() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t312026000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t312026000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t312026000_x18(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t312026000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t312026000_x9(flag1=6000, val2=10, val3=12):
    """State 0,8"""
    assert t312026000_x34()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t312026000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t312026000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t312026000_x10(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t312026000_x11(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t312026000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t312026000_x11(z6=_, val6=_):
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

def t312026000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t312026000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t312026000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t312026000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t312026000_x13():
    """State 0,1"""
    assert t312026000_x11(z6=1101, val6=1101)
    """State 2"""
    return 0

def t312026000_x14(val1=5, z1=1):
    """State 0,2"""
    assert t312026000_x24()
    """State 1"""
    call = t312026000_x15()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t312026000_x26()
    """State 4"""
    return 0

def t312026000_x15():
    """State 0,1"""
    assert t312026000_x11(z6=1000, val6=1000)
    """State 2"""
    return 0

def t312026000_x16(val5=12):
    """State 0,1"""
    call = t312026000_x17()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t312026000_x27()
    """State 3"""
    return 0

def t312026000_x17():
    """State 0,1"""
    assert t312026000_x11(z6=1100, val6=1100)
    """State 2"""
    return 0

def t312026000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t312026000_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t312026000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t312026000_x29()
    """Unused"""
    """State 6"""
    return 0

def t312026000_x19():
    """State 0,2"""
    call = t312026000_x11(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t312026000_x20():
    """State 0,1"""
    assert t312026000_x11(z6=1001, val6=1001)
    """State 2"""
    return 0

def t312026000_x21():
    """State 0,1"""
    assert t312026000_x11(z6=1103, val6=1103)
    """State 2"""
    return 0

def t312026000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t312026000_x23(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t312026000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t312026000_x9(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t312026000_x8(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t312026000_x33() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t312026000_x24():
    """State 0,1"""
    assert t312026000_x25()
    """State 2"""
    return 0

def t312026000_x25():
    """State 0,1"""
    assert t312026000_x11(z6=1104, val6=1104)
    """State 2"""
    return 0

def t312026000_x26():
    """State 0,1"""
    call = t312026000_x11(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t312026000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t312026000_x27():
    """State 0,1"""
    call = t312026000_x11(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t312026000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t312026000_x28():
    """State 0,1"""
    call = t312026000_x11(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t312026000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t312026000_x29():
    """State 0,1"""
    call = t312026000_x11(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t312026000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t312026000_x30(text2=_, z5=_, mode4=1):
    """State 0,5"""
    assert t312026000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text2, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode4:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(z5, 1)
    """State 6"""
    return 0

def t312026000_x31(text1=_, mode3=1):
    """State 0,4"""
    assert t312026000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text1, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode3:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t312026000_x32():
    """State 0,1"""
    assert t312026000_x11(z6=1002, val6=1002)
    """State 2"""
    return 0

def t312026000_x33():
    """State 0,1"""
    assert t312026000_x1()
    """State 2"""
    return 0

def t312026000_x34():
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

def t312026000_x35():
    """State 0,1"""
    if GetEventFlag(3365) == 1:
        """State 7"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t312026000_x40()
    elif GetEventFlag(3366) == 1:
        """State 8"""
        assert t312026000_x38()
    elif GetEventFlag(3367) == 1:
        """State 6"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t312026000_x39()
    elif GetEventFlag(3368) == 1:
        """State 2"""
        pass
    elif GetEventFlag(3369) == 1:
        """State 9"""
        assert t312026000_x41()
    elif GetEventFlag(3370) == 1:
        """State 5"""
        pass
    elif GetEventFlag(3371) == 1:
        """State 10"""
        assert t312026000_x43()
    elif GetEventFlag(3371) == 1:
        """State 3"""
        pass
    else:
        """State 4"""
        pass
    """State 11"""
    return 0

def t312026000_x36():
    """State 0,1"""
    if not GetEventFlag(1051369205):
        """State 16"""
        # talk:31200100:"Oh, Tarnished, are you?"
        assert t312026000_x31(text1=31200100, mode3=1)
        """State 2"""
        ClearTalkListData()
        c1_110()
        """State 3"""
        # action:23121000:"I love a good festival"
        AddTalkListData(1, 23121000, -1)
        # action:23121001:"I'm not the festive type"
        AddTalkListData(2, 23121001, -1)
        """State 4"""
        OpenConversationChoicesMenu(0)
        """State 8"""
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 12"""
            # talk:31200200:"Well, good."
            assert t312026000_x30(text2=31200200, z5=1051369206, mode4=1)
        elif GetTalkListEntryResult() == 2:
            """State 13"""
            # talk:31200300:"Well, you're not much fun, are you, chum?"
            assert t312026000_x31(text1=31200300, mode3=1)
        else:
            """State 9"""
            Goto('L0')
        """State 7"""
        SetEventFlag(1051369205, 1)
    elif not GetEventFlag(1051369211):
        """State 6"""
        if GetEventFlag(1051369206) == 1:
            """State 15"""
            # talk:31200400:"Have patience, mm."
            assert t312026000_x31(text1=31200400, mode3=1)
        else:
            """State 14"""
            # talk:31200600:"One day you will see, chum."
            assert t312026000_x31(text1=31200600, mode3=1)
        """State 10"""
        SetEventFlag(1051369211, 1)
    else:
        """State 11"""
        if GetEventFlag(1051369206) == 1:
            """State 17"""
            # talk:31200500:"Go on, now."
            assert t312026000_x31(text1=31200500, mode3=1)
        else:
            """State 18"""
            # talk:31200700:"Go on, now."
            assert t312026000_x31(text1=31200700, mode3=1)
    """State 19"""
    Label('L0')
    return 0

def t312026000_x37():
    """State 0,1"""
    if GetEventFlag(1034509410) == 1 and not GetEventFlag(1051369210):
        """State 2"""
        ClearTalkListData()
        c1_110()
        """State 3"""
        # action:23121003:"About Iji"
        AddTalkListData(1, 23121003, -1)
        # action:20000009:"Leave"
        AddTalkListData(99, 20000009, -1)
        """State 4"""
        OpenConversationChoicesMenu(0)
        """State 7"""
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 8"""
            # talk:31202000:"Well, I haven't heard that name in an age."
            assert t312026000_x30(text2=31202000, z5=1051369210, mode4=1)
        else:
            """State 6"""
            pass
    else:
        pass
    """State 9"""
    return 0

def t312026000_x38():
    """State 0,7"""
    if GetEventFlag(9410) == 1 and not GetEventFlag(9411):
        """State 12"""
        # talk:31203100:"Are you good and prepared, young chum?"
        assert t312026000_x31(text1=31203100, mode3=1)
        """State 1"""
        ClearTalkListData()
        c1_110()
        """State 2"""
        # action:23121004:"Ready as I'll ever be"
        AddTalkListData(1, 23121004, -1)
        # action:23121005:"Not yet"
        AddTalkListData(2, 23121005, -1)
        """State 3"""
        OpenConversationChoicesMenu(0)
        """State 5"""
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 8"""
            SetEventFlag(1051362702, 1)
            assert GetEventFlag(9411) == 1 and GetCurrentStateElapsedTime() > 0.8
            """State 15"""
            # talk:31203400:"But now, we must make merry."
            assert t312026000_x31(text1=31203400, mode3=1)
            """State 10"""
            if not GetEventFlag(60821):
                """State 9"""
                # gesture:51:Heartening Cry
                AcquireGesture(51)
                SetEventFlag(60821, 1)
            else:
                """State 11"""
                pass
        elif GetTalkListEntryResult() == 2:
            """State 13"""
            # talk:31203600:"I see..."
            assert t312026000_x31(text1=31203600, mode3=1)
        else:
            """State 6"""
            pass
    else:
        """State 14"""
        # talk:31203500:"You will find the field of battle past the church ahead, upon the shore under the fort."
        assert t312026000_x31(text1=31203500, mode3=1)
    """State 16"""
    return 0

def t312026000_x39():
    """State 0,1"""
    if not GetEventFlag(1051369235):
        """State 2"""
        # talk:31204000:"At last, the war festival has ended."
        assert t312026000_x30(text2=31204000, z5=1051369235, mode4=1)
    elif not GetEventFlag(1051369236):
        """State 4"""
        # talk:31204100:"Finally, my work is done."
        assert t312026000_x30(text2=31204100, z5=1051369236, mode4=1)
    else:
        """State 3"""
        # talk:31204200:"It's time I went on my way."
        assert t312026000_x31(text1=31204200, mode3=1)
    """State 5"""
    return 0

def t312026000_x40():
    """State 0,1"""
    assert t312026000_x36()
    """State 2"""
    assert t312026000_x37()
    """State 3"""
    return 0

def t312026000_x41():
    """State 0,1"""
    assert t312026000_x42()
    """State 2"""
    return 0

def t312026000_x42():
    """State 0,1"""
    if not GetEventFlag(1041339255):
        """State 4"""
        # talk:31205000:"Ah, well met."
        assert t312026000_x31(text1=31205000, mode3=1)
        """State 2"""
        SetEventFlag(1041339255, 1)
    elif not GetEventFlag(1041339256):
        """State 5"""
        # talk:31205200:"It is strange, though..."
        assert t312026000_x31(text1=31205200, mode3=1)
        """State 3"""
        SetEventFlag(1041339256, 1)
    else:
        """State 6"""
        # talk:31205300:"I suspect Sellen lives on, elsewhere."
        assert t312026000_x31(text1=31205300, mode3=1)
    """State 7"""
    return 0

def t312026000_x43():
    """State 0,1"""
    assert t312026000_x44()
    """State 2"""
    return 0

def t312026000_x44():
    """State 0,1"""
    if not GetEventFlag(14009355) and GetEventFlag(1034509410) == 1:
        """State 4"""
        # talk:31206000:"My thanks, for the aid given."
        assert t312026000_x31(text1=31206000, mode3=1)
        """State 8"""
        Label('L0')
        # lot:104000:Ancient Dragon Smithing Stone
        assert t312026000_x3(lot1=104000)
        """State 2"""
        SetEventFlag(14009355, 1)
    elif not GetEventFlag(14009355) and not GetEventFlag(1034509410):
        """State 5"""
        # talk:31206100:"My thanks, for the aid given."
        assert t312026000_x31(text1=31206100, mode3=1)
        Goto('L0')
    elif not GetEventFlag(14009356):
        """State 6"""
        # talk:31206300:"Well, I must be leaving now."
        assert t312026000_x31(text1=31206300, mode3=1)
        """State 3"""
        SetEventFlag(14009356, 1)
    else:
        """State 7"""
        # talk:31206400:"Well, I must be leaving now."
        assert t312026000_x31(text1=31206400, mode3=1)
    """State 9"""
    return 0

