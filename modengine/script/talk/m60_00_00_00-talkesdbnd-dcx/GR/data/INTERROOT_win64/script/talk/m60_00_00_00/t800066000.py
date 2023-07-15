# -*- coding: utf-8 -*-
def t800066000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t800066000_x5(flag5=4703, flag6=4701, flag7=4702, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag8=6000, flag9=6001, flag10=6000, flag11=6000, flag12=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000)
    Quit()

def t800066000_1000():
    """State 0,2,1"""
    c1_120(1000)
    Quit()

def t800066000_1001():
    """State 0,2,3"""
    assert t800066000_x31()
    """State 1"""
    c1_120(1001)
    Quit()

def t800066000_1101():
    """State 0,2,3"""
    assert t800066000_x32(flag4=1042399241, z1=4701, z2=1042399247)
    """State 1"""
    c1_120(1101)
    Quit()

def t800066000_1102():
    """State 0,2,3"""
    t800066000_x33(flag1=1042392700, flag2=1042399248, flag3=1042399247)
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t800066000_1103():
    """State 0,2,3"""
    assert t800066000_x34()
    """State 1"""
    c1_120(1103)
    Quit()

def t800066000_x0(actionbutton1=6000, flag9=6001, flag13=6000, flag14=6000, flag15=6000, flag16=6000,
                  flag8=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag9) == 1 or GetEventFlag(flag13) == 1 or GetEventFlag(flag14) == 1 or
                GetEventFlag(flag15) == 1 or GetEventFlag(flag16) == 1)
        """State 4"""
        assert not GetEventFlag(flag8)
        """State 2"""
        if GetEventFlag(flag8) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag9) and not GetEventFlag(flag13) and not GetEventFlag(flag14) and not
              GetEventFlag(flag15) and not GetEventFlag(flag16)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t800066000_x1():
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

def t800066000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t800066000_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2
    """State 3"""
    call = t800066000_x19()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t800066000_x1()
    """State 4"""
    return 0

def t800066000_x4():
    """State 0,1"""
    assert t800066000_x1()
    """State 2"""
    return 0

def t800066000_x5(flag5=4703, flag6=4701, flag7=4702, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag8=6000, flag9=6001, flag10=6000, flag11=6000, flag12=6000, z3=1, z4=1000000, z5=1000000,
                  z6=1000000):
    """State 0"""
    while True:
        """State 2"""
        call = t800066000_x22(flag5=flag5, flag6=flag6, flag7=flag7, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag8=flag8, flag9=flag9,
                              flag10=flag10, flag11=flag11, flag12=flag12, z3=z3, z4=z4, z5=z5, z6=z6)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t800066000_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t800066000_x6(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag8=6000, flag9=6001,
                  flag10=6000, flag11=6000, flag12=6000, z3=1, z4=1000000, z5=1000000, z6=1000000):
    """State 0"""
    while True:
        """State 1"""
        call = t800066000_x9(actionbutton1=actionbutton1, flag8=flag8, flag9=flag9, z4=z4, z5=z5, z6=z6)
        if call.Done():
            """State 3"""
            Label('L0')
            call = t800066000_x13(val1=val1, z3=z3)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif IsAttackedBySomeone() == 1:
            pass
        elif GetEventFlag(flag12) == 1:
            Goto('L0')
        elif GetEventFlag(flag10) == 1 and not GetEventFlag(flag11) and GetDistanceToPlayer() < val4:
            """State 4"""
            call = t800066000_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif (GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0):
            """State 5"""
            assert t800066000_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        """State 2"""
        def ExitPause():
            RemoveMyAggro()
        assert t800066000_x11(val2=val2, val3=val3)
    """Unused"""
    """State 6"""
    return 0

def t800066000_x7(val2=10, val3=12):
    """State 0,1"""
    call = t800066000_x17(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t800066000_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t800066000_x8(flag5=4703, val2=10, val3=12):
    """State 0,1"""
    if GetEventFlag(flag5) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t800066000_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t800066000_x1()
        else:
            """State 5"""
            pass
    """State 8"""
    return 0

def t800066000_x9(actionbutton1=6000, flag8=6000, flag9=6001, z4=1000000, z5=1000000, z6=1000000):
    """State 0,1"""
    call = t800066000_x10(z7=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t800066000_x0(actionbutton1=actionbutton1, flag9=flag9, flag13=6000, flag14=6000, flag15=6000,
                flag16=6000, flag8=flag8))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800066000_x10(z7=_, val6=_):
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

def t800066000_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 4"""
    assert t800066000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1,5"""
        call = t800066000_x12()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 6"""
            assert t800066000_x27()
    else:
        """State 2"""
        pass
    """State 7"""
    return 0

def t800066000_x12():
    """State 0,1"""
    assert t800066000_x10(z7=1101, val6=1101)
    """State 2"""
    return 0

def t800066000_x13(val1=5, z3=1):
    """State 0,2"""
    assert t800066000_x23()
    """State 1"""
    call = t800066000_x14()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6:
        """State 3"""
        assert t800066000_x25()
    """State 4"""
    return 0

def t800066000_x14():
    """State 0,1"""
    assert t800066000_x10(z7=1000, val6=1000)
    """State 2"""
    return 0

def t800066000_x15(val5=12):
    """State 0,1"""
    call = t800066000_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t800066000_x26()
    """State 3"""
    return 0

def t800066000_x16():
    """State 0,1"""
    assert t800066000_x10(z7=1100, val6=1100)
    """State 2"""
    return 0

def t800066000_x17(val2=10, val3=12):
    """State 0"""
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 2"""
        call = t800066000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 3"""
            assert t800066000_x28()
    """Unused"""
    """State 4"""
    return 0

def t800066000_x18():
    """State 0,2"""
    call = t800066000_x10(z7=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t800066000_x19():
    """State 0,1"""
    assert t800066000_x10(z7=1001, val6=1001)
    """State 2"""
    return 0

def t800066000_x20():
    """State 0,1"""
    assert t800066000_x10(z7=1103, val6=1103)
    """State 2"""
    return 0

def t800066000_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t800066000_x22(flag5=4703, flag6=4701, flag7=4702, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag8=6000, flag9=6001, flag10=6000, flag11=6000, flag12=6000, z3=1, z4=1000000, z5=1000000,
                   z6=1000000):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t800066000_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag8=flag8, flag9=flag9, flag10=flag10, flag11=flag11, flag12=flag12, z3=z3,
                             z4=z4, z5=z5, z6=z6)
        if CheckSelfDeath() == 1 or GetEventFlag(flag5) == 1:
            break
        elif GetEventFlag(flag6) == 1 or GetEventFlag(flag7) == 1:
            """State 2"""
            call = t800066000_x7(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag5) == 1:
                break
            elif not GetEventFlag(flag6) and not GetEventFlag(flag7):
                pass
    """State 3"""
    t800066000_x8(flag5=flag5, val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 4"""
    return 0

def t800066000_x23():
    """State 0,1"""
    assert t800066000_x24()
    """State 2"""
    return 0

def t800066000_x24():
    """State 0,1"""
    assert t800066000_x10(z7=1104, val6=1104)
    """State 2"""
    return 0

def t800066000_x25():
    """State 0,1"""
    call = t800066000_x10(z7=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t800066000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800066000_x26():
    """State 0,1"""
    call = t800066000_x10(z7=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t800066000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800066000_x27():
    """State 0,1"""
    call = t800066000_x10(z7=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t800066000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800066000_x28():
    """State 0,1"""
    call = t800066000_x10(z7=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t800066000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800066000_x29(text2=_, flag1=1042392700, mode2=1):
    """State 0,5"""
    assert t800066000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(flag1, 1)
    """State 1"""
    TalkToPlayer(text2, -1, -1, 1)
    """State 4"""
    if not mode2:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t800066000_x30(text1=_, mode1=1):
    """State 0,4"""
    assert t800066000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text1, -1, -1, 1)
    """State 3"""
    if not mode1:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t800066000_x31():
    """State 0,1"""
    assert t800066000_x30(text1=80003700, mode1=1)
    """State 2"""
    return 0

def t800066000_x32(flag4=1042399241, z1=4701, z2=1042399247):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        """State 4"""
        if not GetEventFlag(4980):
            """State 2"""
            if not GetEventFlag(flag4):
                """State 3"""
                SetEventFlag(flag4, 1)
                """State 7"""
                call = t800066000_x30(text1=80090000, mode1=1)
                if call.Done():
                    break
                elif GetCurrentStateElapsedFrames() > 1 and IsPlayerAttacking() == 1:
                    pass
            else:
                """State 6"""
                call = t800066000_x30(text1=80003420, mode1=1)
                if call.Done():
                    break
                elif GetCurrentStateElapsedFrames() > 1 and IsPlayerAttacking() == 1:
                    pass
        else:
            """State 5"""
            SetEventFlag(z2, 1)
            break
    """State 8"""
    return 0

def t800066000_x33(flag1=1042392700, flag2=1042399248, flag3=1042399247):
    """State 0,1"""
    SetEventFlag(4980, 1)
    t800066000_x35(flag1=flag1, flag2=flag2, flag3=flag3)
    def WhilePaused():
        c1_121(11020)
    Quit()
    """Unused"""
    """State 2"""
    return 0

def t800066000_x34():
    """State 0,1"""
    # talk:80003500:"Once I decipher that cryptogram, I'll be packing up shop again."
    assert t800066000_x30(text1=80003500, mode1=1)
    """State 2"""
    return 0

def t800066000_x35(flag1=1042392700, flag2=1042399248, flag3=1042399247):
    """State 0,2"""
    if not GetEventFlag(flag1):
        """State 3"""
        if not GetEventFlag(flag2):
            """State 4"""
            SetEventFlag(flag2, 1)
            """State 5"""
            if not GetEventFlag(flag3):
                """State 7"""
                assert t800066000_x29(text2=80090100, flag1=flag1, mode2=1)
            else:
                """State 9"""
                assert t800066000_x29(text2=80090100, flag1=flag1, mode2=1)
        else:
            """State 6,8"""
            assert t800066000_x29(text2=80090300, flag1=flag1, mode2=1)
    else:
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 10"""
    return 0

