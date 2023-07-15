# -*- coding: utf-8 -*-
def t309006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t309006000_x62(flag1=3683, flag2=3681, flag3=3682, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1)
    Quit()

def t309006000_1000():
    """State 0,2,3"""
    assert t309006000_x0()
    """State 1"""
    c1_120(1000)
    Quit()

def t309006000_1001():
    """State 0,2,3"""
    assert t309006000_x1()
    """State 1"""
    c1_120(1001)
    Quit()

def t309006000_1101():
    """State 0,2,3"""
    assert t309006000_x2()
    """State 1"""
    c1_120(1101)
    Quit()

def t309006000_1102():
    """State 0,2,3"""
    t309006000_x3()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t309006000_1103():
    """State 0,2,3"""
    assert t309006000_x4()
    """State 1"""
    c1_120(1103)
    Quit()

def t309006000_2000():
    """State 0,2,3"""
    assert t309006000_x5(z5=10, z6=12)
    """State 1"""
    c1_120(2000)
    Quit()

def t309006000_x0():
    """State 0,1"""
    if GetEventFlag(3685) == 1:
        """State 3"""
        assert t309006000_x6()
    elif GetEventFlag(3686) == 1:
        """State 10"""
        assert t309006000_x50()
    elif GetEventFlag(3687) == 1:
        """State 7"""
        assert t309006000_x35()
    elif GetEventFlag(3688) == 1:
        """State 4"""
        assert t309006000_x9()
    elif GetEventFlag(3689) == 1:
        """State 5"""
        assert t309006000_x10()
    elif GetEventFlag(3690) == 1:
        """State 8"""
        assert t309006000_x36()
    elif GetEventFlag(3691) == 1 or GetEventFlag(3694) == 1:
        """State 9"""
        assert t309006000_x37()
    elif GetEventFlag(3692) == 1:
        """State 6"""
        assert t309006000_x13()
    elif GetEventFlag(3693) == 1:
        """State 11"""
        assert t309006000_x52()
    else:
        """State 2"""
        pass
    """State 12"""
    return 0

def t309006000_x1():
    """State 0,1"""
    if GetEventFlag(3685) == 1 and not GetEventFlag(31008521):
        """State 2,5"""
        Label('L0')
    elif GetEventFlag(3691) == 1 and not GetEventFlag(31008523):
        """State 3"""
        Goto('L0')
    elif GetEventFlag(3685) == 1 and not GetEventFlag(31009215):
        """State 6,7"""
        # talk:30982100:"There's a special circle, for rotten thieves like you."
        assert t309006000_x87(text1=30982100, mode3=1)
    else:
        """State 4,8"""
        # talk:30982000:"Try not to be so slow on the uptake, eh."
        assert t309006000_x87(text1=30982000, mode3=1)
    """State 9"""
    return 0

def t309006000_x2():
    """State 0"""
    if GetEventFlag(3690) == 1:
        """State 6"""
        """State 7"""
        pass
    elif not GetEventFlag(31002701):
        """State 2,1"""
        SetEventFlag(31002701, 1)
        """State 8"""
        # talk:30980000:"Ngh!"
        assert t309006000_x87(text1=30980000, mode3=1)
    elif not GetEventFlag(31002707):
        """State 3,5"""
        SetEventFlag(31002707, 1)
        """State 9"""
        # talk:30980200:"What's wrong with you?"
        assert t309006000_x87(text1=30980200, mode3=1)
    else:
        """State 4"""
        pass
    """State 10"""
    return 0

def t309006000_x3():
    """State 0"""
    if GetEventFlag(3685) == 1:
        """State 2"""
        call = t309006000_x32()
        if call.Done():
            pass
        elif GetEventFlag(31000800) == 1:
            """State 4"""
            Label('L0')
            assert t309006000_x34()
    elif GetEventFlag(3691) == 1:
        """State 3"""
        call = t309006000_x33()
        if call.Done():
            pass
        elif GetEventFlag(31000850) == 1:
            Goto('L0')
    else:
        Goto('L0')
    """State 1"""
    Quit()
    """Unused"""
    """State 5"""
    return 0

def t309006000_x4():
    """State 0,1"""
    if GetEventFlag(3690) == 1:
        """State 2,5"""
        # talk:30990002:" "
        assert t309006000_x87(text1=30990002, mode3=1)
    else:
        """State 3,4"""
        # talk:30981000:"Well... It was bound to happen some day..."
        def WhilePaused():
            GiveSpEffectToPlayer(9646)
        assert t309006000_x87(text1=30981000, mode3=1) and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 6"""
    return 0

def t309006000_x5(z5=10, z6=12):
    """State 0"""
    while True:
        """State 1"""
        if GetEventFlag(3685) == 1:
            """State 3"""
            call = t309006000_x29(val11=10, z12=12)
            if call.Done():
                break
            elif not GetEventFlag(3685):
                pass
        elif GetEventFlag(3686) == 1:
            """State 4"""
            call = t309006000_x44(val9=10, z10=12)
            if call.Done():
                break
            elif not GetEventFlag(3686):
                pass
        elif GetEventFlag(3687) == 1:
            """State 5"""
            call = t309006000_x45(val8=10, z9=12)
            if call.Done():
                break
            elif not GetEventFlag(3687):
                pass
        elif GetEventFlag(3688) == 1 or GetEventFlag(3693) == 1:
            """State 6"""
            call = t309006000_x46(val7=10, z8=12)
            if call.Done():
                break
            elif not GetEventFlag(3688) and not GetEventFlag(3693):
                pass
        elif GetEventFlag(3689) == 1:
            """State 7"""
            call = t309006000_x47(z14=10, z15=12)
            if call.Done():
                break
            elif not GetEventFlag(3689):
                pass
        elif GetEventFlag(3690) == 1:
            """State 8"""
            call = t309006000_x43(z16=10, z17=12)
            def WhilePaused():
                c5_121(GetEventFlag(1039549206) == 1 and not GetEventFlag(1039549207), 9601)
            if call.Done():
                break
            elif not GetEventFlag(3690):
                pass
        elif GetEventFlag(3691) == 1 or GetEventFlag(3694) == 1:
            """State 9"""
            call = t309006000_x30(val10=10, z11=12)
            if call.Done():
                break
            elif not GetEventFlag(3691) and not GetEventFlag(3694):
                pass
        elif GetEventFlag(3692) == 1:
            """State 10"""
            call = t309006000_x48(val6=10, z7=12)
            if call.Done():
                break
            elif not GetEventFlag(3692):
                pass
        else:
            """State 2"""
            assert GetEventFlagValue(3685, 13) > 1
    """State 11"""
    return 0

def t309006000_x6():
    """State 0,6"""
    assert t309006000_x54()
    """State 1"""
    if not GetEventFlag(31009206):
        """State 3,4"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t309006000_x14()
    else:
        """State 2,5"""
        # talk:30900900:"Don't forget to pop back for another visit, friend."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t309006000_x86(text2=30900900, mode4=1)
    """State 7"""
    return 0

def t309006000_x7():
    """State 0,1"""
    if not GetEventFlag(31009234) and GetEventFlag(31008522) == 1:
        """State 2"""
        if not GetEventFlag(31009231):
            """State 3,16"""
            # talk:30905000:"Ah, oh... How in blazes... You're alive."
            assert t309006000_x86(text2=30905000, mode4=1)
        else:
            """State 4,17"""
            # talk:30905100:"Ah, oh... How in blazes... You're alive."
            assert t309006000_x86(text2=30905100, mode4=1)
        """State 10"""
        SetEventFlag(31009234, 1)
        """State 24"""
        assert t309006000_x53()
        """State 13"""
        Label('L0')
        SetEventFlag(31009207, 0)
        """State 14"""
        Label('L1')
        SetEventFlag(31002708, 1)
    elif not GetEventFlag(31009229) and not GetEventFlag(31008522):
        """State 5,18"""
        # talk:30902000:"Well, nice of you to drop in, finally."
        assert t309006000_x86(text2=30902000, mode4=1)
        """State 11"""
        SetEventFlag(31009229, 1)
        Goto('L0')
    elif GetEventFlag(31002710) == 1 and not GetEventFlag(31002712):
        """State 6,19"""
        # talk:30984100:"So. Do you need something from me?"
        assert t309006000_x86(text2=30984100, mode4=1)
        """State 12"""
        SetEventFlag(31002712, 1)
        Goto('L0')
    elif not GetEventFlag(31002708) and GetEventFlag(31009207) == 1:
        """State 7,20"""
        # talk:30983000:"Well, it looks like you've seen the error of your ways."
        assert t309006000_x86(text2=30983000, mode4=1)
        Goto('L0')
    elif GetEventFlag(31009242) == 1 and GetEventFlag(31009234) == 1 and not GetEventFlag(31002708):
        """State 8,21"""
        # talk:30906000:"Oh yes, by the way. I'm saying goodbye to the old cave."
        assert t309006000_x86(text2=30906000, mode4=1)
        Goto('L1')
    else:
        """State 9,22"""
        assert t309006000_x20(flag9=31002708)
    """State 23"""
    assert t309006000_x38()
    """State 15"""
    assert t309006000_x15()
    """State 25"""
    return 0

def t309006000_x8():
    """State 0,1"""
    if not GetEventFlag(1038419255):
        """State 2,12"""
        # talk:30907000:"Oh, well! It's been a long while."
        assert t309006000_x86(text2=30907000, mode4=1)
        """State 4"""
        SetEventFlag(1038419255, 1)
        """State 9"""
        Label('L0')
        SetEventFlag(1038419265, 0)
        """State 7"""
        SetEventFlag(1037422730, 1)
    elif GetEventFlag(14009300) == 1 and GetEventFlag(1038419259) == 1 and not GetEventFlag(1038419266):
        """State 10,17"""
        # talk:30909000:"Well, fancy meeting you here."
        assert t309006000_x86(text2=30909000, mode4=1)
        """State 11"""
        SetEventFlag(1038419266, 1)
        """State 18"""
        assert t309006000_x53()
        Goto('L0')
    elif GetEventFlag(1037422732) == 1 and not GetEventFlag(1037422734):
        """State 5,15"""
        # talk:30984100:"So. Do you need something from me?"
        assert t309006000_x86(text2=30984100, mode4=1)
        """State 8"""
        SetEventFlag(1037422732, 1)
        Goto('L0')
    elif not GetEventFlag(1037422730) and GetEventFlag(1038419265) == 1:
        """State 6,16"""
        # talk:30983000:"Well, it looks like you've seen the error of your ways."
        assert t309006000_x86(text2=30983000, mode4=1)
        Goto('L0')
    else:
        """State 3,13"""
        assert t309006000_x20(flag9=1037422730)
    """State 14"""
    assert t309006000_x19()
    """State 19"""
    return 0

def t309006000_x9():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(90300, -1)
    assert t309006000_x22()
    """State 2"""
    return 0

def t309006000_x10():
    """State 0,1"""
    if not GetEventFlag(16000800):
        """State 2"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t309006000_x24()
    else:
        """State 3"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t309006000_x25()
    """State 4"""
    return 0

def t309006000_x11():
    """State 0,2"""
    if not GetEventFlag(1039549205):
        """State 3,5"""
        # talk:30916000:"Ah, oh, you again..."
        assert t309006000_x86(text2=30916000, mode4=1)
        """State 1"""
        SetEventFlag(1039549205, 1)
        """State 6"""
        # lot:101810:Dancer's Castanets
        assert t309006000_x59(lot1=101810)
        """State 8"""
        # talk:30916008:"Oh, it's nothing, it's just... Makes me sick to see her all bent out of shape."
        assert t309006000_x86(text2=30916008, mode4=1)
    else:
        """State 4,7"""
        SetEventFlag(1039549206, 1)
        # talk:30916100:"You're able, then?"
        assert t309006000_x86(text2=30916100, mode4=1)
    """State 9"""
    return 0

def t309006000_x12():
    """State 0,12"""
    assert t309006000_x55()
    """State 1"""
    if not GetEventFlag(31009255):
        """State 2,9"""
        # talk:30917500:"Ahhh..."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t309006000_x86(text2=30917500, mode4=1)
        """State 5"""
        SetEventFlag(31009255, 1)
        """State 8"""
        Label('L0')
        SetEventFlag(31009266, 0)
    elif GetEventFlag(31009255) == 1 and GetEventFlag(31009266) == 1:
        """State 7,13"""
        # talk:30983010:"Well, it looks like you've seen the error of your ways."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t309006000_x86(text2=30983010, mode4=1)
        Goto('L0')
    elif not GetEventFlag(31009256):
        """State 3,10"""
        # talk:30917600:"Hell's bells..."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t309006000_x86(text2=30917600, mode4=1)
        """State 6"""
        SetEventFlag(31009256, 1)
    else:
        """State 4,11"""
        # talk:30917700:"...Maybe I'll set up another shop with the lads..."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t309006000_x86(text2=30917700, mode4=1)
    """State 14"""
    return 0

def t309006000_x13():
    """State 0,13"""
    assert t309006000_x51()
    """State 1"""
    ClearTalkActionState()
    c1_110()
    while True:
        """State 2"""
        ClearTalkListData()
        """State 3"""
        # action:20000010:"Purchase"
        AddTalkListData(1, 20000010, -1)
        # action:20000011:"Sell"
        AddTalkListData(2, 20000011, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 9"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 5,10"""
            OpenRegularShop(100100, 100124)
            """State 11"""
            call = t309006000_x21()
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 6,8"""
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        else:
            """State 7,12"""
            assert t309006000_x31()
            """State 14"""
            return 0

def t309006000_x14():
    """State 0,9"""
    # talk:30900600:"Ahhh..."
    assert t309006000_x86(text2=30900600, mode4=1)
    """State 1"""
    ClearTalkListData()
    c1_110()
    """State 2"""
    # action:23091000:"Forgive and forget"
    AddTalkListData(1, 23091000, -1)
    # action:23091001:"Some things can't be forgiven"
    AddTalkListData(2, 23091001, -1)
    """State 3"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 4"""
    if GetTalkListEntryResult() == 1:
        """State 5,10"""
        # talk:30900700:"A true man of reason. Just what I like about you."
        assert t309006000_x86(text2=30900700, mode4=1)
        """State 8"""
        Label('L0')
        SetEventFlag(31009206, 1)
    elif GetTalkListEntryResult() == 2:
        """State 6,11"""
        # talk:30900800:"Slow down, son..."
        assert t309006000_x86(text2=30900800, mode4=1)
        Goto('L0')
    else:
        """State 7"""
        pass
    """State 12"""
    return 0

def t309006000_x15():
    """State 0,1"""
    ClearTalkActionState()
    c1_110()
    while True:
        """State 2"""
        ClearTalkListData()
        """State 14"""
        assert t309006000_x39()
        """State 3"""
        # action:20000010:"Purchase"
        AddTalkListData(1, 20000010, -1)
        # action:20000011:"Sell"
        AddTalkListData(2, 20000011, -1)
        # action:23090000:"About the bandits"
        AddTalkListDataIf(GetEventFlag(31009243) == 1, 3, 23090000, -1)
        # action:23090001:"That chest..."
        AddTalkListDataIf(GetEventFlag(31009244) == 1, 3, 23090001, -1)
        # action:23090002:"Talk"
        AddTalkListDataIf(GetEventFlag(31009245) == 1, 3, 23090002, -1)
        # action:23090003:"What you spoke of before"
        AddTalkListDataIf(GetEventFlag(31009246) == 1, 3, 23090003, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 10"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 5,11"""
            OpenRegularShop(100100, 100124)
            """State 13"""
            call = t309006000_x17()
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 7,6"""
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 8,12"""
            assert t309006000_x16()
        else:
            """State 9,15"""
            assert t309006000_x18()
            """State 16"""
            return 0

def t309006000_x16():
    """State 0,1"""
    if GetEventFlag(31009243) == 1:
        """State 3,11"""
        # talk:30902400:"Yeah, I had those bandits make a clean break."
        assert t309006000_x86(text2=30902400, mode4=1)
        """State 2"""
        SetEventFlag(31009230, 1)
    elif GetEventFlag(31009244) == 1:
        """State 4,12"""
        # talk:30902500:"Hm? Wondering what's inside the treasure chest?"
        assert t309006000_x86(text2=30902500, mode4=1)
        """State 7"""
        SetEventFlag(31009228, 1)
        """State 10"""
        SetEventFlag(31002706, 1)
    elif GetEventFlag(31009245) == 1:
        """State 5,13"""
        # talk:30904100:"By the way, friend..."
        assert t309006000_x86(text2=30904100, mode4=1)
        """State 8"""
        SetEventFlag(31009231, 1)
    else:
        """State 6,14"""
        # talk:30904200:"What's wrong? I've made up my mind."
        assert t309006000_x86(text2=30904200, mode4=1)
        """State 9"""
        SetEventFlag(31009235, 1)
    """State 15"""
    return 0

def t309006000_x17():
    """State 0,1"""
    assert DidYouDoSomethingInTheMenu(0) == 1
    """State 3"""
    SetEventFlag(31009225, 0)
    SetEventFlag(31009226, 0)
    """State 2"""
    if not GetEventFlag(31002705):
        pass
    else:
        Goto('L0')
    """State 6,7"""
    SetEventFlag(31002705, 1)
    """State 8"""
    if not GetEventFlag(31009236):
        """State 9,12"""
        SetEventFlag(31009236, 1)
    elif not GetEventFlag(31009237):
        """State 10,13"""
        SetEventFlag(31009237, 1)
    else:
        """State 11,14"""
        SetEventFlag(31009238, 1)
    """State 15"""
    Quit()
    """State 4"""
    Label('L0')
    """State 5"""
    Quit()
    """Unused"""
    """State 16"""
    return 0

def t309006000_x18():
    """State 0,1"""
    if GetEventFlag(31009226) == 1 and not DidYouDoSomethingInTheMenu(0):
        """State 6,9"""
        # talk:30902300:"Stingy little beggar..."
        assert t309006000_x86(text2=30902300, mode4=1)
    else:
        """State 2"""
        if DidYouDoSomethingInTheMenu(0) == 1:
            """State 3"""
            pass
        elif not GetEventFlag(31009225):
            """State 4,7"""
            SetEventFlag(31009225, 1)
        else:
            """State 5,8"""
            SetEventFlag(31009226, 1)
        """State 10"""
        # talk:30902200:"Cheers for that."
        assert t309006000_x86(text2=30902200, mode4=1)
    """State 11"""
    return 0

def t309006000_x19():
    """State 0,1"""
    c1_110()
    ClearTalkActionState()
    while True:
        """State 2"""
        ClearTalkListData()
        """State 15"""
        assert t309006000_x40()
        """State 3"""
        # action:20000010:"Purchase"
        AddTalkListData(1, 20000010, -1)
        # action:20000011:"Sell"
        AddTalkListData(2, 20000011, -1)
        # action:23090004:"Speaking of..."
        AddTalkListDataIf(not GetEventFlag(1038419258), 3, 23090004, -1)
        # action:23090006:"Talk"
        AddTalkListDataIf(GetEventFlag(1038419262) == 1, 4, 23090006, -1)
        # action:23090007:"What you spoke of before"
        AddTalkListDataIf(GetEventFlag(1038419263) == 1, 4, 23090007, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 10"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 5,11"""
            OpenRegularShop(100100, 100124)
            """State 14"""
            call = t309006000_x21()
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 6,9"""
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 7,18"""
            # talk:30907300:"By the way, have you met that girl Rya?"
            assert t309006000_x86(text2=30907300, mode4=1)
            """State 13"""
            SetEventFlag(1038419258, 1)
        elif GetTalkListEntryResult() == 4:
            """State 12,16"""
            assert t309006000_x41()
        else:
            """State 8,17"""
            assert t309006000_x18()
            """State 19"""
            return 0

def t309006000_x20(flag9=_):
    """State 0,1"""
    if not GetEventFlag(flag9):
        """State 2,5"""
        # talk:30902100:"Hello, again. Welcome to Patches' Emporium."
        assert t309006000_x86(text2=30902100, mode4=1)
        """State 4"""
        SetEventFlag(flag9, 1)
    else:
        """State 3,6"""
        # talk:30902600:"Forgot something on your shopping list?"
        assert t309006000_x86(text2=30902600, mode4=1)
    """State 7"""
    return 0

def t309006000_x21():
    """State 0,1"""
    assert DidYouDoSomethingInTheMenu(0) == 1
    """State 2"""
    SetEventFlag(31009225, 0)
    SetEventFlag(31009226, 0)
    """State 3"""
    Quit()
    """Unused"""
    """State 4"""
    return 0

def t309006000_x22():
    """State 0,1"""
    if not GetEventFlag(1037549206):
        """State 2,7"""
        # talk:30910100:"Oh, erm, hello, yes."
        assert t309006000_x86(text2=30910100, mode4=1)
        """State 4"""
        SetEventFlag(1037549206, 1)
        """State 6"""
        Label('L0')
        SetEventFlag(1037549209, 0)
    elif GetEventFlag(1037549206) == 1 and GetEventFlag(1037549209) == 1:
        """State 5,8"""
        # talk:30983010:"Well, it looks like you've seen the error of your ways."
        assert t309006000_x86(text2=30983010, mode4=1)
        Goto('L0')
    else:
        """State 3,9"""
        # talk:30910200:"What is it? Oh, don't mind me. Off you trot."
        assert t309006000_x86(text2=30910200, mode4=1)
    """State 10"""
    return 0

def t309006000_x23():
    """State 0,1"""
    if not GetEventFlag(1037549207):
        """State 2,7"""
        # talk:30911000:"Oh, my, well, here you are again."
        assert t309006000_x86(text2=30911000, mode4=1)
        """State 5"""
        SetEventFlag(1037549207, 1)
        """State 10"""
        assert t309006000_x53()
        """State 6"""
        Label('L0')
        SetEventFlag(1037549209, 0)
    elif GetEventFlag(1037549207) == 1 and GetEventFlag(1037549209) == 1:
        """State 3,8"""
        # talk:30983010:"Well, it looks like you've seen the error of your ways."
        assert t309006000_x86(text2=30983010, mode4=1)
        Goto('L0')
    else:
        """State 4,9"""
        # talk:30911005:"Stay clear of Volcano Manor, end of discussion."
        assert t309006000_x86(text2=30911005, mode4=1)
    """State 11"""
    return 0

def t309006000_x24():
    """State 0,1"""
    if not GetEventFlag(16009355) and not GetEventFlag(16009207):
        """State 2,10"""
        # talk:30912010:"Well, you've joined the Manor, eh?"
        assert t309006000_x86(text2=30912010, mode4=1)
        """State 6"""
        Label('L0')
        SetEventFlag(16009355, 1)
    elif not GetEventFlag(16009355) and GetEventFlag(16009207) == 1:
        """State 3,11"""
        # talk:30912000:"Well, you've joined the Manor, eh?"
        assert t309006000_x86(text2=30912000, mode4=1)
        Goto('L0')
    elif GetEventFlag(16009356) == 1 and GetEventFlag(16009216) == 1 and not GetEventFlag(16009357):
        """State 8,15"""
        assert t309006000_x28()
    elif not GetEventFlag(16009356):
        """State 4,12"""
        # talk:30912100:"Oh, and of course, we can do business, if you like."
        assert t309006000_x86(text2=30912100, mode4=1)
        """State 7"""
        SetEventFlag(16009356, 1)
        """State 9"""
        SetEventFlag(16002720, 1)
        """State 13"""
        Label('L1')
        assert t309006000_x26()
    else:
        """State 5,14"""
        assert t309006000_x20(flag9=16002720)
        Goto('L1')
    """State 16"""
    return 0

def t309006000_x25():
    """State 0,1"""
    if not GetEventFlag(16009359):
        """State 2,6"""
        # talk:30915000:"Now you've gone and killed Rykard?"
        assert t309006000_x86(text2=30915000, mode4=1)
        """State 4"""
        SetEventFlag(16009359, 1)
    else:
        """State 3,5"""
        # talk:30915100:"What is it?"
        assert t309006000_x86(text2=30915100, mode4=1)
        """State 7"""
        assert t309006000_x26()
    """State 8"""
    return 0

def t309006000_x26():
    """State 0,1"""
    c1_110()
    ClearTalkActionState()
    while True:
        """State 2"""
        ClearTalkListData()
        """State 15"""
        assert t309006000_x42()
        """State 3"""
        # action:20000010:"Purchase"
        AddTalkListData(1, 20000010, -1)
        # action:20000011:"Sell"
        AddTalkListData(2, 20000011, -1)
        # action:23090008:"About the previous request"
        AddTalkListDataIf(GetEventFlag(16009362) == 1, 3, 23090008, -1)
        # action:23090009:"About the previous request"
        AddTalkListDataIf(GetEventFlag(16009363) == 1, 3, 23090009, -1)
        # action:23090010:"The request is done"
        AddTalkListDataIf(GetEventFlag(16009364) == 1, 3, 23090010, -1)
        # action:23090011:"About Patches"
        AddTalkListDataIf(GetEventFlag(16009365) == 1, 3, 23090011, -1)
        # action:23090012:"What about my reward?"
        AddTalkListDataIf(GetEventFlag(16009366) == 1, 3, 23090012, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 10"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 5,11"""
            OpenRegularShop(100100, 100124)
            """State 12"""
            call = t309006000_x21()
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 6,9"""
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 7,14"""
            assert t309006000_x27()
        else:
            """State 8,13"""
            assert t309006000_x18()
            """State 16"""
            return 0

def t309006000_x27():
    """State 0,1"""
    if GetEventFlag(16009362) == 1:
        """State 2,11"""
        # talk:30913200:"What's the matter? Having trouble nabbing your prey?"
        assert t309006000_x86(text2=30913200, mode4=1)
        """State 7"""
        Label('L0')
        SetEventFlag(16009360, 1)
    elif GetEventFlag(16009363) == 1:
        """State 3,12"""
        # talk:30913300:"What's the matter? Having trouble nabbing your prey?"
        assert t309006000_x86(text2=30913300, mode4=1)
        Goto('L0')
    elif GetEventFlag(16009364) == 1:
        """State 4,13"""
        # talk:30913400:"You hunted down Tragoth?"
        assert t309006000_x86(text2=30913400, mode4=1)
        """State 6"""
        SetEventFlag(16009358, 1)
        SetEventFlag(16002721, 1)
    elif GetEventFlag(16009366) == 1:
        """State 5,14"""
        # talk:30913600:"Hmph."
        assert t309006000_x86(text2=30913600, mode4=1)
        """State 8"""
        SetEventFlag(16009367, 1)
        """State 16"""
        # lot:101820:Magma Whip Candlestick
        assert t309006000_x59(lot1=101820)
    else:
        """State 9,15"""
        # talk:30913500:"Are you surprised? That I belong to the Volcano Manor."
        assert t309006000_x86(text2=30913500, mode4=1)
        """State 10"""
        SetEventFlag(16009361, 1)
    """State 17"""
    return 0

def t309006000_x28():
    """State 0,2"""
    # talk:30913000:"Ahh, hello, what impeccable timing."
    assert t309006000_x86(text2=30913000, mode4=1)
    """State 1"""
    SetEventFlag(16009357, 1)
    """State 3"""
    # lot:101800:Letter to Patches
    assert t309006000_x59(lot1=101800)
    """State 4"""
    # talk:30913100:"You're new here at the Manor."
    assert t309006000_x86(text2=30913100, mode4=1)
    """State 5"""
    return 0

def t309006000_x29(val11=10, z12=12):
    """State 0"""
    while True:
        """State 5"""
        # actionbutton:6000:"Talk"
        call = t309006000_x56(actionbutton1=6000, flag5=6001, flag10=6000, flag11=6000, flag12=6000,
                              flag13=6000, flag4=6000)
        if call.Done():
            break
        elif (GetEventFlag(31009211) == 1 and GetEventFlag(31009215) == 1 and not GetEventFlag(31009214)
              and GetDistanceToPlayer() < val11):
            """State 1,2"""
            SetEventFlag(31009214, 1)
            """State 6"""
            # talk:30900500:"Well, finally come around, have you?"
            def WhilePaused():
                GiveSpEffectToPlayer(9646)
            def ExitPause():
                SetEventFlag(31009217, 1)
            assert t309006000_x87(text1=30900500, mode3=1) and CheckSpecificPersonTalkHasEnded(2) == 1
        elif GetEventFlag(31002709) == 1 and not GetEventFlag(31002710) and GetDistanceToPlayer() < 5:
            """State 3,4"""
            SetEventFlag(31002710, 1)
            """State 7"""
            # talk:30984000:"Okay, I can see you mean it."
            assert t309006000_x87(text1=30984000, mode3=1)
    """State 8"""
    return 0

def t309006000_x30(val10=10, z11=12):
    """State 0"""
    while True:
        """State 5"""
        # actionbutton:6000:"Talk"
        call = t309006000_x56(actionbutton1=6000, flag5=6001, flag10=6000, flag11=6000, flag12=6000,
                              flag13=6000, flag4=6000)
        if call.Done():
            break
        elif (GetEventFlag(31002724) == 1 and GetEventFlag(31002728) == 1 and not GetEventFlag(31002727)
              and GetDistanceToPlayer() < val10 and not GetEventFlag(31009267)):
            """State 1,2"""
            SetEventFlag(31002727, 1)
            """State 6"""
            # talk:30917400:"Well, glad to see we're on the same page."
            def WhilePaused():
                GiveSpEffectToPlayer(9646)
            def ExitPause():
                SetEventFlag(31009267, 1)
            assert t309006000_x87(text1=30917400, mode3=1) and CheckSpecificPersonTalkHasEnded(0) == 1
        elif GetEventFlag(31002709) == 1 and not GetEventFlag(31002710) and GetDistanceToPlayer() < 5:
            """State 3,4"""
            SetEventFlag(31002710, 1)
            """State 7"""
            # talk:30984000:"Okay, I can see you mean it."
            assert t309006000_x87(text1=30984000, mode3=1)
    """State 8"""
    return 0

def t309006000_x31():
    """State 0,1"""
    if GetEventFlag(31009226) == 1 and not DidYouDoSomethingInTheMenu(0):
        """State 6,9"""
        # talk:30919300:"What, do I have to beg?"
        assert t309006000_x86(text2=30919300, mode4=1)
    else:
        """State 2"""
        if DidYouDoSomethingInTheMenu(0) == 1:
            """State 3"""
            pass
        elif not GetEventFlag(31009225):
            """State 4,7"""
            SetEventFlag(31009225, 1)
        else:
            """State 5,8"""
            SetEventFlag(31009226, 1)
        """State 10"""
        # talk:30919200:"Cheers for that."
        assert t309006000_x86(text2=30919200, mode4=1)
    """State 11"""
    return 0

def t309006000_x32():
    """State 0"""
    while True:
        """State 5"""
        if not GetEventFlag(31009210) and GetEventFlag(31008521) == 1:
            """State 1"""
            assert GetCurrentStateElapsedTime() > 2.5
            """State 2"""
            SetEventFlag(31009210, 1)
            """State 15"""
            # talk:30900100:"Well, well, well?"
            assert (t309006000_x87(text1=30900100, mode3=1) and (CheckSpecificPersonTalkHasEnded(2) ==
                    1 or GetEventFlag(31002704) == 1))
            """State 3,4"""
            SetEventFlag(31009208, 1)
        elif GetEventFlag(31002704) == 1 and not GetEventFlag(31009211):
            """State 6,7"""
            SetEventFlag(31009211, 1)
            """State 16"""
            # talk:30900200:"Wait, wait, please!"
            assert t309006000_x87(text1=30900200, mode3=1)
            """State 9"""
            assert GetCurrentStateElapsedTime() > 2
            """State 8"""
            RemoveMyAggro()
            """State 10"""
            SetEventFlag(31002703, 1)
        elif not GetEventFlag(31009213) and GetEventFlag(31002713) == 1:
            """State 12,14"""
            SetEventFlag(31009213, 1)
            """State 18"""
            # talk:30900400:"Cripes, are you dense, boy?"
            assert t309006000_x87(text1=30900400, mode3=1)
        elif (not GetEventFlag(31009212) and GetEventFlag(31009211) == 1 and IsPlayerAttacking() == 1
              and not GetEventFlag(31009213)):
            """State 11,13"""
            SetEventFlag(31009212, 1)
            """State 17"""
            # talk:30900300:"For Pete's sake! I concede!"
            assert t309006000_x87(text1=30900300, mode3=1)
    """Unused"""
    """State 19"""
    return 0

def t309006000_x33():
    """State 0"""
    while True:
        """State 1"""
        if not GetEventFlag(31009258) and GetEventFlag(31008523) == 1:
            """State 2"""
            assert GetCurrentStateElapsedTime() > 2.5
            """State 3"""
            SetEventFlag(31009258, 1)
            """State 16"""
            # talk:30917000:"Well, well, well?"
            assert (t309006000_x87(text1=30917000, mode3=1) and (CheckSpecificPersonTalkHasEnded(0) ==
                    1 or GetEventFlag(31002721) == 1))
        elif GetEventFlag(31009258) == 1 and not GetEventFlag(31009257):
            """State 15"""
            pass
        elif GetEventFlag(31002721) == 1 and not GetEventFlag(31002724):
            """State 6,7"""
            SetEventFlag(31002724, 1)
            """State 17"""
            # talk:30917100:"Hm? Wait, don't tell me, is that you?"
            assert t309006000_x87(text1=30917100, mode3=1) and CheckSpecificPersonTalkHasEnded(0) == 1
            """State 8"""
            SetEventFlag(31002730, 1)
            """State 18"""
            # talk:30917105:"I surrender! I surrender, I swear!"
            assert t309006000_x87(text1=30917105, mode3=1) and GetCurrentStateElapsedTime() > 0.5
            """State 9"""
            RemoveMyAggro()
            """State 10"""
            SetEventFlag(31002720, 1)
            continue
        elif not GetEventFlag(31002726) and GetEventFlag(31002722) == 1:
            """State 11,12"""
            SetEventFlag(31002726, 1)
            """State 19"""
            # talk:30917300:"Cripes! Are you dense, mate?"
            assert t309006000_x87(text1=30917300, mode3=1)
            continue
        elif (not GetEventFlag(31002725) and GetEventFlag(31002724) == 1 and IsPlayerAttacking() == 1
              and not GetEventFlag(31002726)):
            """State 13,14"""
            SetEventFlag(31002725, 1)
            """State 20"""
            # talk:30917200:"Do you even hear me? I said "surrender", loud and clear!"
            assert t309006000_x87(text1=30917200, mode3=1)
            continue
        """State 4,5"""
        SetEventFlag(31009257, 1)
    """Unused"""
    """State 21"""
    return 0

def t309006000_x34():
    """State 0"""
    while True:
        """State 2"""
        if not GetEventFlag(31009205):
            """State 3,6"""
            SetEventFlag(31009205, 1)
            """State 5"""
            SetEventFlag(31002700, 1)
            """State 8"""
            # talk:30980300:"Ugh. Hard of hearing, are we?"
            assert t309006000_x87(text1=30980300, mode3=1) and CheckSpecificPersonTalkHasEnded(2) == 1
            """State 7"""
            assert GetCurrentStateElapsedTime() > 3 and GetPlayerRemainingHP() < 30
        elif GetPlayerRemainingHP() < 30:
            """State 4,9"""
            assert t309006000_x49()
            """State 1"""
            Quit()
    """Unused"""
    """State 10"""
    return 0

def t309006000_x35():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(90300, -1)
    assert t309006000_x8()
    """State 2"""
    return 0

def t309006000_x36():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(90315, -1)
        c5_121(GetEventFlag(1039549206) == 1 and not GetEventFlag(1039549207), 9601)
    assert t309006000_x11()
    """State 2"""
    return 0

def t309006000_x37():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(90300, -1)
    assert t309006000_x12()
    """State 2"""
    return 0

def t309006000_x38():
    """State 0,1"""
    if not GetEventFlag(31009240):
        """State 2,5"""
        SetEventFlag(31009240, 1)
    elif not GetEventFlag(31009241):
        """State 3,6"""
        SetEventFlag(31009241, 1)
    else:
        """State 4,7"""
        SetEventFlag(31009242, 1)
    """State 8"""
    return 0

def t309006000_x39():
    """State 0,7"""
    SetEventFlag(31009243, 0)
    SetEventFlag(31009244, 0)
    SetEventFlag(31009245, 0)
    SetEventFlag(31009246, 0)
    """State 1"""
    if not GetEventFlag(31009230):
        """State 2"""
        SetEventFlag(31009243, 1)
    elif not GetEventFlag(31008522) and GetEventFlag(31009230) == 1 and not GetEventFlag(31009228):
        """State 3"""
        SetEventFlag(31009244, 1)
    elif (not GetEventFlag(31008522) and GetEventFlag(31009242) == 1 and GetEventFlag(31009228) == 1
          and not GetEventFlag(31009231) and not GetEventFlag(31002706)):
        """State 4"""
        SetEventFlag(31009245, 1)
    elif not GetEventFlag(31008522) and GetEventFlag(31009231) == 1:
        """State 5"""
        SetEventFlag(31009246, 1)
    else:
        """State 6"""
        pass
    """State 8"""
    return 0

def t309006000_x40():
    """State 0,3"""
    SetEventFlag(1038419262, 0)
    SetEventFlag(1038419263, 0)
    """State 1"""
    if not GetEventFlag(1038419259) and not GetEventFlag(14009300):
        """State 2"""
        SetEventFlag(1038419262, 1)
    elif GetEventFlag(1038419259) == 1 and not GetEventFlag(14009300):
        """State 5"""
        SetEventFlag(1038419263, 1)
    else:
        """State 4"""
        pass
    """State 6"""
    return 0

def t309006000_x41():
    """State 0,1"""
    if GetEventFlag(1038419262) == 1:
        """State 2,5"""
        # talk:30908100:"You're...making your way to the Erdtree, no?"
        assert t309006000_x86(text2=30908100, mode4=1)
        """State 4"""
        SetEventFlag(1038419259, 1)
    else:
        """State 3,6"""
        # talk:30908200:"Oh yeah, great story isn't it. I'll tell you as many times as you like."
        assert t309006000_x86(text2=30908200, mode4=1)
    """State 7"""
    return 0

def t309006000_x42():
    """State 0,7"""
    SetEventFlag(16009362, 0)
    SetEventFlag(16009363, 0)
    SetEventFlag(16009364, 0)
    SetEventFlag(16009365, 0)
    SetEventFlag(16009366, 0)
    """State 1"""
    if not GetEventFlag(16009367) and GetEventFlag(16009358) == 1 and not GetEventFlag(16002721):
        """State 9"""
        SetEventFlag(16009366, 1)
    elif GetEventFlag(16000800) == 1:
        """State 8"""
        pass
    elif (GetEventFlag(16009357) == 1 and GetEventFlag(39209201) == 1 and not GetEventFlag(7606) and
          not GetEventFlag(3448) and not GetEventFlag(3449)):
        """State 2"""
        SetEventFlag(16009362, 1)
    elif (GetEventFlag(16009357) == 1 and GetEventFlag(39209201) == 1 and not GetEventFlag(7606) and
          (GetEventFlag(3448) == 1 or GetEventFlag(3449) == 1)):
        """State 3"""
        SetEventFlag(16009363, 1)
    elif GetEventFlag(7606) == 1 and not GetEventFlag(16009358):
        """State 4"""
        SetEventFlag(16009364, 1)
    elif not GetEventFlag(16009361):
        """State 5"""
        SetEventFlag(16009365, 1)
    else:
        """State 6"""
        pass
    """State 10"""
    return 0

def t309006000_x43(z16=10, z17=12):
    """State 0,5"""
    # actionbutton:6000:"Talk"
    call = t309006000_x56(actionbutton1=6000, flag5=6001, flag10=6000, flag11=6000, flag12=6000, flag13=6000,
                          flag4=6000)
    if call.Done():
        """State 6"""
        return 0
    elif GetEventFlag(1039549206) == 1:
        """State 1"""
        assert DoesSelfHaveSpEffect(9602) == 1
        """State 3"""
        SetEventFlag(1039549207, 1)
    elif GetEventFlag(1039549207) == 1:
        """State 4"""
        pass
    """State 2"""
    Quit()

def t309006000_x44(val9=10, z10=12):
    """State 0"""
    while True:
        """State 3"""
        # actionbutton:6000:"Talk"
        call = t309006000_x56(actionbutton1=6000, flag5=6001, flag10=6000, flag11=6000, flag12=6000,
                              flag13=6000, flag4=6000)
        if call.Done():
            break
        elif GetEventFlag(31002709) == 1 and not GetEventFlag(31002710) and GetDistanceToPlayer() < val9:
            """State 1,2"""
            SetEventFlag(31002710, 1)
            """State 4"""
            # talk:30984000:"Okay, I can see you mean it."
            assert t309006000_x87(text1=30984000, mode3=1)
    """State 5"""
    return 0

def t309006000_x45(val8=10, z9=12):
    """State 0"""
    while True:
        """State 3"""
        # actionbutton:6000:"Talk"
        call = t309006000_x56(actionbutton1=6000, flag5=6001, flag10=6000, flag11=6000, flag12=6000,
                              flag13=6000, flag4=6000)
        if call.Done():
            break
        elif GetEventFlag(1037422731) == 1 and not GetEventFlag(1037422732) and GetDistanceToPlayer() < val8:
            """State 1,2"""
            SetEventFlag(1037422732, 1)
            """State 4"""
            # talk:30984000:"Okay, I can see you mean it."
            assert t309006000_x87(text1=30984000, mode3=1)
    """State 5"""
    return 0

def t309006000_x46(val7=10, z8=12):
    """State 0"""
    while True:
        """State 3"""
        # actionbutton:6000:"Talk"
        call = t309006000_x56(actionbutton1=6000, flag5=6001, flag10=6000, flag11=6000, flag12=6000,
                              flag13=6000, flag4=6000)
        if call.Done():
            break
        elif GetEventFlag(1037542701) == 1 and not GetEventFlag(1037542702) and GetDistanceToPlayer() < val7:
            """State 1,2"""
            SetEventFlag(1037542702, 1)
            """State 4"""
            # talk:30984000:"Okay, I can see you mean it."
            assert t309006000_x87(text1=30984000, mode3=1)
    """State 5"""
    return 0

def t309006000_x47(z14=10, z15=12):
    """State 0,1"""
    # actionbutton:6000:"Talk"
    assert (t309006000_x56(actionbutton1=6000, flag5=6001, flag10=6000, flag11=6000, flag12=6000, flag13=6000,
            flag4=6000))
    """State 2"""
    return 0

def t309006000_x48(val6=10, z7=12):
    """State 0"""
    while True:
        """State 3"""
        # actionbutton:6000:"Talk"
        call = t309006000_x56(actionbutton1=6000, flag5=6001, flag10=6000, flag11=6000, flag12=6000,
                              flag13=6000, flag4=6000)
        if call.Done():
            break
        elif GetEventFlag(31002709) == 1 and not GetEventFlag(31002710) and GetDistanceToPlayer() < val6:
            """State 1,2"""
            SetEventFlag(31002710, 1)
            """State 4"""
            # talk:30984000:"Okay, I can see you mean it."
            assert t309006000_x87(text1=30984000, mode3=1)
    """State 5"""
    return 0

def t309006000_x49():
    """State 0,1"""
    if ((GetEventFlag(3685) == 1 or GetEventFlag(3686) == 1 or GetEventFlag(3691) == 1 or GetEventFlag(3692)
        == 1 or GetEventFlag(3694) == 1) and not GetEventFlag(31002711) and not GetEventFlag(31002710)):
        """State 2,5"""
        SetEventFlag(31002711, 1)
        """State 9"""
        Label('L0')
        # talk:30980600:"Last chance to surrender, mate."
        def ExitPause():
            SetEventFlagIf(GetEventFlag(31002711) == 1, 31009218, 1)
            SetEventFlagIf(GetEventFlag(1037422733) == 1, 1038419267, 1)
            SetEventFlagIf(GetEventFlag(1037542703) == 1, 1037549213, 1)
        assert (t309006000_x87(text1=30980600, mode3=1) and (CheckSpecificPersonTalkHasEnded(2) == 1
                or GetEventFlag(31002709) == 1 or GetEventFlag(1037422731) == 1 or GetEventFlag(1037542701)
                == 1))
    elif GetEventFlag(3687) == 1 and not GetEventFlag(1037422733) and not GetEventFlag(1037422732):
        """State 3,6"""
        SetEventFlag(1037422733, 1)
        Goto('L0')
    elif ((GetEventFlag(3688) == 1 or GetEventFlag(3693) == 1) and not GetEventFlag(1037542703) and not
          GetEventFlag(1037542702)):
        """State 4,7"""
        SetEventFlag(1037542703, 1)
        Goto('L0')
    else:
        """State 8"""
        pass
    """State 10"""
    return 0

def t309006000_x50():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(90300, -1)
    assert t309006000_x7()
    """State 2"""
    return 0

def t309006000_x51():
    """State 0,1"""
    if not GetEventFlag(31009275):
        """State 2,11"""
        # talk:30919000:"Well, finally made it, eh, and just in time."
        assert t309006000_x86(text2=30919000, mode4=1)
        """State 7"""
        SetEventFlag(31009275, 1)
        """State 9"""
        Label('L0')
        SetEventFlag(31009266, 0)
        """State 10"""
        Label('L1')
        SetEventFlag(31002708, 1)
    elif GetEventFlag(31002710) == 1 and not GetEventFlag(31002712):
        """State 3,12"""
        # talk:30984100:"So. Do you need something from me?"
        assert t309006000_x86(text2=30984100, mode4=1)
        """State 8"""
        SetEventFlag(31002712, 1)
        Goto('L0')
    elif not GetEventFlag(31002708) and GetEventFlag(31009266) == 1:
        """State 4,13"""
        # talk:30983000:"Well, it looks like you've seen the error of your ways."
        assert t309006000_x86(text2=30983000, mode4=1)
        Goto('L0')
    elif not GetEventFlag(31002708):
        """State 5,14"""
        # talk:30919100:"Hello, again. Welcome to Patches' Emporium."
        assert t309006000_x86(text2=30919100, mode4=1)
        Goto('L1')
    else:
        """State 6,15"""
        # talk:30919400:"Forgot something on your shopping list?"
        assert t309006000_x86(text2=30919400, mode4=1)
    """State 16"""
    return 0

def t309006000_x52():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(90305, -1)
    assert t309006000_x23()
    """State 2"""
    return 0

def t309006000_x53():
    """State 0,1"""
    if not GetEventFlag(60816):
        """State 2,4"""
        SetEventFlag(60816, 1)
        """State 5"""
        # gesture:25:Calm Down!
        AcquireGesture(25)
    else:
        """State 3"""
        pass
    """State 6"""
    return 0

def t309006000_x54():
    """State 0,1"""
    if not GetEventFlag(60819):
        """State 2,5"""
        SetEventFlag(60819, 1)
        """State 4"""
        # gesture:41:Grovel For Mercy
        AcquireGesture(41)
        assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    else:
        """State 3"""
        pass
    """State 6"""
    return 0

def t309006000_x55():
    """State 0,1"""
    if not GetEventFlag(60832):
        """State 2,5"""
        SetEventFlag(60832, 1)
        """State 4"""
        # gesture:90:Patches' Crouch
        AcquireGesture(90)
        assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    else:
        """State 3"""
        pass
    """State 6"""
    return 0

def t309006000_x56(actionbutton1=6000, flag5=6001, flag10=6000, flag11=6000, flag12=6000, flag13=6000,
                   flag4=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag5) == 1 or GetEventFlag(flag10) == 1 or GetEventFlag(flag11) == 1 or
                GetEventFlag(flag12) == 1 or GetEventFlag(flag13) == 1)
        """State 4"""
        assert not GetEventFlag(flag4)
        """State 2"""
        if GetEventFlag(flag4) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag5) and not GetEventFlag(flag10) and not GetEventFlag(flag11) and not
              GetEventFlag(flag12) and not GetEventFlag(flag13)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t309006000_x57():
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

def t309006000_x58():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t309006000_x59(lot1=_):
    """State 0,1"""
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t309006000_x60(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t309006000_x76()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t309006000_x57()
    else:
        """State 4,7"""
        call = t309006000_x89()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t309006000_x57()
    """State 9"""
    return 0

def t309006000_x61():
    """State 0,1"""
    assert t309006000_x57()
    """State 2"""
    return 0

def t309006000_x62(flag1=3683, flag2=3681, flag3=3682, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t309006000_x79(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t309006000_x78()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t309006000_x63(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                   flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                   mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t309006000_x66(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t309006000_x70(val1=val1, z1=z1)
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
            call = t309006000_x72(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t309006000_x83() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t309006000_x68(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t309006000_x64(val2=10, val3=12):
    """State 0,1"""
    call = t309006000_x74(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t309006000_x60(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t309006000_x65(flag1=3683, val2=10, val3=12):
    """State 0,8"""
    assert t309006000_x91()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t309006000_x77()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t309006000_x57()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t309006000_x66(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t309006000_x67(z13=2000, val12=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t309006000_x56(actionbutton1=actionbutton1, flag5=flag5, flag10=6000, flag11=6000, flag12=6000,
                flag13=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t309006000_x67(z13=_, val12=_):
    """State 0,1"""
    if f203(z13) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z13)
        assert f202() == val12
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t309006000_x68(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t309006000_x57()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t309006000_x69()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t309006000_x84()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t309006000_x69():
    """State 0,1"""
    assert t309006000_x67(z13=1101, val12=1101)
    """State 2"""
    return 0

def t309006000_x70(val1=5, z1=1):
    """State 0,2"""
    assert t309006000_x80()
    """State 1"""
    call = t309006000_x71()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t309006000_x82()
    """State 4"""
    return 0

def t309006000_x71():
    """State 0,1"""
    assert t309006000_x67(z13=1000, val12=1000)
    """State 2"""
    return 0

def t309006000_x72(val5=12):
    """State 0,1"""
    call = t309006000_x73()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t309006000_x83()
    """State 3"""
    return 0

def t309006000_x73():
    """State 0,1"""
    assert t309006000_x67(z13=1100, val12=1100)
    """State 2"""
    return 0

def t309006000_x74(val2=10, val3=12):
    """State 0,5"""
    assert t309006000_x91()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t309006000_x75()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t309006000_x85()
    """Unused"""
    """State 6"""
    return 0

def t309006000_x75():
    """State 0,2"""
    call = t309006000_x67(z13=1102, val12=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t309006000_x76():
    """State 0,1"""
    assert t309006000_x67(z13=1001, val12=1001)
    """State 2"""
    return 0

def t309006000_x77():
    """State 0,1"""
    assert t309006000_x67(z13=1103, val12=1103)
    """State 2"""
    return 0

def t309006000_x78():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t309006000_x79(flag1=3683, flag2=3681, flag3=3682, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t309006000_x63(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                              flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                              z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t309006000_x65(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t309006000_x64(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t309006000_x90() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t309006000_x80():
    """State 0,1"""
    assert t309006000_x81()
    """State 2"""
    return 0

def t309006000_x81():
    """State 0,1"""
    assert t309006000_x67(z13=1104, val12=1104)
    """State 2"""
    return 0

def t309006000_x82():
    """State 0,1"""
    call = t309006000_x67(z13=1201, val12=1201)
    if call.Get() == 1:
        """State 2"""
        assert t309006000_x61()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t309006000_x83():
    """State 0,1"""
    call = t309006000_x67(z13=1300, val12=1300)
    if call.Get() == 1:
        """State 2"""
        assert t309006000_x61()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t309006000_x84():
    """State 0,1"""
    call = t309006000_x67(z13=1301, val12=1301)
    if call.Get() == 1:
        """State 2"""
        assert t309006000_x61()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t309006000_x85():
    """State 0,1"""
    call = t309006000_x67(z13=1302, val12=1302)
    if call.Get() == 1:
        """State 2"""
        assert t309006000_x61()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t309006000_x86(text2=_, mode4=1):
    """State 0,4"""
    assert t309006000_x58() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t309006000_x87(text1=_, mode3=1):
    """State 0,4"""
    assert t309006000_x88() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t309006000_x88():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t309006000_x89():
    """State 0,1"""
    assert t309006000_x67(z13=1002, val12=1002)
    """State 2"""
    return 0

def t309006000_x90():
    """State 0,1"""
    assert t309006000_x57()
    """State 2"""
    return 0

def t309006000_x91():
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

