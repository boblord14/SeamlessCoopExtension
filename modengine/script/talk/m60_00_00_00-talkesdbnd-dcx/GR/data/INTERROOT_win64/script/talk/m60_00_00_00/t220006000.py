# -*- coding: utf-8 -*-
def t220006000_1():
    """State 0,1"""
    SetUpdateDistance(100)
    """State 2"""
    # actionbutton:6000:"Talk"
    t220006000_x6(flag1=3663, flag2=3661, flag3=3662, val1=5, val2=10, val3=12, val4=50, val5=50, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t220006000_1000():
    """State 0,2,3"""
    assert t220006000_x37()
    """State 1"""
    c1_120(1000)
    Quit()

def t220006000_1001():
    """State 0,2,3"""
    assert t220006000_x38()
    """State 1"""
    c1_120(1001)
    Quit()

def t220006000_1101():
    """State 0,2,3"""
    assert t220006000_x39()
    """State 1"""
    c1_120(1101)
    Quit()

def t220006000_1102():
    """State 0,2,3"""
    t220006000_x40()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t220006000_1103():
    """State 0,2,3"""
    assert t220006000_x41()
    """State 1"""
    c1_120(1103)
    Quit()

def t220006000_2000():
    """State 0,2,3"""
    assert t220006000_x42()
    """State 1"""
    c1_120(2000)
    Quit()

def t220006000_x0(actionbutton1=_, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag4=6000):
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

def t220006000_x1():
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

def t220006000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t220006000_x3(lot1=_):
    """State 0,1"""
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t220006000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t220006000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t220006000_x1()
    else:
        """State 4,7"""
        call = t220006000_x34()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t220006000_x1()
    """State 9"""
    return 0

def t220006000_x5():
    """State 0,1"""
    assert t220006000_x1()
    """State 2"""
    return 0

def t220006000_x6(flag1=3663, flag2=3661, flag3=3662, val1=5, val2=10, val3=12, val4=50, val5=50, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t220006000_x23(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t220006000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t220006000_x7(val1=5, val2=10, val3=12, val4=50, val5=50, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t220006000_x10(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t220006000_x14(val1=val1, z1=z1)
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
            call = t220006000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t220006000_x27() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t220006000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t220006000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t220006000_x18(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t220006000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t220006000_x9(flag1=3663, val2=10, val3=12):
    """State 0,8"""
    assert t220006000_x36()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t220006000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t220006000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t220006000_x10(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t220006000_x11(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t220006000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t220006000_x11(z6=_, val6=_):
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

def t220006000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t220006000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t220006000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t220006000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t220006000_x13():
    """State 0,1"""
    assert t220006000_x11(z6=1101, val6=1101)
    """State 2"""
    return 0

def t220006000_x14(val1=5, z1=1):
    """State 0,2"""
    assert t220006000_x24()
    """State 1"""
    call = t220006000_x15()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t220006000_x26()
    """State 4"""
    return 0

def t220006000_x15():
    """State 0,1"""
    assert t220006000_x11(z6=1000, val6=1000)
    """State 2"""
    return 0

def t220006000_x16(val5=50):
    """State 0,1"""
    call = t220006000_x17()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t220006000_x27()
    """State 3"""
    return 0

def t220006000_x17():
    """State 0,1"""
    assert t220006000_x11(z6=1100, val6=1100)
    """State 2"""
    return 0

def t220006000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t220006000_x36()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t220006000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t220006000_x29()
    """Unused"""
    """State 6"""
    return 0

def t220006000_x19():
    """State 0,2"""
    call = t220006000_x11(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t220006000_x20():
    """State 0,1"""
    assert t220006000_x11(z6=1001, val6=1001)
    """State 2"""
    return 0

def t220006000_x21():
    """State 0,1"""
    assert t220006000_x11(z6=1103, val6=1103)
    """State 2"""
    return 0

def t220006000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t220006000_x23(flag1=3663, flag2=3661, flag3=3662, val1=5, val2=10, val3=12, val4=50, val5=50, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t220006000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t220006000_x9(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t220006000_x8(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t220006000_x35() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t220006000_x24():
    """State 0,1"""
    assert t220006000_x25()
    """State 2"""
    return 0

def t220006000_x25():
    """State 0,1"""
    assert t220006000_x11(z6=1104, val6=1104)
    """State 2"""
    return 0

def t220006000_x26():
    """State 0,1"""
    call = t220006000_x11(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t220006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t220006000_x27():
    """State 0,1"""
    call = t220006000_x11(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t220006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t220006000_x28():
    """State 0,1"""
    call = t220006000_x11(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t220006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t220006000_x29():
    """State 0,1"""
    call = t220006000_x11(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t220006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t220006000_x30(text3=_, mode5=1):
    """State 0,4"""
    assert t220006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t220006000_x31(text2=_, z5=_, mode4=1):
    """State 0,5"""
    assert t220006000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t220006000_x32(text1=_, mode3=1):
    """State 0,4"""
    assert t220006000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t220006000_x33():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t220006000_x34():
    """State 0,1"""
    assert t220006000_x11(z6=1002, val6=1002)
    """State 2"""
    return 0

def t220006000_x35():
    """State 0,1"""
    assert t220006000_x1()
    """State 2"""
    return 0

def t220006000_x36():
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

def t220006000_x37():
    """State 0,1"""
    if GetEventFlag(3665) == 1:
        """State 3"""
        assert t220006000_x43()
    elif GetEventFlag(3666) == 1:
        """State 4"""
        assert t220006000_x49()
    elif GetEventFlag(3667) == 1:
        """State 5"""
        def WhilePaused():
            RequestAnimation(20025, -1)
        assert t220006000_x50()
    elif GetEventFlag(3668) == 1:
        """State 6"""
        assert t220006000_x51()
    elif GetEventFlag(3669) == 1:
        """State 7"""
        assert t220006000_x52()
    elif GetEventFlag(3670) == 1:
        """State 8"""
        def WhilePaused():
            RequestAnimation(20045, -1)
        assert t220006000_x53()
    elif GetEventFlag(3671) == 1:
        """State 9"""
        assert t220006000_x54()
    else:
        """State 2"""
        pass
    """State 10"""
    return 0

def t220006000_x38():
    """State 0,1"""
    if not GetEventFlag(13009256):
        """State 2"""
        # talk:22081000:"A finer battle was never witnessed."
        assert t220006000_x32(text1=22081000, mode3=1)
    else:
        """State 3"""
        # talk:22010200:"Good sir, I can't believe your heart was in it at all."
        assert t220006000_x32(text1=22010200, mode3=1)
    """State 4"""
    return 0

def t220006000_x39():
    """State 0,1"""
    if GetEventFlag(3665) == 1 and not GetEventFlag(1043399311):
        """State 2,10"""
        assert t220006000_x48()
    elif GetEventFlag(3669) == 1 and not GetEventFlag(1039449214):
        """State 3,11"""
        assert t220006000_x57()
    elif GetEventFlag(3671) == 1 and GetEventFlag(13009256) == 1:
        """State 5"""
        pass
    else:
        """State 4,7"""
        if not GetEventFlag(1043392711):
            """State 12"""
            # talk:22080000:"Ngh!"
            assert t220006000_x32(text1=22080000, mode3=1)
            """State 8"""
            SetEventFlag(1043392711, 1)
        elif not GetEventFlag(1043392715):
            """State 13"""
            # talk:22080100:"What are you playing at?"
            assert t220006000_x32(text1=22080100, mode3=1)
            """State 6"""
            SetEventFlag(1043392715, 1)
        else:
            """State 9"""
            pass
    """State 14"""
    return 0

def t220006000_x40():
    """State 0,5"""
    if not GetEventFlag(13009256):
        """State 2"""
        if not GetEventFlag(1043399303):
            """State 3,10"""
            # talk:22080200:"Wait, I see. I see it now."
            assert (t220006000_x31(text2=22080200, z5=1043399303, mode4=1) and CheckSpecificPersonTalkHasEnded(0)
                    == 1)
            """State 11"""
            # talk:22080300:"Then there's nothing left to say, except..."
            assert t220006000_x32(text1=22080300, mode3=1)
        else:
            """State 4"""
            pass
    else:
        """State 9"""
        if not GetEventFlag(13009261):
            """State 13"""
            # talk:22009105:"Then let us begin!"
            assert t220006000_x31(text2=22009105, z5=13009261, mode4=1)
        else:
            """State 6"""
            assert GetDistanceToPlayer() < 10
            """State 7"""
            if not GetEventFlag(13002715):
                """State 12"""
                # talk:22009110:"I am the great jar warrior, Iron Fist Alexander!"
                assert t220006000_x31(text2=22009110, z5=13002715, mode4=1)
            else:
                """State 8"""
                pass
    """State 1"""
    Quit()
    """Unused"""
    """State 14"""
    return 0

def t220006000_x41():
    """State 0,1"""
    if not GetEventFlag(13009256):
        """State 3"""
        # talk:22082000:"How could this..."
        assert t220006000_x32(text1=22082000, mode3=1)
    else:
        """State 2"""
        pass
    """State 4"""
    return 0

def t220006000_x42():
    """State 0"""
    while True:
        """State 1"""
        if GetEventFlag(3665) == 1:
            """State 2"""
            call = t220006000_x46()
            if call.Done():
                break
            elif not GetEventFlag(3665):
                pass
        elif GetEventFlag(3669) == 1:
            """State 3"""
            call = t220006000_x55()
            if call.Done():
                break
            elif not GetEventFlag(3669):
                pass
        elif GetEventFlag(3670) == 1:
            """State 4"""
            call = t220006000_x58()
            if call.Done():
                break
            elif not GetEventFlag(3670):
                pass
        elif GetEventFlag(3671) == 1:
            """State 5"""
            call = t220006000_x61()
            if call.Done():
                break
            elif not GetEventFlag(3671):
                pass
        else:
            """State 6"""
            # actionbutton:6270:"Talk"
            call = t220006000_x0(actionbutton1=6270, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                                 flag12=6000, flag4=6000)
            if call.Done():
                break
            elif (GetEventFlag(3665) == 1 or GetEventFlag(3669) == 1 or GetEventFlag(3670) == 1 or GetEventFlag(3671)
                  == 1):
                pass
    """State 7"""
    return 0

def t220006000_x43():
    """State 0,1"""
    if not GetEventFlag(1043399306):
        """State 2"""
        def WhilePaused():
            RequestAnimation(20032, -1)
        assert t220006000_x44()
    elif not GetEventFlag(1043399311):
        """State 3"""
        def WhilePaused():
            RequestAnimation(20032, -1)
        assert t220006000_x62()
    else:
        """State 4"""
        def WhilePaused():
            RequestAnimation(20025, -1)
        assert t220006000_x45()
    """State 5"""
    return 0

def t220006000_x44():
    """State 0,2"""
    if not GetEventFlag(1043399305):
        """State 13"""
        # talk:22000200:"Oh my stars I'm so happy to see you!"
        assert t220006000_x30(text3=22000200, mode5=1)
        """State 11"""
        SetEventFlag(1043392716, 1)
        """State 1"""
        SetEventFlag(1043399305, 1)
        """State 10"""
        SetEventFlag(1043399313, 1)
    else:
        """State 14"""
        # talk:22000900:"Ah, what's that look, good sir?"
        assert t220006000_x30(text3=22000900, mode5=1)
    """State 3"""
    ClearTalkListData()
    """State 7"""
    # action:22201000:"Help him out"
    AddTalkListData(1, 22201000, -1)
    # action:22201001:"Don't help"
    AddTalkListData(2, 22201001, -1)
    """State 6"""
    OpenConversationChoicesMenu(0)
    """State 8"""
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 4"""
    if GetTalkListEntryResult() == 1:
        """State 5"""
        SetEventFlag(1043399306, 1)
        """State 12"""
        c1_121(9743)
        """State 15"""
        # talk:22000230:"My thanks! A thousand thanks!"
        assert t220006000_x30(text3=22000230, mode5=1)
    elif GetTalkListEntryResult() == 2:
        """State 16"""
        # talk:22000800:"I see. More's the pity."
        assert t220006000_x30(text3=22000800, mode5=1)
    else:
        """State 9"""
        pass
    """State 17"""
    return 0

def t220006000_x45():
    """State 0,1"""
    if not GetEventFlag(1043399307):
        """State 4"""
        # talk:22000600:"Ahh! Well played, good sir. Well played!"
        assert t220006000_x30(text3=22000600, mode5=1)
        """State 2"""
        SetEventFlag(1043399307, 1)
        """State 6"""
        # lot:101700:Exalted Flesh
        assert t220006000_x3(lot1=101700)
    elif not GetEventFlag(1043399308):
        """State 5"""
        # talk:22000700:"Once again, the pleasure is mine. I am the warrior jar known as Alexander. Iron Fist Alexander, in fact."
        assert t220006000_x30(text3=22000700, mode5=1)
        """State 3"""
        SetEventFlag(1043399308, 1)
    else:
        """State 7"""
        # talk:22001300:"I'm heading eastward."
        assert t220006000_x30(text3=22001300, mode5=1)
    """State 8"""
    return 0

def t220006000_x46():
    """State 0,1"""
    if GetEventFlag(1043392716) == 1 or GetEventFlag(1043399306) == 1:
        """State 4"""
        # actionbutton:6270:"Talk"
        assert (t220006000_x0(actionbutton1=6270, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                flag4=6000))
    else:
        """State 2"""
        SetEventFlag(32009203, 0)
        """State 3"""
        assert t220006000_x47()
    """State 5"""
    return 0

def t220006000_x47():
    """State 0"""
    while True:
        """State 2"""
        # actionbutton:6270:"Talk"
        call = t220006000_x0(actionbutton1=6270, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                             flag4=6000)
        if call.Done():
            break
        elif call.Done():
            break
        elif (GetEventFlag(1043392712) == 1 and not GetEventFlag(1043392713) and CheckSpecificPersonTalkHasEnded(0)
              == 1 and not GetEventFlag(1043392716) and not GetEventFlag(1043392711)):
            pass
        """State 3"""
        # talk:22000100:"Hello-o? Can you hear me?"
        call = t220006000_x31(text2=22000100, z5=1043392713, mode4=1)
        if call.Done():
            pass
        elif GetEventFlag(1043392716) == 1:
            """State 1"""
            pass
    """State 4"""
    return 0

def t220006000_x48():
    """State 0,9"""
    if GetEventFlag(1043399306) == 1:
        """State 5"""
        if True:
            """State 8"""
            if RelativeAngleBetweenTwoPlayers_SpecifyAxis(180) < 110:
                """State 3"""
                if not GetEventFlag(1043399311) and GetSelfHP() < 93:
                    """State 6"""
                    RequestAnimation(20034, -1)
                    """State 1"""
                    SetEventFlag(1043399312, 1)
                    """State 19"""
                    c1_121(9743)
                    """State 21"""
                    # talk:22000500:"Ahhh!"
                    assert t220006000_x31(text2=22000500, z5=1043399311, mode4=1)
                    """State 17"""
                    SetEventFlag(1043392715, 0)
                    SetEventFlag(1043392711, 0)
                    """State 15"""
                    if not GetEventFlag(60828):
                        """State 14"""
                        # gesture:71:Triumphant Delight
                        AcquireGesture(71)
                        SetEventFlag(60828, 1)
                    else:
                        """State 16"""
                        pass
                elif GetWorkValue(0) > 2:
                    """State 18"""
                    pass
                elif GetWorkValue(0) > 1:
                    """State 4"""
                    SetWorkValue(0, 2)
                    """State 23"""
                    # talk:22000310:"Ouuch!"
                    assert t220006000_x32(text1=22000310, mode3=1)
                elif GetWorkValue(0) > 0:
                    """State 2"""
                    SetWorkValue(0, 1)
                    """State 7"""
                    SetEventFlag(1035532709, 1)
                    """State 22"""
                    # talk:22000300:"Ah!"
                    assert t220006000_x32(text1=22000300, mode3=1)
            else:
                """State 24"""
                # talk:22001200:"G-good gosh, stop, please! That's my face!"
                assert t220006000_x32(text1=22001200, mode3=1)
        else:
            """State 20"""
            # talk:22000400:"S-stop please! That's a little too rough for me, friend."
            assert t220006000_x31(text2=22000400, z5=1043399309, mode4=1)
    else:
        """State 10"""
        if not GetEventFlag(1043392711):
            """State 25"""
            # talk:22080000:"Ngh!"
            assert t220006000_x32(text1=22080000, mode3=1)
            """State 12"""
            SetEventFlag(1043392711, 1)
        elif not GetEventFlag(1043392715):
            """State 26"""
            # talk:22080100:"What are you playing at?"
            assert t220006000_x32(text1=22080100, mode3=1)
            """State 13"""
            SetEventFlag(1043392715, 1)
        else:
            """State 11"""
            pass
    """State 27"""
    return 0

def t220006000_x49():
    """State 0,1"""
    if not GetEventFlag(32070560):
        """State 2"""
        def WhilePaused():
            RequestAnimation(20025, -1)
        assert t220006000_x63()
    else:
        """State 3"""
        def WhilePaused():
            RequestAnimation(20025, -1)
        assert t220006000_x64()
    """State 4"""
    return 0

def t220006000_x50():
    """State 0,2"""
    if not GetEventFlag(1051369255):
        """State 3"""
        if not GetEventFlag(1043399313):
            """State 5"""
            # talk:22004100:"Ah, if it isn't a Tarnished warrior."
            assert t220006000_x30(text3=22004100, mode5=1)
            """State 4"""
            SetEventFlag(1043399313, 1)
        else:
            """State 7"""
            # talk:22004000:"Ah, you came, how delightful!"
            assert t220006000_x30(text3=22004000, mode5=1)
        """State 1"""
        SetEventFlag(1051369255, 1)
    else:
        """State 6"""
        # talk:22004200:"Be sure to get a good vantage, my friend."
        assert t220006000_x30(text3=22004200, mode5=1)
    """State 8"""
    return 0

def t220006000_x51():
    """State 0,5"""
    SetEventFlag(1043399313, 1)
    """State 2"""
    if not GetEventFlag(1051369265):
        """State 6"""
        # talk:22005000:"A-ah, hello there."
        assert t220006000_x30(text3=22005000, mode5=1)
        """State 1"""
        SetEventFlag(1051369265, 1)
    elif not GetEventFlag(1051369266):
        """State 7"""
        # talk:22005100:"...But don't you think I've given up just yet."
        assert t220006000_x30(text3=22005100, mode5=1)
        """State 3"""
        SetEventFlag(1051369266, 1)
    elif not GetEventFlag(1051369267):
        """State 8"""
        # talk:22005300:"The bodies found here are exceedingly fine."
        assert t220006000_x30(text3=22005300, mode5=1)
        """State 4"""
        SetEventFlag(1051369267, 1)
    else:
        """State 9"""
        # talk:22005200:"Alright lads, I'm going to take you on a little journey."
        assert t220006000_x30(text3=22005200, mode5=1)
    """State 10"""
    return 0

def t220006000_x52():
    """State 0,2"""
    SetEventFlag(1043399313, 1)
    """State 1"""
    if not GetEventFlag(1039449206):
        """State 3"""
        def WhilePaused():
            RequestAnimation(20032, -1)
        assert t220006000_x65()
    elif not GetEventFlag(1039449214):
        """State 4"""
        def WhilePaused():
            RequestAnimation(20032, -1)
        assert t220006000_x66()
    else:
        """State 5"""
        def WhilePaused():
            RequestAnimation(20025, -1)
        assert t220006000_x69()
    """State 6"""
    return 0

def t220006000_x53():
    """State 0,1"""
    if not GetEventFlag(1035539205):
        """State 4"""
        # talk:22008100:"Nnngh!"
        assert t220006000_x30(text3=22008100, mode5=1)
        """State 2"""
        SetEventFlag(1035539205, 1)
        """State 3"""
        SetEventFlag(1035539209, 1)
        """State 7"""
        # lot:101720:Jar
        assert t220006000_x3(lot1=101720)
        """State 6"""
        # talk:22008110:"But oh, it's hardly more than lukewarm here."
        assert t220006000_x30(text3=22008110, mode5=1)
    else:
        """State 5"""
        # talk:22008300:"Perhaps I'll head eastward."
        assert t220006000_x30(text3=22008300, mode5=1)
    """State 8"""
    return 0

def t220006000_x54():
    """State 0,2"""
    SetEventFlag(1043399313, 1)
    """State 1"""
    if not GetEventFlag(13009258):
        """State 3"""
        def WhilePaused():
            RequestAnimation(20025, -1)
        assert t220006000_x59()
    else:
        """State 4"""
        def ExitPause():
            SetEventFlag(13009257, 1)
        assert t220006000_x60()
    """State 5"""
    return 0

def t220006000_x55():
    """State 0,1"""
    if GetEventFlag(1039449206) == 1 or GetEventFlag(1043392716) == 1:
        """State 2"""
        # actionbutton:6270:"Talk"
        assert (t220006000_x0(actionbutton1=6270, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                flag4=6000))
    else:
        """State 3"""
        assert t220006000_x56()
    """State 4"""
    return 0

def t220006000_x56():
    """State 0"""
    while True:
        """State 2"""
        # actionbutton:6270:"Talk"
        call = t220006000_x0(actionbutton1=6270, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                             flag4=6000)
        if call.Done():
            break
        elif call.Done():
            break
        elif (GetEventFlag(1039442702) == 1 and not GetEventFlag(1039442703) and CheckSpecificPersonTalkHasEnded(0)
              == 1 and not GetEventFlag(1043392716) and not GetEventFlag(1043392711)):
            pass
        """State 3"""
        # talk:22006000:"Hello-o? Can you hear me?"
        call = t220006000_x31(text2=22006000, z5=1039442703, mode4=1)
        if call.Done():
            pass
        elif GetEventFlag(1043392716) == 1:
            """State 1"""
            pass
    """State 4"""
    return 0

def t220006000_x57():
    """State 0,2"""
    if GetEventFlag(1039449206) == 1:
        """State 1"""
        if not GetEventFlag(1039449207):
            """State 7"""
            assert t220006000_x70()
        else:
            """State 8"""
            assert t220006000_x71()
    else:
        """State 3"""
        if not GetEventFlag(1043392711):
            """State 9"""
            # talk:22080000:"Ngh!"
            assert t220006000_x32(text1=22080000, mode3=1)
            """State 5"""
            SetEventFlag(1043392711, 1)
        elif not GetEventFlag(1043392715):
            """State 10"""
            # talk:22080100:"What are you playing at?"
            assert t220006000_x32(text1=22080100, mode3=1)
            """State 6"""
            SetEventFlag(1043392715, 1)
        else:
            """State 4"""
            pass
    """State 11"""
    return 0

def t220006000_x58():
    """State 0"""
    while True:
        """State 3"""
        # actionbutton:6271:"Talk"
        call = t220006000_x0(actionbutton1=6271, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                             flag4=6000)
        if call.Done():
            break
        elif call.Done():
            break
        elif (GetEventFlag(1035532702) == 1 and CheckSpecificPersonTalkHasEnded(0) == 1 and not GetEventFlag(1035539205)
              and not GetEventFlag(1043392711)):
            pass
        """State 2"""
        SetEventFlag(1035532702, 0)
        """State 4"""
        # talk:22008000:"Ngh!"
        call = t220006000_x31(text2=22008000, z5=1035532703, mode4=1)
        if call.Done():
            pass
        elif GetEventFlag(1035539205) == 1:
            """State 1"""
            pass
    """State 5"""
    return 0

def t220006000_x59():
    """State 0,2"""
    if not GetEventFlag(13009255):
        """State 4"""
        if not GetEventFlag(13009259):
            """State 5"""
            # talk:22009200:"Ah, I see you've finally made it here yourself."
            assert t220006000_x30(text3=22009200, mode5=1)
        else:
            """State 7"""
            # talk:22009000:"Ah, I see you've finally made it here yourself."
            assert t220006000_x30(text3=22009000, mode5=1)
        """State 1"""
        SetEventFlag(13009255, 1)
    else:
        """State 6"""
        # talk:22009100:"You are ready then, I take it?"
        assert t220006000_x30(text3=22009100, mode5=1)
        """State 3"""
        SetEventFlag(13009256, 1)
    """State 8"""
    return 0

def t220006000_x60():
    """State 0,1"""
    SetEventFlag(13009257, 1)
    """State 4"""
    # talk:22010100:"My thanks. I knew you were the stuff of champions."
    call = t220006000_x32(text1=22010100, mode3=1)
    if call.Done() and CheckSpecificPersonTalkHasEnded(0) == 1:
        pass
    elif GetDistanceToPlayer() > 50:
        """State 3"""
        SetEventFlag(13009260, 1)
    """State 2"""
    Quit()
    """Unused"""
    """State 5"""
    return 0

def t220006000_x61():
    """State 0"""
    while True:
        """State 4"""
        # actionbutton:6270:"Talk"
        call = t220006000_x0(actionbutton1=6270, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                             flag4=6000)
        if call.Done():
            break
        elif call.Done():
            break
        elif not GetEventFlag(13009258) and GetEventFlag(13002712) == 1:
            """State 3"""
            StopEventAnimWithoutForcingConversationEnd(0)
            """State 2"""
            SetEventFlag(13009258, 1)
            """State 1"""
            assert GetCurrentStateElapsedTime() > 5.5
            """State 5"""
            # talk:22010000:"As I suspected... Victory...was impossible."
            assert t220006000_x32(text1=22010000, mode3=1)
    """State 6"""
    return 0

def t220006000_x62():
    """State 0,1"""
    if not GetEventFlag(1035532709):
        """State 2"""
        # talk:22001000:"Come on, give me a good smack from behind with something nice and big."
        assert t220006000_x30(text3=22001000, mode5=1)
    else:
        """State 3"""
        # talk:22001100:"Don't stop now, friend."
        assert t220006000_x30(text3=22001100, mode5=1)
    """State 4"""
    return 0

def t220006000_x63():
    """State 0,1"""
    if not GetEventFlag(32009205):
        """State 2"""
        if GetEventFlag(1043399313) == 1:
            """State 6"""
            # talk:22002000:"Oh, I hadn't expected to see your face again."
            assert t220006000_x30(text3=22002000, mode5=1)
        elif not GetEventFlag(1043399313):
            """State 7"""
            # talk:22002200:"Ah, if it isn't a Tarnished warrior."
            assert t220006000_x30(text3=22002200, mode5=1)
            """State 4"""
            SetEventFlag(1043399313, 1)
        """State 3"""
        SetEventFlag(32009205, 1)
    else:
        """State 5"""
        # talk:22002100:"I was created to be a warrior vessel."
        assert t220006000_x30(text3=22002100, mode5=1)
    """State 8"""
    return 0

def t220006000_x64():
    """State 0,1"""
    if not GetEventFlag(32009206):
        """State 2"""
        if GetEventFlag(1043399313) == 1 and not GetEventFlag(32009205):
            """State 6"""
            # talk:22003100:"...!"
            assert t220006000_x30(text3=22003100, mode5=1)
        elif GetEventFlag(1043399313) == 1 and GetEventFlag(32009205) == 1:
            """State 8"""
            # talk:22003000:"...!"
            assert t220006000_x30(text3=22003000, mode5=1)
        elif not GetEventFlag(1043399313):
            """State 7"""
            # talk:22003200:"...!"
            assert t220006000_x30(text3=22003200, mode5=1)
            """State 4"""
            SetEventFlag(1043399313, 1)
        """State 3"""
        SetEventFlag(32009206, 1)
    else:
        """State 5"""
        # talk:22003300:"It's time I set off."
        assert t220006000_x30(text3=22003300, mode5=1)
    """State 9"""
    return 0

def t220006000_x65():
    """State 0,2"""
    if not GetEventFlag(1039449205):
        """State 10"""
        if not GetEventFlag(1043399306):
            """State 14"""
            # talk:22006900:"Ahh, hello! How nice it is to see a friendly face!"
            assert t220006000_x30(text3=22006900, mode5=1)
        else:
            """State 18"""
            # talk:22006100:"Ahh, hello! How nice it is to see a friendly face!"
            assert t220006000_x30(text3=22006100, mode5=1)
        """State 12"""
        SetEventFlag(1043392716, 1)
        """State 1"""
        SetEventFlag(1039449205, 1)
    else:
        """State 15"""
        # talk:22006500:"What's that look, good sir?"
        assert t220006000_x30(text3=22006500, mode5=1)
    """State 3"""
    ClearTalkListData()
    """State 7"""
    # action:22201000:"Help him out"
    AddTalkListData(1, 22201000, -1)
    # action:22201001:"Don't help"
    AddTalkListData(2, 22201001, -1)
    """State 6"""
    OpenConversationChoicesMenu(0)
    """State 8"""
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 4"""
    if GetTalkListEntryResult() == 1:
        """State 5"""
        SetEventFlag(1039449206, 1)
        """State 13"""
        c1_121(9743)
        """State 11"""
        if not GetEventFlag(1043399306):
            """State 16"""
            # talk:22014100:"My thanks! A thousand thanks!"
            assert t220006000_x30(text3=22014100, mode5=1)
        else:
            """State 19"""
            # talk:22006113:"My thanks in advance, I know you're the man for the job!"
            assert t220006000_x30(text3=22006113, mode5=1)
    elif GetTalkListEntryResult() == 2:
        """State 17"""
        # talk:22006400:"I see. More's the pity."
        assert t220006000_x30(text3=22006400, mode5=1)
    else:
        """State 9"""
        pass
    """State 20"""
    return 0

def t220006000_x66():
    """State 0,1"""
    if not GetEventFlag(1039449211):
        """State 2"""
        assert t220006000_x67()
    else:
        """State 3"""
        assert t220006000_x68()
    """State 4"""
    return 0

def t220006000_x67():
    """State 0,1"""
    # talk:22006600:"Come on, give me a good smack from behind with something nice and big!"
    assert t220006000_x30(text3=22006600, mode5=1)
    """State 2"""
    return 0

def t220006000_x68():
    """State 0,1"""
    if GetEventFlag(1039449207) == 1:
        """State 4"""
        # talk:22013000:"By the gods you are a man of vision!"
        assert t220006000_x30(text3=22013000, mode5=1)
    elif GetEventFlag(1039442704) == 1 and not GetEventFlag(1039442705):
        """State 5"""
        # talk:22014000:"Phew."
        assert t220006000_x30(text3=22014000, mode5=1)
        """State 2"""
        SetEventFlag(1039442705, 1)
    elif not GetEventFlag(1039449208):
        """State 7"""
        # talk:22006700:"I can feel my lower half is stuck on something."
        assert t220006000_x30(text3=22006700, mode5=1)
        """State 3"""
        SetEventFlag(1039449208, 1)
    else:
        """State 6"""
        # talk:22006800:"Hmm..."
        assert t220006000_x30(text3=22006800, mode5=1)
    """State 8"""
    return 0

def t220006000_x69():
    """State 0,1"""
    if not GetEventFlag(1039449209):
        """State 4"""
        # talk:22007200:"My thanks! To you and your razor-sharp wits."
        assert t220006000_x30(text3=22007200, mode5=1) and CheckSpecificPersonTalkHasEnded(0) == 1
        """State 2"""
        SetEventFlag(1039449209, 1)
        """State 6"""
        # lot:101710:Exalted Flesh
        assert t220006000_x3(lot1=101710)
        """State 8"""
        # talk:22007300:"Deary me, I'm oilier than a toad!"
        assert t220006000_x30(text3=22007300, mode5=1)
    elif not GetEventFlag(1039449210):
        """State 5"""
        # talk:22007400:"Yes, indeed, I too have a home."
        assert t220006000_x30(text3=22007400, mode5=1)
        """State 3"""
        SetEventFlag(1039449210, 1)
    else:
        """State 7"""
        # talk:22007500:"I'm headed to the fiery mount in the north."
        assert t220006000_x30(text3=22007500, mode5=1)
    """State 9"""
    return 0

def t220006000_x70():
    """State 0,11"""
    if RelativeAngleBetweenTwoPlayers_SpecifyAxis(180) < 110:
        """State 5"""
        if not GetEventFlag(1039449211):
            """State 1"""
            if GetWorkValue(0) > 2 or GetSelfHP() < 95:
                """State 13"""
                # talk:22006300:"P-please! Wait. I have a terrible feeling about this!"
                assert t220006000_x31(text2=22006300, z5=1039449211, mode4=1)
                """State 4"""
                SetWorkValue(0, 0)
            elif GetWorkValue(0) > 1:
                """State 12"""
                # talk:22006210:"Ouuch!"
                assert t220006000_x32(text1=22006210, mode3=1)
                """State 2"""
                SetWorkValue(0, 2)
            elif GetWorkValue(0) > 0:
                """State 14"""
                # talk:22006200:"Ah!"
                assert t220006000_x32(text1=22006200, mode3=1)
                """State 3"""
                SetWorkValue(0, 1)
        else:
            """State 6"""
            if GetWorkValue(0) > 4:
                """State 19"""
                # talk:22013500:"Argh!"
                assert t220006000_x31(text2=22013500, z5=1039442704, mode4=1)
            elif GetWorkValue(0) > 3:
                """State 15"""
                # talk:22013400:"Argh! No!"
                assert t220006000_x32(text1=22013400, mode3=1)
                """State 10"""
                SetWorkValue(0, 4)
            elif GetWorkValue(0) > 2:
                """State 16"""
                # talk:22013300:"I'll break! I'll break before I'm out!"
                assert t220006000_x32(text1=22013300, mode3=1)
                """State 9"""
                SetWorkValue(0, 3)
            elif GetWorkValue(0) > 1:
                """State 17"""
                # talk:22013200:"My lower half is stuck on something down there!"
                assert t220006000_x32(text1=22013200, mode3=1)
                """State 8"""
                SetWorkValue(0, 2)
            elif GetWorkValue(0) > 0:
                """State 20"""
                # talk:22013100:"Argh! Cease! Please!"
                assert t220006000_x32(text1=22013100, mode3=1)
                """State 7"""
                SetWorkValue(0, 1)
    else:
        """State 18"""
        # talk:22001200:"G-good gosh, stop, please! That's my face!"
        assert t220006000_x32(text1=22001200, mode3=1)
    """State 21"""
    return 0

def t220006000_x71():
    """State 0,6"""
    if RelativeAngleBetweenTwoPlayers_SpecifyAxis(180) < 110:
        """State 2"""
        if GetSelfHP() < 90 and GetWorkValue(1) > 1:
            """State 5"""
            RequestAnimation(20034, -1)
            """State 1"""
            SetEventFlag(1043399312, 1)
            """State 12"""
            c1_121(9743)
            """State 13"""
            # talk:22007100:"Nnngh!"
            assert t220006000_x31(text2=22007100, z5=1039449214, mode4=1)
            """State 10"""
            SetEventFlag(1043392715, 0)
            SetEventFlag(1043392711, 0)
            """State 8"""
            if not GetEventFlag(60828):
                """State 7"""
                # gesture:71:Triumphant Delight
                AcquireGesture(71)
                SetEventFlag(60828, 1)
            else:
                """State 9"""
                pass
        elif GetWorkValue(1) > 2:
            """State 11"""
            pass
        elif GetWorkValue(1) > 1:
            """State 15"""
            # talk:22007010:"Nngh!"
            assert t220006000_x32(text1=22007010, mode3=1)
            """State 3"""
            SetWorkValue(1, 2)
        elif GetWorkValue(1) > 0:
            """State 14"""
            # talk:22007000:"Ngh!"
            assert t220006000_x32(text1=22007000, mode3=1)
            """State 4"""
            SetWorkValue(1, 1)
    else:
        """State 16"""
        # talk:22001200:"G-good gosh, stop, please! That's my face!"
        assert t220006000_x32(text1=22001200, mode3=1)
    """State 17"""
    return 0

