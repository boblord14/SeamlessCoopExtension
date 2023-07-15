# -*- coding: utf-8 -*-
def t202006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t202006000_x22(flag1=3643, flag2=3641, flag3=3642, val1=12, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1)
    Quit()

def t202006000_1000():
    """State 0,2,3"""
    assert t202006000_x0()
    """State 1"""
    c1_120(1000)
    Quit()

def t202006000_1001():
    """State 0,2,3"""
    assert t202006000_x1()
    """State 1"""
    c1_120(1001)
    Quit()

def t202006000_1103():
    """State 0,2,3"""
    assert t202006000_x2()
    """State 1"""
    c1_120(1103)
    Quit()

def t202006000_2000():
    """State 0,2,3"""
    assert t202006000_x3(z8=10, z9=12)
    """State 1"""
    c1_120(2000)
    Quit()

def t202006000_x0():
    """State 0,1"""
    if True:
        """State 3"""
        assert t202006000_x4(z5=3, z6=6, z7=9)
    else:
        """State 2"""
        pass
    """State 4"""
    return 0

def t202006000_x1():
    """State 0,1"""
    # talk:20281000:"I must consume more..."
    assert t202006000_x48(text1=20281000, mode4=1)
    """State 2"""
    return 0

def t202006000_x2():
    """State 0,1"""
    # talk:20281100:"Marika...why..."
    assert t202006000_x48(text1=20281100, mode4=1)
    """State 2"""
    return 0

def t202006000_x3(z8=10, z9=12):
    """State 0,1,5"""
    assert t202006000_x5(val6=10, z10=12)
    """State 3"""
    Label('L0')
    SetEventFlag(1051439205, 1)
    """State 6"""
    return 0
    """Unused"""
    """State 2,4"""
    # actionbutton:6220:"Talk"
    assert (t202006000_x16(actionbutton1=6220, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
            flag4=6000))
    Goto('L0')

def t202006000_x4(z5=3, z6=6, z7=9):
    """State 0,1"""
    if GetEventFlag(1051439206) == 1:
        """State 3"""
        assert t202006000_x9(z5=z5, z6=z6, z7=z7)
    else:
        """State 2"""
        assert t202006000_x8(z5=z5, z6=z6, z7=z7)
    """State 4"""
    return 0

def t202006000_x5(val6=10, z10=12):
    """State 0"""
    while True:
        """State 3"""
        call = t202006000_x6(z13=3, z14=6, z15=9)
        if call.Done():
            break
        elif GetEventFlag(1051432703) == 1 and not GetEventFlag(1051432702) and GetDistanceToPlayer() < val6:
            """State 1"""
            Label('L0')
            """State 2"""
            # talk:20202000:"<pained howl>"
            assert t202006000_x47(text2=20202000, z11=1051432702, mode5=1)
        elif GetEventFlag(3646) == 1 and GetEventFlag(3640) == 1 and not GetEventFlag(1051439211):
            """State 4"""
            # talk:20205100:"<pained howl>"
            assert t202006000_x47(text2=20205100, z11=1051439211, mode5=1)
            """State 5"""
            call = t202006000_x6(z13=3, z14=6, z15=9)
            def WhilePaused():
                c5_121(not CheckSpecificPersonTalkHasEnded(0), 9626)
            if call.Done():
                break
            elif (GetEventFlag(1051432703) == 1 and not GetEventFlag(1051432702) and GetDistanceToPlayer()
                  < val6):
                Goto('L0')
    """State 6"""
    return 0

def t202006000_x6(z13=3, z14=6, z15=9):
    """State 0,4"""
    SetEventFlag(1051439206, 0)
    SetEventFlag(1051439207, 0)
    """State 1"""
    if GetEventFlagValue(1051439235, 5) > 9:
        """State 3"""
        Quit()
    elif GetEventFlag(3646) == 1:
        """State 6,10"""
        Label('L0')
        # actionbutton:6222:"Talk"
        assert (t202006000_x16(actionbutton1=6222, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=6000))
    elif GetEventFlag(1051432703) == 1 and not GetEventFlag(1051432704):
        """State 8"""
        Goto('L0')
    else:
        """State 7,11"""
        call = t202006000_x11()
        if call.Get() == 1:
            Goto('L0')
        elif call.Done():
            """State 2,9"""
            # actionbutton:6220:"Talk", actionbutton:6221:"Hand over Deathroot"
            call = t202006000_x7(actionbutton2=6220, actionbutton3=6221, z16=6223)
            if call.Get() == 1:
                """State 5"""
                SetEventFlag(1051439206, 1)
            elif call.Done():
                pass
    """State 12"""
    return 0

def t202006000_x7(actionbutton2=6220, actionbutton3=6221, z16=6223):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 5"""
        # goods:2090:Deathroot
        if ComparePlayerInventoryNumber(3, 2090, 4, 1, 0) == 1:
            """State 2"""
            if (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
                IsCharacterDisabled())):
                continue
            # goods:2090:Deathroot
            elif ComparePlayerInventoryNumber(3, 2090, 3, 0, 0) == 1:
                continue
            # actionbutton:6220:"Talk"
            elif CheckActionButtonArea(actionbutton2):
                pass
            # actionbutton:6221:"Hand over Deathroot"
            elif CheckActionButtonArea(actionbutton3):
                break
        else:
            """State 6"""
            if (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
                IsCharacterDisabled())):
                continue
            # goods:2090:Deathroot
            elif ComparePlayerInventoryNumber(3, 2090, 4, 1, 0) == 1:
                continue
            # actionbutton:6220:"Talk"
            elif CheckActionButtonArea(actionbutton2):
                pass
        """State 3,7"""
        return 0
    """State 4,8"""
    return 1

def t202006000_x8(z5=3, z6=6, z7=9):
    """State 0,2"""
    if GetEventFlag(3646) == 1:
        """State 7"""
        # talk:20205150:"..."
        def WhilePaused():
            RequestAnimation(20030, -1)
        assert t202006000_x46(text3=20205150, mode7=1)
    else:
        """State 5"""
        if GetEventFlag(1051432703) == 1 and not GetEventFlag(1051432704):
            """State 11"""
            # talk:20202050:"<pained howl>"
            def WhilePaused():
                RequestAnimation(20030, -1)
            assert (t202006000_x47(text2=20202050, z11=1051432704, mode5=1) and CheckSpecificPersonTalkHasEnded(0)
                    == 1)
        else:
            """State 3,9"""
            call = t202006000_x11()
            if call.Get() == 1:
                """State 4,10"""
                assert t202006000_x12(mode3=1)
            elif call.Done():
                """State 6"""
                if GetEventFlag(1051432705) == 1:
                    """State 12"""
                    def WhilePaused():
                        RequestAnimation(20030, -1)
                    assert t202006000_x14()
                else:
                    """State 1,8"""
                    # talk:20200100:"..."
                    def WhilePaused():
                        RequestAnimation(20030, -1)
                    assert t202006000_x46(text3=20200100, mode7=1)
    """State 13"""
    return 0

def t202006000_x9(z5=3, z6=6, z7=9):
    """State 0,3"""
    ClearQuantityValueOfChooseQuantityDialog()
    """State 1"""
    OpenChooseQuantityDialog(2090, 22021003)
    assert not (CheckSpecificPersonMenuIsOpen(13, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    if GetValueFromNumberSelectDialog() >= 0:
        """State 4"""
        # goods:2090:Deathroot
        PlayerEquipmentQuantityChange(3, 2090, -1 * GetValueFromNumberSelectDialog())
        """State 5"""
        SetEventFlagValue(1051439230, 5, GetValueFromNumberSelectDialog() + GetEventFlagValue(1051439230, 5))
        """State 6"""
        assert t202006000_x12(mode3=0)
    else:
        pass
    """State 7"""
    return 0

def t202006000_x10(mode3=_):
    """State 0,5"""
    if GetEventFlag(3647) == 1:
        """State 7"""
        if GetEventFlagValue(1051439230, 5) > 9:
            """State 2"""
            SetEventFlagValue(1051439235, 5, 9)
            """State 11"""
            call = t202006000_x15(mode3=mode3)
            def WhilePaused():
                c1_121(9625)
                RequestAnimation(20030, -1)
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 15:
                """State 12"""
                assert t202006000_x17()
        else:
            """State 4"""
            SetEventFlagValue(1051439235, 5, GetEventFlagValue(1051439230, 5))
            """State 10"""
            assert t202006000_x19(lot1=102319 - GetEventFlagValue(1051439230, 5))
    else:
        """State 6"""
        if GetEventFlagValue(1051439230, 5) > 5:
            """State 3"""
            SetEventFlagValue(1051439235, 5, 4)
            """State 9"""
            # lot:102300:Ash of War: Beast's Roar
            assert t202006000_x19(lot1=102300)
        else:
            """State 1"""
            SetEventFlagValue(1051439235, 5, GetEventFlagValue(1051439230, 5))
            """State 8"""
            assert t202006000_x19(lot1=102304 - GetEventFlagValue(1051439230, 5))
    """State 13"""
    return 0

def t202006000_x11():
    """State 0,3"""
    if GetEventFlag(3647) == 1:
        """State 1"""
        if GetEventFlagValue(1051439235, 5) > GetEventFlagValue(1051439230, 5):
            pass
        else:
            """State 7"""
            Label('L0')
            return 1
    else:
        """State 2"""
        if GetEventFlagValue(1051439230, 5) > 4:
            """State 5"""
            if GetEventFlagValue(1051439235, 5) > 4:
                pass
            else:
                Goto('L0')
        else:
            """State 4"""
            if GetEventFlagValue(1051439235, 5) > GetEventFlagValue(1051439230, 5):
                pass
            else:
                Goto('L0')
    """State 6"""
    return 0

def t202006000_x12(mode3=_):
    """State 0,2"""
    def WhilePaused():
        RequestAnimation(20030, -1)
    assert t202006000_x13(val7=4, mode6=1, val8=6, mode3=mode3)
    """State 1"""
    SetEventFlag(1051432705, 1)
    """State 3"""
    assert t202006000_x10(mode3=mode3)
    """State 4"""
    return 0

def t202006000_x13(val7=4, mode6=1, val8=6, mode3=_):
    """State 0,1"""
    if GetEventFlag(3647) == 1:
        """State 2"""
        if GetEventFlagValue(1051439230, 5) > 9:
            """State 3"""
            if mode3 == 1:
                """State 24"""
                # talk:20201100:"Tarnished...my thanks...for thy long...labour."
                assert t202006000_x46(text3=20201100, mode7=1)
            else:
                """State 13"""
                # talk:20201000:"<chewing>"
                assert t202006000_x46(text3=20201000, mode7=1)
        elif GetEventFlagValue(1051439230, 5) > val8 and not GetEventFlagValue(1051439235, 5) > val8:
            """State 7"""
            if mode3 == 1:
                """State 23"""
                # talk:20200700:"I shall grant thee...my claws..."
                assert t202006000_x46(text3=20200700, mode7=1)
            else:
                """State 15"""
                # talk:20200400:"..."
                assert t202006000_x46(text3=20200400, mode7=1)
            """State 11"""
            SetEventFlag(1051432707, 1)
        else:
            """State 9"""
            if mode3 == 1:
                """State 22"""
                # talk:20205301:"I won't forget...again..."
                assert t202006000_x46(text3=20205301, mode7=1)
            else:
                """State 18"""
                # talk:20205300:"<chewing>"
                assert t202006000_x46(text3=20205300, mode7=1)
    else:
        """State 4"""
        if GetEventFlagValue(1051439230, 5) > val7 and not GetEventFlagValue(1051439235, 5) > val7:
            """State 5"""
            if mode3 == 1:
                """State 21"""
                # talk:20205001:"Strange... There's something else..."
                assert t202006000_x46(text3=20205001, mode7=1)
            else:
                """State 14"""
                # talk:20205000:"..."
                assert t202006000_x46(text3=20205000, mode7=1)
        elif GetEventFlagValue(1051439230, 5) > mode6 and not GetEventFlagValue(1051439235, 5) > mode6:
            """State 6"""
            if mode3 == 1:
                """State 20"""
                # talk:20200500:"I shall grant thee... eye...and claw."
                assert t202006000_x46(text3=20200500, mode7=1)
            else:
                """State 16"""
                # talk:20200200:"..."
                assert t202006000_x46(text3=20200200, mode7=1)
            """State 12"""
            RequestAnimation(20020, -1)
            assert GetCurrentStateElapsedFrames() > 1
            """State 10"""
            SetEventFlag(1051432706, 1)
        else:
            """State 8"""
            if mode3 == 1:
                """State 19"""
                # talk:20200600:"More... I am not...sated."
                assert t202006000_x46(text3=20200600, mode7=1)
            else:
                """State 17"""
                # talk:20200300:"..."
                assert t202006000_x46(text3=20200300, mode7=1)
    """State 25"""
    return 0

def t202006000_x14():
    """State 0,1"""
    if GetEventFlag(1051432707) == 1:
        """State 4"""
        # talk:20200700:"I shall grant thee...my claws..."
        assert t202006000_x46(text3=20200700, mode7=1)
    elif GetEventFlag(1051432706) == 1:
        """State 3"""
        # talk:20200550:"I shall grant thee... eye...and claw."
        assert t202006000_x46(text3=20200550, mode7=1)
    else:
        """State 2"""
        # talk:20200600:"More... I am not...sated."
        assert t202006000_x46(text3=20200600, mode7=1)
    """State 5"""
    return 0

def t202006000_x15(mode3=_):
    """State 0,2"""
    # lot:102310:Ancient Dragon Smithing Stone
    call = t202006000_x19(lot1=102310)
    if call.Done():
        pass
    elif GetDistanceToPlayer() > 12:
        """State 5"""
        assert t202006000_x17()
    """State 1"""
    SetEventFlag(1051432709, 1)
    if mode3 == 1:
        """State 4"""
        # talk:20201150:"<plaintive howl>"
        assert t202006000_x48(text1=20201150, mode4=1) and CheckSpecificPersonTalkHasEnded(0) == 1
    else:
        """State 3"""
        # talk:20201050:"<plaintive howl>"
        assert t202006000_x48(text1=20201050, mode4=1) and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 6"""
    return 0

def t202006000_x16(actionbutton1=_, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag4=6000):
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

def t202006000_x17():
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

def t202006000_x18():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t202006000_x19(lot1=_):
    """State 0,1"""
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t202006000_x20(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t202006000_x36()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t202006000_x17()
    else:
        """State 4,7"""
        call = t202006000_x50()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t202006000_x17()
    """State 9"""
    return 0

def t202006000_x21():
    """State 0,1"""
    assert t202006000_x17()
    """State 2"""
    return 0

def t202006000_x22(flag1=3643, flag2=3641, flag3=3642, val1=12, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t202006000_x39(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t202006000_x38()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t202006000_x23(val1=12, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                   flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                   mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t202006000_x26(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t202006000_x30(val1=val1, z1=z1)
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
            call = t202006000_x32(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t202006000_x43() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t202006000_x28(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t202006000_x24(val2=10, val3=12):
    """State 0,1"""
    call = t202006000_x34(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t202006000_x20(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t202006000_x25(flag1=3643, val2=10, val3=12):
    """State 0,8"""
    assert t202006000_x52()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t202006000_x37()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t202006000_x17()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t202006000_x26(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t202006000_x27(z12=2000, val9=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t202006000_x16(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t202006000_x27(z12=_, val9=_):
    """State 0,1"""
    if f203(z12) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z12)
        assert f202() == val9
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t202006000_x28(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t202006000_x17()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t202006000_x29()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t202006000_x44()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t202006000_x29():
    """State 0,1"""
    assert t202006000_x27(z12=1101, val9=1101)
    """State 2"""
    return 0

def t202006000_x30(val1=12, z1=1):
    """State 0,2"""
    assert t202006000_x40()
    """State 1"""
    call = t202006000_x31()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t202006000_x42()
    """State 4"""
    return 0

def t202006000_x31():
    """State 0,1"""
    assert t202006000_x27(z12=1000, val9=1000)
    """State 2"""
    return 0

def t202006000_x32(val5=12):
    """State 0,1"""
    call = t202006000_x33()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t202006000_x43()
    """State 3"""
    return 0

def t202006000_x33():
    """State 0,1"""
    assert t202006000_x27(z12=1100, val9=1100)
    """State 2"""
    return 0

def t202006000_x34(val2=10, val3=12):
    """State 0,5"""
    assert t202006000_x52()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t202006000_x35()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t202006000_x45()
    """Unused"""
    """State 6"""
    return 0

def t202006000_x35():
    """State 0,2"""
    call = t202006000_x27(z12=1102, val9=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t202006000_x36():
    """State 0,1"""
    assert t202006000_x27(z12=1001, val9=1001)
    """State 2"""
    return 0

def t202006000_x37():
    """State 0,1"""
    assert t202006000_x27(z12=1103, val9=1103)
    """State 2"""
    return 0

def t202006000_x38():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t202006000_x39(flag1=3643, flag2=3641, flag3=3642, val1=12, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t202006000_x23(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                              flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                              z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t202006000_x25(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t202006000_x24(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t202006000_x51() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t202006000_x40():
    """State 0,1"""
    assert t202006000_x41()
    """State 2"""
    return 0

def t202006000_x41():
    """State 0,1"""
    assert t202006000_x27(z12=1104, val9=1104)
    """State 2"""
    return 0

def t202006000_x42():
    """State 0,1"""
    call = t202006000_x27(z12=1201, val9=1201)
    if call.Get() == 1:
        """State 2"""
        assert t202006000_x21()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t202006000_x43():
    """State 0,1"""
    call = t202006000_x27(z12=1300, val9=1300)
    if call.Get() == 1:
        """State 2"""
        assert t202006000_x21()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t202006000_x44():
    """State 0,1"""
    call = t202006000_x27(z12=1301, val9=1301)
    if call.Get() == 1:
        """State 2"""
        assert t202006000_x21()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t202006000_x45():
    """State 0,1"""
    call = t202006000_x27(z12=1302, val9=1302)
    if call.Get() == 1:
        """State 2"""
        assert t202006000_x21()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t202006000_x46(text3=_, mode7=1):
    """State 0,4"""
    assert t202006000_x18() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text3, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode7:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t202006000_x47(text2=_, z11=_, mode5=1):
    """State 0,5"""
    assert t202006000_x49() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(z11, 1)
    """State 1"""
    TalkToPlayer(text2, -1, -1, 1)
    """State 4"""
    if not mode5:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t202006000_x48(text1=_, mode4=1):
    """State 0,4"""
    assert t202006000_x49() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text1, -1, -1, 1)
    """State 3"""
    if not mode4:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t202006000_x49():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t202006000_x50():
    """State 0,1"""
    assert t202006000_x27(z12=1002, val9=1002)
    """State 2"""
    return 0

def t202006000_x51():
    """State 0,1"""
    assert t202006000_x17()
    """State 2"""
    return 0

def t202006000_x52():
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

