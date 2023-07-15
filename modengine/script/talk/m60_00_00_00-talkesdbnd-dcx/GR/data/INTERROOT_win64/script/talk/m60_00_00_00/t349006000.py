# -*- coding: utf-8 -*-
def t349006000_1():
    """State 0,1"""
    SetUpdateDistance(50)
    """State 2"""
    # actionbutton:6000:"Talk"
    t349006000_x6(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=26, val5=26, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t349006000_1000():
    """State 0,2,3"""
    assert t349006000_x38()
    """State 1"""
    c1_120(1000)
    Quit()

def t349006000_1103():
    """State 0,2,3"""
    assert t349006000_x39()
    """State 1"""
    c1_120(1103)
    Quit()

def t349006000_2000():
    """State 0,2,3"""
    assert t349006000_x40()
    """State 1"""
    c1_120(2000)
    Quit()

def t349006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t349006000_x1():
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

def t349006000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t349006000_x3(lot1=_):
    """State 0,1"""
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t349006000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t349006000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t349006000_x1()
    else:
        """State 4,7"""
        call = t349006000_x35()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t349006000_x1()
    """State 9"""
    return 0

def t349006000_x5():
    """State 0,1"""
    assert t349006000_x1()
    """State 2"""
    return 0

def t349006000_x6(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=26, val5=26, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t349006000_x23(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t349006000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t349006000_x7(val1=5, val2=10, val3=12, val4=26, val5=26, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t349006000_x10(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t349006000_x14(val1=val1, z1=z1)
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
            call = t349006000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t349006000_x27() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t349006000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t349006000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t349006000_x18(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t349006000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t349006000_x9(flag1=6000, val2=10, val3=12):
    """State 0,8"""
    assert t349006000_x37()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t349006000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t349006000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t349006000_x10(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t349006000_x11(z7=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t349006000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t349006000_x11(z7=_, val6=_):
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

def t349006000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t349006000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t349006000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t349006000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t349006000_x13():
    """State 0,1"""
    assert t349006000_x11(z7=1101, val6=1101)
    """State 2"""
    return 0

def t349006000_x14(val1=5, z1=1):
    """State 0,2"""
    assert t349006000_x24()
    """State 1"""
    call = t349006000_x15()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t349006000_x26()
    """State 4"""
    return 0

def t349006000_x15():
    """State 0,1"""
    assert t349006000_x11(z7=1000, val6=1000)
    """State 2"""
    return 0

def t349006000_x16(val5=26):
    """State 0,1"""
    call = t349006000_x17()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t349006000_x27()
    """State 3"""
    return 0

def t349006000_x17():
    """State 0,1"""
    assert t349006000_x11(z7=1100, val6=1100)
    """State 2"""
    return 0

def t349006000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t349006000_x37()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t349006000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t349006000_x29()
    """Unused"""
    """State 6"""
    return 0

def t349006000_x19():
    """State 0,2"""
    call = t349006000_x11(z7=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t349006000_x20():
    """State 0,1"""
    assert t349006000_x11(z7=1001, val6=1001)
    """State 2"""
    return 0

def t349006000_x21():
    """State 0,1"""
    assert t349006000_x11(z7=1103, val6=1103)
    """State 2"""
    return 0

def t349006000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t349006000_x23(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=26, val5=26, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t349006000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t349006000_x9(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t349006000_x8(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t349006000_x36() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t349006000_x24():
    """State 0,1"""
    assert t349006000_x25()
    """State 2"""
    return 0

def t349006000_x25():
    """State 0,1"""
    assert t349006000_x11(z7=1104, val6=1104)
    """State 2"""
    return 0

def t349006000_x26():
    """State 0,1"""
    call = t349006000_x11(z7=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t349006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t349006000_x27():
    """State 0,1"""
    call = t349006000_x11(z7=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t349006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t349006000_x28():
    """State 0,1"""
    call = t349006000_x11(z7=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t349006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t349006000_x29():
    """State 0,1"""
    call = t349006000_x11(z7=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t349006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t349006000_x30(text4=_, z6=_, mode6=1):
    """State 0,5"""
    assert t349006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t349006000_x31(text3=_, mode5=1):
    """State 0,4"""
    assert t349006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t349006000_x32(text2=34980300, z5=1050389203, mode4=1):
    """State 0,5"""
    assert t349006000_x34() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(z5, 1)
    """State 1"""
    # talk:34980300:"We shall meet again, you and I."
    TalkToPlayer(text2, -1, -1, 1)
    """State 4"""
    if not mode4:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t349006000_x33(text1=_, mode3=1):
    """State 0,4"""
    assert t349006000_x34() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t349006000_x34():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t349006000_x35():
    """State 0,1"""
    assert t349006000_x11(z7=1002, val6=1002)
    """State 2"""
    return 0

def t349006000_x36():
    """State 0,1"""
    assert t349006000_x1()
    """State 2"""
    return 0

def t349006000_x37():
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

def t349006000_x38():
    """State 0,3"""
    SetEventFlag(1050389209, 0)
    """State 1"""
    if GetEventFlag(4165) == 1:
        """State 4"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t349006000_x44()
    elif GetEventFlag(4166) == 1:
        """State 5"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t349006000_x45()
    elif GetEventFlag(4167) == 1:
        """State 6"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t349006000_x48()
    elif GetEventFlag(4168) == 1:
        """State 7"""
        def WhilePaused():
            RequestAnimationIf(not GetEventFlag(1050382704) and not GetEventFlag(1050389230), 90305,
                               -1)
            RequestAnimationIf(GetEventFlag(1050389230) == 1, 90300, -1)
        assert t349006000_x52()
    elif GetEventFlag(4169) == 1:
        """State 8"""
        assert t349006000_x70()
    elif GetEventFlag(4170) == 1:
        """State 9"""
        assert t349006000_x72()
    else:
        """State 2"""
        pass
    """State 10"""
    return 0

def t349006000_x39():
    """State 0,2"""
    if not GetEventFlag(4169) and not GetEventFlag(4170):
        """State 1"""
        if not GetEventFlag(1050389203):
            """State 3"""
            # talk:34980300:"We shall meet again, you and I."
            assert t349006000_x32(text2=34980300, z5=1050389203, mode4=1)
        else:
            """State 4"""
            # talk:34980400:"We shall meet again."
            assert t349006000_x33(text1=34980400, mode3=1)
    else:
        pass
    """State 5"""
    return 0

def t349006000_x40():
    """State 0"""
    while True:
        """State 1"""
        if GetEventFlag(4168) == 1:
            """State 5"""
            call = t349006000_x69()
            if call.Done():
                break
            elif GetEventFlag(4163) == 1:
                """State 3"""
                assert not GetEventFlag(4163)
        else:
            """State 4"""
            # actionbutton:6000:"Talk"
            call = t349006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                                 flag12=6000, flag4=6000)
            if call.Done():
                break
            elif GetEventFlag(4163) == 1:
                """State 2"""
                assert not GetEventFlag(4163)
    """State 6"""
    return 0

def t349006000_x41():
    """State 0,8"""
    if not GetEventFlag(1050389205):
        """State 1"""
        if not GetEventFlag(1050389206):
            """State 12"""
            # talk:34900100:"Oh, a pleasure to see you, a pleasure indeed."
            assert t349006000_x31(text3=34900100, mode5=1)
        else:
            """State 13"""
            # talk:34901400:"Ah, changed your mind, have you?"
            assert t349006000_x31(text3=34901400, mode5=1)
        """State 2"""
        c1_110()
        ClearTalkListData()
        """State 3"""
        # action:23491000:"Hear the request"
        AddTalkListData(1, 23491000, -1)
        # action:23491001:"Refuse"
        AddTalkListData(2, 23491001, -1)
        """State 4"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 15"""
            # talk:34901000:"Ah, then you're willing to lend a hand, are you?"
            assert t349006000_x31(text3=34901000, mode5=1)
            """State 6"""
            SetEventFlag(1050389205, 1)
        elif GetTalkListEntryResult() == 2:
            """State 16"""
            # talk:34901300:"Ah, my apologies. I rather got ahead of myself, didn't I."
            assert t349006000_x31(text3=34901300, mode5=1)
            """State 7"""
            SetEventFlag(1050389206, 1)
        else:
            """State 9"""
            pass
    else:
        """State 10"""
        if not GetEventFlag(1050389208):
            """State 17"""
            # talk:34901100:"The rotting sickness that afflicts Millicent has no cure."
            assert t349006000_x31(text3=34901100, mode5=1)
            """State 11"""
            SetEventFlag(1050389208, 1)
        else:
            """State 14"""
            # talk:34901200:"First, you must find the unalloyed gold needle."
            assert t349006000_x31(text3=34901200, mode5=1)
    """State 18"""
    return 0

def t349006000_x42():
    """State 0,1"""
    if not GetEventFlag(1050389207):
        """State 4"""
        # talk:34902000:"Ohh, you've found the unalloyed gold needle."
        assert t349006000_x31(text3=34902000, mode5=1)
        """State 3"""
        SetEventFlag(1050389207, 1)
        """State 2"""
        # goods:8975:Unalloyed Gold Needle
        PlayerEquipmentQuantityChange(3, 8975, -1)
        """State 7"""
        # lot:103110:Sellia's Secret
        assert t349006000_x3(lot1=103110)
        """State 6"""
        # talk:34902013:"Now, let me have a look at the needle."
        assert t349006000_x31(text3=34902013, mode5=1)
    else:
        """State 5"""
        # talk:34902300:"Can you give me some time with this?"
        assert t349006000_x31(text3=34902300, mode5=1)
    """State 8"""
    return 0

def t349006000_x43():
    """State 0,1"""
    if GetEventFlag(1050382702) == 1 and not GetEventFlag(1050382703):
        """State 2"""
        SetEventFlag(1050382703, 1)
        """State 3"""
        # talk:34908000:"Have you taken the lesson, now?"
        assert t349006000_x31(text3=34908000, mode5=1)
        """State 5"""
        return 1
    else:
        """State 4"""
        return 0

def t349006000_x44():
    """State 0,4"""
    call = t349006000_x43()
    if call.Get() == 0:
        """State 1"""
        # goods:8975:Unalloyed Gold Needle
        if (not GetEventFlag(1050389205) or (not GetEventFlag(1050389207) and ComparePlayerInventoryNumber(3,
            8975, 0, 0, 0) == 1)):
            """State 2"""
            assert t349006000_x41()
        else:
            """State 3"""
            assert t349006000_x42()
    elif call.Done():
        pass
    """State 5"""
    return 0

def t349006000_x45():
    """State 0,2"""
    call = t349006000_x43()
    if call.Get() == 0:
        """State 1"""
        assert t349006000_x46()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t349006000_x46():
    """State 0,1"""
    if not GetEventFlag(1050389210):
        """State 4"""
        # talk:34902100:"I have awaited your return."
        assert t349006000_x31(text3=34902100, mode5=1)
        """State 2"""
        SetEventFlag(1050389210, 1)
        """State 7"""
        # lot:103100:Unalloyed Gold Needle
        assert t349006000_x3(lot1=103100)
        """State 8"""
        # talk:34902114:"Millicent rests at the church atop the cliff, beyond Sellia, the town yonder."
        assert t349006000_x31(text3=34902114, mode5=1)
    elif not GetEventFlag(1050389211):
        """State 5"""
        # talk:34902200:"Do you find it peculiar?"
        assert t349006000_x31(text3=34902200, mode5=1)
        """State 3"""
        SetEventFlag(1050389211, 1)
    else:
        """State 6"""
        # talk:34902700:"Now, all you need do is deliver the needle to Millicent."
        assert t349006000_x31(text3=34902700, mode5=1)
    """State 9"""
    return 0

def t349006000_x47():
    """State 0,1"""
    if not GetEventFlag(1050389215):
        """State 5"""
        # talk:34903000:"Thank you kindly."
        assert t349006000_x31(text3=34903000, mode5=1)
        """State 2"""
        SetEventFlag(1050389215, 1)
        """State 3"""
        Label('L0')
        SetEventFlag(1050382704, 1)
    elif not GetEventFlag(1050389216):
        """State 6"""
        # talk:34903100:"Please make certain that little Millicent goes unharmed."
        assert t349006000_x31(text3=34903100, mode5=1)
        """State 4"""
        SetEventFlag(1050389216, 1)
        Goto('L0')
    elif not GetEventFlag(1050382704):
        """State 8"""
        # talk:34903500:"Ah, welcome, welcome. How may I help?"
        assert t349006000_x31(text3=34903500, mode5=1)
        Goto('L0')
    else:
        """State 7"""
        # talk:34903600:"Do you...need me for something else?"
        assert t349006000_x31(text3=34903600, mode5=1)
    """State 9"""
    return 0

def t349006000_x48():
    """State 0,1"""
    call = t349006000_x43()
    if call.Get() == 0:
        """State 2"""
        assert t349006000_x47()
        """State 3"""
        assert t349006000_x49()
    elif call.Done():
        pass
    """State 4"""
    return 0

def t349006000_x49():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        c1_110()
        """State 11"""
        assert t349006000_x51()
        """State 3"""
        if GetEventFlag(4167) == 1:
            """State 12"""
            assert t349006000_x50()
        elif GetEventFlag(4168) == 1:
            """State 13"""
            assert t349006000_x54()
        else:
            """State 4"""
            pass
        """State 2"""
        # action:23490000:"Study sorcery"
        AddTalkListData(1, 23490000, -1)
        # action:23490011:"Study incantations"
        AddTalkListDataIf(GetEventFlag(1038519257) == 1, 2, 23490011, -1)
        # action:23490001:"Millicent paid a visit"
        AddTalkListDataIf(GetEventFlag(1050389218) == 1, 50, 23490001, -1)
        # action:23490002:"I gave Millicent the prosthesis"
        AddTalkListDataIf(GetEventFlag(1050389220) == 1, 50, 23490002, -1)
        # action:23490003:"About Millicent"
        AddTalkListDataIf(GetEventFlag(1050389222) == 1, 50, 23490003, -1)
        # action:23490004:"About Malenia"
        AddTalkListDataIf(GetEventFlag(1050389224) == 1, 50, 23490004, -1)
        # action:23490005:"What Millicent said"
        AddTalkListDataIf(GetEventFlag(1050389226) == 1, 50, 23490005, -1)
        # action:23490006:"Why are you crying?"
        AddTalkListDataIf(GetEventFlag(1050389229) == 1, 50, 23490006, -1)
        # action:23490009:"Become a flower?"
        AddTalkListDataIf(GetEventFlag(1050389236) == 1, 50, 23490009, -1)
        # action:23490010:"Become a flower?"
        AddTalkListDataIf(GetEventFlag(1050389231) == 1, 50, 23490010, -1)
        # action:20000009:"Leave"
        AddTalkListData(99, 20000009, -1)
        """State 8"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 6"""
            OpenRegularShop(100175, 100184)
            c1_141(5)
            """State 7"""
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 10"""
            OpenRegularShop(100185, 100199)
            c1_141(5)
            """State 9"""
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 50:
            """State 15"""
            assert t349006000_x57() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        else:
            """State 14"""
            assert t349006000_x58()
            """State 17"""
            return 0
        """State 16"""
        assert t349006000_x60() and CheckSpecificPersonTalkHasEnded(0) == 1

def t349006000_x50():
    """State 0,1"""
    if GetEventFlag(1050389266) == 1 and not GetEventFlag(1050389219):
        """State 2"""
        SetEventFlag(1050389218, 1)
    elif GetEventFlag(1038519257) == 1 and not GetEventFlag(1050389221):
        """State 3"""
        SetEventFlag(1050389220, 1)
    elif GetEventFlag(1050389221) == 1 and not GetEventFlag(1050389223):
        """State 4"""
        SetEventFlag(1050389222, 1)
    elif GetEventFlag(1050389217) == 1 and not GetEventFlag(1050389225):
        """State 5"""
        SetEventFlag(1050389224, 1)
    elif GetEventFlag(15009206) == 1 and not GetEventFlag(1050389227):
        """State 6"""
        SetEventFlag(1050389226, 1)
    else:
        """State 7"""
        pass
    """State 8"""
    return 0

def t349006000_x51():
    """State 0,1"""
    SetEventFlag(1050389218, 0)
    SetEventFlag(1050389220, 0)
    SetEventFlag(1050389222, 0)
    SetEventFlag(1050389224, 0)
    SetEventFlag(1050389226, 0)
    SetEventFlag(1050389229, 0)
    SetEventFlag(1050389231, 0)
    SetEventFlag(1050389236, 0)
    """State 2"""
    return 0

def t349006000_x52():
    """State 0,1"""
    if not GetEventFlag(1050389230):
        """State 3"""
        Label('L0')
        assert t349006000_x53()
        """State 4"""
        assert t349006000_x49()
    else:
        """State 2"""
        call = t349006000_x43()
        if call.Get() == 0:
            Goto('L0')
        elif call.Done():
            pass
    """State 5"""
    return 0

def t349006000_x53():
    """State 0,1"""
    if not GetEventFlag(1050382704) and not GetEventFlag(1050389230):
        """State 4"""
        # talk:34907100:"Oh, mm, I didn't notice you there."
        assert t349006000_x31(text3=34907100, mode5=1)
    elif GetEventFlag(1050389230) == 1 and not GetEventFlag(1050382704):
        """State 5"""
        # talk:34907500:"Welcome, welcome. How may I help you?"
        assert t349006000_x31(text3=34907500, mode5=1)
        """State 3"""
        SetEventFlag(1050389233, 1)
    else:
        """State 6"""
        # talk:34903600:"Do you...need me for something else?"
        assert t349006000_x31(text3=34903600, mode5=1)
    """State 2"""
    SetEventFlag(1050382704, 1)
    """State 7"""
    return 0

def t349006000_x54():
    """State 0,1"""
    if not GetEventFlag(1050389230):
        """State 2"""
        SetEventFlag(1050389229, 1)
    elif GetEventFlag(1050389230) == 1 and not GetEventFlag(1050389237):
        """State 5"""
        SetEventFlag(1050389236, 1)
    elif GetEventFlag(1050389237) == 1:
        """State 3"""
        SetEventFlag(1050389231, 1)
    else:
        """State 4"""
        pass
    """State 6"""
    return 0

def t349006000_x55():
    """State 0,1"""
    if GetEventFlag(1050389218) == 1:
        """State 3"""
        assert t349006000_x62()
    elif GetEventFlag(1050389220) == 1:
        """State 4"""
        assert t349006000_x63()
    elif GetEventFlag(1050389222) == 1:
        """State 5"""
        assert t349006000_x64()
    elif GetEventFlag(1050389224) == 1:
        """State 6"""
        assert t349006000_x65()
    elif GetEventFlag(1050389226) == 1:
        """State 7"""
        assert t349006000_x66()
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t349006000_x56():
    """State 0,1"""
    if GetEventFlag(1050389229) == 1:
        """State 3"""
        assert t349006000_x67()
    elif GetEventFlag(1050389236) == 1:
        """State 5"""
        assert t349006000_x71()
    elif GetEventFlag(1050389231) == 1:
        """State 4"""
        assert t349006000_x68()
    else:
        """State 2"""
        pass
    """State 6"""
    return 0

def t349006000_x57():
    """State 0,1"""
    if GetEventFlag(4167) == 1:
        """State 3"""
        assert t349006000_x55()
    elif GetEventFlag(4168) == 1:
        """State 4"""
        assert t349006000_x56()
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t349006000_x58():
    """State 0,1"""
    if GetEventFlag(4168) == 1:
        """State 3"""
        assert t349006000_x59()
    else:
        """State 2"""
        pass
    """State 4"""
    return 0

def t349006000_x59():
    """State 0,1"""
    if not GetEventFlag(1050389233):
        pass
    else:
        """State 2"""
        # talk:34907600:"When the time is ripe..."
        assert t349006000_x31(text3=34907600, mode5=1)
    """State 3"""
    return 0

def t349006000_x60():
    """State 0,1"""
    if GetEventFlag(4167) == 1:
        """State 3"""
        assert t349006000_x61()
    else:
        """State 2"""
        pass
    """State 4"""
    return 0

def t349006000_x61():
    """State 0,1"""
    if GetEventFlag(1050389228) == 1 and not GetEventFlag(1050389217):
        """State 3"""
        # talk:34905000:"Do you have an interest in rot incantations?"
        assert t349006000_x31(text3=34905000, mode5=1)
        """State 2"""
        SetEventFlag(1050389217, 1)
    else:
        pass
    """State 4"""
    return 0

def t349006000_x62():
    """State 0,2"""
    # talk:34903200:"Oh, you noticed, did you?"
    assert t349006000_x31(text3=34903200, mode5=1)
    """State 1"""
    SetEventFlag(1050389219, 1)
    """State 3"""
    return 0

def t349006000_x63():
    """State 0,2"""
    # talk:34904000:"So, you gave Millicent a golden arm replacement…"
    assert t349006000_x31(text3=34904000, mode5=1)
    """State 1"""
    SetEventFlag(1050389221, 1)
    """State 3"""
    return 0

def t349006000_x64():
    """State 0,2"""
    # talk:34904100:"The girl, Millicent. She is a bud."
    assert t349006000_x31(text3=34904100, mode5=1)
    """State 1"""
    SetEventFlag(1050389223, 1)
    """State 3"""
    return 0

def t349006000_x65():
    """State 0,5"""
    # talk:34905100:"Queen Marika and her King Consort Radagon were blessed with twin demigods, and Malenia was one of them."
    assert t349006000_x31(text3=34905100, mode5=1)
    """State 3"""
    if not GetEventFlag(60842):
        """State 2"""
        # gesture:101:Desperate Prayer
        AcquireGesture(101)
        SetEventFlag(60842, 1)
    else:
        """State 4"""
        pass
    """State 1"""
    SetEventFlag(1050389225, 1)
    """State 6"""
    return 0

def t349006000_x66():
    """State 0,2"""
    # talk:34906000:"Oh, Millicent. Finding herself, is she?"
    assert t349006000_x31(text3=34906000, mode5=1)
    """State 1"""
    SetEventFlag(1050389227, 1)
    """State 3"""
    return 0

def t349006000_x67():
    """State 0,2"""
    # talk:34907200:"Oh, it's just…"
    assert t349006000_x31(text3=34907200, mode5=1)
    """State 1"""
    SetEventFlag(1050389230, 1)
    """State 3"""
    return 0

def t349006000_x68():
    """State 0,1"""
    # talk:34907400:"You can't tell me you don't wish to see it."
    assert t349006000_x31(text3=34907400, mode5=1)
    """State 2"""
    return 0

def t349006000_x69():
    """State 0"""
    while True:
        """State 2"""
        # actionbutton:6000:"Talk"
        call = t349006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                             flag4=6000)
        if call.Done():
            break
        elif GetDistanceToPlayer() < 16 and not GetEventFlag(1050382704) and not GetEventFlag(1050389230):
            """State 3"""
            # talk:34907000:"<sobbing>"
            call = t349006000_x33(text1=34907000, mode3=1)
            if call.Done():
                """State 4"""
                # actionbutton:6000:"Talk"
                call = t349006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                                     flag12=6000, flag4=6000)
                if call.Done():
                    break
                elif CheckSpecificPersonTalkHasEnded(0) == 1 and GetCurrentStateElapsedTime() > 25:
                    pass
            elif GetEventFlag(1050382704) == 1 or GetDistanceToPlayer() > 26:
                """State 1"""
                pass
    """State 5"""
    return 0

def t349006000_x70():
    """State 0,1"""
    if not GetEventFlag(1050389234):
        """State 2"""
        # talk:34907610:"<sigh>"
        assert t349006000_x30(text4=34907610, z6=1050389234, mode6=1)
    else:
        """State 3"""
        # talk:34907800:"Millicent..."
        assert t349006000_x31(text3=34907800, mode5=1)
    """State 4"""
    return 0

def t349006000_x71():
    """State 0,2"""
    # talk:34907210:"Which is why..."
    assert t349006000_x31(text3=34907210, mode5=1)
    """State 1"""
    SetEventFlag(1050389237, 1)
    """State 3"""
    return 0

def t349006000_x72():
    """State 0,1"""
    if not GetEventFlag(1050389235):
        """State 2"""
        # talk:34908010:"<sobbing>"
        assert t349006000_x30(text4=34908010, z6=1050389235, mode6=1)
    else:
        """State 3"""
        # talk:34910100:"Oh, Millicent..."
        assert t349006000_x31(text3=34910100, mode5=1)
    """State 4"""
    return 0

