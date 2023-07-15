# -*- coding: utf-8 -*-
def t318006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t318006000_x24(flag1=3623, flag2=3621, flag3=3622, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1)
    def WhilePaused():
        c5_121(CheckSpecificPersonTalkHasEnded(0) == 1 and GetEventFlag(3631) == 1, 9620)
    Quit()

def t318006000_1000():
    """State 0,2,3"""
    assert t318006000_x0()
    """State 1"""
    c1_120(1000)
    Quit()

def t318006000_1001():
    """State 0,2,3"""
    assert t318006000_x1()
    """State 1"""
    c1_120(1001)
    Quit()

def t318006000_1101():
    """State 0,2,3"""
    assert t318006000_x2()
    """State 1"""
    c1_120(1101)
    Quit()

def t318006000_1102():
    """State 0,2,3"""
    t318006000_x3()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t318006000_1103():
    """State 0,2,3"""
    assert t318006000_x4()
    """State 1"""
    c1_120(1103)
    Quit()

def t318006000_2000():
    """State 0,2,3"""
    assert t318006000_x5(val6=10, z5=12)
    """State 1"""
    c1_120(2000)
    Quit()

def t318006000_x0():
    """State 0,1"""
    if GetEventFlag(3625) == 1:
        """State 3"""
        assert t318006000_x6()
    elif GetEventFlag(3626) == 1:
        """State 4"""
        assert t318006000_x7()
    elif GetEventFlag(3627) == 1:
        """State 5"""
        assert t318006000_x8()
    elif GetEventFlag(3630) == 1:
        """State 6"""
        assert t318006000_x9()
    elif GetEventFlag(3631) == 1:
        """State 7"""
        assert t318006000_x10()
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t318006000_x1():
    """State 0,1"""
    if GetEventFlag(3630) == 1:
        """State 4"""
        """State 5"""
        pass
    elif not GetEventFlag(3631):
        """State 2,6"""
        # talk:31880300:"I had no choice."
        assert t318006000_x49(text1=31880300, mode3=1)
    else:
        """State 3,7"""
        # talk:31882300:"How very unfortunate."
        assert t318006000_x49(text1=31882300, mode3=1)
    """State 8"""
    return 0

def t318006000_x2():
    """State 0"""
    if GetEventFlag(3630) == 1:
        """State 6"""
        """State 7"""
        pass
    elif not GetEventFlag(1043372711):
        """State 2,1"""
        SetEventFlag(1043372711, 1)
        if not GetEventFlag(3631):
            """State 4,12"""
            # talk:31880000:"Ugh."
            assert t318006000_x49(text1=31880000, mode3=1)
        else:
            """State 5,13"""
            # talk:31882000:"What's this?"
            assert t318006000_x49(text1=31882000, mode3=1)
    elif not GetEventFlag(1043372719):
        """State 8,9"""
        SetEventFlag(1043372719, 1)
        if not GetEventFlag(3631):
            """State 10,14"""
            # talk:31880100:"That will be quite enough."
            assert t318006000_x49(text1=31880100, mode3=1)
        else:
            """State 11,15"""
            # talk:31882100:"Well, this is peculiar."
            assert t318006000_x49(text1=31882100, mode3=1)
    else:
        """State 3"""
        pass
    """State 16"""
    return 0

def t318006000_x3():
    """State 0"""
    if GetEventFlag(3630) == 1:
        """State 11"""
        """State 12"""
        pass
    else:
        """State 2"""
        if not GetEventFlag(1043379255):
            """State 3,7"""
            SetEventFlag(1043379255, 1)
            """State 6"""
            SetEventFlag(1043372710, 1)
            if not GetEventFlag(3631):
                """State 9,13"""
                # talk:31880200:"Too late for you, eh?"
                assert t318006000_x49(text1=31880200, mode3=1)
            else:
                """State 10,14"""
                # talk:31882200:"This, I did not expect."
                assert t318006000_x49(text1=31882200, mode3=1)
        elif not GetEventFlag(1043372710):
            """State 4,8"""
            SetEventFlag(1043372710, 1)
        else:
            """State 5"""
            pass
    """State 1"""
    Quit()
    """Unused"""
    """State 15"""
    return 0

def t318006000_x4():
    """State 0,1"""
    if GetEventFlag(3630) == 1:
        """State 4"""
        """State 5"""
        pass
    elif not GetEventFlag(3631):
        """State 2,6"""
        # talk:31880500:"I must not die..."
        assert t318006000_x49(text1=31880500, mode3=1)
    else:
        """State 3,7"""
        # talk:31882400:"Shabriri is chaos incarnate. I cannot die."
        def WhilePaused():
            c1_121(9600)
        assert (t318006000_x49(text1=31882400, mode3=1) and (GetCurrentStateElapsedTime() > 60 or CheckSpecificPersonTalkHasEnded(0)
                == 1))
    """State 8"""
    return 0

def t318006000_x5(val6=10, z5=12):
    """State 0"""
    while True:
        """State 4"""
        if GetEventFlag(3627) == 1:
            """State 3,7"""
            call = t318006000_x16(val6=val6, z5=z5)
            if call.Done():
                break
            elif not GetEventFlag(3627):
                pass
        elif GetEventFlag(3630) == 1:
            """State 1,6"""
            call = t318006000_x11()
            if call.Done():
                break
            elif not GetEventFlag(3630):
                pass
        else:
            """State 2,5"""
            # actionbutton:6000:"Talk"
            call = t318006000_x18(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                                  flag12=6000, flag4=6000)
            if call.Done():
                break
            elif GetEventFlag(3627) == 1 or GetEventFlag(3630) == 1:
                pass
    """State 8"""
    return 0

def t318006000_x6():
    """State 0,1"""
    if not GetEventFlag(1044389206):
        """State 2,6"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t318006000_x17()
    elif not GetEventFlag(1044389208) and GetEventFlag(1044389211) == 1 and not GetEventFlag(1043360800):
        """State 3,7"""
        # talk:31801500:"One last word of warning."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t318006000_x48(text2=31801500, mode4=1)
        """State 5"""
        SetEventFlag(1044389208, 1)
    else:
        """State 4,8"""
        # talk:31801600:"Be on your way."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t318006000_x48(text2=31801600, mode4=1)
    """State 9"""
    return 0

def t318006000_x7():
    """State 0,1"""
    if not GetEventFlag(1043359258) and not GetEventFlag(1043360800):
        """State 2,5"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t318006000_x12()
    elif not GetEventFlag(1043360800):
        """State 3,6"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t318006000_x13()
    else:
        """State 4,7"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t318006000_x14()
    """State 8"""
    return 0

def t318006000_x8():
    """State 0,1"""
    if not GetEventFlag(1035469206):
        """State 2,6"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t318006000_x15()
    elif not GetEventFlag(1035469207):
        """State 3,7"""
        # talk:31804200:"Yes, I've been tracking Eleonora for quite some time."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t318006000_x48(text2=31804200, mode4=1)
        """State 5"""
        SetEventFlag(1035469207, 1)
    else:
        """State 4,8"""
        # talk:31804300:"Be on your way."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t318006000_x48(text2=31804300, mode4=1)
    """State 9"""
    return 0

def t318006000_x9():
    """State 0,1"""
    # talk:31807000:"Eleonora, it seems I am no match for you."
    def WhilePaused():
        RequestAnimation(90305, -1)
    def ExitPause():
        SetEventFlag(1039529205, 1)
    assert t318006000_x48(text2=31807000, mode4=1)
    """State 2"""
    return 0

def t318006000_x10():
    """State 0,1"""
    if not GetEventFlag(1049539205):
        """State 2,14"""
        # talk:31808000:"Finally, we meet."
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t318006000_x48(text2=31808000, mode4=1)
        """State 8"""
        SetEventFlag(1049539205, 1)
    elif not GetEventFlag(1049539206) and not GetEventFlag(110):
        """State 3,15"""
        # talk:31808100:"You are about to sacrifice something precious."
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t318006000_x48(text2=31808100, mode4=1)
        """State 9"""
        SetEventFlag(1049539206, 1)
    elif not GetEventFlag(1049539207) and not GetEventFlag(110):
        """State 4,16"""
        # talk:31808200:"Chosen Tarnished and would-be Lord, dare to tread the path of true rigor."
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t318006000_x48(text2=31808200, mode4=1)
        """State 10"""
        SetEventFlag(1049539207, 1)
    elif not GetEventFlag(1049539208) and not GetEventFlag(110):
        """State 5,17"""
        # talk:31808300:"Chosen Tarnished, and would-be Lord."
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t318006000_x48(text2=31808300, mode4=1)
        """State 11"""
        SetEventFlag(1049539208, 1)
    elif not GetEventFlag(1049539209) and not GetEventFlag(35000500):
        """State 6,18"""
        # talk:31808400:"Chosen Tarnished, and would-be Lord."
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t318006000_x48(text2=31808400, mode4=1)
        """State 12"""
        SetEventFlag(1049539209, 1)
    else:
        """State 7,19"""
        # talk:31808500:"Burn the Erdtree to the ground,"
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t318006000_x48(text2=31808500, mode4=1)
        """State 13"""
        SetEventFlag(1049539209, 0)
    """State 20"""
    return 0

def t318006000_x11():
    """State 0,2"""
    # actionbutton:6000:"Talk"
    call = t318006000_x18(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                          flag4=6000)
    if call.Done():
        """State 3"""
        return 0
    elif GetEventFlag(1039529205) == 1 or GetEventFlag(1039529206) == 1 or GetEventFlag(1039529207) == 1:
        """State 1"""
        Quit()

def t318006000_x12():
    """State 0,1"""
    if not GetEventFlag(1043359255):
        """State 2"""
        if not GetEventFlag(1043379260):
            """State 3,10"""
            # talk:31802400:"Ah, you must be the new Tarnished."
            assert t318006000_x48(text2=31802400, mode4=1)
            """State 7"""
            SetEventFlag(1043379260, 1)
        elif not GetEventFlag(1044389208):
            """State 4,11"""
            # talk:31802000:"Well, we meet again."
            assert t318006000_x48(text2=31802000, mode4=1)
        else:
            """State 5,12"""
            # talk:31802100:"Hmm, I gave you fair warning."
            assert t318006000_x48(text2=31802100, mode4=1)
        """State 8"""
        SetEventFlag(1043359255, 1)
        """State 9"""
        SetEventFlag(1043359252, 1)
    else:
        """State 6,13"""
        # talk:31802200:"Don't be a fool. Turn back, before it's too late."
        assert t318006000_x48(text2=31802200, mode4=1)
    """State 14"""
    return 0

def t318006000_x13():
    """State 0,1"""
    if not GetEventFlag(1043359256):
        """State 2"""
        if not GetEventFlag(1043379260):
            """State 4,9"""
            # talk:31802700:"Ah, you must be the new Tarnished."
            assert t318006000_x48(text2=31802700, mode4=1)
        else:
            """State 5,10"""
            # talk:31802500:"You bloody halfwit."
            assert t318006000_x48(text2=31802500, mode4=1)
        """State 6"""
        SetEventFlag(1043379260, 1)
        """State 7"""
        SetEventFlag(1043359256, 1)
        """State 8"""
        SetEventFlag(1043359252, 1)
    else:
        """State 3,11"""
        # talk:31802800:"I can tell you want to see it through."
        assert t318006000_x48(text2=31802800, mode4=1)
    """State 12"""
    return 0

def t318006000_x14():
    """State 0,1"""
    if not GetEventFlag(1043359257):
        """State 2"""
        if not GetEventFlag(1043379260) and not GetEventFlag(1043369201):
            """State 4,15"""
            # talk:31803500:"Ah, you must be the new Tarnished."
            assert t318006000_x48(text2=31803500, mode4=1)
            """State 8"""
            Label('L0')
            SetEventFlag(1043379260, 1)
        elif not GetEventFlag(1043379260) and GetEventFlag(1043369201) == 1:
            """State 5,11"""
            # talk:31803400:"Ah, you must be the new Tarnished."
            assert t318006000_x48(text2=31803400, mode4=1)
            Goto('L0')
        elif GetEventFlag(1043379260) == 1 and not GetEventFlag(1043369201):
            """State 6,14"""
            # talk:31803200:"Beautiful work, felling that dragon."
            assert t318006000_x48(text2=31803200, mode4=1)
        else:
            """State 7,12"""
            # talk:31803000:"There you are. That was my first dragon hunt in quite some time."
            assert t318006000_x48(text2=31803000, mode4=1)
        """State 9"""
        SetEventFlag(1043359257, 1)
        """State 10"""
        SetEventFlag(1043359252, 1)
    else:
        """State 3,13"""
        # talk:31803100:"You must not forget, though."
        assert t318006000_x48(text2=31803100, mode4=1)
    """State 16"""
    return 0

def t318006000_x15():
    """State 0,2"""
    # talk:31804000:"Ah, oh, it's you. Thanks for your help there."
    assert t318006000_x48(text2=31804000, mode4=1)
    """State 1"""
    SetEventFlag(1035469206, 1)
    """State 4"""
    # lot:101610:Smithing Stone [5]
    assert t318006000_x21(lot1=101610)
    """State 3"""
    # talk:31804100:"I may not have much time."
    assert t318006000_x48(text2=31804100, mode4=1)
    """State 5"""
    return 0

def t318006000_x16(val6=10, z5=12):
    """State 0"""
    while True:
        """State 3"""
        # actionbutton:6000:"Talk"
        call = t318006000_x18(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                              flag4=6000)
        if call.Done():
            break
        elif not GetEventFlag(1035469208) and GetDistanceToPlayer() < val6:
            """State 1,2"""
            SetEventFlag(1035469208, 1)
            """State 4"""
            # talk:31803300:"..."
            assert t318006000_x49(text1=31803300, mode3=1)
    """State 5"""
    return 0

def t318006000_x17():
    """State 0,1"""
    if not GetEventFlag(1043379260) and GetEventFlag(1043379262) == 1:
        """State 2,10"""
        # talk:31801000:"Just joining the fray, Tarnished?"
        assert t318006000_x48(text2=31801000, mode4=1)
        """State 4"""
        Label('L0')
        SetEventFlag(1043379260, 1)
        """State 5"""
        SetEventFlag(1044389211, 1)
    elif not GetEventFlag(1043379260) and not GetEventFlag(1043379262):
        """State 7,12"""
        # talk:31801010:"Just joining the fray, Tarnished?"
        assert t318006000_x48(text2=31801010, mode4=1)
        Goto('L0')
    elif GetEventFlag(1043379260) == 1 and GetEventFlag(1043379262) == 1:
        """State 3,11"""
        # talk:31802300:"Ah, we meet again."
        assert t318006000_x48(text2=31802300, mode4=1)
    else:
        """State 8,13"""
        # talk:31802310:"Ah, we meet again."
        assert t318006000_x48(text2=31802310, mode4=1)
    """State 6"""
    SetEventFlag(1044389206, 1)
    """State 9"""
    SetEventFlag(1044389202, 1)
    """State 14"""
    return 0

def t318006000_x18(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t318006000_x19():
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

def t318006000_x20():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t318006000_x21(lot1=101610):
    """State 0,1"""
    # lot:101610:Smithing Stone [5]
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t318006000_x22(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t318006000_x38()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t318006000_x19()
    else:
        """State 4,7"""
        call = t318006000_x51()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t318006000_x19()
    """State 9"""
    return 0

def t318006000_x23():
    """State 0,1"""
    assert t318006000_x19()
    """State 2"""
    return 0

def t318006000_x24(flag1=3623, flag2=3621, flag3=3622, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t318006000_x41(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t318006000_x40()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t318006000_x25(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                   flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                   mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t318006000_x28(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t318006000_x32(val1=val1, z1=z1)
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
            call = t318006000_x34(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t318006000_x45() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t318006000_x30(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t318006000_x26(val2=10, val3=12):
    """State 0,1"""
    call = t318006000_x36(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t318006000_x22(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t318006000_x27(flag1=3623, val2=10, val3=12):
    """State 0,8"""
    assert t318006000_x53()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t318006000_x39()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t318006000_x19()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t318006000_x28(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t318006000_x29(z6=2000, val7=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t318006000_x18(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t318006000_x29(z6=_, val7=_):
    """State 0,1"""
    if f203(z6) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z6)
        assert f202() == val7
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t318006000_x30(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t318006000_x19()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t318006000_x31()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t318006000_x46()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t318006000_x31():
    """State 0,1"""
    assert t318006000_x29(z6=1101, val7=1101)
    """State 2"""
    return 0

def t318006000_x32(val1=5, z1=1):
    """State 0,2"""
    assert t318006000_x42()
    """State 1"""
    call = t318006000_x33()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t318006000_x44()
    """State 4"""
    return 0

def t318006000_x33():
    """State 0,1"""
    assert t318006000_x29(z6=1000, val7=1000)
    """State 2"""
    return 0

def t318006000_x34(val5=12):
    """State 0,1"""
    call = t318006000_x35()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t318006000_x45()
    """State 3"""
    return 0

def t318006000_x35():
    """State 0,1"""
    assert t318006000_x29(z6=1100, val7=1100)
    """State 2"""
    return 0

def t318006000_x36(val2=10, val3=12):
    """State 0,5"""
    assert t318006000_x53()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t318006000_x37()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t318006000_x47()
    """Unused"""
    """State 6"""
    return 0

def t318006000_x37():
    """State 0,2"""
    call = t318006000_x29(z6=1102, val7=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t318006000_x38():
    """State 0,1"""
    assert t318006000_x29(z6=1001, val7=1001)
    """State 2"""
    return 0

def t318006000_x39():
    """State 0,1"""
    assert t318006000_x29(z6=1103, val7=1103)
    """State 2"""
    return 0

def t318006000_x40():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t318006000_x41(flag1=3623, flag2=3621, flag3=3622, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t318006000_x25(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                              flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                              z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t318006000_x27(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t318006000_x26(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t318006000_x52() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t318006000_x42():
    """State 0,1"""
    assert t318006000_x43()
    """State 2"""
    return 0

def t318006000_x43():
    """State 0,1"""
    assert t318006000_x29(z6=1104, val7=1104)
    """State 2"""
    return 0

def t318006000_x44():
    """State 0,1"""
    call = t318006000_x29(z6=1201, val7=1201)
    if call.Get() == 1:
        """State 2"""
        assert t318006000_x23()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t318006000_x45():
    """State 0,1"""
    call = t318006000_x29(z6=1300, val7=1300)
    if call.Get() == 1:
        """State 2"""
        assert t318006000_x23()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t318006000_x46():
    """State 0,1"""
    call = t318006000_x29(z6=1301, val7=1301)
    if call.Get() == 1:
        """State 2"""
        assert t318006000_x23()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t318006000_x47():
    """State 0,1"""
    call = t318006000_x29(z6=1302, val7=1302)
    if call.Get() == 1:
        """State 2"""
        assert t318006000_x23()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t318006000_x48(text2=_, mode4=1):
    """State 0,4"""
    assert t318006000_x20() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t318006000_x49(text1=_, mode3=1):
    """State 0,4"""
    assert t318006000_x50() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t318006000_x50():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t318006000_x51():
    """State 0,1"""
    assert t318006000_x29(z6=1002, val7=1002)
    """State 2"""
    return 0

def t318006000_x52():
    """State 0,1"""
    assert t318006000_x19()
    """State 2"""
    return 0

def t318006000_x53():
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

