# -*- coding: utf-8 -*-
def t313006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t313006000_x34(flag1=3423, flag2=3421, flag3=3422, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1)
    Quit()

def t313006000_1000():
    """State 0,2,3"""
    assert t313006000_x0()
    """State 1"""
    c1_120(1000)
    Quit()

def t313006000_1101():
    """State 0,2,3"""
    assert t313006000_x1()
    """State 1"""
    c1_120(1101)
    Quit()

def t313006000_2000():
    """State 0,2,3"""
    assert t313006000_x2(val6=10, z5=12)
    """State 1"""
    c1_120(2000)
    Quit()

def t313006000_x0():
    """State 0,1"""
    if GetEventFlag(3425) == 1:
        """State 3"""
        def ExitPause():
            SetEventFlagIf(GetEventFlag(1037422701) == 1, 1037422709, 1)
        assert t313006000_x3()
    elif GetEventFlag(3426) == 1:
        """State 4"""
        def ExitPause():
            SetEventFlagIf(GetEventFlag(1038512701) == 1, 1038512705, 1)
        assert t313006000_x11()
    elif GetEventFlag(3427) == 1:
        """State 7"""
        assert t313006000_x17()
    elif GetEventFlag(3428) == 1:
        """State 5"""
        assert t313006000_x12()
    elif GetEventFlag(3429) == 1:
        """State 6"""
        assert t313006000_x13()
    elif GetEventFlag(3430) == 1:
        """State 8"""
        assert t313006000_x21()
    else:
        """State 2"""
        pass
    """State 9"""
    return 0

def t313006000_x1():
    """State 0"""
    if not GetEventFlag(1037422701):
        """State 2,1"""
        SetEventFlag(1037422701, 1)
    else:
        """State 3"""
        pass
    """State 4"""
    return 0

def t313006000_x2(val6=10, z5=12):
    """State 0"""
    while True:
        """State 3"""
        if GetEventFlag(3425) == 1:
            """State 2,6"""
            call = t313006000_x7(val6=val6, z5=z5)
            if call.Done():
                break
            elif not GetEventFlag(3425):
                pass
        elif GetEventFlag(3426) == 1:
            """State 4,7"""
            call = t313006000_x22(val6=val6, z5=z5)
            if call.Done():
                break
            elif not GetEventFlag(3426):
                pass
        else:
            """State 1,5"""
            # actionbutton:6000:"Talk"
            call = t313006000_x28(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                                  flag12=6000, flag4=6000)
            if call.Done():
                break
            elif GetEventFlag(3425) == 1 or GetEventFlag(3426) == 1:
                pass
    """State 8"""
    return 0

def t313006000_x3():
    """State 0,1"""
    if not GetEventFlag(1037429209):
        """State 2,5"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t313006000_x14()
    elif not GetEventFlag(1037429210):
        """State 3,6"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t313006000_x15()
    else:
        """State 4,7"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t313006000_x16()
    """State 8"""
    return 0

def t313006000_x4():
    """State 0,2"""
    if not GetEventFlag(1038519206):
        """State 1,12"""
        # talk:31301200:"I've been waiting for you."
        assert t313006000_x58(text2=31301200, mode4=1)
    else:
        """State 3,13"""
        # talk:31301500:"Are you ready, then?"
        assert t313006000_x58(text2=31301500, mode4=1)
    """State 4"""
    ClearTalkListData()
    c1_110()
    """State 5"""
    # action:23131002:"Take Rya's hand"
    AddTalkListData(1, 23131002, -1)
    # action:23131003:"Refuse Rya's hand"
    AddTalkListData(2, 23131003, -1)
    """State 6"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 7"""
    if GetTalkListEntryResult() == 1:
        """State 8,14"""
        # talk:31301600:"Give me your hand."
        assert t313006000_x58(text2=31301600, mode4=1)
        """State 16"""
        assert t313006000_x26()
    elif GetTalkListEntryResult() == 2:
        """State 9,15"""
        # talk:31301400:"Very well."
        assert t313006000_x58(text2=31301400, mode4=1)
        """State 11"""
        SetEventFlag(1038519206, 1)
    else:
        """State 10"""
        pass
    """State 17"""
    return 0

def t313006000_x5():
    """State 0,1"""
    if not GetEventFlag(16009318):
        """State 2"""
        if not GetEventFlag(16009315):
            """State 4,8"""
            SetWorkValue(0, 1)
            # talk:31303200:"Um, oh, it's you."
            assert t313006000_x58(text2=31303200, mode4=1)
        else:
            """State 5,9"""
            # talk:31303300:"The serpent that lurked in the shadows that night..."
            assert t313006000_x58(text2=31303300, mode4=1)
        """State 12"""
        assert t313006000_x8()
    else:
        """State 3"""
        if not GetEventFlag(16009319):
            """State 6,10"""
            # talk:31304100:"Lady Tanith, my own mother, has deceived me..."
            assert t313006000_x58(text2=31304100, mode4=1)
            """State 13"""
            assert t313006000_x9()
        else:
            """State 7,11"""
            # talk:31304200:"I want to know. How I was born, and met Lady Tanith."
            assert t313006000_x58(text2=31304200, mode4=1)
    """State 14"""
    return 0

def t313006000_x6():
    """State 0,1"""
    if GetEventFlag(16009327) == 1:
        """State 2,15"""
        assert t313006000_x24()
    elif not GetEventFlag(16000800) or GetEventFlag(16002715) == 1 or not GetEventFlag(16009326):
        """State 3"""
        if not GetEventFlag(16009326):
            """State 5,9"""
            # talk:31305000:"Oh, it's you..."
            assert t313006000_x58(text2=31305000, mode4=1)
        else:
            """State 6,10"""
            # talk:31306000:"I know that you have done so much for me."
            assert t313006000_x58(text2=31306000, mode4=1)
        """State 13"""
        assert t313006000_x10(z6=16009326, z7=16002715)
    else:
        """State 4"""
        if not GetEventFlag(16009328):
            """State 7,11"""
            # talk:31306100:"You're not willing to kill me, are you."
            assert t313006000_x58(text2=31306100, mode4=1)
        else:
            """State 8,12"""
            # talk:31306200:"I suppose I knew in my heart of hearts."
            assert t313006000_x58(text2=31306200, mode4=1)
        """State 14"""
        assert t313006000_x10(z6=16009328, z7=16009328)
    """State 16"""
    return 0

def t313006000_x7(val6=10, z5=12):
    """State 0"""
    while True:
        """State 13"""
        # actionbutton:6000:"Talk"
        call = t313006000_x28(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                              flag4=6000)
        if call.Done():
            break
        elif (not GetEventFlag(1037429209) and not GetEventFlag(1037429207) and not GetEventFlag(1037422703)
              and GetDistanceToPlayer() < 27):
            """State 1,3"""
            SetEventFlag(1037422703, 1)
            SetEventFlag(1037429205, 1)
            """State 14"""
            # talk:31300100:"Hello... Hello..."
            call = t313006000_x59(text1=31300100, mode3=1)
            def WhilePaused():
                c1_121(9625)
            if call.Done() and (GetDistanceToPlayer() < 5 or CheckSpecificPersonTalkHasEnded(0) == 1):
                continue
            elif GetDistanceToPlayer() > 29:
                pass
        elif (not GetEventFlag(1037429209) and not GetEventFlag(1037429207) and GetEventFlag(1037422704)
              == 1 and not GetEventFlag(1037422705) and GetDistanceToPlayer() < 27):
            """State 2,4"""
            SetEventFlag(1037422705, 1)
            """State 15"""
            # talk:31300200:"Hello... Hello..."
            call = t313006000_x59(text1=31300200, mode3=1)
            def WhilePaused():
                c1_121(9625)
            if call.Done() and (GetDistanceToPlayer() < 5 or CheckSpecificPersonTalkHasEnded(0) == 1):
                continue
            elif GetDistanceToPlayer() > 29:
                pass
        elif (GetEventFlag(1037422702) == 1 and not GetEventFlag(1037422701) and GetDistanceToPlayer()
              < val6 and not GetEventFlag(1037422708)):
            """State 5,6"""
            SetEventFlag(1037422703, 1)
            SetEventFlag(1037422705, 1)
            """State 7"""
            SetEventFlag(1037422701, 1)
            """State 16"""
            # talk:31380000:"Please, stop, Brave Tarnished."
            def ExitPause():
                SetEventFlag(1037422720, 1)
            assert t313006000_x59(text1=31380000, mode3=1) and CheckSpecificPersonTalkHasEnded(0) == 1
            """State 12"""
            Label('L0')
            assert GetEventFlag(1037422708) == 1 or (GetEventFlag(1037422706) == 1 and not GetEventFlag(1037422707))
            continue
        elif (GetEventFlag(1037422706) == 1 and not GetEventFlag(1037422707) and GetDistanceToPlayer()
              < val6 and not GetEventFlag(1037422708)):
            """State 8,9"""
            SetEventFlag(1037422707, 1)
            """State 17"""
            # talk:31380100:"Besides, I am no foe of yours."
            def ExitPause():
                SetEventFlag(1037422721, 1)
            assert t313006000_x59(text1=31380100, mode3=1) and CheckSpecificPersonTalkHasEnded(0) == 1
            Goto('L0')
        elif GetEventFlag(1037422708) == 1 and not GetEventFlag(1037422709) and GetDistanceToPlayer() < val6:
            """State 10,11"""
            SetEventFlag(1037422709, 1)
            """State 18"""
            # talk:31380200:"I see that you have reconsidered."
            assert t313006000_x59(text1=31380200, mode3=1)
            continue
        """State 19"""
        assert t313006000_x29()
    """State 20"""
    return 0

def t313006000_x8():
    """State 0,1"""
    if GetEventFlag(16009316) == 1:
        """State 2,3"""
        ClearTalkListData()
        c1_110()
        """State 4"""
        # action:23131004:"Tell her of the dark side of Volcano Manor"
        AddTalkListData(1, 23131004, -1)
        # action:23131005:"Don't tell her"
        AddTalkListData(2, 23131005, -1)
        """State 5"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 8"""
        if GetTalkListEntryResult() == 1:
            """State 6,12"""
            # talk:31303400:"Really..."
            assert t313006000_x58(text2=31303400, mode4=1)
            """State 9"""
            SetEventFlag(16009318, -1)
            """State 11"""
            SetEventFlag(16009315, 1)
            """State 13"""
            assert t313006000_x9()
        else:
            """State 7"""
            Label('L0')
            """State 10"""
            SetEventFlag(16009315, 1)
    else:
        Goto('L0')
    """State 14"""
    return 0

def t313006000_x9():
    """State 0,1"""
    # goods:8129:Serpent's Amnion
    if ComparePlayerInventoryNumber(3, 8129, 4, 1, 0) == 1:
        """State 2,4"""
        ClearTalkListData()
        c1_110()
        """State 5"""
        # action:23131006:"Give Serpent's Amnion"
        AddTalkListData(1, 23131006, -1)
        # action:23131007:"Don't give it"
        AddTalkListData(2, 23131007, -1)
        """State 6"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 7"""
        if GetTalkListEntryResult() == 1:
            """State 8,10"""
            # goods:8129:Serpent's Amnion
            PlayerEquipmentQuantityChange(3, 8129, -1)
            """State 11"""
            SetEventFlag(16009319, 1)
            """State 12"""
            # talk:31304000:"Hmm, what is this?"
            assert t313006000_x58(text2=31304000, mode4=1)
        else:
            """State 9"""
            pass
    else:
        """State 3"""
        pass
    """State 13"""
    return 0

def t313006000_x10(z6=_, z7=_):
    """State 0,10"""
    # goods:8128:Tonic of Forgetfulness
    if ComparePlayerInventoryNumber(3, 8128, 4, 1, 0) == 1:
        """State 11,1"""
        ClearTalkListData()
        c1_110()
        """State 2"""
        # action:23131009:"Give Tonic of Forgetfulness"
        AddTalkListData(1, 23131009, -1)
        # action:23131012:"Don't give it"
        AddTalkListData(2, 23131012, -1)
        """State 3"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 6,15"""
            # talk:31305200:"I'm to drink this, then?"
            assert t313006000_x58(text2=31305200, mode4=1)
            """State 8"""
            SetEventFlag(16009327, 1)
            """State 7"""
            # goods:8128:Tonic of Forgetfulness
            PlayerEquipmentQuantityChange(3, 8128, -1)
            """State 13"""
            def WhilePaused():
                RequestAnimation(90205, -1)
            assert GetCurrentStateElapsedTime() > 5
            """State 16"""
            # talk:31305205:"..."
            assert t313006000_x58(text2=31305205, mode4=1)
            """State 12"""
            SetEventFlag(16009329, 1)
        else:
            """State 5"""
            Label('L0')
            """State 9"""
            SetEventFlag(z6, 1)
            """State 14"""
            SetEventFlag(z7, 1)
    else:
        Goto('L0')
    """State 17"""
    return 0

def t313006000_x11():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(90300, -1)
    assert t313006000_x4()
    """State 2"""
    return 0

def t313006000_x12():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(90300, -1)
    def ExitPause():
        SetWorkValueIf(not GetEventFlag(16009315), 0, 0)
    assert t313006000_x5()
    """State 2"""
    return 0

def t313006000_x13():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(90305, -1)
    assert t313006000_x6()
    """State 2"""
    return 0

def t313006000_x14():
    """State 0,1"""
    if not GetEventFlag(1037429207):
        """State 2,14"""
        # talk:31300300:"Hello."
        assert t313006000_x58(text2=31300300, mode4=1)
    else:
        """State 3,15"""
        # talk:31300600:"Have you had a change of heart?"
        assert t313006000_x58(text2=31300600, mode4=1)
    """State 4"""
    ClearTalkListData()
    c1_110()
    """State 5"""
    # action:23131000:"Hear the request"
    AddTalkListData(1, 23131000, -1)
    # action:23131001:"Refuse"
    AddTalkListData(2, 23131001, -1)
    """State 6"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 7"""
    if GetTalkListEntryResult() == 1:
        """State 8,16"""
        # talk:31300400:"Ohh, thank you dearly."
        assert t313006000_x58(text2=31300400, mode4=1)
        """State 11"""
        SetEventFlag(1037429209, 1)
        """State 13"""
        Label('L0')
        SetUpdateDistance(17)
    elif GetTalkListEntryResult() == 2:
        """State 9,17"""
        # talk:31300500:"Yes, I see. Most unfortunate, but I'll have to make do."
        assert t313006000_x58(text2=31300500, mode4=1)
        """State 12"""
        SetEventFlag(1037429207, 1)
        Goto('L0')
    else:
        """State 10"""
        pass
    """State 18"""
    return 0

def t313006000_x15():
    """State 0,12"""
    # talk:31300700:"The thug should be resting at an abandoned home down the way..."
    assert t313006000_x58(text2=31300700, mode4=1)
    """State 9"""
    # goods:8136:Rya's Necklace
    if ComparePlayerInventoryNumber(3, 8136, 4, 1, 0) == 1:
        """State 10,1"""
        ClearTalkListData()
        c1_110()
        """State 2"""
        # eventflag:400300:shop:100150:Rya's Necklace, action:23131010:"Give Rya's Necklace"
        AddTalkListDataIf(GetEventFlag(400300) == 1, 1, 23131010, -1)
        # action:23131011:"Don't give it"
        AddTalkListData(2, 23131011, -1)
        """State 3"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 5,13"""
            # talk:31301000:"Oh, yes, that is my missing necklace."
            assert t313006000_x58(text2=31301000, mode4=1)
            """State 7"""
            SetEventFlag(1037429210, 1)
            """State 8"""
            # goods:8136:Rya's Necklace
            PlayerEquipmentQuantityChange(3, 8136, -1)
            """State 14"""
            # lot:100900:Volcano Manor Invitation
            assert t313006000_x31(lot1=100900)
            """State 15"""
            # talk:31301010:"Brave Tarnished, seek the Altus Plateau, the realm of the Erdtree."
            assert t313006000_x58(text2=31301010, mode4=1)
        else:
            """State 6"""
            pass
    else:
        """State 11"""
        pass
    """State 16"""
    return 0

def t313006000_x16():
    """State 0,1"""
    if not GetEventFlag(1037429211):
        """State 2,5"""
        # talk:31301100:"Ohh, and... One more thing, only for you..."
        assert t313006000_x58(text2=31301100, mode4=1)
        """State 4"""
        SetEventFlag(1037429211, 1)
    else:
        """State 3,6"""
        # talk:31302400:"Seek the old ruins in the cliff."
        assert t313006000_x58(text2=31302400, mode4=1)
    """State 7"""
    return 0

def t313006000_x17():
    """State 0,1"""
    if DoesSelfHaveSpEffect(9829) == 1:
        """State 2,4"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t313006000_x18()
    else:
        """State 3,5"""
        def WhilePaused():
            RequestAnimation(20000, -1)
        assert t313006000_x19()
    """State 6"""
    return 0

def t313006000_x18():
    """State 0,1"""
    if GetEventFlag(16009308) == 1 and not GetEventFlag(16002710):
        """State 2,5"""
        assert t313006000_x19()
    elif GetEventFlag(16009305) == 1 and GetEventFlagValue(16009260, 3) > 1:
        """State 3,6"""
        assert t313006000_x23()
    else:
        """State 4,7"""
        assert t313006000_x20()
    """State 8"""
    return 0

def t313006000_x19():
    """State 0,1"""
    if not GetEventFlag(16009306):
        """State 2,8"""
        # talk:31302100:"Brave Tarnished, what is your business here?"
        assert t313006000_x58(text2=31302100, mode4=1)
        """State 5"""
        SetEventFlag(16009306, 1)
        """State 6"""
        SetEventFlag(16002711, 1)
    elif not GetEventFlag(16009307):
        """State 3,9"""
        # talk:31302200:"Lady Tanith is my mother."
        assert t313006000_x58(text2=31302200, mode4=1)
        """State 7"""
        SetEventFlag(16009307, 1)
    else:
        """State 4,10"""
        # talk:31302300:"My serpentine form, and the name Zorayas,"
        assert t313006000_x58(text2=31302300, mode4=1)
    """State 11"""
    return 0

def t313006000_x20():
    """State 0,1"""
    if GetEventFlag(1038519205) == 1 and not GetEventFlag(16009305):
        """State 2,8"""
        # talk:31303000:"Hello again. Brave Tarnished."
        assert t313006000_x58(text2=31303000, mode4=1)
        """State 6"""
        Label('L0')
        SetEventFlag(16009305, 1)
    elif GetEventFlag(1037429210) == 1 and not GetEventFlag(16009305):
        """State 3,9"""
        # talk:31303500:"Hello again. Brave Tarnished."
        assert t313006000_x58(text2=31303500, mode4=1)
        Goto('L0')
    elif (GetEventFlag(1037429207) == 1 or GetEventFlag(1037429209) == 1) and not GetEventFlag(16009305):
        """State 4,10"""
        # talk:31303600:"Hello again. Brave Tarnished."
        assert t313006000_x58(text2=31303600, mode4=1)
        Goto('L0')
    elif not GetEventFlag(16009305):
        """State 5,11"""
        # talk:31303700:"A pleasure to meet you. Brave Tarnished."
        assert t313006000_x58(text2=31303700, mode4=1)
        Goto('L0')
    else:
        """State 7,12"""
        # talk:31303800:"Brave Tarnished."
        assert t313006000_x58(text2=31303800, mode4=1)
    """State 13"""
    return 0

def t313006000_x21():
    """State 0,1"""
    if not GetEventFlag(16009335):
        """State 2,5"""
        # talk:31307100:"Oh, it's you."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t313006000_x58(text2=31307100, mode4=1)
        """State 4"""
        SetEventFlag(16009335, 1)
    else:
        """State 3,6"""
        # talk:31307200:"I await Lady Tanith."
        def WhilePaused():
            RequestAnimation(90300, -1)
        assert t313006000_x58(text2=31307200, mode4=1)
    """State 7"""
    return 0

def t313006000_x22(val6=10, z5=12):
    """State 0"""
    while True:
        """State 8"""
        # actionbutton:6000:"Talk"
        call = t313006000_x28(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                              flag4=6000)
        if call.Done():
            break
        elif (GetEventFlag(1038512700) == 1 and not GetEventFlag(1038512701) and GetDistanceToPlayer()
              < val6 and not GetEventFlag(1038512704)):
            """State 1,2"""
            SetEventFlag(1038512701, 1)
            """State 9"""
            # talk:31380000:"Please, stop, Brave Tarnished."
            def ExitPause():
                SetEventFlag(1038512706, 1)
            assert t313006000_x59(text1=31380000, mode3=1) and CheckSpecificPersonTalkHasEnded(0) == 1
        elif (GetEventFlag(1038512702) == 1 and not GetEventFlag(1038512703) and GetDistanceToPlayer()
              < val6 and not GetEventFlag(1038512704)):
            """State 3,4"""
            SetEventFlag(1038512703, 1)
            """State 10"""
            # talk:31380100:"Besides, I am no foe of yours."
            def ExitPause():
                SetEventFlag(1038512707, 1)
            assert t313006000_x59(text1=31380100, mode3=1) and CheckSpecificPersonTalkHasEnded(0) == 1
        elif GetEventFlag(1038512704) == 1 and not GetEventFlag(1038512705) and GetDistanceToPlayer() < val6:
            """State 5,6"""
            SetEventFlag(1038512705, 1)
            """State 11"""
            # talk:31380200:"I see that you have reconsidered."
            assert t313006000_x59(text1=31380200, mode3=1)
            continue
        """State 7"""
        assert GetEventFlag(1038512704) == 1 or (GetEventFlag(1038512702) == 1 and not GetEventFlag(1038512703))
    """State 12"""
    return 0

def t313006000_x23():
    """State 0,1"""
    if not GetEventFlag(16009308):
        """State 2,6"""
        # talk:31303100:"Have you ever..."
        assert t313006000_x58(text2=31303100, mode4=1)
        """State 4"""
        SetEventFlag(16009308, 1)
        """State 5"""
        SetEventFlag(16002710, 1)
    else:
        """State 3,7"""
        # talk:31303900:"Sometimes I hear strange sounds beyond the walls."
        assert t313006000_x58(text2=31303900, mode4=1)
    """State 8"""
    return 0

def t313006000_x24():
    """State 0,1"""
    if not GetEventFlag(16009329):
        """State 2,5"""
        # talk:31305206:"Ahh... How delightfully sweet..."
        assert t313006000_x58(text2=31305206, mode4=1)
        """State 4"""
        SetEventFlag(16009329, 1)
    else:
        """State 3,6"""
        # talk:31307000:"..."
        assert t313006000_x58(text2=31307000, mode4=1)
    """State 7"""
    return 0

def t313006000_x25(flag15=_, flag16=_):
    """State 0,2"""
    assert GetEventFlag(flag15) == 1 and GetEventFlag(flag16) == 1
    """State 3"""
    assert GetCurrentStateElapsedTime() > 6
    """State 1"""
    SetEventFlag(1038519205, 1)
    """State 4"""
    return 0

def t313006000_x26():
    """State 0,1"""
    if GetEventFlag(1038519207) == 1:
        """State 2,4"""
        assert t313006000_x27(flag13=1038512725, flag14=1038512728, flag15=1038512726, flag16=1038512729)
    else:
        """State 3,5"""
        assert t313006000_x27(flag13=1038502705, flag14=1038502708, flag15=1038502706, flag16=1038502709)
    """State 6"""
    return 0

def t313006000_x27(flag13=_, flag14=_, flag15=_, flag16=_):
    """State 0,1"""
    SetEventFlag(flag13, 1)
    SetEventFlag(flag14, 1)
    call = t313006000_x25(flag15=flag15, flag16=flag16)
    def ExitPause():
        SetEventFlag(flag13, 0)
        SetEventFlag(flag14, 0)
    if call.Done():
        pass
    elif not GetEventFlag(flag13) or not GetEventFlag(flag14):
        pass
    """State 2"""
    return 0

def t313006000_x28(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t313006000_x29():
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

def t313006000_x30():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t313006000_x31(lot1=100900):
    """State 0,1"""
    # lot:100900:Volcano Manor Invitation
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t313006000_x32(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t313006000_x48()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t313006000_x29()
    else:
        """State 4,7"""
        call = t313006000_x61()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t313006000_x29()
    """State 9"""
    return 0

def t313006000_x33():
    """State 0,1"""
    assert t313006000_x29()
    """State 2"""
    return 0

def t313006000_x34(flag1=3423, flag2=3421, flag3=3422, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t313006000_x51(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t313006000_x50()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t313006000_x35(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                   flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                   mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t313006000_x38(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t313006000_x42(val1=val1, z1=z1)
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
            call = t313006000_x44(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t313006000_x55() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t313006000_x40(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t313006000_x36(val2=10, val3=12):
    """State 0,1"""
    call = t313006000_x46(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t313006000_x32(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t313006000_x37(flag1=3423, val2=10, val3=12):
    """State 0,8"""
    assert t313006000_x63()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t313006000_x49()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t313006000_x29()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t313006000_x38(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t313006000_x39(z8=2000, val7=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t313006000_x28(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t313006000_x39(z8=_, val7=_):
    """State 0,1"""
    if f203(z8) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z8)
        assert f202() == val7
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t313006000_x40(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t313006000_x29()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t313006000_x41()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t313006000_x56()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t313006000_x41():
    """State 0,1"""
    assert t313006000_x39(z8=1101, val7=1101)
    """State 2"""
    return 0

def t313006000_x42(val1=5, z1=1):
    """State 0,2"""
    assert t313006000_x52()
    """State 1"""
    call = t313006000_x43()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t313006000_x54()
    """State 4"""
    return 0

def t313006000_x43():
    """State 0,1"""
    assert t313006000_x39(z8=1000, val7=1000)
    """State 2"""
    return 0

def t313006000_x44(val5=12):
    """State 0,1"""
    call = t313006000_x45()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t313006000_x55()
    """State 3"""
    return 0

def t313006000_x45():
    """State 0,1"""
    assert t313006000_x39(z8=1100, val7=1100)
    """State 2"""
    return 0

def t313006000_x46(val2=10, val3=12):
    """State 0,5"""
    assert t313006000_x63()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t313006000_x47()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t313006000_x57()
    """Unused"""
    """State 6"""
    return 0

def t313006000_x47():
    """State 0,2"""
    call = t313006000_x39(z8=1102, val7=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t313006000_x48():
    """State 0,1"""
    assert t313006000_x39(z8=1001, val7=1001)
    """State 2"""
    return 0

def t313006000_x49():
    """State 0,1"""
    assert t313006000_x39(z8=1103, val7=1103)
    """State 2"""
    return 0

def t313006000_x50():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t313006000_x51(flag1=3423, flag2=3421, flag3=3422, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t313006000_x35(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                              flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                              z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t313006000_x37(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t313006000_x36(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t313006000_x62() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t313006000_x52():
    """State 0,1"""
    assert t313006000_x53()
    """State 2"""
    return 0

def t313006000_x53():
    """State 0,1"""
    assert t313006000_x39(z8=1104, val7=1104)
    """State 2"""
    return 0

def t313006000_x54():
    """State 0,1"""
    call = t313006000_x39(z8=1201, val7=1201)
    if call.Get() == 1:
        """State 2"""
        assert t313006000_x33()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t313006000_x55():
    """State 0,1"""
    call = t313006000_x39(z8=1300, val7=1300)
    if call.Get() == 1:
        """State 2"""
        assert t313006000_x33()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t313006000_x56():
    """State 0,1"""
    call = t313006000_x39(z8=1301, val7=1301)
    if call.Get() == 1:
        """State 2"""
        assert t313006000_x33()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t313006000_x57():
    """State 0,1"""
    call = t313006000_x39(z8=1302, val7=1302)
    if call.Get() == 1:
        """State 2"""
        assert t313006000_x33()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t313006000_x58(text2=_, mode4=1):
    """State 0,4"""
    assert t313006000_x30() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t313006000_x59(text1=_, mode3=1):
    """State 0,4"""
    assert t313006000_x60() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t313006000_x60():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t313006000_x61():
    """State 0,1"""
    assert t313006000_x39(z8=1002, val7=1002)
    """State 2"""
    return 0

def t313006000_x62():
    """State 0,1"""
    assert t313006000_x29()
    """State 2"""
    return 0

def t313006000_x63():
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

