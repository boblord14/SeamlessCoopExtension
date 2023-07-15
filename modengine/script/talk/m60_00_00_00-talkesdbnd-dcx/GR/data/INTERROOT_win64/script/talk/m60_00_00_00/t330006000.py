# -*- coding: utf-8 -*-
def t330006000_1():
    """State 0,1"""
    # actionbutton:6240:"Talk"
    t330006000_x5(flag6=3723, flag7=3721, flag8=3722, val9=12, val10=10, val11=12, val12=10, val13=12,
                  actionbutton1=6240, flag9=6000, flag10=6001, flag11=6000, flag12=6000, flag13=6000,
                  z4=1, z5=1000000, z6=1000000, z7=1000000, mode2=1, mode3=1)
    Quit()

def t330006000_1000():
    """State 0,2,3"""
    assert t330006000_x40()
    """State 1"""
    c1_120(1000)
    Quit()

def t330006000_1101():
    """State 0,2,3"""
    assert t330006000_x41(flag1=1037462710, flag2=1037462711, flag3=1037462712, flag4=1037462713, flag5=1037462714)
    """State 1"""
    c1_120(1101)
    Quit()

def t330006000_1103():
    """State 0,2,3"""
    assert t330006000_x42()
    """State 1"""
    c1_120(1103)
    Quit()

def t330006000_2000():
    """State 0,2,3"""
    assert t330006000_x43()
    """State 1"""
    c1_120(2000)
    Quit()

def t330006000_x0(actionbutton1=6240, flag10=6001, flag14=6000, flag15=6000, flag16=6000, flag17=6000,
                  flag9=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag10) == 1 or GetEventFlag(flag14) == 1 or GetEventFlag(flag15) == 1 or
                GetEventFlag(flag16) == 1 or GetEventFlag(flag17) == 1)
        """State 4"""
        assert not GetEventFlag(flag9)
        """State 2"""
        if GetEventFlag(flag9) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag10) and not GetEventFlag(flag14) and not GetEventFlag(flag15) and
              not GetEventFlag(flag16) and not GetEventFlag(flag17)):
            pass
        # actionbutton:6240:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t330006000_x1():
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

def t330006000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t330006000_x3(val10=10, val11=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val10 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t330006000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val11 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t330006000_x1()
    else:
        """State 4,7"""
        call = t330006000_x34()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val11 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t330006000_x1()
    """State 9"""
    return 0

def t330006000_x4():
    """State 0,1"""
    assert t330006000_x1()
    """State 2"""
    return 0

def t330006000_x5(flag6=3723, flag7=3721, flag8=3722, val9=12, val10=10, val11=12, val12=10, val13=12,
                  actionbutton1=6240, flag9=6000, flag10=6001, flag11=6000, flag12=6000, flag13=6000,
                  z4=1, z5=1000000, z6=1000000, z7=1000000, mode2=1, mode3=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t330006000_x22(flag6=flag6, flag7=flag7, flag8=flag8, val9=val9, val10=val10, val11=val11,
                              val12=val12, val13=val13, actionbutton1=actionbutton1, flag9=flag9, flag10=flag10,
                              flag11=flag11, flag12=flag12, flag13=flag13, z4=z4, z5=z5, z6=z6, z7=z7,
                              mode2=mode2, mode3=mode3)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t330006000_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t330006000_x6(val9=12, val10=10, val11=12, val12=10, val13=12, actionbutton1=6240, flag9=6000, flag10=6001,
                  flag11=6000, flag12=6000, flag13=6000, z4=1, z5=1000000, z6=1000000, z7=1000000, mode2=1,
                  mode3=1):
    """State 0"""
    while True:
        """State 2"""
        call = t330006000_x9(actionbutton1=actionbutton1, flag9=flag9, flag10=flag10, z5=z5, z6=z6, z7=z7)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t330006000_x13(val9=val9, z4=z4)
            def WhilePaused():
                c5_138(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
                GiveSpEffectToPlayer(9640)
                c5_139(1 == (mode2 == 1), -1, 0)
                c5_139(1 == (mode3 == 1), 0, -1)
            def ExitPause():
                c1_138(-1)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif IsAttackedBySomeone() == 1 and not DoesSelfHaveSpEffect(9626) and not DoesSelfHaveSpEffect(9627):
            pass
        elif GetEventFlag(flag13) == 1:
            Goto('L0')
        elif GetEventFlag(flag11) == 1 and not GetEventFlag(flag12) and GetDistanceToPlayer() < val12:
            """State 5"""
            call = t330006000_x15(val13=val13)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val13 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t330006000_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t330006000_x11(val10=val10, val11=val11)
    """Unused"""
    """State 7"""
    return 0

def t330006000_x7(val10=10, val11=12):
    """State 0,1"""
    call = t330006000_x17(val10=val10, val11=val11)
    assert IsPlayerDead() == 1
    """State 2"""
    t330006000_x3(val10=val10, val11=val11)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t330006000_x8(flag6=3723, val10=10, val11=12):
    """State 0,8"""
    assert t330006000_x39()
    """State 1"""
    if GetEventFlag(flag6) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val10:
            """State 4,6"""
            call = t330006000_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val11 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t330006000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t330006000_x9(actionbutton1=6240, flag9=6000, flag10=6001, z5=1000000, z6=1000000, z7=1000000):
    """State 0,1"""
    call = t330006000_x10(z10=2000, val16=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t330006000_x0(actionbutton1=actionbutton1, flag10=flag10, flag14=6000, flag15=6000, flag16=6000,
                flag17=6000, flag9=flag9))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t330006000_x10(z10=_, val16=_):
    """State 0,1"""
    if f203(z10) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z10)
        assert f202() == val16
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t330006000_x11(val10=10, val11=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t330006000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val10:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t330006000_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val11 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t330006000_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t330006000_x12():
    """State 0,1"""
    assert t330006000_x10(z10=1101, val16=1101)
    """State 2"""
    return 0

def t330006000_x13(val9=12, z4=1):
    """State 0,2"""
    assert t330006000_x23()
    """State 1"""
    call = t330006000_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val9 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t330006000_x25()
    """State 4"""
    return 0

def t330006000_x14():
    """State 0,1"""
    assert t330006000_x10(z10=1000, val16=1000)
    """State 2"""
    return 0

def t330006000_x15(val13=12):
    """State 0,1"""
    call = t330006000_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val13 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t330006000_x26()
    """State 3"""
    return 0

def t330006000_x16():
    """State 0,1"""
    assert t330006000_x10(z10=1100, val16=1100)
    """State 2"""
    return 0

def t330006000_x17(val10=10, val11=12):
    """State 0,5"""
    assert t330006000_x39()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val10
        """State 3"""
        call = t330006000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val11 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t330006000_x28()
    """Unused"""
    """State 6"""
    return 0

def t330006000_x18():
    """State 0,2"""
    call = t330006000_x10(z10=1102, val16=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t330006000_x19():
    """State 0,1"""
    assert t330006000_x10(z10=1001, val16=1001)
    """State 2"""
    return 0

def t330006000_x20():
    """State 0,1"""
    assert t330006000_x10(z10=1103, val16=1103)
    """State 2"""
    return 0

def t330006000_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t330006000_x22(flag6=3723, flag7=3721, flag8=3722, val9=12, val10=10, val11=12, val12=10, val13=12,
                   actionbutton1=6240, flag9=6000, flag10=6001, flag11=6000, flag12=6000, flag13=6000,
                   z4=1, z5=1000000, z6=1000000, z7=1000000, mode2=1, mode3=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t330006000_x6(val9=val9, val10=val10, val11=val11, val12=val12, val13=val13, actionbutton1=actionbutton1,
                             flag9=flag9, flag10=flag10, flag11=flag11, flag12=flag12, flag13=flag13,
                             z4=z4, z5=z5, z6=z6, z7=z7, mode2=mode2, mode3=mode3)
        if CheckSelfDeath() == 1 or GetEventFlag(flag6) == 1:
            """State 3"""
            Label('L0')
            call = t330006000_x8(flag6=flag6, val10=val10, val11=val11)
            if not CheckSelfDeath() and not GetEventFlag(flag6):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag7) == 1 or GetEventFlag(flag8) == 1:
            """State 2"""
            call = t330006000_x7(val10=val10, val11=val11)
            if CheckSelfDeath() == 1 or GetEventFlag(flag6) == 1:
                Goto('L0')
            elif not GetEventFlag(flag7) and not GetEventFlag(flag8):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t330006000_x38() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t330006000_x23():
    """State 0,1"""
    assert t330006000_x24()
    """State 2"""
    return 0

def t330006000_x24():
    """State 0,1"""
    assert t330006000_x10(z10=1104, val16=1104)
    """State 2"""
    return 0

def t330006000_x25():
    """State 0,1"""
    call = t330006000_x10(z10=1201, val16=1201)
    if call.Get() == 1:
        """State 2"""
        assert t330006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t330006000_x26():
    """State 0,1"""
    call = t330006000_x10(z10=1300, val16=1300)
    if call.Get() == 1:
        """State 2"""
        assert t330006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t330006000_x27():
    """State 0,1"""
    call = t330006000_x10(z10=1301, val16=1301)
    if call.Get() == 1:
        """State 2"""
        assert t330006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t330006000_x28():
    """State 0,1"""
    call = t330006000_x10(z10=1302, val16=1302)
    if call.Get() == 1:
        """State 2"""
        assert t330006000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t330006000_x29(text4=_, z9=_, mode7=1):
    """State 0,5"""
    assert t330006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text4, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode7:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(z9, 1)
    """State 6"""
    return 0

def t330006000_x30(text1=_, mode6=1):
    """State 0,4"""
    assert t330006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text1, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode6:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t330006000_x31(text3=_, flag1=_, mode5=1):
    """State 0,5"""
    assert t330006000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(flag1, 1)
    """State 1"""
    TalkToPlayer(text3, -1, -1, 1)
    """State 4"""
    if not mode5:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t330006000_x32(text2=33080500, mode4=1):
    """State 0,4"""
    assert t330006000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    # talk:33080500:"Aaa...aaargh!"
    TalkToPlayer(text2, -1, -1, 1)
    """State 3"""
    if not mode4:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t330006000_x33():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t330006000_x34():
    """State 0,1"""
    assert t330006000_x10(z10=1002, val16=1002)
    """State 2"""
    return 0

def t330006000_x35(val1=_, val2=_, val5=_, z2=0):
    """State 0,1"""
    SetWorkValue(z2, 0)
    while True:
        """State 2"""
        if (ComparePlayerInventoryNumber(3, val1 + GetWorkValue(z2), 4, 1, 0) == 1 and not GetEventFlag(val5
            + GetWorkValue(z2))):
            """State 4"""
            return 1
        elif GetWorkValue(z2) > val2 - val1:
            break
        else:
            """Pass"""
            SetWorkValue(z2, GetWorkValue(z2) + 1)
    """State 3"""
    return 0

def t330006000_x36(val15=_, val7=_, val1=_, val2=_, val5=_, z8=0):
    """State 0,1"""
    SetWorkValue(z8, 0)
    while True:
        """State 2"""
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, val1 + GetWorkValue(z8), 4, 1, 0) == 1 and not GetEventFlag(val5 + GetWorkValue(z8)),
                          val15 + GetWorkValue(z8), val7 + GetWorkValue(z8), -1)
        if GetWorkValue(z8) > val2 - val1:
            break
        else:
            """Pass"""
            SetWorkValue(z8, GetWorkValue(z8) + 1)
    """State 3,4"""
    return 0

def t330006000_x37(val14=_, val1=_, val5=_, text1=33010000):
    """State 0,1"""
    PlayerEquipmentQuantityChange(3, val1 + GetTalkListEntryResult() - val14, -1)
    """State 2"""
    SetEventFlag(val5 + GetTalkListEntryResult() - val14, 1)
    """State 3"""
    assert t330006000_x30(text1=text1, mode6=1)
    """State 4"""
    return 0

def t330006000_x38():
    """State 0,1"""
    assert t330006000_x1()
    """State 2"""
    return 0

def t330006000_x39():
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

def t330006000_x40():
    """State 0,1"""
    if GetEventFlag(3725) == 1:
        """State 3"""
        def WhilePaused():
            RequestAnimation(20009, -1)
        assert t330006000_x44()
    else:
        """State 2"""
        pass
    """State 4"""
    return 0

def t330006000_x41(flag1=1037462710, flag2=1037462711, flag3=1037462712, flag4=1037462713, flag5=1037462714):
    """State 0,1"""
    SetEventFlag(1037462715, 1)
    if not GetEventFlag(flag1):
        """State 3"""
        # talk:33080000:"Mngh!"
        assert t330006000_x31(text3=33080000, flag1=flag1, mode5=1)
    elif not GetEventFlag(flag2):
        """State 4"""
        # talk:33080100:"Stop it, please."
        assert t330006000_x31(text3=33080100, flag1=flag2, mode5=1)
    elif not GetEventFlag(flag3):
        """State 5"""
        # talk:33080200:"I cannot be wounded. I cannot die."
        assert t330006000_x31(text3=33080200, flag1=flag3, mode5=1)
    elif not GetEventFlag(flag4) and GetSelfHP() < 66:
        """State 6"""
        # talk:33080300:"Well, aren't we determined."
        assert t330006000_x31(text3=33080300, flag1=flag4, mode5=1)
    elif not GetEventFlag(flag5) and GetSelfHP() < 33:
        """State 7"""
        # talk:33080400:"..."
        assert t330006000_x31(text3=33080400, flag1=flag5, mode5=1)
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t330006000_x42():
    """State 0,1"""
    # talk:33080500:"Aaa...aaargh!"
    assert t330006000_x32(text2=33080500, mode4=1)
    """State 2"""
    return 0

def t330006000_x43():
    """State 0"""
    while True:
        """State 2"""
        # actionbutton:6240:"Talk"
        call = t330006000_x0(actionbutton1=6240, flag10=6001, flag14=6000, flag15=6000, flag16=6000,
                             flag17=6000, flag9=6000)
        if call.Done():
            break
        elif DoesSelfHaveSpEffect(11436) == 1:
            """State 1"""
            assert not DoesSelfHaveSpEffect(11436)
    """State 3"""
    return 0

def t330006000_x44():
    """State 0,1"""
    if GetEventFlag(1037469256) == 1:
        """State 2"""
        if GetEventFlag(1037462715) == 1:
            """State 4"""
            assert t330006000_x46()
        else:
            """State 5"""
            assert t330006000_x47()
    else:
        """State 3"""
        assert t330006000_x45()
    """State 6"""
    return 0

def t330006000_x45():
    """State 0,1"""
    if GetEventFlag(1037462715) == 1:
        """State 3"""
        # talk:33002100:"Are you quite finished?"
        assert t330006000_x30(text1=33002100, mode6=1)
        """State 5"""
        assert t330006000_x48(mode1=1)
    else:
        """State 2"""
        # talk:33000100:"You're Tarnished, aren't you?"
        assert t330006000_x30(text1=33000100, mode6=1)
        """State 4"""
        assert t330006000_x48(mode1=0)
    """State 6"""
    return 0

def t330006000_x46():
    """State 0,1"""
    if not GetEventFlag(1037469259):
        """State 5"""
        # talk:33002000:"Are you quite finished?"
        assert t330006000_x29(text4=33002000, z9=1037469259, mode7=1)
    else:
        """State 4"""
        # talk:33002200:"Are you quite finished, now?"
        assert t330006000_x30(text1=33002200, mode6=1)
    """State 3"""
    SetEventFlag(1037462715, 0)
    """State 2"""
    SetEventFlag(1037462719, 1)
    """State 6"""
    return 0

def t330006000_x47():
    """State 0,3"""
    if not GetEventFlag(1037469257):
        """State 8"""
        # talk:33000300:"Oh, was there something you needed?"
        assert t330006000_x29(text4=33000300, z9=1037469257, mode7=1)
        """State 1"""
        Label('L0')
        SetEventFlag(1037462719, 1)
    else:
        """State 2"""
        if not GetEventFlag(1037462719):
            """State 6"""
            # talk:33001000:"Greetings. Do you need anything?"
            assert t330006000_x30(text1=33001000, mode6=1)
            """State 4"""
            SetEventFlag(1037460701, 1)
            Goto('L0')
        else:
            """State 7"""
            # talk:33000400:"Is there something else?"
            assert t330006000_x30(text1=33000400, mode6=1)
    """State 5"""
    assert t330006000_x49(z1=0, val1=8850, val2=8854, val3=8855, val4=8865, val5=1037469300, val6=1037469305)
    """State 9"""
    return 0

def t330006000_x48(mode1=_):
    """State 0,1"""
    c1_110()
    """State 2"""
    ClearTalkListData()
    """State 3"""
    # action:23301000:"I don't know"
    AddTalkListData(1, 23301000, -1)
    """State 4"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 5"""
    if GetTalkListEntryResult() == 1:
        """State 9"""
        # talk:33000200:"Well, that is a shame. But who can blame you?"
        assert t330006000_x29(text4=33000200, z9=1037469256, mode7=1)
        """State 8"""
        SetEventFlag(1037462719, 1)
        if mode1 == 1:
            """State 7"""
            SetEventFlag(1037469259, 1)
            SetEventFlag(1037462715, 0)
        else:
            pass
    else:
        """State 6"""
        pass
    """State 10"""
    return 0

def t330006000_x49(z1=0, val1=8850, val2=8854, val3=8855, val4=8865, val5=1037469300, val6=1037469305):
    """State 0"""
    while Loop('mainloop'):
        """State 1"""
        c1_110()
        while True:
            """State 2"""
            Label('L0')
            ClearTalkListData()
            """State 7"""
            assert t330006000_x50(z1=z1, val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, val6=val6)
            """State 3"""
            ShowShopMessage(1)
            assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 4"""
            if GetTalkListEntryResult() == 1:
                Break('mainloop')
            elif GetTalkListEntryResult() == 2:
                """State 8"""
                assert t330006000_x57()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 3:
                """State 9"""
                assert t330006000_x63()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 4:
                """State 10"""
                assert t330006000_x62()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 5:
                """State 11"""
                assert t330006000_x58()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 6:
                """State 12"""
                assert t330006000_x64()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 7:
                """State 13"""
                assert t330006000_x59()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 8:
                """State 14"""
                assert t330006000_x65()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 9:
                """State 6"""
                OpenRegularShop(100425, 100474)
                assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            elif GetTalkListEntryResult() == 10:
                """State 15"""
                assert t330006000_x60()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 11:
                """State 17"""
                # action:23160026:"Don't give a scroll"
                assert t330006000_x68(z2=0, val1=val1, val2=val2, val5=val5, val7=23160021, action1=23160026)
            elif GetTalkListEntryResult() == 12:
                """State 16"""
                # action:23510022:"Don't give a prayerbook"
                assert t330006000_x67(z3=0, val3=val3, val4=val4, val6=val6, val8=23510011, action2=23510022)
            else:
                """State 18"""
                return 0
    """State 5"""
    OpenRegularShop(100400, 100424)
    assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    Goto('L0')

def t330006000_x50(z1=0, val1=8850, val2=8854, val3=8855, val4=8865, val5=1037469300, val6=1037469305):
    """State 0,1"""
    # action:23300000:"Study sorcery"
    AddTalkListData(1, 23300000, -1)
    # action:23300013:"Study incantations"
    AddTalkListData(9, 23300013, -1)
    """State 4"""
    assert t330006000_x66(z1=z1, val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, val6=val6)
    """State 3"""
    assert t330006000_x51()
    """State 2"""
    # action:20000009:"Leave"
    AddTalkListData(99, 20000009, -1)
    """State 5"""
    return 0

def t330006000_x51():
    """State 0,1"""
    assert t330006000_x52()
    """State 2"""
    assert t330006000_x53()
    """State 3"""
    assert t330006000_x54()
    """State 4"""
    return 0

def t330006000_x52():
    """State 0,1"""
    SetEventFlag(1037469270, 0)
    SetEventFlag(1037469260, 0)
    SetEventFlag(1037469262, 0)
    SetEventFlag(1037469271, 0)
    SetEventFlag(1037469272, 0)
    SetEventFlag(1037469273, 0)
    SetEventFlag(1037469274, 0)
    SetEventFlag(1037469275, 0)
    """State 5"""
    assert t330006000_x61()
    """State 2"""
    SetEventFlagIf((GetEventFlag(1037469263) == 1 or GetEventFlag(1037469261) == 1) and not GetEventFlag(1037469264),
                   1037469271, 1)
    """State 3"""
    assert t330006000_x55()
    """State 4"""
    assert t330006000_x56()
    """State 6"""
    return 0

def t330006000_x53():
    """State 0,1"""
    if GetEventFlag(1037469271) == 1:
        """State 3"""
        SetEventFlag(1037469272, 0)
        SetEventFlag(1037469274, 0)
        SetEventFlag(1037469275, 0)
    else:
        """State 4"""
        if GetEventFlag(1037469272) == 1:
            """State 6"""
            SetEventFlag(1037469271, 0)
            SetEventFlag(1037469274, 0)
            SetEventFlag(1037469275, 0)
        else:
            """State 2"""
            if GetEventFlag(1037469274) == 1:
                """State 7"""
                SetEventFlag(1037469271, 0)
                SetEventFlag(1037469272, 0)
                SetEventFlag(1037469275, 0)
            else:
                """State 5"""
                if GetEventFlag(1037469275) == 1:
                    """State 8"""
                    SetEventFlag(1037469271, 0)
                    SetEventFlag(1037469272, 0)
                    SetEventFlag(1037469274, 0)
                else:
                    pass
    """State 9"""
    return 0

def t330006000_x54():
    """State 0,1"""
    # action:23300002:"Show Celestial Dew"
    AddTalkListDataIf(GetEventFlag(1037469270) == 1, 2, 23300002, -1)
    # action:23300006:"About absolution"
    AddTalkListDataIf(GetEventFlag(1037469262) == 1, 4, 23300006, -1)
    # action:23300003:"Talk"
    AddTalkListDataIf(GetEventFlag(1037469271) == 1, 10, 23300003, -1)
    # action:23300007:"About Radagon"
    AddTalkListDataIf(GetEventFlag(1037469272) == 1, 5, 23300007, -1)
    # action:23300008:"About Radagon"
    AddTalkListDataIf(GetEventFlag(1037469273) == 1 and not GetEventFlag(1037469266), 6, 23300008, -1)
    # action:23300009:"About Rennala"
    AddTalkListDataIf(GetEventFlag(1037469274) == 1, 7, 23300009, -1)
    # action:23300010:"About Rennala"
    AddTalkListDataIf(GetEventFlag(1037469275) == 1, 8, 23300010, -1)
    # action:23300005:"About the miracle"
    AddTalkListDataIf(GetEventFlag(1037469260) == 1, 3, 23300005, -1)
    # action:23300008:"About Radagon"
    AddTalkListDataIf(GetEventFlag(1037469273) == 1 and GetEventFlag(1037469266) == 1, 6, 23300008, -1)
    """State 2"""
    return 0

def t330006000_x55():
    """State 0,1"""
    if GetEventFlag(1037469265) == 1:
        """State 3"""
        if GetEventFlag(1037469266) == 1 and GetEventFlag(11009555) == 1:
            pass
        else:
            """State 4"""
            SetEventFlag(1037469273, 1)
    else:
        """State 2"""
        SetEventFlag(1037469272, 1)
    """State 5"""
    return 0

def t330006000_x56():
    """State 0,1"""
    if GetEventFlag(1037469267) == 1:
        """State 2"""
        if GetEventFlag(1037469268) == 1:
            pass
        else:
            """State 4"""
            SetEventFlag(1037469275, 1)
    else:
        """State 3"""
        SetEventFlag(1037469274, 1)
    """State 5"""
    return 0

def t330006000_x57():
    """State 0,1"""
    # talk:33001100:"Do you possess any celestial dew?"
    assert t330006000_x29(text4=33001100, z9=1037469263, mode7=1)
    """State 2"""
    return 0

def t330006000_x58():
    """State 0,1"""
    # talk:33005000:"You wish to know more of Lord Radagon?"
    assert t330006000_x29(text4=33005000, z9=1037469265, mode7=1)
    """State 2"""
    return 0

def t330006000_x59():
    """State 0,1"""
    # talk:33005200:"You wish to know more of Lady Rennala?"
    assert t330006000_x29(text4=33005200, z9=1037469267, mode7=1)
    """State 2"""
    return 0

def t330006000_x60():
    """State 0,1"""
    # talk:33001200:"My faith does not waver."
    assert t330006000_x29(text4=33001200, z9=1037469264, mode7=1)
    """State 2"""
    return 0

def t330006000_x61():
    """State 0,1"""
    if GetEventFlag(1037469277) == 1:
        """State 3"""
        if GetEventFlag(1037469261) == 1:
            pass
        else:
            """State 4"""
            SetEventFlag(1037469262, 1)
    else:
        """State 5"""
        if GetEventFlag(1037469263) == 1:
            """State 6"""
            SetEventFlag(1037469260, 1)
        else:
            """State 7"""
            # goods:2130:Celestial Dew
            if ComparePlayerInventoryNumber(3, 2130, 2, 0, 0) == 1:
                """State 2"""
                SetEventFlag(1037469270, 1)
            else:
                pass
    """State 8"""
    return 0

def t330006000_x62():
    """State 0,1"""
    # talk:33003300:"Ah, I see you have undergone absolution, the miracle that blossoms from these grounds."
    assert t330006000_x29(text4=33003300, z9=1037469261, mode7=1)
    """State 2"""
    return 0

def t330006000_x63():
    """State 0,1"""
    # talk:33003100:"To experience the miracle, kneel in the basin at the back, and cleanse yourself with celestial dew."
    assert t330006000_x30(text1=33003100, mode6=1)
    """State 2"""
    return 0

def t330006000_x64():
    """State 0,1"""
    # talk:33005100:"You know, it's said that Lord Radagon harboured a secret..."
    assert t330006000_x29(text4=33005100, z9=1037469266, mode7=1)
    """State 2"""
    return 0

def t330006000_x65():
    """State 0,1"""
    # talk:33005300:"In the end, Lady Rennala was left alone, cradling the amber egg Lord Radagon bequeathed her."
    assert t330006000_x29(text4=33005300, z9=1037469268, mode7=1)
    """State 2"""
    return 0

def t330006000_x66(z1=0, val1=8850, val2=8854, val3=8855, val4=8865, val5=1037469300, val6=1037469305):
    """State 0,3"""
    call = t330006000_x35(val1=val1, val2=val2, val5=val5, z2=z1)
    if call.Get() == 1:
        """State 1"""
        Label('L0')
        # action:23300011:"Give a scroll"
        AddTalkListData(11, 23300011, -1)
    elif call.Done():
        """State 5"""
        call = t330006000_x35(val1=8866, val2=8866, val5=1037469316, z2=z1)
        if call.Get() == 1:
            Goto('L0')
        elif call.Done():
            pass
    """State 4"""
    call = t330006000_x35(val1=val3, val2=val4, val5=val6, z2=z1)
    if call.Get() == 1:
        """State 2"""
        # action:23300012:"Give a prayerbook"
        AddTalkListData(12, 23300012, -1)
    elif call.Done():
        pass
    """State 6"""
    return 0

def t330006000_x67(z3=0, val3=8855, val4=8865, val6=1037469305, val8=23510011, action2=23510022):
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        """State 5"""
        assert t330006000_x36(val15=1, val7=val8, val1=val3, val2=val4, val5=val6, z8=0)
        """State 2"""
        # action:23510022:"Don't give a prayerbook"
        AddTalkListData(99, action2, -1)
        """State 3"""
        ShowShopMessage(0)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if not GetTalkListEntryResult() or GetTalkListEntryResult() == 99:
            break
        else:
            """State 6"""
            # talk:33010000:"Oh, what have we here?"
            assert t330006000_x37(val14=1, val1=val3, val5=val6, text1=33010000)
            """State 7"""
            call = t330006000_x35(val1=val3, val2=val4, val5=val6, z2=z3)
            if call.Get() == 1:
                pass
            elif call.Done():
                break
    """State 8"""
    return 0

def t330006000_x68(z2=0, val1=8850, val2=8854, val5=1037469300, val7=23160021, action1=23160026):
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        """State 5"""
        assert t330006000_x36(val15=1, val7=val7, val1=val1, val2=val2, val5=val5, z8=0)
        """State 8"""
        assert t330006000_x36(val15=50, val7=23160028, val1=8866, val2=8866, val5=1037469316, z8=0)
        """State 2"""
        # action:23160026:"Don't give a scroll"
        AddTalkListData(99, action1, -1)
        """State 3"""
        ShowShopMessage(0)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if not GetTalkListEntryResult() or GetTalkListEntryResult() == 99:
            break
        elif GetTalkListEntryResult() == 50:
            """State 9"""
            # talk:33010000:"Oh, what have we here?"
            assert t330006000_x37(val14=50, val1=8866, val5=1037469316, text1=33010000)
            """State 7"""
            Label('L0')
            call = t330006000_x35(val1=val1, val2=val2, val5=val5, z2=z2)
            if call.Get() == 1:
                pass
            elif call.Done():
                """State 10"""
                call = t330006000_x35(val1=8866, val2=8866, val5=1037469316, z2=z2)
                if call.Get() == 1:
                    pass
                elif call.Done():
                    break
        else:
            """State 6"""
            # talk:33010000:"Oh, what have we here?"
            assert t330006000_x37(val14=1, val1=val1, val5=val5, text1=33010000)
            Goto('L0')
    """State 11"""
    return 0

