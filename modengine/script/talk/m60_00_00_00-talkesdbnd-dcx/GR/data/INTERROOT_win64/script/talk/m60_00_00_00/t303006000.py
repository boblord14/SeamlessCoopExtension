# -*- coding: utf-8 -*-
def t303006000_1():
    """State 0"""
    while True:
        """State 2"""
        # actionbutton:6000:"Talk"
        call = t303006000_x5(flag1=3283, flag2=3281, flag3=3282, val1=5, val2=10, val3=12, val4=10, val5=12,
                             actionbutton1=6000, flag4=6000, flag5=6001, flag6=1043359216, flag7=1043359217,
                             flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1)
        assert not GetEventFlag(3285)
        """State 3"""
        assert t303006000_x1()
        """State 1"""
        assert GetEventFlag(3285) == 1

def t303006000_1000():
    """State 0,2,3"""
    assert t303006000_x37()
    """State 1"""
    c1_120(1000)
    Quit()

def t303006000_1001():
    """State 0,2,3"""
    assert t303006000_x38()
    """State 1"""
    c1_120(1001)
    Quit()

def t303006000_1100():
    """State 0,2,3"""
    assert t303006000_x39()
    """State 1"""
    c1_120(1100)
    Quit()

def t303006000_1101():
    """State 0,2,3"""
    assert t303006000_x40()
    """State 1"""
    c1_120(1101)
    Quit()

def t303006000_1102():
    """State 0,2,3"""
    t303006000_x41()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t303006000_1103():
    """State 0,2,3"""
    assert t303006000_x42()
    """State 1"""
    c1_120(1103)
    Quit()

def t303006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t303006000_x1():
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

def t303006000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t303006000_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t303006000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t303006000_x1()
    else:
        """State 4,7"""
        call = t303006000_x34()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t303006000_x1()
    """State 9"""
    return 0

def t303006000_x4():
    """State 0,1"""
    assert t303006000_x1()
    """State 2"""
    return 0

def t303006000_x5(flag1=3283, flag2=3281, flag3=3282, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=1043359216, flag7=1043359217, flag8=6000, z1=1, z2=1000000,
                  z3=1000000, z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t303006000_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t303006000_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t303006000_x6(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=1043359216, flag7=1043359217, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000,
                  mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t303006000_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t303006000_x13(val1=val1, z1=z1)
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
            call = t303006000_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t303006000_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t303006000_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t303006000_x7(val2=10, val3=12):
    """State 0,1"""
    call = t303006000_x17(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t303006000_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t303006000_x8(flag1=3283, val2=10, val3=12):
    """State 0,8"""
    assert t303006000_x36()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t303006000_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t303006000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t303006000_x9(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t303006000_x10(z7=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t303006000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t303006000_x10(z7=_, val6=_):
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

def t303006000_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t303006000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t303006000_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t303006000_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t303006000_x12():
    """State 0,1"""
    assert t303006000_x10(z7=1101, val6=1101)
    """State 2"""
    return 0

def t303006000_x13(val1=5, z1=1):
    """State 0,2"""
    assert t303006000_x23()
    """State 1"""
    call = t303006000_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t303006000_x25()
    """State 4"""
    return 0

def t303006000_x14():
    """State 0,1"""
    assert t303006000_x10(z7=1000, val6=1000)
    """State 2"""
    return 0

def t303006000_x15(val5=12):
    """State 0,1"""
    call = t303006000_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t303006000_x26()
    """State 3"""
    return 0

def t303006000_x16():
    """State 0,1"""
    assert t303006000_x10(z7=1100, val6=1100)
    """State 2"""
    return 0

def t303006000_x17(val2=10, val3=12):
    """State 0,5"""
    assert t303006000_x36()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t303006000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t303006000_x28()
    """Unused"""
    """State 6"""
    return 0

def t303006000_x18():
    """State 0,2"""
    call = t303006000_x10(z7=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t303006000_x19():
    """State 0,1"""
    assert t303006000_x10(z7=1001, val6=1001)
    """State 2"""
    return 0

def t303006000_x20():
    """State 0,1"""
    assert t303006000_x10(z7=1103, val6=1103)
    """State 2"""
    return 0

def t303006000_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t303006000_x22(flag1=3283, flag2=3281, flag3=3282, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=1043359216, flag7=1043359217, flag8=6000, z1=1, z2=1000000,
                   z3=1000000, z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t303006000_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t303006000_x8(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t303006000_x7(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t303006000_x35() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t303006000_x23():
    """State 0,1"""
    assert t303006000_x24()
    """State 2"""
    return 0

def t303006000_x24():
    """State 0,1"""
    assert t303006000_x10(z7=1104, val6=1104)
    """State 2"""
    return 0

def t303006000_x25():
    """State 0,1"""
    call = t303006000_x10(z7=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t303006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t303006000_x26():
    """State 0,1"""
    call = t303006000_x10(z7=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t303006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t303006000_x27():
    """State 0,1"""
    call = t303006000_x10(z7=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t303006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t303006000_x28():
    """State 0,1"""
    call = t303006000_x10(z7=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t303006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t303006000_x29(text4=_, z6=_, mode6=1):
    """State 0,5"""
    assert t303006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
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

def t303006000_x30(text3=_, mode5=1):
    """State 0,4"""
    assert t303006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t303006000_x31(text2=_, z5=_, mode4=1):
    """State 0,5"""
    assert t303006000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t303006000_x32(text1=_, mode3=1):
    """State 0,4"""
    assert t303006000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t303006000_x33():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t303006000_x34():
    """State 0,1"""
    assert t303006000_x10(z7=1002, val6=1002)
    """State 2"""
    return 0

def t303006000_x35():
    """State 0,1"""
    assert t303006000_x1()
    """State 2"""
    return 0

def t303006000_x36():
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

def t303006000_x37():
    """State 0,1"""
    if GetEventFlag(3285) == 1:
        """State 3"""
        assert t303006000_x43()
    elif GetEventFlag(3286) == 1:
        """State 4"""
        assert t303006000_x44()
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t303006000_x38():
    """State 0,1"""
    if not GetEventFlag(3295):
        """State 2"""
        # talk:30390900:"Death ought to be earned."
        assert t303006000_x32(text1=30390900, mode3=1)
    else:
        """State 3"""
        # talk:30390800:"Don't you see now?"
        assert t303006000_x32(text1=30390800, mode3=1)
    """State 4"""
    return 0

def t303006000_x39():
    """State 0,1"""
    SetEventFlag(1043359217, 1)
    """State 2"""
    if not GetEventFlag(3295):
        """State 3"""
        pass
    else:
        """State 4"""
        def ExitPause():
            SetEventFlag(3281, 1)
            SetEventFlag(1043359220, 1)
            SetEventFlag(1043359221, 1)
            SetEventFlag(1043352700, 1)
            RequestAnimation(90160, -1)
        assert t303006000_x46()
    """State 5"""
    return 0

def t303006000_x40():
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        """State 2"""
        if not GetEventFlag(1043352701):
            """State 3"""
            SetEventFlag(1043352701, 1)
            """State 4"""
            # talk:30390200:"Whoah, what're you playing at? (OKテイク, v303902000_ALT_3)\nWhat're you playing at?"
            call = t303006000_x32(text1=30390200, mode3=1)
            if call.Done():
                break
            elif IsAttackedBySomeone() == 1:
                pass
        else:
            """State 6"""
            return 1
    """State 5"""
    return 0

def t303006000_x41():
    """State 0,2"""
    if not GetEventFlag(1043352700):
        """State 6"""
        SetEventFlag(1043352700, 1)
        """State 4"""
        if not GetEventFlag(3295):
            """State 3"""
            if not GetEventFlag(1043359248):
                """State 5"""
                SetEventFlag(1043359248, 1)
                """State 7"""
                # talk:30390300:"..."
                assert t303006000_x31(text2=30390300, z5=1043352700, mode4=1)
            else:
                """State 8"""
                # talk:30390400:"Not too sharp, are you?"
                assert t303006000_x31(text2=30390400, z5=1043352700, mode4=1)
        else:
            """State 9"""
            def ExitPause():
                SetEventFlag(1043352702, 1)
                SetEventFlag(1043359220, 1)
                SetEventFlag(1043359221, 1)
                RequestAnimation(90160, -1)
            assert t303006000_x45()
    else:
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 10"""
    return 0

def t303006000_x42():
    """State 0,1"""
    if not GetEventFlag(3295):
        """State 2"""
        # talk:30390700:"Oh, my Lord. Good God of Vengeance!"
        assert t303006000_x32(text1=30390700, mode3=1)
    else:
        """State 3"""
        # talk:30390600:"Let it be known."
        assert t303006000_x32(text1=30390600, mode3=1)
    """State 4"""
    return 0

def t303006000_x43():
    """State 0,8"""
    if not GetEventFlag(1043359201):
        """State 1,7"""
        SetEventFlag(1043359245, 1)
        """State 17"""
        # talk:30300100:"Good Lord! Good God of Vengeance!"
        def ExitPause():
            RequestAnimation(90161, -1)
        assert t303006000_x30(text3=30300100, mode5=1)
        """State 10"""
        assert GetCurrentStateElapsedTime() > 2.5
        """State 12"""
        # talk:30300200:"Oh..."
        def ExitPause():
            RequestAnimation(90172, -1)
        assert t303006000_x29(text4=30300200, z6=1043359201, mode6=1)
        """State 11"""
        SetEventFlag(1044359201, 1)
    elif not GetEventFlag(1043359202):
        """State 6,16"""
        # talk:30300300:"By the way..."
        def ExitPause():
            RequestAnimation(90172, -1)
        assert t303006000_x29(text4=30300300, z6=1043359202, mode6=1)
    elif not GetEventFlag(1043359203):
        """State 2,13"""
        # talk:30300400:"These fellows?"
        def ExitPause():
            RequestAnimation(90172, -1)
        assert t303006000_x29(text4=30300400, z6=1043359203, mode6=1)
    else:
        """State 9,15"""
        # talk:30300600:"In the Lands Between, everyone lives longer than they should."
        def ExitPause():
            RequestAnimation(90172, -1)
        assert t303006000_x30(text3=30300600, mode5=1)
        """State 4"""
        SetEventFlag(1043359203, 0)
        """State 5"""
        SetEventFlag(1043359204, 0)
    """State 18"""
    Label('L0')
    return 0
    """Unused"""
    """State 3,14"""
    # talk:30300500:"You're Tarnished. Then you're here to fight, aren't you?"
    def ExitPause():
        RequestAnimation(90172, -1)
    assert t303006000_x29(text4=30300500, z6=1043359204, mode6=1)
    Goto('L0')

def t303006000_x44():
    """State 0,8"""
    if not GetEventFlag(1043359210):
        """State 1,2"""
        if not GetEventFlag(1044359202):
            """State 10"""
            # talk:30301100:"Ah, you..."
            def ExitPause():
                RequestAnimation(90172, -1)
            assert t303006000_x30(text3=30301100, mode5=1)
        else:
            """State 11"""
            # talk:30301000:"Oh, there you are..."
            def ExitPause():
                RequestAnimation(90172, -1)
            assert t303006000_x30(text3=30301000, mode5=1)
        """State 4"""
        SetEventFlag(1043359210, 1)
    elif not GetEventFlag(1043359211):
        """State 3,12"""
        # talk:30301300:"Alright, then."
        def ExitPause():
            RequestAnimation(90172, -1)
        assert t303006000_x30(text3=30301300, mode5=1)
        """State 5"""
        SetEventFlag(1043359211, 1)
    elif not GetEventFlag(1043359213):
        """State 6,13"""
        # talk:30301400:"I was thinking..."
        def ExitPause():
            RequestAnimation(90172, -1)
        assert t303006000_x30(text3=30301400, mode5=1)
        """State 7"""
        SetEventFlag(1043359213, 1)
    else:
        """State 9,14"""
        # talk:30301500:"Ahh, my head is throbbing, everything is bright red..."
        def ExitPause():
            RequestAnimation(90172, -1)
        assert t303006000_x30(text3=30301500, mode5=1)
    """State 15"""
    return 0

def t303006000_x45():
    """State 0,1"""
    if not GetEventFlag(1043359220) and not GetEventFlag(1043359221):
        """State 3"""
        # talk:30390000:"Well, well, you've made yourself a target of vengeance."
        assert (t303006000_x31(text2=30390000, z5=1043359221, mode4=1) and CheckSpecificPersonTalkHasEnded(0)
                == 1)
        """State 4"""
        assert t303006000_x31(text2=30390011, z5=3281, mode4=1)
        """State 2"""
        SetEventFlag(1043359220, 1)
        SetEventFlag(1043359221, 1)
        SetEventFlag(1043352700, 1)
    else:
        """State 5"""
        # talk:30391000:"Didn't I tell you before?"
        assert (t303006000_x31(text2=30391000, z5=1043352702, mode4=1) and CheckSpecificPersonTalkHasEnded(0)
                == 1)
        """State 6"""
        assert call.Done()
    """State 7"""
    return 0

def t303006000_x46():
    """State 0,2"""
    if not GetEventFlag(1043359220) and not GetEventFlag(1043359221):
        """State 3"""
        SetEventFlag(1043352700, 1)
        """State 1"""
        if not GetEventFlag(1043359245):
            """State 5"""
            # talk:30390100:"Hello there, I don't believe we've met."
            assert (t303006000_x31(text2=30390100, z5=1043359220, mode4=1) and CheckSpecificPersonTalkHasEnded(0)
                    == 1)
            """State 6"""
            assert t303006000_x32(text1=30390111, mode3=1)
        else:
            """State 4"""
            # talk:30390000:"Well, well, you've made yourself a target of vengeance."
            assert (t303006000_x31(text2=30390000, z5=1043359221, mode4=1) and CheckSpecificPersonTalkHasEnded(0)
                    == 1)
            """State 7"""
            assert t303006000_x32(text1=30390011, mode3=1)
    else:
        pass
    """State 8"""
    return 0

