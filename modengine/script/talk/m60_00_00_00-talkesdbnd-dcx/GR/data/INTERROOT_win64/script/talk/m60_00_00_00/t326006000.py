# -*- coding: utf-8 -*-
def t326006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t326006000_x23(flag1=3883, flag2=3881, flag3=3882, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1)
    Quit()

def t326006000_1000():
    """State 0,2,3"""
    assert t326006000_x0()
    """State 1"""
    c1_120(1000)
    Quit()

def t326006000_1001():
    """State 0,2,3"""
    assert t326006000_x1()
    """State 1"""
    c1_120(1001)
    Quit()

def t326006000_1101():
    """State 0,2,3"""
    assert t326006000_x2()
    """State 1"""
    c1_120(1101)
    Quit()

def t326006000_1102():
    """State 0,2,3"""
    t326006000_x3()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t326006000_1103():
    """State 0,2,3"""
    assert t326006000_x4()
    """State 1"""
    c1_120(1103)
    Quit()

def t326006000_2000():
    """State 0,2,3"""
    assert t326006000_x5()
    """State 1"""
    c1_120(2000)
    Quit()

def t326006000_x0():
    """State 0,1"""
    if GetEventFlag(3885) == 1:
        """State 3"""
        assert t326006000_x6()
    elif GetEventFlag(3886) == 1:
        """State 4"""
        assert t326006000_x7()
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t326006000_x1():
    """State 0,1"""
    # talk:32680200:"Dog eat dog, once again. A sad lot, we Tarnished."
    assert t326006000_x48(text1=32680200, mode3=1)
    """State 2"""
    return 0

def t326006000_x2():
    """State 0"""
    if not GetEventFlag(1042382711):
        """State 2,1"""
        SetEventFlag(1042382711, 1)
        """State 4"""
        # talk:32680000:"Agh!"
        assert t326006000_x48(text1=32680000, mode3=1)
    else:
        """State 3"""
        pass
    """State 5"""
    return 0

def t326006000_x3():
    """State 0,2"""
    if not GetEventFlag(1042389253):
        """State 3,7"""
        SetEventFlag(1042389253, 1)
        """State 6"""
        SetEventFlag(1042382710, 1)
        """State 8"""
        # talk:32680100:"I suppose I have no choice, then."
        assert t326006000_x48(text1=32680100, mode3=1)
    elif not GetEventFlag(1042382710):
        """State 4"""
        pass
    else:
        """State 5"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 9"""
    return 0

def t326006000_x4():
    """State 0,1"""
    # talk:32680300:"You are an enigma, to be certain."
    assert t326006000_x48(text1=32680300, mode3=1)
    """State 2"""
    return 0

def t326006000_x5():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    assert (t326006000_x17(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
            flag4=6000))
    """State 2"""
    return 0

def t326006000_x6():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(90305, -1)
    assert t326006000_x8()
    """State 2"""
    return 0

def t326006000_x7():
    """State 0,1"""
    if GetEventFlag(16009460) == 1:
        """State 2,6"""
        # talk:32602100:"O Greater Will, hear my voice."
        assert t326006000_x47(text2=32602100, mode4=1)
    elif GetEventFlag(16000800) == 1 and not GetEventFlag(16009460):
        """State 5"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t326006000_x13()
    elif GetEventFlag(16009455) == 1 and GetEventFlagValue(16009260, 4) > 1 and not GetEventFlag(16002740):
        """State 4"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t326006000_x12()
    else:
        """State 3"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t326006000_x11()
    """State 7"""
    return 0

def t326006000_x8():
    """State 0,1"""
    if not GetEventFlag(1042389255) and not GetEventFlag(1042389256):
        """State 2,16"""
        # talk:32600100:"Not seen you before."
        assert t326006000_x47(text2=32600100, mode4=1)
        """State 3"""
        c1_110()
        ClearTalkListData()
        """State 4"""
        # action:23261000:"My faith holds firm"
        AddTalkListData(1, 23261000, -1)
        # action:23261001:"I'm not sure"
        AddTalkListData(2, 23261001, -1)
        """State 5"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 6"""
        if GetTalkListEntryResult() == 1:
            """State 7,17"""
            # talk:32600200:"Yes, you're a Tarnished through and through."
            assert t326006000_x47(text2=32600200, mode4=1)
            """State 9"""
            SetEventFlag(1042389255, 1)
        elif GetTalkListEntryResult() == 2:
            """State 8,18"""
            # talk:32600600:"Honest to a fault, I see."
            assert t326006000_x47(text2=32600600, mode4=1)
            """State 10"""
            SetEventFlag(1042389256, 1)
        else:
            """State 11"""
            Goto('L2')
        """State 15"""
        SetEventFlag(1042382713, 1)
        """State 22"""
        Label('L0')
        call = t326006000_x9()
        if call.Done():
            pass
        elif call.Done():
            pass
    elif not GetEventFlag(1042389258):
        """State 12,19"""
        # talk:32600800:"There you are. Decided to bear the torch of my battle arts?"
        assert t326006000_x47(text2=32600800, mode4=1)
        """State 23"""
        Label('L1')
        assert t326006000_x16()
        Goto('L0')
    elif GetEventFlag(1042382712) == 1:
        """State 13,20"""
        # talk:32600300:"Oh, not had your fill, eh? Worry not, I've enough to keep you busy."
        assert t326006000_x47(text2=32600300, mode4=1)
        Goto('L1')
    else:
        """State 14,21"""
        # talk:32600400:"Ah, hello. Glad to see you safe."
        assert t326006000_x47(text2=32600400, mode4=1)
        Goto('L1')
    """State 24"""
    Label('L2')
    return 0

def t326006000_x9():
    """State 0,1"""
    c1_110()
    ClearTalkActionState()
    while True:
        """State 9"""
        ClearTalkListData()
        """State 2"""
        # action:23260000:"Learn skills"
        AddTalkListData(1, 23260000, -1)
        # action:23260001:"Talk"
        AddTalkListDataIf(not GetEventFlag(1042389257), 2, 23260001, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 5,8"""
            OpenRegularShop(100075, 100099)
            """State 13"""
            call = t326006000_x10()
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 6,14"""
            # talk:32600500:"There's a myriad of battle arts in these lands that I've yet to discover."
            assert t326006000_x47(text2=32600500, mode4=1)
            """State 10"""
            SetEventFlag(1042389257, 1)
        else:
            """State 7"""
            if not GetEventFlag(1042389258):
                """State 11,15"""
                # talk:32600700:"Not floating your boat, eh?"
                assert t326006000_x47(text2=32600700, mode4=1)
            else:
                """State 12,16"""
                # talk:32600900:"Well, until we meet again."
                assert t326006000_x47(text2=32600900, mode4=1)
            """State 17"""
            return 0

def t326006000_x10():
    """State 0,1"""
    assert DidYouDoSomethingInTheMenu(0) == 1
    """State 2"""
    if GetEventFlag(3885) == 1:
        """State 3,5"""
        SetEventFlag(1042389258, 1)
    else:
        """State 4"""
        pass
    """State 6"""
    SetEventFlag(1042382712, 1)
    """State 7"""
    Quit()
    """Unused"""
    """State 8"""
    return 0

def t326006000_x11():
    """State 0,1"""
    if not GetEventFlag(16009455) and not GetEventFlag(16009456):
        """State 2"""
        if not GetEventFlag(1042389255) and not GetEventFlag(1042389256):
            """State 14,16"""
            # talk:32603000:"Who are you?"
            assert t326006000_x47(text2=32603000, mode4=1)
            """State 5"""
            Label('L0')
            c1_110()
            ClearTalkListData()
            """State 6"""
            # action:23261002:"I understand"
            AddTalkListData(1, 23261002, -1)
            # action:23261003:"I don't understand"
            AddTalkListData(2, 23261003, -1)
            """State 7"""
            OpenConversationChoicesMenu(0)
            assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 8"""
            if GetTalkListEntryResult() == 1:
                """State 9,21"""
                assert t326006000_x15()
                """State 11"""
                SetEventFlag(16009455, 1)
                SetEventFlag(16002740, 1)
            elif GetTalkListEntryResult() == 2:
                """State 10,19"""
                # talk:32604100:"Then you must leave immediately."
                assert t326006000_x47(text2=32604100, mode4=1)
                """State 12"""
                SetEventFlag(16009456, 1)
            else:
                """State 13"""
                pass
        else:
            """State 15,20"""
            # talk:32601000:"You..."
            assert t326006000_x47(text2=32601000, mode4=1)
            Goto('L0')
    elif not GetEventFlag(16009455) and GetEventFlag(16009456) == 1:
        """State 3,17"""
        # talk:32604200:"I thought I told you to leave."
        assert t326006000_x47(text2=32604200, mode4=1)
        Goto('L0')
    else:
        """State 4,18"""
        # talk:32601200:"This blasphemous path leads only to a pitiful death."
        assert t326006000_x47(text2=32601200, mode4=1)
    """State 22"""
    return 0

def t326006000_x12():
    """State 0,1"""
    if (not GetEventFlag(16009458) and GetEventFlag(16009457) == 1 and not GetEventFlag(16002741) and
        GetEventFlagValue(16009260, 4) > 2 and not GetEventFlag(118)):
        """State 2,10"""
        # talk:32601700:"Look at you. A recusant through and through."
        assert t326006000_x47(text2=32601700, mode4=1)
        """State 7"""
        SetEventFlag(16009458, 1)
        """State 14"""
        # lot:102900:Letter to Bernahl
        assert t326006000_x20(lot1=102900)
        """State 18"""
        # talk:32601705:"A special invitation, to hunt some of the first Tarnished who sat at the Roundtable Hold."
        assert t326006000_x47(text2=32601705, mode4=1)
    elif not GetEventFlag(16009461) and GetEventFlag(7605) == 1:
        """State 8,16"""
        # talk:32601800:"Ah, I had hoped you'd soon return."
        assert t326006000_x47(text2=32601800, mode4=1)
        """State 9"""
        SetEventFlag(16009461, 1)
        """State 17"""
        # lot:102910:Gelmir's Fury
        assert t326006000_x20(lot1=102910)
        """State 19"""
        # talk:32601805:"Let us tread the path of the recusant together."
        assert t326006000_x47(text2=32601805, mode4=1)
    elif not GetEventFlag(16009457):
        """State 3,11"""
        # talk:32601300:"So. You've bloodied your sword in the hunt."
        assert t326006000_x47(text2=32601300, mode4=1)
        """State 6"""
        SetEventFlag(16009457, 1)
        SetEventFlag(16002741, 1)
        """State 15"""
        Label('L0')
        assert t326006000_x14()
    elif GetEventFlag(1042382712) == 1:
        """State 4,12"""
        # talk:32601400:"Oh, not had your fill, eh?"
        assert t326006000_x47(text2=32601400, mode4=1)
        Goto('L0')
    else:
        """State 5,13"""
        # talk:32601500:"You're still alive, I see."
        assert t326006000_x47(text2=32601500, mode4=1)
        Goto('L0')
    """State 20"""
    return 0

def t326006000_x13():
    """State 0,1,2,4"""
    # talk:32602000:"So. You killed Rykard?"
    assert t326006000_x47(text2=32602000, mode4=1)
    """State 3"""
    SetEventFlag(16009460, 1)
    """State 5"""
    return 0

def t326006000_x14():
    """State 0,1"""
    ClearTalkActionState()
    c1_110()
    while True:
        """State 2"""
        ClearTalkListData()
        """State 3"""
        # action:23260000:"Learn skills"
        AddTalkListData(1, 23260000, -1)
        # action:23260002:"Talk"
        AddTalkListDataIf(not GetEventFlag(16009459), 2, 23260002, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 7,6"""
            OpenRegularShop(100075, 100099)
            """State 11"""
            call = t326006000_x10()
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 8,12"""
            # talk:32601600:"You've come to understand, now, eh?"
            assert t326006000_x47(text2=32601600, mode4=1)
            """State 9"""
            SetEventFlag(16009459, 1)
        else:
            """State 10,13"""
            # talk:32600900:"Well, until we meet again."
            assert t326006000_x47(text2=32600900, mode4=1)
            """State 14"""
            return 0

def t326006000_x15():
    """State 0,1"""
    if not GetEventFlag(1042389255) and not GetEventFlag(1042389256):
        """State 2,5"""
        # talk:32604300:"Well. As long as you understand what you're saying."
        assert t326006000_x47(text2=32604300, mode4=1)
    elif GetEventFlag(1042389255) == 1:
        """State 3,6"""
        # talk:32601100:"Well. As long as you understand what you're saying."
        assert t326006000_x47(text2=32601100, mode4=1)
    else:
        """State 4,7"""
        # talk:32604000:"Well. As long as you understand what you're saying."
        assert t326006000_x47(text2=32604000, mode4=1)
    """State 8"""
    return 0

def t326006000_x16():
    """State 0,1"""
    if GetEventFlag(1042382713) == 1:
        """State 2"""
        pass
    else:
        """State 3,4"""
        SetEventFlag(1042380701, 1)
    """State 5"""
    return 0

def t326006000_x17(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t326006000_x18():
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

def t326006000_x19():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t326006000_x20(lot1=_):
    """State 0,1"""
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t326006000_x21(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t326006000_x37()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t326006000_x18()
    else:
        """State 4,7"""
        call = t326006000_x50()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t326006000_x18()
    """State 9"""
    return 0

def t326006000_x22():
    """State 0,1"""
    assert t326006000_x18()
    """State 2"""
    return 0

def t326006000_x23(flag1=3883, flag2=3881, flag3=3882, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t326006000_x40(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t326006000_x39()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t326006000_x24(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                   flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                   mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t326006000_x27(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t326006000_x31(val1=val1, z1=z1)
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
            call = t326006000_x33(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t326006000_x44() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t326006000_x29(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t326006000_x25(val2=10, val3=12):
    """State 0,1"""
    call = t326006000_x35(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t326006000_x21(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t326006000_x26(flag1=3883, val2=10, val3=12):
    """State 0,8"""
    assert t326006000_x52()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t326006000_x38()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t326006000_x18()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t326006000_x27(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t326006000_x28(z5=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t326006000_x17(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t326006000_x28(z5=_, val6=_):
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

def t326006000_x29(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t326006000_x18()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t326006000_x30()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t326006000_x45()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t326006000_x30():
    """State 0,1"""
    assert t326006000_x28(z5=1101, val6=1101)
    """State 2"""
    return 0

def t326006000_x31(val1=5, z1=1):
    """State 0,2"""
    assert t326006000_x41()
    """State 1"""
    call = t326006000_x32()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t326006000_x43()
    """State 4"""
    return 0

def t326006000_x32():
    """State 0,1"""
    assert t326006000_x28(z5=1000, val6=1000)
    """State 2"""
    return 0

def t326006000_x33(val5=12):
    """State 0,1"""
    call = t326006000_x34()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t326006000_x44()
    """State 3"""
    return 0

def t326006000_x34():
    """State 0,1"""
    assert t326006000_x28(z5=1100, val6=1100)
    """State 2"""
    return 0

def t326006000_x35(val2=10, val3=12):
    """State 0,5"""
    assert t326006000_x52()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t326006000_x36()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t326006000_x46()
    """Unused"""
    """State 6"""
    return 0

def t326006000_x36():
    """State 0,2"""
    call = t326006000_x28(z5=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t326006000_x37():
    """State 0,1"""
    assert t326006000_x28(z5=1001, val6=1001)
    """State 2"""
    return 0

def t326006000_x38():
    """State 0,1"""
    assert t326006000_x28(z5=1103, val6=1103)
    """State 2"""
    return 0

def t326006000_x39():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t326006000_x40(flag1=3883, flag2=3881, flag3=3882, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t326006000_x24(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                              flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                              z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t326006000_x26(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t326006000_x25(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t326006000_x51() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t326006000_x41():
    """State 0,1"""
    assert t326006000_x42()
    """State 2"""
    return 0

def t326006000_x42():
    """State 0,1"""
    assert t326006000_x28(z5=1104, val6=1104)
    """State 2"""
    return 0

def t326006000_x43():
    """State 0,1"""
    call = t326006000_x28(z5=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t326006000_x22()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t326006000_x44():
    """State 0,1"""
    call = t326006000_x28(z5=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t326006000_x22()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t326006000_x45():
    """State 0,1"""
    call = t326006000_x28(z5=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t326006000_x22()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t326006000_x46():
    """State 0,1"""
    call = t326006000_x28(z5=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t326006000_x22()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t326006000_x47(text2=_, mode4=1):
    """State 0,4"""
    assert t326006000_x19() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t326006000_x48(text1=_, mode3=1):
    """State 0,4"""
    assert t326006000_x49() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t326006000_x49():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t326006000_x50():
    """State 0,1"""
    assert t326006000_x28(z5=1002, val6=1002)
    """State 2"""
    return 0

def t326006000_x51():
    """State 0,1"""
    assert t326006000_x18()
    """State 2"""
    return 0

def t326006000_x52():
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

