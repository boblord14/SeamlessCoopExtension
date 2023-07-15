# -*- coding: utf-8 -*-
def t348006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t348006000_x6(flag1=4183, flag2=4181, flag3=4182, val1=15, val2=10, val3=12, val4=35, val5=35, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    def WhilePaused():
        c5_121(GetEventFlag(4185) == 1 and not GetEventFlag(1050382715) and not GetEventFlag(1050389255),
               9620)
    Quit()

def t348006000_1000():
    """State 0,2,3"""
    assert t348006000_x36()
    """State 1"""
    c1_120(1000)
    Quit()

def t348006000_1001():
    """State 0,2,3"""
    assert t348006000_x37()
    """State 1"""
    c1_120(1001)
    Quit()

def t348006000_1101():
    """State 0,2,3"""
    assert t348006000_x38()
    """State 1"""
    c1_120(1101)
    Quit()

def t348006000_1102():
    """State 0,2,3"""
    t348006000_x39()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t348006000_1103():
    """State 0,2,3"""
    assert t348006000_x40()
    """State 1"""
    c1_120(1103)
    Quit()

def t348006000_2000():
    """State 0,2,3"""
    assert t348006000_x41()
    """State 1"""
    c1_120(2000)
    Quit()

def t348006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t348006000_x1():
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

def t348006000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t348006000_x3(lot1=103200):
    """State 0,1"""
    # lot:103200:Prosthesis-Wearer Heirloom
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t348006000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t348006000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t348006000_x1()
    else:
        """State 4,7"""
        call = t348006000_x33()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t348006000_x1()
    """State 9"""
    return 0

def t348006000_x5():
    """State 0,1"""
    assert t348006000_x1()
    """State 2"""
    return 0

def t348006000_x6(flag1=4183, flag2=4181, flag3=4182, val1=15, val2=10, val3=12, val4=35, val5=35, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t348006000_x23(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t348006000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t348006000_x7(val1=15, val2=10, val3=12, val4=35, val5=35, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t348006000_x10(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t348006000_x14(val1=val1, z1=z1)
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
            call = t348006000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t348006000_x27() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t348006000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t348006000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t348006000_x18(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t348006000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t348006000_x9(flag1=4183, val2=10, val3=12):
    """State 0,8"""
    assert t348006000_x35()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t348006000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t348006000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t348006000_x10(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t348006000_x11(z5=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t348006000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t348006000_x11(z5=_, val6=_):
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

def t348006000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t348006000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t348006000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t348006000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t348006000_x13():
    """State 0,1"""
    assert t348006000_x11(z5=1101, val6=1101)
    """State 2"""
    return 0

def t348006000_x14(val1=15, z1=1):
    """State 0,2"""
    assert t348006000_x24()
    """State 1"""
    call = t348006000_x15()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t348006000_x26()
    """State 4"""
    return 0

def t348006000_x15():
    """State 0,1"""
    assert t348006000_x11(z5=1000, val6=1000)
    """State 2"""
    return 0

def t348006000_x16(val5=35):
    """State 0,1"""
    call = t348006000_x17()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t348006000_x27()
    """State 3"""
    return 0

def t348006000_x17():
    """State 0,1"""
    assert t348006000_x11(z5=1100, val6=1100)
    """State 2"""
    return 0

def t348006000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t348006000_x35()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t348006000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t348006000_x29()
    """Unused"""
    """State 6"""
    return 0

def t348006000_x19():
    """State 0,2"""
    call = t348006000_x11(z5=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t348006000_x20():
    """State 0,1"""
    assert t348006000_x11(z5=1001, val6=1001)
    """State 2"""
    return 0

def t348006000_x21():
    """State 0,1"""
    assert t348006000_x11(z5=1103, val6=1103)
    """State 2"""
    return 0

def t348006000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t348006000_x23(flag1=4183, flag2=4181, flag3=4182, val1=15, val2=10, val3=12, val4=35, val5=35, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t348006000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t348006000_x9(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t348006000_x8(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t348006000_x34() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t348006000_x24():
    """State 0,1"""
    assert t348006000_x25()
    """State 2"""
    return 0

def t348006000_x25():
    """State 0,1"""
    assert t348006000_x11(z5=1104, val6=1104)
    """State 2"""
    return 0

def t348006000_x26():
    """State 0,1"""
    call = t348006000_x11(z5=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t348006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t348006000_x27():
    """State 0,1"""
    call = t348006000_x11(z5=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t348006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t348006000_x28():
    """State 0,1"""
    call = t348006000_x11(z5=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t348006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t348006000_x29():
    """State 0,1"""
    call = t348006000_x11(z5=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t348006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t348006000_x30(text2=_, mode4=1):
    """State 0,4"""
    assert t348006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t348006000_x31(text1=_, mode3=1):
    """State 0,4"""
    assert t348006000_x32() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t348006000_x32():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t348006000_x33():
    """State 0,1"""
    assert t348006000_x11(z5=1002, val6=1002)
    """State 2"""
    return 0

def t348006000_x34():
    """State 0,1"""
    assert t348006000_x1()
    """State 2"""
    return 0

def t348006000_x35():
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

def t348006000_x36():
    """State 0,1"""
    if GetEventFlag(4185) == 1:
        """State 3"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t348006000_x43()
    elif GetEventFlag(4186) == 1:
        """State 4"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t348006000_x44()
    elif GetEventFlag(4187) == 1:
        """State 5"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t348006000_x46()
    elif GetEventFlag(4188) == 1:
        """State 6"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t348006000_x47()
    elif GetEventFlag(4189) == 1:
        """State 9"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t348006000_x54()
    elif GetEventFlag(4190) == 1:
        """State 7"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t348006000_x56()
    elif GetEventFlag(4191) == 1:
        """State 8"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t348006000_x58()
    else:
        """State 2"""
        pass
    """State 10"""
    return 0

def t348006000_x37():
    """State 0,1"""
    if not GetEventFlag(4185):
        """State 2"""
        # talk:34880300:"I will not forget what you did for me."
        assert t348006000_x31(text1=34880300, mode3=1)
    else:
        pass
    """State 3"""
    return 0

def t348006000_x38():
    """State 0,5"""
    if not GetEventFlag(4185):
        """State 1"""
        if not GetEventFlag(1050382711):
            """State 3"""
            SetEventFlag(1050382711, 1)
            """State 6"""
            # talk:34880000:"Ugh."
            assert t348006000_x31(text1=34880000, mode3=1)
        elif not GetEventFlag(1050382712):
            """State 4"""
            SetEventFlag(1050382712, 1)
            """State 7"""
            # talk:34880100:"Is there something wrong?"
            assert t348006000_x31(text1=34880100, mode3=1)
        else:
            """State 2"""
            pass
    else:
        pass
    """State 8"""
    return 0

def t348006000_x39():
    """State 0,5"""
    if not GetEventFlag(4185):
        """State 2"""
        if not GetEventFlag(1050389253):
            """State 3"""
            SetEventFlag(1050389253, 1)
            """State 6"""
            # talk:34880200:"Why are you doing this?"
            assert t348006000_x31(text1=34880200, mode3=1)
        else:
            """State 4"""
            pass
    else:
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 7"""
    return 0

def t348006000_x40():
    """State 0,1"""
    if not GetEventFlag(4185):
        """State 2"""
        # talk:34880400:"I did not imagine it ending like this."
        assert t348006000_x31(text1=34880400, mode3=1)
    else:
        pass
    """State 3"""
    return 0

def t348006000_x41():
    """State 0"""
    while True:
        """State 1"""
        if not GetEventFlag(4185):
            """State 2"""
            # actionbutton:6000:"Talk"
            call = t348006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                                 flag12=6000, flag4=6000)
            if call.Done():
                break
            elif GetEventFlag(4185) == 1:
                pass
        else:
            """State 3"""
            assert t348006000_x48()
            break
    """State 4"""
    return 0

def t348006000_x42():
    """State 0,1"""
    if not GetEventFlag(1050389256):
        """State 4"""
        # talk:34800200:"Ngh... W-who's there?"
        assert t348006000_x30(text2=34800200, mode4=1)
        """State 2"""
        SetEventFlag(1050389256, 1)
    else:
        """State 5"""
        # talk:34800300:"If you are wise, you will leave, immediately."
        assert t348006000_x30(text2=34800300, mode4=1)
    """State 3"""
    SetEventFlag(1050382715, 1)
    """State 6"""
    return 0

def t348006000_x43():
    """State 0,1"""
    if not GetEventFlag(1050382718):
        """State 2"""
        assert t348006000_x42()
        """State 3"""
        def ExitPause():
            SetEventFlagIf(GetEventFlag(1050389255) == 1, 1050382718, 1)
            RequestAnimationIf(GetEventFlag(1050389255) == 1, 90201, -1)
        assert t348006000_x60()
    else:
        """State 4"""
        assert t348006000_x61()
    """State 5"""
    return 0

def t348006000_x44():
    """State 0,1"""
    assert t348006000_x45()
    """State 2"""
    return 0

def t348006000_x45():
    """State 0,1"""
    if not GetEventFlag(1050389257):
        """State 4"""
        # talk:34802000:"I...hoped to see you again."
        assert t348006000_x30(text2=34802000, mode4=1)
        """State 2"""
        SetEventFlag(1050389257, 1)
        """State 7"""
        # lot:103200:Prosthesis-Wearer Heirloom
        assert t348006000_x3(lot1=103200)
    elif not GetEventFlag(1050389258):
        """State 5"""
        # talk:34802100:"I'm considering leaving. On a journey."
        assert t348006000_x30(text2=34802100, mode4=1)
        """State 3"""
        SetEventFlag(1050389258, 1)
    else:
        """State 6"""
        # talk:34802200:"I'm considering leaving. On a journey."
        assert t348006000_x30(text2=34802200, mode4=1)
    """State 8"""
    return 0

def t348006000_x46():
    """State 0,1"""
    if GetEventFlag(1050389265) == 1:
        """State 2"""
        assert t348006000_x49()
    elif GetEventFlag(1038519255) == 1 and not GetEventFlag(1038519257):
        """State 3"""
        assert t348006000_x50()
    else:
        """State 4"""
        assert t348006000_x51()
    """State 5"""
    return 0

def t348006000_x47():
    """State 0,1"""
    assert t348006000_x53()
    """State 2"""
    return 0

def t348006000_x48():
    """State 0"""
    while True:
        """State 4"""
        # actionbutton:6000:"Talk"
        call = t348006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                             flag4=6000)
        if call.Done():
            break
        elif (not GetEventFlag(1050382715) and not GetEventFlag(1050389255) and GetEventFlag(1050382713)
              == 1 and GetDistanceToPlayer() < 30):
            """State 5"""
            # talk:34800100:"Ah...ahh..."
            call = t348006000_x31(text1=34800100, mode3=1)
            if call.Done():
                """State 6"""
                # actionbutton:6000:"Talk"
                call = t348006000_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                                     flag12=6000, flag4=6000)
                if call.Done():
                    break
                elif CheckSpecificPersonTalkHasEnded(0) == 1 and GetCurrentStateElapsedTime() > 20:
                    pass
            elif GetEventFlag(1050382715) == 1:
                """State 1"""
                pass
        elif GetDistanceToPlayer() > 15 and GetEventFlag(1050382719) == 1:
            """State 2"""
            RequestAnimation(90301, -1)
            """State 3"""
            SetEventFlag(1050382719, 0)
    """State 7"""
    return 0

def t348006000_x49():
    """State 0,2"""
    if not GetEventFlag(1050389266):
        """State 4"""
        # talk:34802500:"Oh, hello again."
        assert t348006000_x30(text2=34802500, mode4=1)
        """State 1"""
        SetEventFlag(1050389266, 1)
        """State 3"""
        SetEventFlag(1042559206, 1)
        SetEventFlag(1042559207, 0)
        SetEventFlag(1042559208, 0)
        SetEventFlag(1042559209, 0)
    else:
        """State 5"""
        # talk:34802600:"Well, never mind that."
        assert t348006000_x30(text2=34802600, mode4=1)
    """State 6"""
    return 0

def t348006000_x50():
    """State 0,1"""
    if not GetEventFlag(1038519256):
        """State 4"""
        # talk:34803000:"Ah. We meet again."
        assert t348006000_x30(text2=34803000, mode4=1)
        """State 2"""
        SetEventFlag(1038519256, -1)
    elif not GetEventFlag(1038519258):
        """State 5"""
        # talk:34803100:"Now, I'm tracing the path Malenia took,"
        assert t348006000_x30(text2=34803100, mode4=1)
        """State 3"""
        SetEventFlag(1038519258, -1)
    else:
        """State 7"""
        # talk:34803500:"Now, I'm tracing the path Malenia took."
        assert t348006000_x30(text2=34803500, mode4=1)
    """State 6"""
    assert t348006000_x52()
    """State 8"""
    return 0

def t348006000_x51():
    """State 0,1"""
    # talk:34803300:"If the arm serves well enough,"
    assert t348006000_x30(text2=34803300, mode4=1)
    """State 2"""
    return 0

def t348006000_x52():
    """State 0,7"""
    # goods:8977:Valkyrie's Prosthesis
    if ComparePlayerInventoryNumber(3, 8977, 4, 1, 0) == 1:
        """State 1"""
        c1_110()
        ClearTalkListData()
        """State 2"""
        # action:23481002:"Give the Valkyrie's Prosthesis"
        AddTalkListData(1, 23481002, -1)
        # action:23481001:"Don't give it"
        AddTalkListData(2, 23481001, -1)
        """State 3"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 10"""
            # talk:34803200:"Are you..."
            assert t348006000_x30(text2=34803200, mode4=1)
            """State 6"""
            SetEventFlag(1038519257, 1)
            """State 9"""
            SetEventFlag(1042559206, 0)
            SetEventFlag(1042559207, 1)
            SetEventFlag(1042559208, 1)
            SetEventFlag(1042559209, 1)
            """State 8"""
            # goods:8977:Valkyrie's Prosthesis
            PlayerEquipmentQuantityChange(3, 8977, -1)
        else:
            """State 5"""
            pass
    else:
        pass
    """State 11"""
    return 0

def t348006000_x53():
    """State 0,1"""
    if not GetEventFlag(1042559205) and GetEventFlag(1042559204) == 1:
        """State 3"""
        # talk:34804000:"Ah, we meet yet again."
        assert t348006000_x30(text2=34804000, mode4=1)
        """State 2"""
        Label('L0')
        SetEventFlag(1042559205, 1)
    elif not GetEventFlag(1042559205) and not GetEventFlag(1042559204):
        """State 4"""
        # talk:34804100:"Ah, we meet yet again."
        assert t348006000_x30(text2=34804100, mode4=1)
        Goto('L0')
    else:
        """State 5"""
        # talk:34804200:"I would have you call upon me in battle, should you ever have the need."
        assert t348006000_x30(text2=34804200, mode4=1)
    """State 6"""
    return 0

def t348006000_x54():
    """State 0,1"""
    assert t348006000_x55()
    """State 2"""
    return 0

def t348006000_x55():
    """State 0,1"""
    if not GetEventFlag(1051569255):
        """State 4"""
        # talk:34805000:"To think we'd meet in such a place..."
        assert t348006000_x30(text2=34805000, mode4=1)
        """State 2"""
        SetEventFlag(1051569255, 1)
    elif not GetEventFlag(1051569256):
        """State 5"""
        # talk:34805100:"I'm searching for a fort to the north of the ruins."
        assert t348006000_x30(text2=34805100, mode4=1)
        """State 3"""
        SetEventFlag(1051569256, 1)
    else:
        """State 6"""
        # talk:34805200:"I'm searching for a fort to the north of the ruins."
        assert t348006000_x30(text2=34805200, mode4=1)
    """State 7"""
    return 0

def t348006000_x56():
    """State 0,1"""
    assert t348006000_x57()
    """State 2"""
    return 0

def t348006000_x57():
    """State 0,1"""
    if not GetEventFlag(15009205):
        """State 4"""
        # talk:34806000:"Again we meet."
        assert t348006000_x30(text2=34806000, mode4=1)
        """State 2"""
        SetEventFlag(15009205, 1)
    elif not GetEventFlag(15009206):
        """State 5"""
        # talk:34806100:"There is something I must return to Malenia."
        assert t348006000_x30(text2=34806100, mode4=1)
        """State 3"""
        SetEventFlag(15009206, 1)
    else:
        """State 6"""
        # talk:34806200:"There is something I must return to Malenia."
        assert t348006000_x30(text2=34806200, mode4=1)
    """State 7"""
    return 0

def t348006000_x58():
    """State 0,1"""
    assert t348006000_x59()
    """State 2"""
    return 0

def t348006000_x59():
    """State 0,1"""
    if not GetEventFlag(15009207):
        """State 5"""
        # talk:34807000:"Oh, hello."
        assert t348006000_x30(text2=34807000, mode4=1)
        """State 2"""
        SetEventFlag(15009207, 1)
    elif not GetEventFlag(15009210):
        """State 6"""
        # talk:34807100:"But this is where things end."
        assert t348006000_x30(text2=34807100, mode4=1)
        """State 3"""
        SetEventFlag(15009210, 1)
    else:
        """State 7"""
        # talk:34807200:"Please, let me pass alone."
        assert t348006000_x30(text2=34807200, mode4=1)
        """State 4"""
        SetEventFlag(15009211, 1)
    """State 8"""
    return 0

def t348006000_x60():
    """State 0,8"""
    # goods:8976:Unalloyed Gold Needle
    if ComparePlayerInventoryNumber(3, 8976, 4, 1, 0) == 1:
        """State 1"""
        c1_110()
        ClearTalkListData()
        """State 2"""
        # action:23481000:"Give an Unalloyed Gold Needle"
        AddTalkListData(1, 23481000, -1)
        # action:23481001:"Don't give it"
        AddTalkListData(2, 23481001, -1)
        """State 3"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 12"""
            SetEventFlag(1050382719, 1)
            """State 14"""
            # talk:34801000:"You ask that I stab myself with the needle..."
            assert t348006000_x30(text2=34801000, mode4=1)
            """State 13"""
            SetEventFlag(1050382719, 0)
            """State 7"""
            SetEventFlag(1050382716, 1)
            """State 6"""
            SetEventFlag(1050389255, 1)
            """State 11"""
            SetEventFlag(1050389259, 0)
            """State 9"""
            # goods:8976:Unalloyed Gold Needle
            PlayerEquipmentQuantityChange(3, 8976, -1)
            assert GetEventFlag(1050382717) == 1
            """State 10"""
            assert GetCurrentStateElapsedTime() > 0.8
            """State 15"""
            # talk:34801115:"Well. That was easier than expected."
            assert t348006000_x30(text2=34801115, mode4=1)
        else:
            """State 5"""
            pass
    else:
        pass
    """State 16"""
    return 0

def t348006000_x61():
    """State 0,1"""
    # talk:34801200:"..."
    assert t348006000_x30(text2=34801200, mode4=1)
    """State 2"""
    return 0

