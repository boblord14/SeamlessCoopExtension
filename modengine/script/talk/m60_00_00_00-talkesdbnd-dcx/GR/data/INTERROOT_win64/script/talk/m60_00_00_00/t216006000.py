# -*- coding: utf-8 -*-
def t216006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t216006000_x34(flag1=3603, flag2=3601, flag3=3602, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1)
    Quit()

def t216006000_1000():
    """State 0,2,3"""
    assert t216006000_x0()
    """State 1"""
    c1_120(1000)
    Quit()

def t216006000_1001():
    """State 0,2,3"""
    assert t216006000_x1()
    """State 1"""
    c1_120(1001)
    Quit()

def t216006000_1101():
    """State 0,2,3"""
    assert t216006000_x2()
    """State 1"""
    c1_120(1101)
    Quit()

def t216006000_1102():
    """State 0,2,3"""
    t216006000_x3()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t216006000_1103():
    """State 0,2,3"""
    assert t216006000_x4()
    """State 1"""
    c1_120(1103)
    Quit()

def t216006000_2000():
    """State 0,2,3"""
    assert t216006000_x5(val6=10, z5=12)
    """State 1"""
    c1_120(2000)
    Quit()

def t216006000_x0():
    """State 0,1"""
    if GetEventFlag(3605) == 1:
        """State 4"""
        def WhilePaused():
            RequestAnimation(20030, -1)
        assert t216006000_x6()
    elif GetEventFlag(3607) == 1:
        """State 5"""
        def WhilePaused():
            RequestAnimation(20030, -1)
        assert t216006000_x7()
    elif GetEventFlag(3610) == 1:
        """State 6"""
        def WhilePaused():
            RequestAnimation(20030, -1)
        assert t216006000_x12()
    elif GetEventFlag(3611) == 1:
        """State 7"""
        Label('L0')
        def WhilePaused():
            RequestAnimation(20030, -1)
        assert t216006000_x14()
    elif GetEventFlag(3612) == 1:
        Goto('L0')
    elif GetEventFlag(3613) == 1:
        """State 8"""
        def WhilePaused():
            RequestAnimation(20030, -1)
        assert t216006000_x20()
    elif GetEventFlag(3615) == 1:
        """State 9"""
        def WhilePaused():
            RequestAnimation(20030, -1)
        assert t216006000_x23()
    else:
        """State 2"""
        pass
    """State 3"""
    SetEventFlag(1045379208, 1)
    """State 10"""
    return 0

def t216006000_x1():
    """State 0,1"""
    if GetEventFlag(3617) == 1:
        """State 3"""
        pass
    elif GetEventFlag(3615) == 1:
        """State 2,4"""
        # talk:21680900:"I am no bringer of bale."
        assert t216006000_x61(text1=21680900, mode3=1)
    else:
        """State 5"""
        # talk:21680400:"Hmph. Pathetic little man.", talk:21680500:"Don't show your face again."
        assert t216006000_x25(text3=21680400, text4=21680500)
    """State 6"""
    return 0

def t216006000_x2():
    """State 0,1"""
    if GetEventFlag(3605) == 1:
        """State 2"""
        # talk:21680000:"Oh?", talk:21680100:"What are you playing at?"
        assert t216006000_x27(flag9=1045372700, flag10=1045372701, text5=21680000, text6=21680100)
    elif GetEventFlag(3607) == 1:
        """State 3"""
        # talk:21680000:"Oh?", talk:21680100:"What are you playing at?"
        assert t216006000_x27(flag9=1044342700, flag10=1044342701, text5=21680000, text6=21680100)
    elif GetEventFlag(3610) == 1:
        """State 4"""
        # talk:21680000:"Oh?", talk:21680100:"What are you playing at?"
        assert t216006000_x27(flag9=12022730, flag10=12022731, text5=21680000, text6=21680100)
    elif GetEventFlag(3611) == 1:
        """State 5"""
        # talk:21680000:"Oh?", talk:21680100:"What are you playing at?"
        assert t216006000_x27(flag9=1051362730, flag10=1051362731, text5=21680000, text6=21680100)
    elif GetEventFlag(3613) == 1:
        """State 7"""
        # talk:21680000:"Oh?", talk:21680100:"What are you playing at?"
        assert t216006000_x27(flag9=1052382720, flag10=1052382721, text5=21680000, text6=21680100)
    elif GetEventFlag(3615) == 1:
        """State 6"""
        # talk:21680800:"Stop, please...", talk:21680810:"You think me a bringer of bale as well?"
        assert t216006000_x27(flag9=1044352710, flag10=1044352711, text5=21680800, text6=21680810)
    """State 8"""
    return 0

def t216006000_x3():
    """State 0,1"""
    if GetEventFlag(3605) == 1:
        """State 3"""
        # talk:21680200:"Fine.", talk:21680300:"Alright then.", talk:21681100:"Didn't I say? No harm can befall a shadow.", talk:21681200:"I...am shadowbound."
        assert (t216006000_x9(flag11=1045379202, text7=21680200, text8=21680300, text9=21681100, text10=21681200,
                text11=21681200, text12=21681200))
    elif GetEventFlag(3607) == 1:
        """State 5"""
        # talk:21680200:"Fine.", talk:21680300:"Alright then.", talk:21681100:"Didn't I say? No harm can befall a shadow.", talk:21681200:"I...am shadowbound."
        assert (t216006000_x9(flag11=1044349252, text7=21680200, text8=21680300, text9=21681100, text10=21681200,
                text11=21681200, text12=21681200))
    elif GetEventFlag(3610) == 1:
        """State 6"""
        # talk:21680200:"Fine.", talk:21680300:"Alright then.", talk:21681100:"Didn't I say? No harm can befall a shadow.", talk:21681200:"I...am shadowbound."
        assert (t216006000_x9(flag11=12029152, text7=21680200, text8=21680300, text9=21681100, text10=21681200,
                text11=21681200, text12=21681200))
    elif GetEventFlag(3611) == 1:
        """State 7"""
        # talk:21680200:"Fine.", talk:21680300:"Alright then.", talk:21681100:"Didn't I say? No harm can befall a shadow.", talk:21681200:"I...am shadowbound."
        assert (t216006000_x9(flag11=1051369352, text7=21680200, text8=21680300, text9=21681100, text10=21681200,
                text11=21681200, text12=21681200))
    elif GetEventFlag(3613) == 1:
        """State 9"""
        # talk:21680200:"Fine.", talk:21680300:"Alright then.", talk:21681100:"Didn't I say? No harm can befall a shadow.", talk:21681200:"I...am shadowbound."
        assert (t216006000_x9(flag11=1052389302, text7=21680200, text8=21680300, text9=21681100, text10=21681200,
                text11=21681200, text12=21681200))
    elif GetEventFlag(3615) == 1:
        """State 8"""
        # talk:21680820:"Fine. I am Ranni's shadow and it's for her that I fight.", talk:21681100:"Didn't I say? No harm can befall a shadow.", talk:21681200:"I...am shadowbound."
        assert (t216006000_x9(flag11=1044359252, text7=21680820, text8=21680820, text9=21681100, text10=21681200,
                text11=21681200, text12=21681200))
    elif GetEventFlag(3617) == 1:
        """State 4"""
        assert t216006000_x10()
    """State 2"""
    Quit()
    """Unused"""
    """State 10"""
    return 0

def t216006000_x4():
    """State 0,1"""
    if GetEventFlag(3617) == 1:
        """State 3"""
        pass
    elif GetEventFlag(3615) == 1:
        """State 2,4"""
        # talk:21681000:"Tell...me..."
        assert t216006000_x61(text1=21681000, mode3=1)
    else:
        """State 5"""
        # talk:21680600:"You're...you're strong of arm.", talk:21680700:"Traitorous wretch..."
        assert t216006000_x26(text1=21680600, text2=21680700)
    """State 6"""
    return 0

def t216006000_x5(val6=10, z5=12):
    """State 0"""
    while True:
        """State 3"""
        if GetEventFlag(3605) == 1:
            """State 2,6"""
            call = t216006000_x8(val6=val6, z5=z5)
            if call.Done():
                break
            elif not GetEventFlag(3605):
                pass
        elif GetEventFlag(3611) == 1 or GetEventFlag(3612) == 1:
            """State 7"""
            # actionbutton:6000:"Talk"
            call = t216006000_x28(actionbutton1=6000, flag5=6001, flag12=6000, flag13=6000, flag14=6000,
                                  flag15=6000, flag4=6000)
            if call.Done():
                """State 4"""
                SetEventFlag(1051369358, 1)
                break
            elif not GetEventFlag(3611) and not GetEventFlag(3612):
                pass
        elif GetEventFlag(3617) == 1:
            """State 8"""
            call = t216006000_x10()
            if call.Done():
                break
            elif not GetEventFlag(3617):
                pass
        elif (GetEventFlag(3607) == 1 or GetEventFlag(3610) == 1 or GetEventFlag(3613) == 1 or GetEventFlag(3615)
              == 1):
            """State 1,5"""
            # actionbutton:6000:"Talk"
            call = t216006000_x28(actionbutton1=6000, flag5=6001, flag12=6000, flag13=6000, flag14=6000,
                                  flag15=6000, flag4=6000)
            if call.Done():
                break
            elif (not GetEventFlag(3607) and not GetEventFlag(3610) and not GetEventFlag(3613) and not
                  GetEventFlag(3615)):
                pass
    """State 9"""
    return 0

def t216006000_x6():
    """State 0,1"""
    if not GetEventFlag(1045379205):
        """State 2,4"""
        # talk:21600200:"Who goes there?"
        assert t216006000_x58(text14=21600200, z6=1045379205, mode6=1)
    else:
        """State 3,5"""
        # talk:21600300:"Darriwil is nothing but a traitor."
        assert t216006000_x59(text13=21600300, mode5=1)
    """State 6"""
    return 0

def t216006000_x7():
    """State 0,1"""
    if not GetEventFlag(1044349255):
        """State 2,5"""
        # talk:21602000:"...Right. There you are."
        assert t216006000_x58(text14=21602000, z6=1044349255, mode6=1)
        """State 6"""
        # lot:101500:Somber Smithing Stone [2]
        assert t216006000_x31(lot1=101500)
    elif not GetEventFlag(1044349256):
        """State 3,7"""
        # talk:21602100:"Oh yes, I should say,"
        assert t216006000_x58(text14=21602100, z6=1044349256, mode6=1)
    else:
        """State 4,8"""
        # talk:21602200:"That's enough chit-chat for now."
        assert t216006000_x59(text13=21602200, mode5=1)
    """State 9"""
    return 0

def t216006000_x8(val6=10, z5=12):
    """State 0,5"""
    if GetEventFlag(1045370711) == 1:
        """State 6"""
        Label('L0')
        # actionbutton:6000:"Talk"
        assert (t216006000_x28(actionbutton1=6000, flag5=6001, flag12=6000, flag13=6000, flag14=6000,
                flag15=6000, flag4=6000))
    else:
        """State 7"""
        call = t216006000_x11()
        assert GetEventFlag(1045370711) == 1
        """State 8"""
        assert t216006000_x29()
        """State 1"""
        assert GetEventFlag(1045372707) == 1
        """State 2"""
        if GetDistanceToPlayer() < val6:
            """State 4"""
            pass
        else:
            """State 3"""
            Goto('L0')
    """State 9"""
    return 0

def t216006000_x9(flag11=_, text7=_, text8=_, text9=21681100, text10=21681200, text11=21681200, text12=21681200):
    """State 0,2"""
    if not GetEventFlag(flag11):
        """State 4"""
        if GetEventFlag(1045379207) == 1:
            """State 6"""
            assert t216006000_x24(flag11=flag11, text7=text9, text8=text10)
        elif GetEventFlag(1045379209) == 1:
            """State 7"""
            assert t216006000_x24(flag11=flag11, text7=text11, text8=text12)
        else:
            """State 5"""
            assert t216006000_x24(flag11=flag11, text7=text7, text8=text8)
    else:
        """State 3"""
        pass
    """State 1"""
    Quit()
    """Unused"""
    """State 8"""
    return 0

def t216006000_x10():
    """State 0"""
    while True:
        """State 2"""
        if not GetEventFlag(1034509225) and GetDistanceToPlayer() < 50 and not GetEventFlag(1034502700):
            """State 1,3"""
            # talk:21612000:"..."
            call = t216006000_x60(text5=21612000, flag9=1034509225, mode4=1)
            def WhilePaused():
                c5_121(not CheckSpecificPersonTalkHasEnded(0), 9625)
            if call.Done() and CheckSpecificPersonTalkHasEnded(0) == 1:
                pass
            elif GetEventFlag(1034502700) == 1:
                pass
            elif GetDistanceToPlayer() > 60:
                """State 5"""
                assert t216006000_x29()
        elif not GetEventFlag(1034509226) and GetEventFlag(1034502700) == 1 and GetDistanceToPlayer() < 70:
            """State 4"""
            # talk:21612100:"<growling>"
            call = t216006000_x60(text5=21612100, flag9=1034509226, mode4=1)
            def WhilePaused():
                c5_121(not CheckSpecificPersonTalkHasEnded(0), 9625)
            if call.Done() and CheckSpecificPersonTalkHasEnded(0) == 1:
                pass
            elif GetDistanceToPlayer() > 80:
                """State 6"""
                assert t216006000_x29()
    """Unused"""
    """State 7"""
    return 0

def t216006000_x11():
    """State 0"""
    while True:
        """State 2"""
        if GetEventFlag(1045379220) == 1:
            """State 1,5"""
            SetEventFlag(1045379220, 0)
            SetEventFlag(1045379206, 1)
            """State 10"""
            # talk:21600100:"<howl>"
            assert t216006000_x61(text1=21600100, mode3=1)
            """State 3"""
            def WhilePaused():
                c5_121(not CheckSpecificPersonTalkHasEnded(0), 9625)
            def ExitPause():
                SetEventFlag(1045372705, 1)
            if GetDistanceToPlayer() > 155:
                pass
            elif CheckSpecificPersonTalkHasEnded(0) == 1:
                continue
            elif GetEventFlag(1045379222) == 1:
                """State 4"""
                Label('L0')
                """State 6"""
                SetEventFlag(1045379222, 0)
                """State 8"""
                SetEventFlag(1045372705, 1)
                SetEventFlag(1045379206, 1)
                """State 11"""
                # talk:21600100:"<howl>"
                assert t216006000_x61(text1=21600100, mode3=1)
                """State 7"""
                def WhilePaused():
                    c5_121(not CheckSpecificPersonTalkHasEnded(0), 9625)
                def ExitPause():
                    SetEventFlag(1045372706, 1)
                if GetDistanceToPlayer() > 45:
                    pass
                elif CheckSpecificPersonTalkHasEnded(0) == 1:
                    continue
        elif GetEventFlag(1045379222) == 1:
            Goto('L0')
        """State 9"""
        call = t216006000_x29()
        if call.Done():
            pass
        elif call.Done():
            pass
    """Unused"""
    """State 12"""
    return 0

def t216006000_x12():
    """State 0,1"""
    if GetEventFlag(12029155) == 1:
        """State 2"""
        if GetEventFlag(12029156) == 1:
            """State 3"""
            if not GetEventFlag(1034509330) and not GetEventFlag(1034499224):
                """State 7"""
                # talk:21604300:"Leave this place to me. You just do what you feel is right."
                assert t216006000_x59(text13=21604300, mode5=1)
            else:
                """State 4"""
                if GetEventFlag(12029157) == 1:
                    """State 9"""
                    # talk:21605100:"You're coming too, right? To Radahn's festivities..."
                    assert t216006000_x59(text13=21605100, mode5=1)
                else:
                    """State 8"""
                    assert t216006000_x13()
        else:
            """State 6"""
            # talk:21604100:"I jest, I wouldn't go that far."
            assert t216006000_x58(text14=21604100, z6=12029156, mode6=1)
    else:
        """State 5"""
        # talk:21604000:"Ah, good to see you."
        assert t216006000_x58(text14=21604000, z6=12029155, mode6=1)
    """State 10"""
    return 0

def t216006000_x13():
    """State 0,8"""
    # talk:21604200:"Ah. Well met."
    assert t216006000_x59(text13=21604200, mode5=1)
    """State 2"""
    c1_110()
    """State 3"""
    ClearTalkListData()
    """State 4"""
    if GetEventFlag(1034499224) == 1 or GetEventFlag(1044369223) == 1:
        """State 1"""
        # action:22161001:"Tell Sellen's story"
        AddTalkListDataIf(GetEventFlag(1044369223) == 1, 2, 22161001, -1)
        # action:22161003:"Tell Iji's story"
        AddTalkListDataIf(GetEventFlag(1034499224) == 1, 3, 22161003, -1)
        # action:22161002:"Don't say anything"
        AddTalkListData(4, 22161002, -1)
    else:
        """State 5"""
        # action:22161000:"I still don't understand"
        AddTalkListData(1, 22161000, -1)
    """State 6"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 7"""
    if GetTalkListEntryResult() == 1:
        """State 9"""
        Label('L0')
        # talk:21605200:"Right. I see."
        assert t216006000_x59(text13=21605200, mode5=1)
    elif GetTalkListEntryResult() == 2:
        """State 11"""
        # talk:21605000:"Hmm..."
        assert t216006000_x58(text14=21605000, z6=12029157, mode6=1)
    elif GetTalkListEntryResult() == 3:
        """State 10"""
        # talk:21605300:"Hmm..."
        assert t216006000_x58(text14=21605300, z6=12029157, mode6=1)
    elif GetTalkListEntryResult() == 4:
        Goto('L0')
    else:
        pass
    """State 12"""
    return 0

def t216006000_x14():
    """State 0,1"""
    if GetEventFlag(1034509410) == 1:
        """State 2"""
        assert t216006000_x15()
    else:
        """State 3"""
        assert t216006000_x16()
    """State 4"""
    return 0

def t216006000_x15():
    """State 0,1"""
    if GetEventFlag(1051369355) == 1:
        """State 3"""
        assert t216006000_x18()
    else:
        """State 2"""
        assert t216006000_x17()
    """State 4"""
    return 0

def t216006000_x16():
    """State 0,1"""
    if GetEventFlag(1051369355) == 1:
        """State 3"""
        # talk:21606600:"Hm. Nothing to do but wait. Until the festival begins."
        assert t216006000_x59(text13=21606600, mode5=1)
    else:
        """State 2"""
        assert t216006000_x19()
    """State 4"""
    return 0

def t216006000_x17():
    """State 0,1"""
    if GetEventFlag(12029157) == 1:
        """State 2"""
        # talk:21606000:"Ah, there you are. Took your sweet time."
        assert t216006000_x58(text14=21606000, z6=1051369355, mode6=1)
    else:
        """State 3"""
        # talk:21606300:"Ah, thought I might find you here."
        assert t216006000_x58(text14=21606300, z6=1051369355, mode6=1)
    """State 4"""
    return 0

def t216006000_x18():
    """State 0,1"""
    if GetEventFlag(1044349258) == 1:
        """State 2"""
        # talk:21606100:"Once more into the fray together, eh."
        assert t216006000_x59(text13=21606100, mode5=1)
    else:
        """State 3"""
        # talk:21606200:"Into the fray together, eh."
        assert t216006000_x59(text13=21606200, mode5=1)
    """State 4"""
    return 0

def t216006000_x19():
    """State 0,1"""
    if GetEventFlag(1045379208) == 1:
        """State 3"""
        # talk:21606400:"Hm. Long time."
        assert t216006000_x58(text14=21606400, z6=1051369355, mode6=1)
    else:
        """State 4"""
        # talk:21606500:"Mm... As a fellow combatant, allow me to introduce myself."
        assert t216006000_x58(text14=21606500, z6=1051369355, mode6=1)
        """State 2"""
        SetEventFlag(1045379208, 1)
    """State 5"""
    return 0

def t216006000_x20():
    """State 0,1"""
    if GetEventFlag(1034509412) == 1:
        """State 2"""
        assert t216006000_x21()
    else:
        """State 3"""
        assert t216006000_x22()
    """State 4"""
    return 0

def t216006000_x21():
    """State 0,1"""
    if GetEventFlag(1052389305) == 1:
        """State 4"""
        # talk:21608100:"Let's meet where the falling star bit the earth."
        assert t216006000_x59(text13=21608100, mode5=1)
    else:
        """State 3"""
        # talk:21608000:"Ah, good. I was waiting for you."
        assert t216006000_x58(text14=21608000, z6=1052389305, mode6=1)
        """State 2"""
        SetEventFlag(1052389306, 1)
    """State 5"""
    return 0

def t216006000_x22():
    """State 0,1"""
    if GetEventFlag(1052389305) == 1:
        """State 2"""
        if GetEventFlag(1052389307) == 1:
            """State 6"""
            # talk:21608400:"If it's on the cards, I'd be glad to meet again."
            assert t216006000_x59(text13=21608400, mode5=1)
        else:
            """State 5"""
            # talk:21608300:"Well, it's time I left."
            assert t216006000_x58(text14=21608300, z6=1052389307, mode6=1)
            """State 3"""
            SetEventFlag(1052389306, 1)
    else:
        """State 4"""
        # talk:21608200:"Hmph, what a sick way to fight, eh mate."
        assert t216006000_x58(text14=21608200, z6=1052389305, mode6=1)
    """State 7"""
    return 0

def t216006000_x23():
    """State 0,1"""
    if GetEventFlag(1044359256) == 1:
        """State 3"""
        # talk:21611100:"I'm going to see mistress Ranni, now."
        assert t216006000_x59(text13=21611100, mode5=1)
    else:
        """State 2"""
        # talk:21611000:"My thanks, friend."
        assert t216006000_x58(text14=21611000, z6=1044359256, mode6=1)
    """State 4"""
    return 0

def t216006000_x24(flag11=_, text7=_, text8=_):
    """State 0,1"""
    if GetEventFlag(1034509410) == 1:
        """State 3"""
        t216006000_x60(text5=text8, flag9=flag11, mode4=1)
        Quit()
    else:
        """State 2"""
        t216006000_x60(text5=text7, flag9=flag11, mode4=1)
        Quit()
    """Unused"""
    """State 4"""
    return 0

def t216006000_x25(text3=21680400, text4=21680500):
    """State 0,1"""
    if GetEventFlag(1034509410) == 1:
        """State 2"""
        assert t216006000_x61(text1=text4, mode3=1)
    else:
        """State 3"""
        assert t216006000_x61(text1=text3, mode3=1)
    """State 4"""
    return 0

def t216006000_x26(text1=21680600, text2=21680700):
    """State 0,1"""
    if GetEventFlag(1034509410) == 1:
        """State 3"""
        assert t216006000_x61(text1=text2, mode3=1)
    else:
        """State 2"""
        assert t216006000_x61(text1=text1, mode3=1)
    """State 4"""
    return 0

def t216006000_x27(flag9=_, flag10=_, text5=_, text6=_):
    """State 0,1"""
    if not GetEventFlag(flag9):
        """State 3"""
        assert t216006000_x60(text5=text5, flag9=flag9, mode4=1)
    elif not GetEventFlag(flag10):
        """State 4"""
        assert t216006000_x60(text5=text6, flag9=flag10, mode4=1)
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t216006000_x28(actionbutton1=6000, flag5=6001, flag12=6000, flag13=6000, flag14=6000, flag15=6000,
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

def t216006000_x29():
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

def t216006000_x30():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t216006000_x31(lot1=101500):
    """State 0,1"""
    # lot:101500:Somber Smithing Stone [2]
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t216006000_x32(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t216006000_x48()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t216006000_x29()
    else:
        """State 4,7"""
        call = t216006000_x63()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t216006000_x29()
    """State 9"""
    return 0

def t216006000_x33():
    """State 0,1"""
    assert t216006000_x29()
    """State 2"""
    return 0

def t216006000_x34(flag1=3603, flag2=3601, flag3=3602, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t216006000_x51(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t216006000_x50()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t216006000_x35(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                   flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                   mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t216006000_x38(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t216006000_x42(val1=val1, z1=z1)
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
            call = t216006000_x44(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t216006000_x55() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t216006000_x40(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t216006000_x36(val2=10, val3=12):
    """State 0,1"""
    call = t216006000_x46(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t216006000_x32(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t216006000_x37(flag1=3603, val2=10, val3=12):
    """State 0,8"""
    assert t216006000_x65()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t216006000_x49()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t216006000_x29()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t216006000_x38(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t216006000_x39(z7=2000, val7=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t216006000_x28(actionbutton1=actionbutton1, flag5=flag5, flag12=6000, flag13=6000, flag14=6000,
                flag15=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t216006000_x39(z7=_, val7=_):
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

def t216006000_x40(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t216006000_x29()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t216006000_x41()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t216006000_x56()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t216006000_x41():
    """State 0,1"""
    assert t216006000_x39(z7=1101, val7=1101)
    """State 2"""
    return 0

def t216006000_x42(val1=5, z1=1):
    """State 0,2"""
    assert t216006000_x52()
    """State 1"""
    call = t216006000_x43()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t216006000_x54()
    """State 4"""
    return 0

def t216006000_x43():
    """State 0,1"""
    assert t216006000_x39(z7=1000, val7=1000)
    """State 2"""
    return 0

def t216006000_x44(val5=12):
    """State 0,1"""
    call = t216006000_x45()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t216006000_x55()
    """State 3"""
    return 0

def t216006000_x45():
    """State 0,1"""
    assert t216006000_x39(z7=1100, val7=1100)
    """State 2"""
    return 0

def t216006000_x46(val2=10, val3=12):
    """State 0,5"""
    assert t216006000_x65()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t216006000_x47()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t216006000_x57()
    """Unused"""
    """State 6"""
    return 0

def t216006000_x47():
    """State 0,2"""
    call = t216006000_x39(z7=1102, val7=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t216006000_x48():
    """State 0,1"""
    assert t216006000_x39(z7=1001, val7=1001)
    """State 2"""
    return 0

def t216006000_x49():
    """State 0,1"""
    assert t216006000_x39(z7=1103, val7=1103)
    """State 2"""
    return 0

def t216006000_x50():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t216006000_x51(flag1=3603, flag2=3601, flag3=3602, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t216006000_x35(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                              flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                              z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t216006000_x37(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t216006000_x36(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t216006000_x64() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t216006000_x52():
    """State 0,1"""
    assert t216006000_x53()
    """State 2"""
    return 0

def t216006000_x53():
    """State 0,1"""
    assert t216006000_x39(z7=1104, val7=1104)
    """State 2"""
    return 0

def t216006000_x54():
    """State 0,1"""
    call = t216006000_x39(z7=1201, val7=1201)
    if call.Get() == 1:
        """State 2"""
        assert t216006000_x33()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t216006000_x55():
    """State 0,1"""
    call = t216006000_x39(z7=1300, val7=1300)
    if call.Get() == 1:
        """State 2"""
        assert t216006000_x33()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t216006000_x56():
    """State 0,1"""
    call = t216006000_x39(z7=1301, val7=1301)
    if call.Get() == 1:
        """State 2"""
        assert t216006000_x33()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t216006000_x57():
    """State 0,1"""
    call = t216006000_x39(z7=1302, val7=1302)
    if call.Get() == 1:
        """State 2"""
        assert t216006000_x33()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t216006000_x58(text14=_, z6=_, mode6=1):
    """State 0,5"""
    assert t216006000_x30() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text14, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode6:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(z6, 1)
    """State 6"""
    return 0

def t216006000_x59(text13=_, mode5=1):
    """State 0,4"""
    assert t216006000_x30() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text13, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode5:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t216006000_x60(text5=_, flag9=_, mode4=1):
    """State 0,5"""
    assert t216006000_x62() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(flag9, 1)
    """State 1"""
    TalkToPlayer(text5, -1, -1, 1)
    """State 4"""
    if not mode4:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t216006000_x61(text1=_, mode3=1):
    """State 0,4"""
    assert t216006000_x62() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t216006000_x62():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t216006000_x63():
    """State 0,1"""
    assert t216006000_x39(z7=1002, val7=1002)
    """State 2"""
    return 0

def t216006000_x64():
    """State 0,1"""
    assert t216006000_x29()
    """State 2"""
    return 0

def t216006000_x65():
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

