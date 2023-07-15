# -*- coding: utf-8 -*-
def t319006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t319006000_x43(flag1=4043, flag2=4041, flag3=4042, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1)
    Quit()

def t319006000_1000():
    """State 0,2,3"""
    assert t319006000_x0()
    """State 1"""
    c1_120(1000)
    Quit()

def t319006000_1001():
    """State 0,2,3"""
    assert t319006000_x1()
    """State 1"""
    c1_120(1001)
    Quit()

def t319006000_1101():
    """State 0,2,3"""
    assert t319006000_x2()
    """State 1"""
    c1_120(1101)
    Quit()

def t319006000_1102():
    """State 0,2,3"""
    t319006000_x3()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t319006000_1103():
    """State 0,2,3"""
    assert t319006000_x4()
    """State 1"""
    c1_120(1103)
    Quit()

def t319006000_2000():
    """State 0,2,3"""
    assert t319006000_x5(z5=10, z6=12)
    """State 1"""
    c1_120(2000)
    Quit()

def t319006000_x0():
    """State 0,1"""
    if GetEventFlag(4045) == 1:
        """State 4"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t319006000_x6()
    elif GetEventFlag(4046) == 1:
        """State 3"""
        def WhilePaused():
            RequestAnimation(90305, -1)
        assert t319006000_x7()
    elif GetEventFlag(4047) == 1:
        """State 5"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t319006000_x21()
    else:
        """State 2"""
        pass
    """State 6"""
    return 0

def t319006000_x1():
    """State 0,1"""
    # talk:31980200:"I swear, there's a blight spreading amongst the Tarnished."
    t319006000_x70(text1=31980200, mode3=1)
    Quit()
    """Unused"""
    """State 2"""
    return 0

def t319006000_x2():
    """State 0,1"""
    if GetEventFlag(4046) == 1:
        """State 3"""
        assert t319006000_x30(flag9=1045392700, flag10=1045392701)
    else:
        """State 2"""
        assert t319006000_x30(flag9=1044392700, flag10=1044392701)
    """State 4"""
    return 0

def t319006000_x3():
    """State 0,2,3"""
    if GetEventFlag(4046) == 1:
        """State 5"""
        assert t319006000_x11(flag11=1045399202)
    else:
        """State 4"""
        assert t319006000_x11(flag11=1044399202)
    """State 1"""
    Quit()
    """Unused"""
    """State 6"""
    return 0

def t319006000_x4():
    """State 0,1"""
    # talk:31980300:"How could this...happen...?"
    t319006000_x70(text1=31980300, mode3=1)
    Quit()
    """Unused"""
    """State 2"""
    return 0

def t319006000_x5(z5=10, z6=12):
    """State 0,3"""
    if GetEventFlag(4045) == 1:
        """State 1,5"""
        Label('L0')
        call = t319006000_x10(z5=z5, z6=z6)
        if call.Done():
            pass
        elif not GetEventFlag(4045):
            """State 4"""
            Label('L1')
            # actionbutton:6000:"Talk"
            call = t319006000_x37(actionbutton1=6000, flag5=6001, flag12=6000, flag13=6000, flag14=6000,
                                  flag15=6000, flag4=6000)
            if call.Done():
                pass
            elif GetEventFlag(4045) == 1:
                Goto('L0')
    else:
        """State 2"""
        Goto('L1')
    """State 6"""
    return 0

def t319006000_x6():
    """State 0,1"""
    if not GetEventFlag(1044399205):
        """State 3,6"""
        # talk:31900200:"Ah, a Tarnished, are you?"
        assert t319006000_x67(text4=31900200, z7=1044399205, mode8=1)
        """State 2"""
        SetEventFlag(1044399207, 1)
        SetEventFlag(1044399206, 1)
    else:
        """State 4,5"""
        # talk:31900300:"The village here has been touched by Death."
        assert t319006000_x68(text3=31900300, mode7=1)
    """State 7"""
    return 0

def t319006000_x7():
    """State 0,2"""
    if GetEventFlag(1045399206) == 1:
        """State 1,4"""
        assert t319006000_x13()
    else:
        """State 3"""
        assert t319006000_x12()
    """State 5"""
    return 0

def t319006000_x8():
    """State 0,1"""
    if GetEventFlag(1045399208) == 1:
        """State 5,9"""
        assert t319006000_x34()
    elif GetEventFlag(1045399209) == 1:
        """State 4,8"""
        assert t319006000_x33()
    elif GetEventFlag(1044399207) == 1:
        """State 3,7"""
        assert t319006000_x32()
    else:
        """State 2,6"""
        assert t319006000_x31()
    """State 10"""
    return 0

def t319006000_x9():
    """State 0,1"""
    assert t319006000_x15()
    """State 2"""
    assert t319006000_x16()
    """State 3"""
    assert t319006000_x17()
    """State 4"""
    return 0

def t319006000_x10(z5=10, z6=12):
    """State 0"""
    while True:
        """State 7"""
        # actionbutton:6000:"Talk"
        call = t319006000_x37(actionbutton1=6000, flag5=6001, flag12=6000, flag13=6000, flag14=6000,
                              flag15=6000, flag4=6000)
        if call.Done():
            break
        elif GetEventFlag(1044399210) == 1:
            pass
        """State 1"""
        SetEventFlag(1044399210, 0)
        if not GetEventFlag(1044399211):
            """State 8"""
            # talk:31900100:"There's no mistake, is there?"
            assert t319006000_x69(text2=31900100, flag9=1044399211, mode4=1)
        elif not GetEventFlag(1044399212):
            """State 9"""
            # talk:31900110:"I'm sorry, I cannot give you your proper rites..."
            assert t319006000_x69(text2=31900110, flag9=1044399212, mode4=1)
        else:
            """State 2"""
            Quit()
    """State 3"""
    SetEventFlag(1044399213, 1)
    """State 4"""
    if RelativeAngleBetweenTwoPlayers_SpecifyAxis(0) < 120:
        """State 5"""
        RequestAnimation(90204, -1)
        assert GetCurrentStateElapsedFrames() > 1
    else:
        """State 6"""
        RequestAnimation(90202, -1)
        assert GetCurrentStateElapsedFrames() > 1
    """State 10"""
    return 0

def t319006000_x11(flag11=_):
    """State 0,2"""
    if not GetEventFlag(flag11):
        """State 3,5"""
        # talk:31980100:"Very well."
        assert t319006000_x69(text2=31980100, flag9=flag11, mode4=1)
    else:
        """State 4"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 6"""
    return 0

def t319006000_x12():
    """State 0,1"""
    if not GetEventFlag(1045399205):
        """State 2,5"""
        assert t319006000_x14()
    else:
        """State 3,4"""
        # talk:31901500:"What now? Had a change of heart?"
        assert t319006000_x68(text3=31901500, mode7=1)
    """State 6"""
    assert t319006000_x19()
    """State 7"""
    return 0

def t319006000_x13():
    """State 0,1"""
    if not GetEventFlag(1045399207):
        """State 2,4"""
        # talk:31901200:"I have a matter of my own to attend to."
        assert t319006000_x67(text4=31901200, z7=1045399207, mode8=1)
    else:
        """State 3,5"""
        # talk:31901300:"What is it? Still milling about?"
        assert t319006000_x68(text3=31901300, mode7=1)
    """State 6"""
    return 0

def t319006000_x14():
    """State 0,1"""
    if GetEventFlag(1044399206) == 1:
        """State 3,5"""
        # talk:31901000:"Another fool who won't listen to reason, eh?"
        assert t319006000_x68(text3=31901000, mode7=1)
    else:
        """State 2,4"""
        # talk:31901600:"Ah, a Tarnished, are you?"
        assert t319006000_x68(text3=31901600, mode7=1)
    """State 6"""
    return 0

def t319006000_x15():
    """State 0,1"""
    if not GetEventFlag(11102770):
        """State 2,5"""
        assert t319006000_x18()
    else:
        """State 3,4"""
        # talk:31914100:"Did you need something else?"
        assert t319006000_x68(text3=31914100, mode7=1)
    """State 6"""
    return 0

def t319006000_x16():
    """State 0"""
    while Loop('mainloop'):
        """State 7"""
        Label('L0')
        c1_110()
        while True:
            """State 1"""
            ClearTalkListData()
            """State 15"""
            assert t319006000_x23()
            """State 2"""
            ShowShopMessage(1)
            assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 4"""
            if GetTalkListEntryResult() == 1:
                """State 5,8"""
                OpenRegularShop(100125, 100149)
                assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            elif GetTalkListEntryResult() == 2:
                """State 6,12"""
                # talk:31915000:"I serve the Golden Order."
                assert t319006000_x67(text4=31915000, z7=11109621, mode8=1)
                Continue('mainloop')
            elif GetTalkListEntryResult() == 3:
                Break('mainloop')
            elif GetTalkListEntryResult() == 4:
                """State 10,14"""
                # talk:31915200:"Well, what have we here?"
                assert t319006000_x67(text4=31915200, z7=11109625, mode8=1)
                """State 11"""
                # goods:8980:Weathered Dagger
                PlayerEquipmentQuantityChange(3, 8980, -1)
                Continue('mainloop')
            else:
                """State 3,16"""
                return 0
    """State 9,13"""
    # talk:31915100:"Are you acquainted with a man named Rogier?"
    assert t319006000_x67(text4=31915100, z7=11109623, mode8=1)
    Goto('L0')

def t319006000_x17():
    """State 0,1"""
    return 0

def t319006000_x18():
    """State 0,2"""
    if GetEventFlag(1051439205) == 1 and not GetEventFlag(11109617):
        """State 3,7"""
        # talk:31914000:"You've met Gurranq, I take it?"
        assert t319006000_x67(text4=31914000, z7=11109617, mode8=1)
        """State 6"""
        SetEventFlag(1044399206, 1)
    elif not GetEventFlag(11109618) and GetEventFlagValue(1051439230, 5) > 1:
        """State 4,8"""
        # talk:31914300:"Ah, hello. You've been busy weeding Deathroot, I take it."
        assert t319006000_x67(text4=31914300, z7=11109618, mode8=1)
    else:
        """State 5,9"""
        # talk:31914200:"Ah, hello there. What can I do for you?"
        assert t319006000_x68(text3=31914200, mode7=1)
    """State 1"""
    SetEventFlag(11102770, 1)
    """State 10"""
    return 0

def t319006000_x19():
    """State 0,8"""
    c1_110()
    """State 1"""
    ClearTalkListData()
    """State 3"""
    # action:23191002:"Accept introduction"
    AddTalkListData(1, 23191002, -1)
    # action:23191003:"Refuse"
    AddTalkListData(2, 23191003, -1)
    """State 2"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 5"""
    if GetTalkListEntryResult() == 1:
        """State 6,12"""
        # talk:31901100:"Very well. Show me your map."
        assert t319006000_x68(text3=31901100, mode7=1)
        """State 11"""
        SetEventFlag(1045399208, 1)
        SetEventFlag(1045399206, 1)
        """State 14"""
        # action:23191011:"A red mark was made on the map"
        assert t319006000_x40(action1=23191011)
        """State 9"""
        Label('L0')
        SetEventFlag(1044399207, 1)
        SetEventFlag(1044399206, 1)
    elif GetTalkListEntryResult() == 2:
        """State 7,13"""
        # talk:31901400:"Well, all right, then."
        assert t319006000_x68(text3=31901400, mode7=1)
        """State 10"""
        SetEventFlag(1045399205, 1)
        SetEventFlag(1045399209, 1)
        Goto('L0')
    else:
        """State 4"""
        pass
    """State 15"""
    return 0

def t319006000_x20(mode6=_):
    """State 0,8"""
    c1_110()
    """State 1"""
    ClearTalkListData()
    """State 3"""
    # action:23191002:"Accept introduction"
    AddTalkListData(1, 23191002, -1)
    # action:23191003:"Refuse"
    AddTalkListData(2, 23191003, -1)
    """State 2"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 5"""
    if GetTalkListEntryResult() == 1:
        """State 6,10"""
        # talk:31913100:"Very well. Show me your map."
        assert t319006000_x67(text4=31913100, z7=1045399206, mode8=1)
        """State 12"""
        # action:23191011:"A red mark was made on the map"
        assert t319006000_x40(action1=23191011)
    elif GetTalkListEntryResult() == 2 and not mode6:
        """State 7,11"""
        # talk:31913400:"Well, all right, then."
        assert t319006000_x68(text3=31913400, mode7=1)
        """State 9"""
        SetEventFlag(1045399205, 1)
    else:
        """State 4"""
        pass
    """State 13"""
    return 0

def t319006000_x21():
    """State 0,3"""
    if GetEventFlag(1044399206) == 1:
        """State 1"""
        if GetEventFlag(1051439205) == 1:
            """State 5"""
            assert t319006000_x9()
        else:
            """State 2"""
            if GetEventFlag(11109625) == 1:
                """State 7"""
                assert t319006000_x29()
            else:
                """State 6"""
                assert t319006000_x8()
    else:
        """State 8"""
        # talk:31912000:"I don't believe we've met."
        assert t319006000_x67(text4=31912000, z7=1044399206, mode8=1)
        """State 4"""
        if GetEventFlag(1051439205) == 1:
            pass
        else:
            """State 9"""
            assert t319006000_x28(mode5=1)
    """State 10"""
    return 0

def t319006000_x22():
    """State 0,9"""
    if GetEventFlag(11109625) == 1:
        """State 4"""
        Label('L0')
    else:
        """State 8"""
        # goods:8980:Weathered Dagger
        if ComparePlayerInventoryNumber(3, 8980, 4, 1, 0) == 1:
            """State 7"""
            c1_110()
            """State 1"""
            ClearTalkListData()
            """State 3"""
            # action:23191006:"Give the Weathered Dagger"
            AddTalkListData(1, 23191006, -1)
            # action:23191007:"Don't give it"
            AddTalkListData(2, 23191007, -1)
            """State 2"""
            OpenConversationChoicesMenu(0)
            assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 5"""
            if GetTalkListEntryResult() == 1:
                """State 6,11"""
                # talk:31915200:"Well, what have we here?"
                assert t319006000_x67(text4=31915200, z7=11109625, mode8=1)
                """State 10"""
                # goods:8980:Weathered Dagger
                PlayerEquipmentQuantityChange(3, 8980, -1)
            else:
                Goto('L0')
        else:
            Goto('L0')
    """State 12"""
    return 0

def t319006000_x23():
    """State 0,1"""
    # action:23190000:"Study incantations"
    AddTalkListData(1, 23190000, -1)
    """State 3"""
    assert t319006000_x24()
    """State 2"""
    # action:20000009:"Leave"
    AddTalkListData(99, 20000009, -1)
    """State 4"""
    return 0

def t319006000_x24():
    """State 0,1"""
    assert t319006000_x25()
    """State 2"""
    assert t319006000_x26()
    """State 3"""
    assert t319006000_x27()
    """State 4"""
    return 0

def t319006000_x25():
    """State 0,2"""
    SetEventFlag(11109620, 0)
    SetEventFlag(11109622, 0)
    SetEventFlag(11109624, 0)
    """State 1"""
    SetEventFlagIf(not GetEventFlag(11109621), 11109620, 1)
    """State 3"""
    SetEventFlagIf(not GetEventFlag(11109623) and GetEventFlag(11109505) == 1, 11109622, 1)
    """State 4"""
    # goods:8980:Weathered Dagger
    SetEventFlagIf(not GetEventFlag(11109625) and ComparePlayerInventoryNumber(3, 8980, 4, 1, 0) == 1,
                   11109624, 1)
    """State 5"""
    return 0

def t319006000_x26():
    """State 0,1"""
    if GetEventFlag(11109622) == 1:
        """State 2"""
        SetEventFlag(11109620, 0)
    else:
        """State 4"""
        if GetEventFlag(11109620) == 1:
            """State 3"""
            SetEventFlag(11109622, 0)
        else:
            pass
    """State 5"""
    return 0

def t319006000_x27():
    """State 0,1"""
    # action:23190001:"About D"
    AddTalkListDataIf(GetEventFlag(11109620) == 1, 2, 23190001, -1)
    # action:23190002:"About Rogier"
    AddTalkListDataIf(GetEventFlag(11109622) == 1, 3, 23190002, -1)
    # action:23190003:"Give the Weathered Dagger"
    AddTalkListDataIf(GetEventFlag(11109624) == 1, 4, 23190003, -1)
    """State 2"""
    return 0

def t319006000_x28(mode5=_):
    """State 0,1"""
    # goods:2090:Deathroot
    if ComparePlayerInventoryNumber(3, 2090, 4, 1, 0) == 1:
        """State 3,10"""
        c1_110()
        """State 4"""
        ClearTalkListData()
        """State 6"""
        # action:23191004:"Show Deathroot"
        AddTalkListData(1, 23191004, -1)
        # action:23191005:"Don't show it"
        AddTalkListData(2, 23191005, -1)
        """State 5"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 8"""
        if GetTalkListEntryResult() == 1:
            """State 9"""
            if mode5 == 1:
                """State 11"""
                # talk:31913000:"Well, well..."
                assert t319006000_x68(text3=31913000, mode7=1)
            else:
                """State 14"""
                # talk:31913050:"Well, well..."
                assert t319006000_x68(text3=31913050, mode7=1)
            """State 12"""
            assert t319006000_x20(mode6=0)
        else:
            """State 7"""
            pass
    else:
        """State 2,13"""
        assert t319006000_x22()
    """State 15"""
    return 0

def t319006000_x29():
    """State 0,1"""
    # talk:31915600:"Did you need something else?"
    assert t319006000_x68(text3=31915600, mode7=1)
    """State 2"""
    return 0

def t319006000_x30(flag9=_, flag10=_):
    """State 0,3,4"""
    if not GetEventFlag(flag9):
        """State 1,6"""
        # talk:31980000:"<wince>"
        assert t319006000_x69(text2=31980000, flag9=flag9, mode4=1)
    elif not GetEventFlag(flag10):
        """State 2,7"""
        # talk:31980010:"Don't you dare."
        assert t319006000_x69(text2=31980010, flag9=flag10, mode4=1)
    else:
        """State 5"""
        pass
    """State 8"""
    return 0

def t319006000_x31():
    """State 0,1"""
    if GetEventFlag(1045399206) == 1:
        """State 5"""
        assert t319006000_x35()
    else:
        """State 2"""
        if GetEventFlag(1045399205) == 1:
            """State 6"""
            assert t319006000_x36()
        else:
            """State 3"""
            # talk:31912100:"Those Who Live in Death should be left well alone."
            assert t319006000_x68(text3=31912100, mode7=1)
            """State 4"""
            assert t319006000_x28(mode5=0)
    """State 7"""
    return 0

def t319006000_x32():
    """State 0,1"""
    if GetEventFlag(1045399206) == 1:
        """State 6"""
        assert t319006000_x35()
    else:
        """State 2"""
        if GetEventFlag(1045399205) == 1:
            """State 7"""
            assert t319006000_x36()
        else:
            """State 3"""
            if GetEventFlag(11109611) == 1:
                """State 4"""
                # talk:31912100:"Those Who Live in Death should be left well alone."
                assert t319006000_x68(text3=31912100, mode7=1)
            else:
                """State 8"""
                # talk:31912200:"Ah...we meet again."
                assert t319006000_x67(text4=31912200, z7=11109611, mode8=1)
            """State 5"""
            assert t319006000_x28(mode5=0)
    """State 9"""
    return 0

def t319006000_x33():
    """State 0,1"""
    if GetEventFlag(1045399206) == 1:
        """State 2"""
        assert t319006000_x35()
    else:
        """State 3"""
        # talk:31915400:"Ah, hello there. What can I do for you?"
        assert t319006000_x68(text3=31915400, mode7=1)
        """State 4"""
        assert t319006000_x20(mode6=1)
    """State 5"""
    return 0

def t319006000_x34():
    """State 0,1"""
    if not GetEventFlag(11109608):
        """State 2"""
        # talk:31914400:"Ah, hello again."
        assert t319006000_x67(text4=31914400, z7=11109608, mode8=1)
    else:
        """State 3"""
        # talk:31914500:"Go to Gurranq only if you feel the time is right."
        assert t319006000_x68(text3=31914500, mode7=1)
    """State 4"""
    assert t319006000_x22()
    """State 5"""
    return 0

def t319006000_x35():
    """State 0,1"""
    # talk:31913300:"What is it? Still milling about?"
    assert t319006000_x68(text3=31913300, mode7=1)
    """State 2"""
    assert t319006000_x22()
    """State 3"""
    return 0

def t319006000_x36():
    """State 0,1"""
    # talk:31901500:"What now? Had a change of heart?"
    assert t319006000_x68(text3=31901500, mode7=1)
    """State 2"""
    assert t319006000_x20(mode6=0)
    """State 3"""
    return 0

def t319006000_x37(actionbutton1=6000, flag5=6001, flag12=6000, flag13=6000, flag14=6000, flag15=6000,
                   flag4=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag5) == 1 or GetEventFlag(flag12) == 1 or GetEventFlag(flag13) == 1 or
                GetEventFlag(flag14) == 1 or GetEventFlag(flag15) == 1)
        """State 4"""
        assert not GetEventFlag(flag4)
        """State 2"""
        if GetEventFlag(flag4) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag5) and not GetEventFlag(flag12) and not GetEventFlag(flag13) and not
              GetEventFlag(flag14) and not GetEventFlag(flag15)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t319006000_x38():
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

def t319006000_x39():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t319006000_x40(action1=23191011):
    """State 0,1"""
    # action:23191011:"A red mark was made on the map"
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t319006000_x41(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t319006000_x57()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t319006000_x38()
    else:
        """State 4,7"""
        call = t319006000_x72()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t319006000_x38()
    """State 9"""
    return 0

def t319006000_x42():
    """State 0,1"""
    assert t319006000_x38()
    """State 2"""
    return 0

def t319006000_x43(flag1=4043, flag2=4041, flag3=4042, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t319006000_x60(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t319006000_x59()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t319006000_x44(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                   flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                   mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t319006000_x47(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t319006000_x51(val1=val1, z1=z1)
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
            call = t319006000_x53(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t319006000_x64() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t319006000_x49(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t319006000_x45(val2=10, val3=12):
    """State 0,1"""
    call = t319006000_x55(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t319006000_x41(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t319006000_x46(flag1=4043, val2=10, val3=12):
    """State 0,8"""
    assert t319006000_x74()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t319006000_x58()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t319006000_x38()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t319006000_x47(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t319006000_x48(z8=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t319006000_x37(actionbutton1=actionbutton1, flag5=flag5, flag12=6000, flag13=6000, flag14=6000,
                flag15=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t319006000_x48(z8=_, val6=_):
    """State 0,1"""
    if f203(z8) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z8)
        assert f202() == val6
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t319006000_x49(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t319006000_x38()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t319006000_x50()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t319006000_x65()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t319006000_x50():
    """State 0,1"""
    assert t319006000_x48(z8=1101, val6=1101)
    """State 2"""
    return 0

def t319006000_x51(val1=5, z1=1):
    """State 0,2"""
    assert t319006000_x61()
    """State 1"""
    call = t319006000_x52()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t319006000_x63()
    """State 4"""
    return 0

def t319006000_x52():
    """State 0,1"""
    assert t319006000_x48(z8=1000, val6=1000)
    """State 2"""
    return 0

def t319006000_x53(val5=12):
    """State 0,1"""
    call = t319006000_x54()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t319006000_x64()
    """State 3"""
    return 0

def t319006000_x54():
    """State 0,1"""
    assert t319006000_x48(z8=1100, val6=1100)
    """State 2"""
    return 0

def t319006000_x55(val2=10, val3=12):
    """State 0,5"""
    assert t319006000_x74()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t319006000_x56()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t319006000_x66()
    """Unused"""
    """State 6"""
    return 0

def t319006000_x56():
    """State 0,2"""
    call = t319006000_x48(z8=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t319006000_x57():
    """State 0,1"""
    assert t319006000_x48(z8=1001, val6=1001)
    """State 2"""
    return 0

def t319006000_x58():
    """State 0,1"""
    assert t319006000_x48(z8=1103, val6=1103)
    """State 2"""
    return 0

def t319006000_x59():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t319006000_x60(flag1=4043, flag2=4041, flag3=4042, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t319006000_x44(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                              flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                              z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t319006000_x46(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t319006000_x45(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t319006000_x73() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t319006000_x61():
    """State 0,1"""
    assert t319006000_x62()
    """State 2"""
    return 0

def t319006000_x62():
    """State 0,1"""
    assert t319006000_x48(z8=1104, val6=1104)
    """State 2"""
    return 0

def t319006000_x63():
    """State 0,1"""
    call = t319006000_x48(z8=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t319006000_x42()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t319006000_x64():
    """State 0,1"""
    call = t319006000_x48(z8=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t319006000_x42()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t319006000_x65():
    """State 0,1"""
    call = t319006000_x48(z8=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t319006000_x42()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t319006000_x66():
    """State 0,1"""
    call = t319006000_x48(z8=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t319006000_x42()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t319006000_x67(text4=_, z7=_, mode8=1):
    """State 0,5"""
    assert t319006000_x39() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text4, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode8:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(z7, 1)
    """State 6"""
    return 0

def t319006000_x68(text3=_, mode7=1):
    """State 0,4"""
    assert t319006000_x39() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t319006000_x69(text2=_, flag9=_, mode4=1):
    """State 0,5"""
    assert t319006000_x71() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(flag9, 1)
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

def t319006000_x70(text1=_, mode3=1):
    """State 0,4"""
    assert t319006000_x71() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t319006000_x71():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t319006000_x72():
    """State 0,1"""
    assert t319006000_x48(z8=1002, val6=1002)
    """State 2"""
    return 0

def t319006000_x73():
    """State 0,1"""
    assert t319006000_x38()
    """State 2"""
    return 0

def t319006000_x74():
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

