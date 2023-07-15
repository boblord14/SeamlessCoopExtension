# -*- coding: utf-8 -*-
def t223006000_1():
    """State 0,1"""
    # actionbutton:6280:"Talk"
    t223006000_x52(flag1=3943, flag2=3941, flag3=3942, val1=5, val2=10, val3=12, val4=50, val5=50, actionbutton1=6280,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1)
    Quit()

def t223006000_1000():
    """State 0,2,3"""
    assert t223006000_x0()
    """State 1"""
    c1_120(1000)
    Quit()

def t223006000_1001():
    """State 0,2,3"""
    assert t223006000_x1()
    """State 1"""
    c1_120(1001)
    Quit()

def t223006000_1101():
    """State 0,2,3"""
    assert t223006000_x2()
    """State 1"""
    c1_120(1101)
    Quit()

def t223006000_1102():
    """State 0,2,3"""
    t223006000_x3()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t223006000_1103():
    """State 0,2,3"""
    assert t223006000_x4()
    """State 1"""
    c1_120(1103)
    Quit()

def t223006000_2000():
    """State 0,2,3"""
    assert t223006000_x5(val6=50, z5=50)
    """State 1"""
    c1_120(2000)
    Quit()

def t223006000_x0():
    """State 0,1"""
    if GetEventFlag(3945) == 1:
        """State 7"""
        assert t223006000_x6()
    elif GetEventFlag(3946) == 1:
        """State 8"""
        assert t223006000_x7()
    elif GetEventFlag(3947) == 1:
        """State 3"""
        if not GetEventFlag(1039402712):
            """State 5"""
            SetEventFlag(1039402711, 0)
        else:
            """State 4"""
            SetEventFlag(1039402711, 1)
            """State 6"""
            SetEventFlag(1039402712, 0)
        """State 9"""
        def WhilePaused():
            RequestAnimationIf(not GetEventFlag(1039402711), 20030, -1)
            RequestAnimationIf(GetEventFlag(1039402711) == 1, 20039, -1)
        assert t223006000_x8()
    elif GetEventFlag(3948) == 1:
        """State 10"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        def ExitPause():
            SetEventFlag(1039402711, 1)
        assert t223006000_x42()
    else:
        """State 2"""
        pass
    """State 11"""
    return 0

def t223006000_x1():
    """State 0,1"""
    if not GetEventFlag(1039409255):
        """State 4"""
        # talk:22380200:"No..."
        assert t223006000_x78(text1=22380200, mode3=1)
    elif not GetEventFlag(1039519206):
        """State 2"""
        # talk:22381300:"Oh, master, what have I done..."
        assert t223006000_x78(text1=22381300, mode3=1)
    else:
        """State 3"""
        # talk:22382300:"M'lord, what have I done..."
        assert t223006000_x78(text1=22382300, mode3=1)
    """State 5"""
    return 0

def t223006000_x2():
    """State 0,1"""
    if not GetEventFlag(3946):
        """State 2,6"""
        if not GetEventFlag(1039409255):
            """State 7"""
            assert t223006000_x15()
        else:
            """State 8"""
            assert t223006000_x40()
    elif True:
        """State 4"""
        """State 5"""
        pass
    else:
        """State 3"""
        pass
    """State 9"""
    return 0

def t223006000_x3():
    """State 0,1"""
    if not GetEventFlag(3946):
        """State 3,5"""
        if not GetEventFlag(1039409255):
            """State 6"""
            assert t223006000_x13()
        else:
            """State 7"""
            assert t223006000_x12()
    else:
        """State 4"""
        pass
    """State 2"""
    Quit()
    """Unused"""
    """State 8"""
    return 0

def t223006000_x4():
    """State 0,1,2"""
    if not GetEventFlag(1039409255):
        """State 5"""
        # talk:22380300:"Mum..."
        assert t223006000_x78(text1=22380300, mode3=1)
    elif not GetEventFlag(1039519206):
        """State 3"""
        # talk:22381400:"Master..."
        assert t223006000_x78(text1=22381400, mode3=1)
    else:
        """State 4"""
        # talk:22382400:"M'lord..."
        assert t223006000_x78(text1=22382400, mode3=1)
    """State 6"""
    return 0

def t223006000_x5(val6=50, z5=50):
    """State 0"""
    while Loop('mainloop'):
        """State 1"""
        if GetEventFlag(3945) == 1:
            """State 2,11"""
            call = t223006000_x10(val6=val6, z5=z5)
            if call.Done():
                break
            elif not GetEventFlag(3945):
                pass
        elif GetEventFlag(3946) == 1:
            """State 3,12"""
            call = t223006000_x11(val6=val6, z5=z5)
            if call.Done():
                break
            elif not GetEventFlag(3946):
                pass
        elif GetEventFlag(3947) == 1:
            """State 4,7"""
            SetUpdateDistance(100)
            while True:
                """State 13"""
                # actionbutton:6000:"Talk"
                call = t223006000_x46(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                                      flag12=6000, flag4=6000)
                if call.Done():
                    """State 8"""
                    SetUpdateDistance(17)
                    Break('mainloop')
                elif not GetEventFlag(3947):
                    break
                elif GetDistanceToPlayer() > 80 and GetEventFlag(1039402712) == 1:
                    """State 6"""
                    RequestAnimation(20039, -1)
                    SetEventFlag(1039402711, 0)
                    SetEventFlag(1039402712, 0)
            """State 9"""
            SetUpdateDistance(17)
        else:
            """State 5,10"""
            # actionbutton:6000:"Talk"
            call = t223006000_x46(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                                  flag12=6000, flag4=6000)
            if call.Done():
                break
            elif GetEventFlag(3945) == 1 or GetEventFlag(3946) == 1:
                pass
    """State 14"""
    return 0

def t223006000_x6():
    """State 0,1"""
    if not GetEventFlag(1043379355):
        """State 2,7"""
        # talk:22300300:"Hm? Oh, yes, I remember."
        def WhilePaused():
            RequestAnimation(20030, -1)
        assert t223006000_x77(text2=22300300, mode4=1)
        """State 5"""
        SetEventFlag(1043379355, 1)
        """State 6"""
        SetEventFlag(1043379352, 1)
    elif not GetEventFlag(1043379356):
        """State 3,9"""
        def WhilePaused():
            RequestAnimation(20030, -1)
        assert t223006000_x14()
    else:
        """State 4,8"""
        # talk:22300500:"Right, but I'll need a moment."
        def WhilePaused():
            RequestAnimation(20030, -1)
        assert t223006000_x77(text2=22300500, mode4=1)
    """State 10"""
    return 0

def t223006000_x7():
    """State 0,1"""
    if not GetEventFlag(31159206):
        """State 2,5"""
        def WhilePaused():
            RequestAnimation(20040, -1)
        assert t223006000_x9()
    else:
        """State 3,4"""
        # talk:22301200:"Thank you."
        def WhilePaused():
            RequestAnimation(20035, -1)
        assert t223006000_x77(text2=22301200, mode4=1)
    """State 6"""
    return 0

def t223006000_x8():
    """State 0,1"""
    assert t223006000_x16()
    """State 2"""
    SetEventFlag(1039402711, 0)
    assert t223006000_x18()
    """State 3"""
    return 0

def t223006000_x9():
    """State 0,16"""
    # talk:22301000:"Oh, what are you doing here?"
    assert t223006000_x77(text2=22301000, mode4=1)
    """State 1"""
    SetEventFlag(31159205, 1)
    """State 14"""
    SetEventFlag(31159202, 1)
    """State 2"""
    # goods:8161:Sewing Needle
    if ComparePlayerInventoryNumber(3, 8161, 4, 1, 0) == 1:
        """State 3,5"""
        c1_110()
        ClearTalkListData()
        """State 6"""
        # action:22231000:"Give the Sewing Needle"
        AddTalkListData(1, 22231000, -1)
        # action:22231001:"Don't give it"
        AddTalkListData(2, 22231001, -1)
        """State 7"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 8"""
        if GetTalkListEntryResult() == 1:
            """State 9,17"""
            # talk:22301100:"Wait, is that what I think it is?"
            assert t223006000_x77(text2=22301100, mode4=1)
            """State 11"""
            SetEventFlag(31159206, 1)
            """State 12"""
            # goods:8161:Sewing Needle
            PlayerEquipmentQuantityChange(3, 8161, -1)
            """State 15"""
            TurnCharacterToFaceEntity(-1, 10000, -1, -1)
            assert GetCurrentStateElapsedFrames() > 1 and GetWhetherChrEventAnimHasEnded(10000) == 1
            """State 13"""
            TurnCharacterToFaceEntity(90000, 10000, -1, -1)
            def WhilePaused():
                RequestAnimation(20042, -1)
            assert GetCurrentStateElapsedTime() > 10
            """State 18"""
            # talk:22301103:"<sob>"
            assert t223006000_x77(text2=22301103, mode4=1)
        else:
            """State 10"""
            pass
    else:
        """State 4"""
        pass
    """State 19"""
    return 0

def t223006000_x10(val6=50, z5=50):
    """State 0"""
    while True:
        """State 9"""
        # actionbutton:6280:"Talk"
        call = t223006000_x46(actionbutton1=6280, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                              flag4=6000)
        if call.Done():
            break
        elif (GetEventFlag(1043372732) == 1 and not GetEventFlag(1043372733) and not GetEventFlag(1043379357)
              and GetDistanceToPlayer() < val6):
            """State 1,3"""
            SetEventFlag(1043372733, 1)
            """State 10"""
            # talk:22300100:"Oi! You there!"
            assert t223006000_x78(text1=22300100, mode3=1)
        elif (GetEventFlag(1043372734) == 1 and not GetEventFlag(1043372735) and not GetEventFlag(1043379357)
              and GetDistanceToPlayer() < val6):
            """State 5,6"""
            SetEventFlag(1043372735, 1)
            """State 12"""
            # talk:22300103:"You, yeah, you there!"
            assert t223006000_x78(text1=22300103, mode3=1)
        elif (GetEventFlag(1043372736) == 1 and not GetEventFlag(1043372737) and not GetEventFlag(1043379357)
              and GetDistanceToPlayer() < val6):
            """State 7,8"""
            SetEventFlag(1043372737, 1)
            """State 13"""
            # talk:22300106:"Why won't anyone look me in the eye?"
            assert t223006000_x78(text1=22300106, mode3=1)
        elif GetEventFlag(1043379357) == 1 and not GetEventFlag(1043379358) and GetDistanceToPlayer() < val6:
            """State 2,4"""
            SetEventFlag(1043379358, 1)
            """State 11"""
            # talk:22300200:"Ow!"
            assert t223006000_x78(text1=22300200, mode3=1)
    """State 14"""
    return 0

def t223006000_x11(val6=50, z5=50):
    """State 0"""
    while True:
        """State 3"""
        # actionbutton:6280:"Talk"
        call = t223006000_x46(actionbutton1=6280, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                              flag4=6000)
        if call.Done():
            break
        elif not GetEventFlag(31152700) and not GetEventFlag(31159205) and GetDistanceToPlayer() < val6:
            """State 1,2"""
            SetEventFlag(31152700, 1)
            """State 4"""
            # talk:22301300:"Oh..."
            assert t223006000_x78(text1=22301300, mode3=1)
    """State 5"""
    return 0

def t223006000_x12():
    """State 0,2"""
    if not GetEventFlag(1043379353):
        """State 3,7"""
        SetEventFlag(1043379353, 1)
        """State 6"""
        SetEventFlag(1043372730, 1)
        """State 9"""
        if not GetEventFlag(1039519206):
            """State 10"""
            # talk:22381200:"Oh, my..."
            assert t223006000_x78(text1=22381200, mode3=1)
        else:
            """State 11"""
            # talk:22382200:"Oh, my..."
            assert t223006000_x78(text1=22382200, mode3=1)
    elif not GetEventFlag(1043372730):
        """State 4,8"""
        SetEventFlag(1043372730, 1)
    else:
        """State 5"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 12"""
    return 0

def t223006000_x13():
    """State 0,2"""
    if not GetEventFlag(1043379353):
        """State 3,7"""
        SetEventFlag(1043379353, 1)
        """State 6"""
        SetEventFlag(1043372730, 1)
        """State 9"""
        # talk:22380100:"Oh, now, you too, is it?"
        assert t223006000_x78(text1=22380100, mode3=1)
    elif not GetEventFlag(1043372730):
        """State 4,8"""
        SetEventFlag(1043372730, 1)
    else:
        """State 5"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 10"""
    return 0

def t223006000_x14():
    """State 0,2"""
    # talk:22300400:"Oh, what a shame."
    assert t223006000_x77(text2=22300400, mode4=1)
    """State 1"""
    SetEventFlag(1043379356, 1)
    """State 4"""
    # lot:102710:Mushroom
    assert t223006000_x49(lot1=102710)
    """State 3"""
    # talk:22300405:"Or, if you can afford to wait for a while,"
    assert t223006000_x77(text2=22300405, mode4=1)
    """State 5"""
    return 0

def t223006000_x15():
    """State 0,1"""
    if not GetEventFlag(1043372731):
        """State 2,5"""
        SetEventFlag(1043372731, 1)
        """State 7"""
        # talk:22380000:"Ow!"
        assert t223006000_x78(text1=22380000, mode3=1)
    elif not GetEventFlag(1043372738):
        """State 3,6"""
        SetEventFlag(1043372738, 1)
        """State 8"""
        # talk:22380002:"Why'd you go and do that?"
        assert t223006000_x78(text1=22380002, mode3=1)
    else:
        """State 4"""
        pass
    """State 9"""
    return 0

def t223006000_x16():
    """State 0,1"""
    if not GetEventFlag(1039409255):
        """State 4"""
        # talk:22302000:"Good to see you! Master."
        assert t223006000_x76(text3=22302000, z6=1039409255, mode5=1)
    elif not GetEventFlag(1039519206):
        """State 2"""
        # talk:22302100:"Boc the seamster, at your service, Master."
        assert t223006000_x77(text2=22302100, mode4=1)
    else:
        """State 3"""
        # talk:22304300:"Boc the seamster, at your service, m'lord."
        assert t223006000_x77(text2=22304300, mode4=1)
    """State 5"""
    return 0

def t223006000_x17():
    """State 0,11"""
    # talk:22304000:"Master, may I ask you something?"
    assert t223006000_x77(text2=22304000, mode4=1)
    """State 1"""
    ClearTalkListData()
    c1_110()
    """State 2"""
    # action:22231002:"You may call me lord"
    AddTalkListData(1, 22231002, -1)
    # action:22231003:"Don't call me that"
    AddTalkListData(2, 22231003, -1)
    """State 3"""
    OpenConversationChoicesMenu(0)
    """State 6"""
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 7"""
    if GetTalkListEntryResult() == 1:
        """State 13"""
        # talk:22304100:"You don't say! Thank you, thank you!"
        assert t223006000_x76(text3=22304100, z6=1039519206, mode5=1)
        """State 9"""
        if not GetEventFlag(60805):
            """State 8"""
            # gesture:5:My Lord
            AcquireGesture(5)
            SetEventFlag(60805, 1)
            """State 4"""
            Label('L0')
            SetEventFlag(1039519205, 1)
        else:
            """State 10"""
            Goto('L0')
    elif GetTalkListEntryResult() == 2:
        """State 12"""
        # talk:22304200:"No, and why would you..."
        assert t223006000_x77(text2=22304200, mode4=1)
        Goto('L0')
    else:
        """State 5"""
        pass
    """State 14"""
    return 0

def t223006000_x18():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        c1_110()
        """State 8"""
        assert t223006000_x20()
        """State 11"""
        assert t223006000_x27()
        """State 2"""
        # action:22230000:"Alter garments"
        AddTalkListData(1, 22230000, -1)
        # action:22230011:"I have a favor to ask"
        AddTalkListDataIf(GetEventFlag(1039519208) == 1, 10, 22230011, -1)
        # action:22230012:"You may call me lord"
        AddTalkListDataIf(GetEventFlag(1039519207) == 1, 10, 22230012, -1)
        # action:22230001:"Don't tell me..."
        AddTalkListDataIf(GetEventFlag(1039409256) == 1, 25, 22230001, -1)
        # action:22230002:"I'm sorry..."
        AddTalkListDataIf(GetEventFlag(1036489205) == 1, 25, 22230002, -1)
        # action:22230003:"Give the Gold Sewing Needle"
        AddTalkListDataIf(GetEventFlag(1036489207) == 1, 25, 22230003, -1)
        # action:22230004:"Surely she'd be happy for you?"
        AddTalkListDataIf(GetEventFlag(1036489209) == 1, 25, 22230004, -1)
        # action:22230009:"I heard a voice"
        AddTalkListDataIf(GetEventFlag(1039409258) == 1, 50, 22230009, -1)
        # action:22230013:"Did you see it?"
        AddTalkListDataIf(GetEventFlag(11109307) == 1, 25, 22230013, -1)
        # action:22230010:"The voice was mine"
        AddTalkListDataIf(GetEventFlag(1039409261) == 1, 50, 22230010, -1)
        # action:22230005:"Have you ever thought so?"
        AddTalkListDataIf(GetEventFlag(11109805) == 1, 50, 22230005, -1)
        # action:22230007:"Please wait"
        AddTalkListDataIf(GetEventFlag(11109809) == 1, 50, 22230007, -1)
        # action:22230006:"Give a Larval Tear"
        AddTalkListDataIf(GetEventFlag(11109807) == 1, 50, 22230006, -1)
        # action:22230008:"What do you really think?"
        AddTalkListDataIf(GetEventFlag(11109811) == 1, 55, 22230008, -1)
        # action:20000009:"Leave"
        AddTalkListData(99, 20000009, -1)
        """State 3"""
        ShowShopMessage(1)
        """State 5"""
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 6"""
            OpenTailoringShop(110000, 110399)
            """State 7"""
            assert not (CheckSpecificPersonMenuIsOpen(26, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 10:
            """State 14"""
            assert t223006000_x45() and CheckSpecificPersonTalkHasEnded(0) == 1
        elif GetTalkListEntryResult() == 25:
            """State 9"""
            assert t223006000_x21() and CheckSpecificPersonTalkHasEnded(0) == 1
        elif GetTalkListEntryResult() == 50:
            """State 12"""
            assert t223006000_x28() and CheckSpecificPersonTalkHasEnded(0) == 1
        elif GetTalkListEntryResult() == 55:
            """State 13"""
            assert t223006000_x36() and CheckSpecificPersonTalkHasEnded(0) == 1
        else:
            """State 10"""
            def ExitPause():
                RequestAnimation(20038, -1)
            assert t223006000_x22()
            """State 15"""
            return 0

def t223006000_x19():
    """State 0,1"""
    if not GetEventFlag(1039409257):
        """State 2"""
        SetEventFlag(1039409256, 1)
        """State 4"""
        return 0
    else:
        """State 3,5"""
        return 1

def t223006000_x20():
    """State 0,1"""
    SetEventFlag(1039409256, 0)
    SetEventFlag(1039409258, 0)
    SetEventFlag(1039409261, 0)
    SetEventFlag(1036489205, 0)
    SetEventFlag(1036489207, 0)
    SetEventFlag(1036489209, 0)
    SetEventFlag(1039519207, 0)
    SetEventFlag(11109807, 0)
    SetEventFlag(11109809, 0)
    SetEventFlag(11109811, 0)
    SetEventFlag(11109805, 0)
    SetEventFlag(1039519208, 0)
    SetEventFlag(11109307, 0)
    """State 2"""
    return 0

def t223006000_x21():
    """State 0,1"""
    if GetEventFlag(1039409256) == 1:
        """State 2"""
        assert t223006000_x29()
    elif GetEventFlag(1036489205) == 1:
        """State 3"""
        assert t223006000_x30()
    elif GetEventFlag(1036489207) == 1:
        """State 4"""
        assert t223006000_x31()
    elif GetEventFlag(1036489209) == 1:
        """State 5"""
        assert t223006000_x32()
    elif GetEventFlag(11109307) == 1:
        """State 6"""
        assert t223006000_x44()
    """State 7"""
    return 0

def t223006000_x22():
    """State 0,2"""
    SetEventFlag(1039402712, 1)
    """State 1"""
    if not GetEventFlag(1039519206):
        """State 3"""
        # talk:22302200:"Oh, going so soon?"
        assert t223006000_x77(text2=22302200, mode4=1)
    else:
        """State 4"""
        # talk:22304400:"Going already, m'lord?"
        assert t223006000_x77(text2=22304400, mode4=1)
    """State 5"""
    return 0

def t223006000_x23():
    """State 0,6"""
    assert t223006000_x41()
    """State 5"""
    if GetEventFlag(1039409257) == 1 and not GetEventFlag(1036489206) and GetEventFlag(1036489211) == 1:
        """State 1"""
        SetEventFlag(1036489205, 1)
    # goods:8162:Gold Sewing Needle
    elif (ComparePlayerInventoryNumber(3, 8162, 4, 1, 0) == 1 and GetEventFlag(1036489206) == 1 and not
          GetEventFlag(1036489208)):
        """State 2"""
        SetEventFlag(1036489207, 1)
    elif GetEventFlag(1036489208) == 1 and not GetEventFlag(1036489210):
        """State 3"""
        SetEventFlag(1036489209, 1)
    else:
        """State 4,8"""
        return 1
    """State 7"""
    return 0

def t223006000_x24():
    """State 0,1"""
    if GetEventFlag(1039402710) == 1 and not GetEventFlag(1039409259):
        """State 2"""
        SetEventFlag(1039409258, 1)
    elif GetEventFlag(1039409259) == 1 and not GetEventFlag(1039409260):
        """State 3"""
        SetEventFlag(1039409261, 1)
    else:
        """State 4"""
        pass
    """State 5"""
    return 0

def t223006000_x25():
    """State 0,1"""
    if GetEventFlag(1036489208) == 1 and not GetEventFlag(1039519205):
        """State 4"""
        SetEventFlag(1039519208, 1)
    elif not GetEventFlag(1039519206) and GetEventFlag(1039519205) == 1:
        """State 2"""
        SetEventFlag(1039519207, 1)
    else:
        """State 3,6"""
        return 1
    """State 5"""
    return 0

def t223006000_x26():
    """State 0,9"""
    if GetEventFlag(11109806) == 1 and not GetEventFlag(11109808) and not GetEventFlag(11109812):
        """State 7"""
        if GetEventFlag(11109304) == 1:
            """State 4"""
            SetEventFlag(11109811, 1)
        else:
            """State 8"""
            pass
    else:
        pass
    """State 1"""
    if GetEventFlag(9118) == 1 and GetEventFlag(1036489208) == 1 and not GetEventFlag(11109806):
        """State 2"""
        SetEventFlag(11109805, 1)
    # goods:8185:Larval Tear
    elif (ComparePlayerInventoryNumber(3, 8185, 4, 1, 0) == 1 and GetEventFlag(11109806) == 1 and not
          GetEventFlag(11109808)):
        """State 3"""
        SetEventFlag(11109807, 1)
    elif GetEventFlag(11109808) == 1:
        """State 6"""
        SetEventFlag(11109809, 1)
    else:
        """State 5"""
        pass
    """State 10"""
    return 0

def t223006000_x27():
    """State 0,1"""
    if GetEventFlag(11109819) == 1 and not GetEventFlag(1039409260):
        """State 8"""
        assert t223006000_x26()
        """State 10"""
        Label('L0')
        call = t223006000_x43()
        if call.Get() == 1:
            """State 6"""
            Label('L1')
            call = t223006000_x23()
            if call.Get() == 1:
                """State 5"""
                Label('L2')
                call = t223006000_x19()
                if call.Get() == 1:
                    """State 2"""
                    Label('L3')
                elif call.Done():
                    pass
            elif call.Done():
                pass
        elif call.Done():
            pass
    elif GetEventFlag(11109819) == 1:
        Goto('L0')
    elif GetEventFlag(1036489213) == 1 or GetEventFlag(1039519209) == 1 or GetEventFlag(11109819) == 1:
        Goto('L1')
    elif (GetEventFlag(1039409264) == 1 or GetEventFlag(1036489213) == 1 or GetEventFlag(1039519209)
          == 1 or GetEventFlag(11109819) == 1):
        Goto('L2')
    else:
        Goto('L3')
    """State 9"""
    assert t223006000_x24()
    """State 3"""
    if GetEventFlag(1039519209) == 1 or GetEventFlag(11109819) == 1:
        """State 7"""
        assert t223006000_x25()
    else:
        """State 4"""
        pass
    """State 11"""
    return 0

def t223006000_x28():
    """State 0,1"""
    if GetEventFlag(1039409258) == 1:
        """State 2"""
        assert t223006000_x38()
    elif GetEventFlag(1039409261) == 1:
        """State 3"""
        assert t223006000_x39()
    elif GetEventFlag(11109805) == 1:
        """State 4"""
        assert t223006000_x34()
    elif GetEventFlag(11109807) == 1:
        """State 5"""
        assert t223006000_x35()
    elif GetEventFlag(11109809) == 1:
        """State 6"""
        assert t223006000_x37()
    """State 7"""
    return 0

def t223006000_x29():
    """State 0,1"""
    # talk:22302300:"Master, I was wondering..."
    assert t223006000_x76(text3=22302300, z6=1039409257, mode5=1)
    """State 2"""
    return 0

def t223006000_x30():
    """State 0,1"""
    # talk:22303000:"Master, my apologies."
    assert t223006000_x76(text3=22303000, z6=1036489206, mode5=1)
    """State 2"""
    return 0

def t223006000_x31():
    """State 0,2"""
    # talk:22303100:"Is that a gift for my undeserving self?"
    assert t223006000_x76(text3=22303100, z6=1036489208, mode5=1)
    """State 1"""
    # goods:8162:Gold Sewing Needle
    PlayerEquipmentQuantityChange(3, 8162, -1)
    """State 3"""
    return 0

def t223006000_x32():
    """State 0,1"""
    # talk:22303200:"Do you think that Mum would be pleased if she knew?"
    assert t223006000_x76(text3=22303200, z6=1036489210, mode5=1)
    """State 2"""
    return 0

def t223006000_x33():
    """State 0,4"""
    # talk:22304100:"You don't say! Thank you, thank you!"
    assert t223006000_x76(text3=22304100, z6=1039519206, mode5=1)
    """State 2"""
    if not GetEventFlag(60805):
        """State 1"""
        # gesture:5:My Lord
        AcquireGesture(5)
        SetEventFlag(60805, 1)
    else:
        """State 3"""
        pass
    """State 5"""
    return 0

def t223006000_x34():
    """State 0,1"""
    if not GetEventFlag(1039519206):
        """State 2"""
        # talk:22305400:"Master... Have you ever wished you might be born again?"
        assert t223006000_x76(text3=22305400, z6=11109806, mode5=1)
    else:
        """State 3"""
        # talk:22305000:"M'lord... Have you ever wished you might be born again?"
        assert t223006000_x76(text3=22305000, z6=11109806, mode5=1)
    """State 4"""
    return 0

def t223006000_x35():
    """State 0,2"""
    if not GetEventFlag(1039519206):
        """State 3"""
        # talk:22305500:"Master, what's this?"
        assert t223006000_x76(text3=22305500, z6=11109808, mode5=1)
    else:
        """State 4"""
        # talk:22305100:"M'lord, what's this?"
        assert t223006000_x76(text3=22305100, z6=11109808, mode5=1)
    """State 1"""
    # goods:8185:Larval Tear
    PlayerEquipmentQuantityChange(3, 8185, -1)
    """State 5"""
    return 0

def t223006000_x36():
    """State 0,1"""
    if not GetEventFlag(1039519206):
        """State 2"""
        # talk:22305700:"Master."
        assert t223006000_x76(text3=22305700, z6=11109812, mode5=1)
    else:
        """State 3"""
        # talk:22305300:"M'lord."
        assert t223006000_x76(text3=22305300, z6=11109812, mode5=1)
    """State 4"""
    return 0

def t223006000_x37():
    """State 0,1"""
    if not GetEventFlag(1039519206):
        """State 2"""
        # talk:22305600:"Master, it shouldn't take me long."
        assert t223006000_x76(text3=22305600, z6=11109810, mode5=1)
    else:
        """State 3"""
        # talk:22305200:"M'lord, it shouldn't take me long."
        assert t223006000_x76(text3=22305200, z6=11109810, mode5=1)
    """State 4"""
    return 0

def t223006000_x38():
    """State 0,6"""
    if not GetEventFlag(1039519206):
        """State 11"""
        # talk:22306500:"Did I just hear my mum speaking?"
        assert t223006000_x77(text2=22306500, mode4=1)
    else:
        """State 14"""
        # talk:22306000:"Did I just hear my mum speaking?"
        assert t223006000_x77(text2=22306000, mode4=1)
    """State 1"""
    ClearTalkListData()
    c1_110()
    """State 2"""
    # action:22231004:"That's right"
    AddTalkListData(1, 22231004, -1)
    # action:22231005:"Not at all"
    AddTalkListData(2, 22231005, -1)
    """State 3"""
    OpenConversationChoicesMenu(0)
    """State 9"""
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 10"""
    if GetTalkListEntryResult() == 1:
        """State 7"""
        if not GetEventFlag(1039519206):
            """State 13"""
            # talk:22306600:"<sob>"
            assert t223006000_x76(text3=22306600, z6=1039409260, mode5=1)
            """State 4"""
            Label('L0')
            SetEventFlag(1039409259, 1)
        else:
            """State 15"""
            # talk:22306100:"<sob>"
            assert t223006000_x76(text3=22306100, z6=1039409260, mode5=1)
            Goto('L0')
    elif GetTalkListEntryResult() == 2:
        """State 8"""
        if not GetEventFlag(1039519206):
            """State 12"""
            # talk:22306700:"No, why on earth would you..."
            assert t223006000_x77(text2=22306700, mode4=1)
            Goto('L0')
        else:
            """State 16"""
            # talk:22306200:"No, why on earth would you..."
            assert t223006000_x77(text2=22306200, mode4=1)
            Goto('L0')
    else:
        """State 5"""
        pass
    """State 17"""
    return 0

def t223006000_x39():
    """State 0,1"""
    if not GetEventFlag(1039519206):
        """State 2"""
        # talk:22306600:"<sob>"
        assert t223006000_x76(text3=22306600, z6=1039409260, mode5=1)
    else:
        """State 3"""
        # talk:22306100:"<sob>"
        assert t223006000_x76(text3=22306100, z6=1039409260, mode5=1)
    """State 4"""
    return 0

def t223006000_x40():
    """State 0,1"""
    if not GetEventFlag(1043372731):
        """State 2,5"""
        SetEventFlag(1043372731, 1)
        """State 7"""
        if not GetEventFlag(1039519206):
            """State 9"""
            # talk:22381000:"Ow!"
            assert t223006000_x78(text1=22381000, mode3=1)
        else:
            """State 11"""
            # talk:22382000:"Ow!"
            assert t223006000_x78(text1=22382000, mode3=1)
    elif not GetEventFlag(1043372738):
        """State 3,6"""
        SetEventFlag(1043372738, 1)
        """State 8"""
        if not GetEventFlag(1039519206):
            """State 10"""
            # talk:22381100:"Master, what's happened..."
            assert t223006000_x78(text1=22381100, mode3=1)
        else:
            """State 12"""
            # talk:22382100:"M'lord, what's happened..."
            assert t223006000_x78(text1=22382100, mode3=1)
    else:
        """State 4"""
        pass
    """State 13"""
    return 0

def t223006000_x41():
    """State 0,1"""
    # protector:460100:Elden Lord Armor, protector:470100:Radahn's Lion Armor, protector:480100:Lord of Blood's Robe, protector:760100:Maliketh's Armor, protector:770100:Malenia's Armor
    if (ComparePlayerInventoryNumber(1, 460100, 4, 1, 0) == 1 or ComparePlayerInventoryNumber(1, 470100,
        4, 1, 0) == 1 or ComparePlayerInventoryNumber(1, 480100, 4, 1, 0) == 1 or ComparePlayerInventoryNumber(1,
        760100, 4, 1, 0) == 1 or ComparePlayerInventoryNumber(1, 770100, 4, 1, 0) == 1):
        """State 2"""
        SetEventFlag(1036489211, 1)
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t223006000_x42():
    """State 0,1"""
    SetEventFlag(11109315, 1)
    """State 2"""
    # talk:22311000:"..."
    assert t223006000_x77(text2=22311000, mode4=1)
    """State 3"""
    return 0

def t223006000_x43():
    """State 0,1"""
    if not GetEventFlag(11109308) and not GetEventFlag(9116):
        """State 3"""
        SetEventFlag(11109307, 1)
        """State 4"""
        return 0
    else:
        """State 2,5"""
        return 1

def t223006000_x44():
    """State 0,1"""
    if not GetEventFlag(1039519206):
        """State 2"""
        # talk:22304500:"Master, did you see it?"
        assert t223006000_x76(text3=22304500, z6=11109308, mode5=1)
    else:
        """State 3"""
        # talk:22304600:"M'lord, did you see it?"
        assert t223006000_x76(text3=22304600, z6=11109308, mode5=1)
    """State 4"""
    return 0

def t223006000_x45():
    """State 0,1"""
    if GetEventFlag(1039519208) == 1:
        """State 3"""
        assert t223006000_x17()
    elif GetEventFlag(1039519207) == 1:
        """State 2"""
        assert t223006000_x33()
    """State 4"""
    return 0

def t223006000_x46(actionbutton1=_, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag4=6000):
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

def t223006000_x47():
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

def t223006000_x48():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t223006000_x49(lot1=102710):
    """State 0,1"""
    # lot:102710:Mushroom
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t223006000_x50(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t223006000_x66()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t223006000_x47()
    else:
        """State 4,7"""
        call = t223006000_x80()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t223006000_x47()
    """State 9"""
    return 0

def t223006000_x51():
    """State 0,1"""
    assert t223006000_x47()
    """State 2"""
    return 0

def t223006000_x52(flag1=3943, flag2=3941, flag3=3942, val1=5, val2=10, val3=12, val4=50, val5=50, actionbutton1=6280,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t223006000_x69(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t223006000_x68()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t223006000_x53(val1=5, val2=10, val3=12, val4=50, val5=50, actionbutton1=6280, flag4=6000, flag5=6001,
                   flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                   mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t223006000_x56(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t223006000_x60(val1=val1, z1=z1)
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
            call = t223006000_x62(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t223006000_x73() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t223006000_x58(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t223006000_x54(val2=10, val3=12):
    """State 0,1"""
    call = t223006000_x64(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t223006000_x50(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t223006000_x55(flag1=3943, val2=10, val3=12):
    """State 0,8"""
    assert t223006000_x82()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t223006000_x67()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t223006000_x47()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t223006000_x56(actionbutton1=6280, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t223006000_x57(z7=2000, val7=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t223006000_x46(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t223006000_x57(z7=_, val7=_):
    """State 0,1"""
    if f203(z7) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z7)
        assert f202() == val7
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t223006000_x58(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t223006000_x47()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t223006000_x59()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t223006000_x74()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t223006000_x59():
    """State 0,1"""
    assert t223006000_x57(z7=1101, val7=1101)
    """State 2"""
    return 0

def t223006000_x60(val1=5, z1=1):
    """State 0,2"""
    assert t223006000_x70()
    """State 1"""
    call = t223006000_x61()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t223006000_x72()
    """State 4"""
    return 0

def t223006000_x61():
    """State 0,1"""
    assert t223006000_x57(z7=1000, val7=1000)
    """State 2"""
    return 0

def t223006000_x62(val5=50):
    """State 0,1"""
    call = t223006000_x63()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t223006000_x73()
    """State 3"""
    return 0

def t223006000_x63():
    """State 0,1"""
    assert t223006000_x57(z7=1100, val7=1100)
    """State 2"""
    return 0

def t223006000_x64(val2=10, val3=12):
    """State 0,5"""
    assert t223006000_x82()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t223006000_x65()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t223006000_x75()
    """Unused"""
    """State 6"""
    return 0

def t223006000_x65():
    """State 0,2"""
    call = t223006000_x57(z7=1102, val7=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t223006000_x66():
    """State 0,1"""
    assert t223006000_x57(z7=1001, val7=1001)
    """State 2"""
    return 0

def t223006000_x67():
    """State 0,1"""
    assert t223006000_x57(z7=1103, val7=1103)
    """State 2"""
    return 0

def t223006000_x68():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t223006000_x69(flag1=3943, flag2=3941, flag3=3942, val1=5, val2=10, val3=12, val4=50, val5=50, actionbutton1=6280,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t223006000_x53(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                              flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                              z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t223006000_x55(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t223006000_x54(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t223006000_x81() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t223006000_x70():
    """State 0,1"""
    assert t223006000_x71()
    """State 2"""
    return 0

def t223006000_x71():
    """State 0,1"""
    assert t223006000_x57(z7=1104, val7=1104)
    """State 2"""
    return 0

def t223006000_x72():
    """State 0,1"""
    call = t223006000_x57(z7=1201, val7=1201)
    if call.Get() == 1:
        """State 2"""
        assert t223006000_x51()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t223006000_x73():
    """State 0,1"""
    call = t223006000_x57(z7=1300, val7=1300)
    if call.Get() == 1:
        """State 2"""
        assert t223006000_x51()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t223006000_x74():
    """State 0,1"""
    call = t223006000_x57(z7=1301, val7=1301)
    if call.Get() == 1:
        """State 2"""
        assert t223006000_x51()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t223006000_x75():
    """State 0,1"""
    call = t223006000_x57(z7=1302, val7=1302)
    if call.Get() == 1:
        """State 2"""
        assert t223006000_x51()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t223006000_x76(text3=_, z6=_, mode5=1):
    """State 0,5"""
    assert t223006000_x48() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text3, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode5:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(z6, 1)
    """State 6"""
    return 0

def t223006000_x77(text2=_, mode4=1):
    """State 0,4"""
    assert t223006000_x48() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t223006000_x78(text1=_, mode3=1):
    """State 0,4"""
    assert t223006000_x79() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t223006000_x79():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t223006000_x80():
    """State 0,1"""
    assert t223006000_x57(z7=1002, val7=1002)
    """State 2"""
    return 0

def t223006000_x81():
    """State 0,1"""
    assert t223006000_x47()
    """State 2"""
    return 0

def t223006000_x82():
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

