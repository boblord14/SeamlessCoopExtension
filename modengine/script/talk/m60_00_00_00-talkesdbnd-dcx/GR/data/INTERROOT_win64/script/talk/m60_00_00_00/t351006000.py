# -*- coding: utf-8 -*-
def t351006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t351006000_x5(flag1=4203, flag2=4201, flag3=4202, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    def WhilePaused():
        c5_121(GetEventFlag(4211) == 1, 9620)
    Quit()

def t351006000_1000():
    """State 0,2,3"""
    assert t351006000_x37()
    """State 1"""
    c1_120(1000)
    Quit()

def t351006000_1001():
    """State 0,2,3"""
    assert t351006000_x38()
    """State 1"""
    c1_120(1001)
    Quit()

def t351006000_1101():
    """State 0,2,3"""
    assert t351006000_x39()
    """State 1"""
    c1_120(1101)
    Quit()

def t351006000_1102():
    """State 0,2,3"""
    t351006000_x40()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t351006000_1103():
    """State 0,2,3"""
    assert t351006000_x41()
    """State 1"""
    c1_120(1103)
    Quit()

def t351006000_2000():
    """State 0,2,3"""
    assert t351006000_x42()
    """State 1"""
    c1_120(2000)
    Quit()

def t351006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t351006000_x1():
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

def t351006000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t351006000_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t351006000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t351006000_x1()
    else:
        """State 4,7"""
        call = t351006000_x34()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t351006000_x1()
    """State 9"""
    return 0

def t351006000_x4():
    """State 0,1"""
    assert t351006000_x1()
    """State 2"""
    return 0

def t351006000_x5(flag1=4203, flag2=4201, flag3=4202, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t351006000_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t351006000_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t351006000_x6(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t351006000_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t351006000_x13(val1=val1, z1=z1)
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
            call = t351006000_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t351006000_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t351006000_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t351006000_x7(val2=10, val3=12):
    """State 0,1"""
    call = t351006000_x17(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t351006000_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t351006000_x8(flag1=4203, val2=10, val3=12):
    """State 0,8"""
    assert t351006000_x36()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t351006000_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t351006000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t351006000_x9(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t351006000_x10(z7=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t351006000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t351006000_x10(z7=_, val6=_):
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

def t351006000_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t351006000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t351006000_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t351006000_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t351006000_x12():
    """State 0,1"""
    assert t351006000_x10(z7=1101, val6=1101)
    """State 2"""
    return 0

def t351006000_x13(val1=5, z1=1):
    """State 0,2"""
    assert t351006000_x23()
    """State 1"""
    call = t351006000_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t351006000_x25()
    """State 4"""
    return 0

def t351006000_x14():
    """State 0,1"""
    assert t351006000_x10(z7=1000, val6=1000)
    """State 2"""
    return 0

def t351006000_x15(val5=12):
    """State 0,1"""
    call = t351006000_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t351006000_x26()
    """State 3"""
    return 0

def t351006000_x16():
    """State 0,1"""
    assert t351006000_x10(z7=1100, val6=1100)
    """State 2"""
    return 0

def t351006000_x17(val2=10, val3=12):
    """State 0,5"""
    assert t351006000_x36()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t351006000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t351006000_x28()
    """Unused"""
    """State 6"""
    return 0

def t351006000_x18():
    """State 0,2"""
    call = t351006000_x10(z7=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t351006000_x19():
    """State 0,1"""
    assert t351006000_x10(z7=1001, val6=1001)
    """State 2"""
    return 0

def t351006000_x20():
    """State 0,1"""
    assert t351006000_x10(z7=1103, val6=1103)
    """State 2"""
    return 0

def t351006000_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t351006000_x22(flag1=4203, flag2=4201, flag3=4202, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t351006000_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t351006000_x8(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t351006000_x7(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t351006000_x35() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t351006000_x23():
    """State 0,1"""
    assert t351006000_x24()
    """State 2"""
    return 0

def t351006000_x24():
    """State 0,1"""
    assert t351006000_x10(z7=1104, val6=1104)
    """State 2"""
    return 0

def t351006000_x25():
    """State 0,1"""
    call = t351006000_x10(z7=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t351006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t351006000_x26():
    """State 0,1"""
    call = t351006000_x10(z7=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t351006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t351006000_x27():
    """State 0,1"""
    call = t351006000_x10(z7=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t351006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t351006000_x28():
    """State 0,1"""
    call = t351006000_x10(z7=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t351006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t351006000_x29(text4=_, z6=_, mode6=1):
    """State 0,5"""
    assert t351006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(z6, 1)
    """State 1"""
    TalkToPlayer(text4, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode6:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t351006000_x30(text3=_, mode5=1):
    """State 0,4"""
    assert t351006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t351006000_x31(text2=_, z5=_, mode4=1):
    """State 0,5"""
    assert t351006000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t351006000_x32(text1=_, mode3=1):
    """State 0,4"""
    assert t351006000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t351006000_x33():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t351006000_x34():
    """State 0,1"""
    assert t351006000_x10(z7=1002, val6=1002)
    """State 2"""
    return 0

def t351006000_x35():
    """State 0,1"""
    assert t351006000_x1()
    """State 2"""
    return 0

def t351006000_x36():
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

def t351006000_x37():
    """State 0,1"""
    if GetEventFlag(4205) == 1:
        """State 3"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t351006000_x43()
    elif GetEventFlag(4206) == 1:
        """State 4"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t351006000_x47()
    elif GetEventFlag(4207) == 1 or GetEventFlag(1040549254) == 1:
        """State 5"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t351006000_x48()
    elif GetEventFlag(4208) == 1 or GetEventFlag(11009554) == 1:
        """State 6"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t351006000_x51()
    elif GetEventFlag(4209) == 1:
        """State 7"""
        def WhilePaused():
            RequestAnimation(90310, -1)
        assert t351006000_x52()
    elif GetEventFlag(4210) == 1:
        """State 8"""
        def WhilePaused():
            RequestAnimation(90310, -1)
        assert t351006000_x54()
    elif GetEventFlag(4211) == 1:
        """State 9"""
        assert t351006000_x56()
    else:
        """State 2"""
        pass
    """State 10"""
    return 0

def t351006000_x38():
    """State 0,1"""
    if GetEventFlag(4205) == 1 or GetEventFlag(4206) == 1 or GetEventFlag(4210) == 1:
        """State 2"""
        # talk:35180300:"I pray..."
        assert t351006000_x32(text1=35180300, mode3=1)
    else:
        """State 3"""
        # talk:35180400:"Please don't trouble us again."
        assert t351006000_x32(text1=35180400, mode3=1)
    """State 4"""
    return 0

def t351006000_x39():
    """State 0,1"""
    if not GetEventFlag(1040522710):
        """State 3"""
        # talk:35180000:"Ngh!"
        assert t351006000_x31(text2=35180000, z5=1040522710, mode4=1)
    elif not GetEventFlag(1040522711):
        """State 4"""
        # talk:35180100:"What are you trying to achieve?"
        assert t351006000_x31(text2=35180100, z5=1040522711, mode4=1)
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t351006000_x40():
    """State 0,2"""
    if not GetEventFlag(1040529253):
        """State 4"""
        # talk:35180200:"You've done it now."
        assert t351006000_x31(text2=35180200, z5=1040529253, mode4=1)
    else:
        """State 3"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 5"""
    return 0

def t351006000_x41():
    """State 0,1"""
    if GetEventFlag(4205) == 1 or GetEventFlag(4206) == 1 or GetEventFlag(4210) == 1:
        """State 2"""
        # talk:35180500:"O guidance...of grace..."
        assert t351006000_x32(text1=35180500, mode3=1)
    else:
        """State 3"""
        # talk:35180600:"O, master..."
        assert t351006000_x32(text1=35180600, mode3=1)
    """State 4"""
    return 0

def t351006000_x42():
    """State 0,1"""
    if GetEventFlag(4208) == 1 and GetEventFlag(11009554) == 1:
        """State 3"""
        assert t351006000_x76()
    else:
        """State 2"""
        # actionbutton:6000:"Talk"
        assert (t351006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                flag4=6000))
    """State 4"""
    return 0

def t351006000_x43():
    """State 0,1"""
    if GetEventFlag(3063) == 1 and GetEventFlag(11109855) == 1 and not GetEventFlag(11102812):
        """State 3"""
        assert t351006000_x45()
        """State 4"""
        Label('L0')
        assert t351006000_x58()
    else:
        """State 2"""
        call = t351006000_x44()
        if call.Get() == 1:
            Goto('L0')
        elif call.Get() == 0:
            pass
    """State 5"""
    return 0

def t351006000_x44():
    """State 0,7"""
    if not GetEventFlag(11109855):
        """State 8"""
        if not GetEventFlag(11109856):
            """State 20"""
            # talk:35100100:"Oh, I see you've just arrived."
            assert t351006000_x30(text3=35100100, mode5=1)
        else:
            """State 21"""
            # talk:35100400:"What is it?"
            assert t351006000_x30(text3=35100400, mode5=1)
        """State 1"""
        c1_110()
        ClearTalkListData()
        """State 2"""
        # action:23511000:"I see it"
        AddTalkListData(1, 23511000, -1)
        # action:23511001:"I don't see it"
        AddTalkListData(2, 23511001, -1)
        """State 3"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 22"""
            # talk:35100200:"You do! Wonderful news."
            assert t351006000_x30(text3=35100200, mode5=1)
            """State 18"""
            if not GetEventFlag(60841):
                """State 17"""
                # gesture:100:Prayer
                AcquireGesture(100)
                SetEventFlag(60841, 1)
            else:
                """State 19"""
                pass
            """State 10"""
            SetEventFlag(11109855, 1)
            """State 14"""
            SetEventFlag(11102814, 1)
            """State 12"""
            SetEventFlag(11102812, 1)
            Goto('L0')
        elif GetTalkListEntryResult() == 2:
            """State 11"""
            if not GetEventFlag(11109856):
                """State 23"""
                # talk:35100300:"Ah, well, that is unfortunate."
                assert t351006000_x30(text3=35100300, mode5=1)
                """State 6"""
                SetEventFlag(11109856, 1)
                """State 15"""
                SetEventFlag(11102814, 1)
            else:
                """State 24"""
                # talk:35100500:"Ah, I see."
                assert t351006000_x30(text3=35100500, mode5=1)
            """State 16"""
            SetEventFlag(11102812, 1)
        else:
            """State 5"""
            pass
        """State 27"""
        return 0
    else:
        """State 9"""
        if not GetEventFlag(11102812):
            """State 26"""
            # talk:35101100:"Ah, you appear to be doing well. Very good."
            assert t351006000_x30(text3=35101100, mode5=1)
            """State 13"""
            SetEventFlag(11102812, 1)
        else:
            """State 25"""
            # talk:35101000:"Further study of incantations, is it?"
            assert t351006000_x30(text3=35101000, mode5=1)
    """State 28"""
    Label('L0')
    return 1

def t351006000_x45():
    """State 0,1"""
    if GetEventFlag(11109858) == 1 and not GetEventFlag(11109859):
        """State 4"""
        # talk:35102000:"Ah, I had been waiting for your return."
        assert t351006000_x30(text3=35102000, mode5=1)
        """State 2"""
        Label('L0')
        SetEventFlag(11109859, 1)
        """State 3"""
        Label('L1')
        SetEventFlag(11102813, 1)
    elif not GetEventFlag(11109858) and not GetEventFlag(11109859):
        """State 5"""
        # talk:35102100:"Ah, I had been waiting for your return."
        assert t351006000_x30(text3=35102100, mode5=1)
        Goto('L0')
    elif not GetEventFlag(11102813):
        """State 7"""
        # talk:35101100:"Ah, you appear to be doing well. Very good."
        assert t351006000_x30(text3=35101100, mode5=1)
        Goto('L1')
    else:
        """State 6"""
        # talk:35101000:"Further study of incantations, is it?"
        assert t351006000_x30(text3=35101000, mode5=1)
    """State 8"""
    return 0

def t351006000_x46():
    """State 0,2"""
    if not GetEventFlag(1040529259):
        """State 1"""
        if not GetEventFlag(1040529255):
            """State 5"""
            # talk:35103000:"Ah, look who we have here."
            assert t351006000_x30(text3=35103000, mode5=1)
            """State 3"""
            SetEventFlag(1040529255, -1)
        elif not GetEventFlag(1040522712):
            """State 6"""
            # talk:35101100:"Ah, you appear to be doing well. Very good."
            assert t351006000_x30(text3=35101100, mode5=1)
        else:
            """State 7"""
            # talk:35101000:"Further study of incantations, is it?"
            assert t351006000_x30(text3=35101000, mode5=1)
            Goto('L0')
        """State 4"""
        SetEventFlag(1040522712, 1)
    else:
        """State 8"""
        # talk:35103700:"I will soon leave to join the noble Goldmask."
        assert t351006000_x30(text3=35103700, mode5=1)
    """State 9"""
    Label('L0')
    return 0

def t351006000_x47():
    """State 0,1"""
    assert t351006000_x46()
    """State 2"""
    assert t351006000_x58()
    """State 3"""
    return 0

def t351006000_x48():
    """State 0,1"""
    assert t351006000_x49()
    """State 2"""
    assert t351006000_x58()
    """State 3"""
    return 0

def t351006000_x49():
    """State 0,1"""
    if not GetEventFlag(1040549205):
        """State 4"""
        # talk:35104000:"Ah, we meet yet again."
        assert t351006000_x30(text3=35104000, mode5=1)
        """State 2"""
        SetEventFlag(1040549205, 1)
        """State 3"""
        Label('L0')
        SetEventFlag(1040542702, 1)
    elif not GetEventFlag(1040542702):
        """State 5"""
        # talk:35104200:"Ah, you appear to be doing well. Very good."
        assert t351006000_x30(text3=35104200, mode5=1)
        Goto('L0')
    else:
        """State 6"""
        # talk:35104100:"Further study of incantations, is it?"
        assert t351006000_x30(text3=35104100, mode5=1)
    """State 7"""
    return 0

def t351006000_x50():
    """State 0,2"""
    if not GetEventFlag(11009555) or GetEventFlag(11009455) == 1:
        """State 6"""
        if not GetEventFlag(11009460):
            """State 11"""
            # talk:35104700:"Oh, was that you? Sorry, I hardly noticed."
            assert t351006000_x30(text3=35104700, mode5=1)
            """State 7"""
            SetEventFlag(11009460, 1)
        else:
            """State 8"""
            if not GetEventFlag(11009455):
                """State 1"""
                if not GetEventFlag(11002732):
                    """State 12"""
                    # talk:35104900:"Oh, was that you?"
                    assert t351006000_x30(text3=35104900, mode5=1)
                else:
                    """State 14"""
                    # talk:35104800:"Did you need something else?"
                    assert t351006000_x30(text3=35104800, mode5=1)
                    Goto('L0')
            else:
                """State 9"""
                if not GetEventFlag(11002732):
                    """State 15"""
                    # talk:35104200:"Ah, you appear to be doing well. Very good."
                    assert t351006000_x30(text3=35104200, mode5=1)
                    """State 10"""
                    SetEventFlag(11002732, 1)
                    Goto('L0')
                else:
                    """State 16"""
                    # talk:35104100:"Further study of incantations, is it?"
                    assert t351006000_x30(text3=35104100, mode5=1)
                    Goto('L0')
        """State 3"""
        SetEventFlag(11002732, 1)
    else:
        """State 13"""
        # talk:35105100:"What on earth did you do to the master?"
        assert t351006000_x30(text3=35105100, mode5=1)
        """State 4"""
        SetEventFlag(11009455, 1)
        """State 5"""
        SetEventFlag(11002732, 1)
    """State 17"""
    Label('L0')
    return 0

def t351006000_x51():
    """State 0,1"""
    assert t351006000_x50()
    """State 2"""
    assert t351006000_x58()
    """State 3"""
    return 0

def t351006000_x52():
    """State 0,1"""
    assert t351006000_x53()
    """State 2"""
    assert t351006000_x58()
    """State 3"""
    return 0

def t351006000_x53():
    """State 0,4"""
    if not GetEventFlag(1051569361):
        """State 1"""
        if not GetEventFlag(1051569355):
            """State 5"""
            # talk:35106000:"Ah, nice to see you."
            assert t351006000_x30(text3=35106000, mode5=1)
            """State 2"""
            SetEventFlag(1051569355, 1)
        elif not GetEventFlag(1051562732):
            """State 6"""
            # talk:35106200:"Ah, nice to see you."
            assert t351006000_x30(text3=35106200, mode5=1)
        else:
            """State 7"""
            # talk:35106100:"Do you need...something else?"
            assert t351006000_x30(text3=35106100, mode5=1)
            Goto('L0')
        """State 3"""
        SetEventFlag(1051562732, 1)
    else:
        """State 8"""
        # talk:35106710:"It will make me forget, you say?"
        assert t351006000_x30(text3=35106710, mode5=1)
    """State 9"""
    Label('L0')
    return 0

def t351006000_x54():
    """State 0,1"""
    assert t351006000_x55()
    """State 2"""
    return 0

def t351006000_x55():
    """State 0,1"""
    # talk:35107000:"Oh, it's you."
    assert t351006000_x29(text4=35107000, z6=11059207, mode6=1)
    """State 2"""
    return 0

def t351006000_x56():
    """State 0,1"""
    assert t351006000_x57()
    """State 2"""
    return 0

def t351006000_x57():
    """State 0,1"""
    # talk:35108000:"Master...where did you go?"
    assert t351006000_x29(text4=35108000, z6=1051569362, mode6=1)
    """State 2"""
    return 0

def t351006000_x58():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        c1_110()
        """State 8"""
        assert t351006000_x61()
        """State 13"""
        assert t351006000_x75()
        """State 9"""
        assert t351006000_x71()
        """State 14"""
        assert t351006000_x73()
        """State 2"""
        # action:23510000:"Study incantations"
        AddTalkListData(1, 23510000, -1)
        # action:23510001:"Talk"
        AddTalkListDataIf(GetEventFlag(11109857) == 1, 50, 23510001, -1)
        # action:23510002:"About the noble Goldmask"
        AddTalkListDataIf(GetEventFlag(1040529256) == 1, 50, 23510002, -1)
        # action:23510003:"Tell the noble Goldmask's whereabouts"
        AddTalkListDataIf(GetEventFlag(1040529258) == 1, 50, 23510003, -1)
        # action:23510004:"About the noble Goldmask"
        AddTalkListDataIf(GetEventFlag(1040549206) == 1, 50, 23510004, -1)
        # action:23510005:"About the noble Goldmask"
        AddTalkListDataIf(GetEventFlag(11009456) == 1, 50, 23510005, -1)
        # action:23510006:"About the noble Goldmask"
        AddTalkListDataIf(GetEventFlag(11009458) == 1, 50, 23510006, -1)
        # action:23510007:"About the noble Goldmask"
        AddTalkListDataIf(GetEventFlag(1051569356) == 1, 50, 23510007, -1)
        # action:23510008:"About the noble Goldmask"
        AddTalkListDataIf(GetEventFlag(1051569358) == 1, 50, 23510008, -1)
        # action:23510009:"Give Tonic of Forgetfulness"
        AddTalkListDataIf(GetEventFlag(1051569360) == 1, 50, 23510009, -1)
        # action:23510010:"Give a prayerbook"
        AddTalkListDataIf(GetEventFlag(11109886) == 1, 75, 23510010, -1)
        # action:20000009:"Leave"
        AddTalkListData(99, 20000009, -1)
        """State 6"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 3"""
        if GetTalkListEntryResult() == 1:
            """State 4"""
            OpenRegularShop(100350, 100399)
            c1_141(5)
            """State 5"""
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            continue
        elif GetTalkListEntryResult() == 50:
            """State 10"""
            call = t351006000_x66()
            if call.Get() == 0 and CheckSpecificPersonTalkHasEnded(0) == 1:
                continue
            elif call.Get() == 1 and CheckSpecificPersonTalkHasEnded(0) == 1:
                pass
        elif GetTalkListEntryResult() == 75:
            """State 7"""
            SetEventFlag(11102815, 0)
            SetEventFlag(11102816, 0)
            """State 12"""
            assert t351006000_x74() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        else:
            """State 11"""
            assert t351006000_x72()
        """State 15"""
        return 0

def t351006000_x59():
    """State 0,1"""
    if (not GetEventFlag(11109858) and GetEventFlag(132) == 1 and not GetEventFlag(11102814) and not
        GetEventFlag(11109859)):
        """State 2"""
        SetEventFlag(11109857, 1)
    else:
        """State 3"""
        pass
    """State 4"""
    return 0

def t351006000_x60():
    """State 0,1"""
    if GetEventFlag(11109857) == 1:
        """State 4"""
        # talk:35101500:"There's something I should mention to you, as well."
        assert t351006000_x30(text3=35101500, mode5=1)
        """State 3"""
        SetEventFlag(11109858, 1)
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t351006000_x61():
    """State 0,1"""
    SetEventFlag(11109857, 0)
    SetEventFlag(1040529256, 0)
    SetEventFlag(1040529258, 0)
    SetEventFlag(1040549206, 0)
    SetEventFlag(11009456, 0)
    SetEventFlag(11009458, 0)
    SetEventFlag(1051569356, 0)
    SetEventFlag(1051569358, 0)
    SetEventFlag(1051569360, 0)
    """State 2"""
    return 0

def t351006000_x62():
    """State 0,1"""
    if not GetEventFlag(1040549255) and not GetEventFlag(1040529259):
        """State 2"""
        SetEventFlag(1040529256, 1)
    elif GetEventFlag(1040549255) == 1 and not GetEventFlag(1040529259):
        """State 4"""
        SetEventFlag(1040529258, 1)
    else:
        """State 3"""
        pass
    """State 5"""
    return 0

def t351006000_x63():
    """State 0,1"""
    if not GetEventFlag(1040549207):
        """State 2"""
        SetEventFlag(1040549206, 1)
    else:
        """State 3"""
        pass
    """State 4"""
    return 0

def t351006000_x64():
    """State 0,1"""
    if not GetEventFlag(11009455):
        """State 2"""
        SetEventFlag(11009456, 1)
    elif GetEventFlag(11009455) == 1 and not GetEventFlag(11009459):
        """State 4"""
        SetEventFlag(11009458, 1)
    else:
        """State 3"""
        pass
    """State 5"""
    return 0

def t351006000_x65():
    """State 0,1"""
    if not GetEventFlag(1051569357):
        """State 2"""
        SetEventFlag(1051569356, 1)
    elif GetEventFlag(1051569357) == 1 and not GetEventFlag(1051569359):
        """State 3"""
        SetEventFlag(1051569358, 1)
    # goods:8128:Tonic of Forgetfulness
    elif ComparePlayerInventoryNumber(3, 8128, 4, 1, 0) == 1 and not GetEventFlag(1051569361):
        """State 4"""
        SetEventFlag(1051569360, 1)
    else:
        """State 5"""
        pass
    """State 6"""
    return 0

def t351006000_x66():
    """State 0,1"""
    if GetEventFlag(4205) == 1:
        """State 3"""
        assert t351006000_x60()
    elif GetEventFlag(4206) == 1:
        """State 4"""
        assert t351006000_x67()
    elif GetEventFlag(4207) == 1 or GetEventFlag(1040549254) == 1:
        """State 5"""
        assert t351006000_x68()
    elif GetEventFlag(4208) == 1 or GetEventFlag(11009554) == 1:
        """State 6"""
        assert t351006000_x69()
    elif GetEventFlag(4209) == 1:
        """State 7"""
        call = t351006000_x70()
        if call.Get() == 0:
            pass
        elif call.Get() == 1:
            """State 9"""
            return 1
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t351006000_x67():
    """State 0,1"""
    if GetEventFlag(1040529256) == 1:
        """State 4"""
        # talk:35103500:"I'm yet to find the noble Goldmask."
        assert t351006000_x30(text3=35103500, mode5=1)
    elif GetEventFlag(1040529258) == 1:
        """State 5"""
        # talk:35103600:"Do...do you sport with me!?"
        assert t351006000_x30(text3=35103600, mode5=1)
        """State 2"""
        SetEventFlag(1040529259, 1)
    else:
        """State 3"""
        pass
    """State 6"""
    return 0

def t351006000_x68():
    """State 0,1"""
    if GetEventFlag(1040549206) == 1:
        """State 4"""
        # talk:35104500:"The master is always deep in contemplation."
        assert t351006000_x30(text3=35104500, mode5=1)
        """State 2"""
        SetEventFlag(1040549207, 1)
    else:
        """State 3"""
        pass
    """State 5"""
    return 0

def t351006000_x69():
    """State 0,1"""
    if GetEventFlag(11009456) == 1:
        """State 5"""
        if not GetEventFlag(11009457):
            """State 6"""
            # talk:35105000:"The master's reflections had heightened as we neared the Erdtree."
            assert t351006000_x30(text3=35105000, mode5=1)
            """State 3"""
            SetEventFlag(11009457, 1)
        else:
            """State 8"""
            # talk:35105300:"Who exactly was Radagon?"
            assert t351006000_x30(text3=35105300, mode5=1)
    elif GetEventFlag(11009458) == 1:
        """State 7"""
        # talk:35105200:"To think, that Radagon was Marika herself."
        assert t351006000_x30(text3=35105200, mode5=1)
        """State 4"""
        SetEventFlag(11009459, 1)
    else:
        """State 2"""
        pass
    """State 9"""
    return 0

def t351006000_x70():
    """State 0,1"""
    if GetEventFlag(1051569356) == 1:
        """State 6"""
        # talk:35106500:"I've…been gripped by a terrifying thought."
        assert t351006000_x30(text3=35106500, mode5=1)
        """State 2"""
        SetEventFlag(1051569357, 1)
    elif GetEventFlag(1051569358) == 1:
        """State 7"""
        # talk:35106600:"Oh master, put my mind at ease."
        assert t351006000_x30(text3=35106600, mode5=1)
        """State 4"""
        SetEventFlag(1051569359, 1)
    elif GetEventFlag(1051569360) == 1:
        """State 8"""
        # talk:35106700:"What...is this?"
        assert t351006000_x30(text3=35106700, mode5=1)
        """State 5"""
        SetEventFlag(1051569361, 1)
        """State 10"""
        return 1
    else:
        """State 3"""
        pass
    """State 9"""
    return 0

def t351006000_x71():
    """State 0,1"""
    if GetEventFlag(4205) == 1:
        """State 3"""
        assert t351006000_x59()
    elif GetEventFlag(4206) == 1:
        """State 4"""
        assert t351006000_x62()
    elif GetEventFlag(4207) == 1 or GetEventFlag(1040549254) == 1:
        """State 5"""
        assert t351006000_x63()
    elif GetEventFlag(4208) == 1 or GetEventFlag(11009554) == 1:
        """State 6"""
        assert t351006000_x64()
    elif GetEventFlag(4209) == 1:
        """State 7"""
        assert t351006000_x65()
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t351006000_x72():
    """State 0,1"""
    if GetEventFlag(4205) == 1 or GetEventFlag(4206) == 1:
        """State 3"""
        # talk:35101200:"May the Golden Order shine through you."
        assert t351006000_x30(text3=35101200, mode5=1)
    elif GetEventFlag(4207) == 1:
        """State 4"""
        # talk:35104300:"May the Golden Order shine through you."
        assert t351006000_x30(text3=35104300, mode5=1)
    elif GetEventFlag(4209) == 1 and GetEventFlag(1051569361) == 1:
        """State 5"""
        # talk:35104300:"May the Golden Order shine through you."
        assert t351006000_x30(text3=35104300, mode5=1)
    else:
        """State 2"""
        pass
    """State 6"""
    return 0

def t351006000_x73():
    """State 0"""
    while True:
        """State 1"""
        # goods:8855:Fire Monks' Prayerbook
        if (ComparePlayerInventoryNumber(3, 8855, 4, 1, 0) == 1 and not GetEventFlag(11109860) and not
            GetEventFlag(11109874)):
            """State 2"""
            SetEventFlag(11109860, 1)
        # goods:8856:Giant's Prayerbook
        elif (ComparePlayerInventoryNumber(3, 8856, 4, 1, 0) == 1 and not GetEventFlag(11109861) and
              not GetEventFlag(11109875)):
            """State 3"""
            SetEventFlag(11109861, 1)
        # goods:8857:Godskin Prayerbook
        elif (ComparePlayerInventoryNumber(3, 8857, 4, 1, 0) == 1 and not GetEventFlag(11109862) and
              not GetEventFlag(11109876)):
            """State 4"""
            SetEventFlag(11109862, 1)
        # goods:8858:Two Fingers' Prayerbook
        elif (ComparePlayerInventoryNumber(3, 8858, 4, 1, 0) == 1 and not GetEventFlag(11109863) and
              not GetEventFlag(11109877)):
            """State 5"""
            SetEventFlag(11109863, 1)
        # goods:8859:Assassin's Prayerbook
        elif (ComparePlayerInventoryNumber(3, 8859, 4, 1, 0) == 1 and not GetEventFlag(11109864) and
              not GetEventFlag(11109878)):
            """State 9"""
            SetEventFlag(11109864, 1)
        # goods:8862:Golden Order Principia
        elif (ComparePlayerInventoryNumber(3, 8862, 4, 1, 0) == 1 and not GetEventFlag(11109867) and
              not GetEventFlag(11109881)):
            """State 8"""
            SetEventFlag(11109867, 1)
        # goods:8863:[ERROR]Golden Order Principles
        elif (ComparePlayerInventoryNumber(3, 8863, 4, 1, 0) == 1 and not GetEventFlag(11109868) and
              not GetEventFlag(11109882)):
            """State 10"""
            SetEventFlag(11109868, 1)
        # goods:8864:Dragon Cult Prayerbook
        elif (ComparePlayerInventoryNumber(3, 8864, 4, 1, 0) == 1 and not GetEventFlag(11109869) and
              not GetEventFlag(11109883)):
            """State 11"""
            SetEventFlag(11109869, 1)
        # goods:8865:Ancient Dragon Prayerbook
        elif (ComparePlayerInventoryNumber(3, 8865, 4, 1, 0) == 1 and not GetEventFlag(11109870) and
              not GetEventFlag(11109884)):
            """State 12"""
            SetEventFlag(11109870, 1)
        else:
            """State 7,13"""
            return 0
        """State 6"""
        SetEventFlag(11109886, 1)

def t351006000_x74():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        c1_110()
        """State 38"""
        assert t351006000_x61()
        """State 34"""
        assert t351006000_x75()
        """State 33"""
        assert t351006000_x73()
        """State 30"""
        if GetEventFlag(11109886) == 1:
            """State 2"""
            # action:23510018:"Give the Golden Order Principia"
            AddTalkListDataIf(GetEventFlag(11109867) == 1, 8, 23510018, -1)
            # action:23510019:"Give the Golden Order Canon"
            AddTalkListDataIf(GetEventFlag(11109868) == 1, 9, 23510019, -1)
            # action:23510011:"Give the Fire Monks' Prayerbook"
            AddTalkListDataIf(GetEventFlag(11109860) == 1, 1, 23510011, -1)
            # action:23510012:"Give the Giant's Prayerbook"
            AddTalkListDataIf(GetEventFlag(11109861) == 1, 2, 23510012, -1)
            # action:23510013:"Give the Godskin Prayerbook"
            AddTalkListDataIf(GetEventFlag(11109862) == 1, 3, 23510013, -1)
            # action:23510014:"Give the Two Fingers' Prayerbook"
            AddTalkListDataIf(GetEventFlag(11109863) == 1, 4, 23510014, -1)
            # action:23510015:"Give the Assassin's Prayerbook"
            AddTalkListDataIf(GetEventFlag(11109864) == 1, 5, 23510015, -1)
            # action:23510016:"Give the Erdtree Prayerbook"
            AddTalkListDataIf(GetEventFlag(11109865) == 1, 6, 23510016, -1)
            # action:23510017:"Give the Erdtree Codex"
            AddTalkListDataIf(GetEventFlag(11109866) == 1, 7, 23510017, -1)
            # action:23510020:"Give the Dragon Cult Prayerbook"
            AddTalkListDataIf(GetEventFlag(11109869) == 1, 10, 23510020, -1)
            # action:23510021:"Give the Ancient Dragon Prayerbook"
            AddTalkListDataIf(GetEventFlag(11109870) == 1, 11, 23510021, -1)
            # action:23510022:"Don't give a prayerbook"
            AddTalkListData(99, 23510022, -1)
            """State 3"""
            ShowShopMessage(1)
            assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 5"""
            if GetTalkListEntryResult() == 8:
                """State 6"""
                SetEventFlag(11109881, 1)
                """State 7"""
                # goods:8862:Golden Order Principia
                PlayerEquipmentQuantityChange(3, 8862, -1)
            elif GetTalkListEntryResult() == 9:
                """State 9"""
                SetEventFlag(11109882, 1)
                """State 8"""
                # goods:8863:[ERROR]Golden Order Principles
                PlayerEquipmentQuantityChange(3, 8863, -1)
            elif (GetTalkListEntryResult() == 1 or GetTalkListEntryResult() == 2 or GetTalkListEntryResult()
                  == 3 or GetTalkListEntryResult() == 4 or GetTalkListEntryResult() == 5 or GetTalkListEntryResult()
                  == 6 or GetTalkListEntryResult() == 7 or GetTalkListEntryResult() == 10 or GetTalkListEntryResult()
                  == 11):
                """State 14"""
                if GetTalkListEntryResult() == 1:
                    """State 10"""
                    SetEventFlag(11109874, 1)
                    """State 11"""
                    # goods:8855:Fire Monks' Prayerbook
                    PlayerEquipmentQuantityChange(3, 8855, -1)
                elif GetTalkListEntryResult() == 2:
                    """State 13"""
                    SetEventFlag(11109875, 1)
                    """State 12"""
                    # goods:8856:Giant's Prayerbook
                    PlayerEquipmentQuantityChange(3, 8856, -1)
                elif GetTalkListEntryResult() == 3:
                    """State 19"""
                    SetEventFlag(11109876, 1)
                    """State 18"""
                    # goods:8857:Godskin Prayerbook
                    PlayerEquipmentQuantityChange(3, 8857, -1)
                elif GetTalkListEntryResult() == 4:
                    """State 16"""
                    SetEventFlag(11109877, 1)
                    """State 17"""
                    # goods:8858:Two Fingers' Prayerbook
                    PlayerEquipmentQuantityChange(3, 8858, -1)
                elif GetTalkListEntryResult() == 5:
                    """State 27"""
                    SetEventFlag(11109878, 1)
                    """State 26"""
                    # goods:8859:Assassin's Prayerbook
                    PlayerEquipmentQuantityChange(3, 8859, -1)
                elif GetTalkListEntryResult() == 6:
                    """State 24"""
                    SetEventFlag(11109879, 1)
                    """State 25"""
                    # goods:8860:Erdtree Prayerbook
                    PlayerEquipmentQuantityChange(3, 8860, -1)
                elif GetTalkListEntryResult() == 7:
                    """State 20"""
                    SetEventFlag(11109880, 1)
                    """State 21"""
                    # goods:8861:Erdtree Codex
                    PlayerEquipmentQuantityChange(3, 8861, -1)
                elif GetTalkListEntryResult() == 10:
                    """State 23"""
                    SetEventFlag(11109883, 1)
                    """State 22"""
                    # goods:8864:Dragon Cult Prayerbook
                    PlayerEquipmentQuantityChange(3, 8864, -1)
                elif GetTalkListEntryResult() == 11:
                    """State 28"""
                    SetEventFlag(11109884, 1)
                    """State 29"""
                    # goods:8865:Ancient Dragon Prayerbook
                    PlayerEquipmentQuantityChange(3, 8865, -1)
                """State 31,4"""
                if not GetEventFlag(4207) and not GetEventFlag(4208) and not GetEventFlag(4209):
                    """State 35"""
                    # talk:35109210:"That...is a work of heresy."
                    assert t351006000_x30(text3=35109210, mode5=1)
                else:
                    """State 37"""
                    # talk:35109200:"That...is a work of heresy."
                    assert t351006000_x30(text3=35109200, mode5=1)
                """State 32"""
                assert CheckSpecificPersonTalkHasEnded(0) == 1
                continue
            else:
                """State 15"""
                Goto('L0')
            """State 36"""
            # talk:35109000:"This...is a volume of incantation."
            assert t351006000_x30(text3=35109000, mode5=1) and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        else:
            pass
        """State 39"""
        Label('L0')
        return 0

def t351006000_x75():
    """State 0,1"""
    SetEventFlag(11109886, 0)
    SetEventFlag(11109860, 0)
    SetEventFlag(11109861, 0)
    SetEventFlag(11109862, 0)
    SetEventFlag(11109863, 0)
    SetEventFlag(11109864, 0)
    SetEventFlag(11109865, 0)
    SetEventFlag(11109866, 0)
    SetEventFlag(11109867, 0)
    SetEventFlag(11109868, 0)
    SetEventFlag(11109869, 0)
    SetEventFlag(11109870, 0)
    """State 2"""
    if not GetEventFlag(4207) and not GetEventFlag(4208) and not GetEventFlag(4209):
        pass
    else:
        """State 3"""
        SetEventFlag(11109887, 0)
    """State 4"""
    return 0

def t351006000_x76():
    """State 0"""
    while True:
        """State 2"""
        # actionbutton:6000:"Talk"
        call = t351006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                             flag4=6000)
        if call.Done():
            break
        elif (GetDistanceToPlayer() < 50 and GetEventFlag(11002733) == 1 and not GetEventFlag(11002734)
              and not GetEventFlag(11009460)):
            pass
        """State 3"""
        # talk:35104600:"Master! What ever is the matter?"
        call = t351006000_x31(text2=35104600, z5=11002734, mode4=1)
        if call.Done():
            pass
        elif GetEventFlag(11009460) == 1:
            """State 1"""
            pass
    """State 4"""
    return 0

