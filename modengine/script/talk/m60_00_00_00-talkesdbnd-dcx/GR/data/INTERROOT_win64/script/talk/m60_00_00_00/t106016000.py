# -*- coding: utf-8 -*-
def t106016000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t106016000_x40(flag1=3743, flag2=3741, flag3=3742, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1)
    Quit()

def t106016000_1000():
    """State 0,2,3"""
    assert t106016000_x0()
    """State 1"""
    c1_120(1000)
    Quit()

def t106016000_1101():
    """State 0,2,3"""
    assert t106016000_x1()
    """State 1"""
    c1_120(1101)
    Quit()

def t106016000_1102():
    """State 0,2,3"""
    t106016000_x2()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t106016000_2000():
    """State 0,2,3"""
    assert t106016000_x3()
    """State 1"""
    c1_120(2000)
    Quit()

def t106016000_x0():
    """State 0,2"""
    if GetEventFlag(3747) == 1:
        """State 3"""
        def WhilePaused():
            RequestAnimation(20000, -1)
            c1_139(-1, 10000)
        assert t106016000_x9()
    elif GetEventFlag(3748) == 1:
        """State 4"""
        assert t106016000_x31()
    else:
        """State 1"""
        pass
    """State 5"""
    return 0

def t106016000_x1():
    """State 0,1,2"""
    SetEventFlag(1034502745, 1)
    """State 3"""
    RequestAnimation(20008, -1)
    assert t106016000_x5(flag9=1034502740, flag10=1034502741)
    """State 4"""
    return 0

def t106016000_x2():
    """State 0,1"""
    assert not GetEventFlag(1034509403) and not GetEventFlag(1034502743)
    """State 3"""
    SetEventFlag(1034502742, 1)
    # talk:10630020:"To think such was thy plot."
    def WhilePaused():
        RequestAnimation(20000, -1)
    def ExitPause():
        SetEventFlag(1034502742, 0)
    assert (t106016000_x66(text1=10630020, flag9=1034509403, mode3=1) and CheckSpecificPersonTalkHasEnded(0)
            == 1)
    """State 2"""
    def WhilePaused():
        RequestAnimation(20000, -1)
    Quit()
    """Unused"""
    """State 4"""
    return 0

def t106016000_x3():
    """State 0"""
    while Loop('mainloop'):
        """State 2"""
        Label('L0')
        SetEventFlag(1034509422, 0)
        while True:
            """State 1"""
            if GetEventFlag(3747) == 1:
                """State 6"""
                call = t106016000_x4()
                if call.Done():
                    break
                elif not GetEventFlag(3747):
                    pass
            elif GetEventFlag(3748) == 1:
                """State 9"""
                call = t106016000_x32()
                if call.Done():
                    """State 3"""
                    if GetEventFlag(1034509422) == 1:
                        """State 7"""
                        call = t106016000_x30()
                        if call.Get() == 0:
                            break
                        elif call.Done():
                            Continue('mainloop')
                        elif GetDistanceToPlayer() > 5:
                            Break('mainloop')
                    else:
                        """State 4"""
                        # goods:8159:Fingerslayer Blade
                        if (ComparePlayerInventoryNumber(3, 8159, 4, 1, 0) == 1 or GetEventFlag(1034509420)
                            == 1):
                            """State 5"""
                            SetEventFlag(1034502745, 1)
                            break
                        else:
                            break
                elif not GetEventFlag(3748):
                    pass
        """State 10"""
        return 0
    """State 8"""
    assert t106016000_x35()
    Goto('L0')

def t106016000_x4():
    """State 0,1"""
    if GetEventFlag(1034509432) == 1 and not GetEventFlag(1034509409):
        """State 3"""
        # actionbutton:6413:"Where did the body go?"
        assert (t106016000_x34(actionbutton1=6413, flag5=6001, flag11=6000, flag12=6000, flag13=6000,
                flag14=6000, flag4=6000))
    else:
        """State 2"""
        # actionbutton:6000:"Talk"
        assert (t106016000_x34(actionbutton1=6000, flag5=6001, flag11=6000, flag12=6000, flag13=6000,
                flag14=6000, flag4=6000))
    """State 4"""
    return 0

def t106016000_x5(flag9=1034502740, flag10=1034502741):
    """State 0,1"""
    if not GetEventFlag(flag9):
        """State 3"""
        # talk:10630000:"What hopest thou to profit?"
        assert t106016000_x66(text1=10630000, flag9=flag9, mode3=1)
    elif not GetEventFlag(flag10):
        """State 4"""
        # talk:10630010:"..."
        assert t106016000_x66(text1=10630010, flag9=flag10, mode3=1)
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t106016000_x6():
    """State 0,1"""
    if GetEventFlag(1034509405) == 1:
        """State 2"""
        Label('L0')
        """State 5"""
        assert t106016000_x7()
    elif GetEventFlag(1034509431) == 1:
        """State 4"""
        Label('L1')
        """State 6"""
        assert t106016000_x15()
    else:
        """State 3"""
        if GetEventFlag(11109506) == 1:
            Goto('L0')
        else:
            Goto('L1')
    """State 7"""
    return 0

def t106016000_x7():
    """State 0,1"""
    if GetEventFlag(1034509432) == 1:
        """State 3"""
        assert t106016000_x13()
    else:
        """State 2"""
        assert t106016000_x12()
    """State 4"""
    return 0

def t106016000_x8():
    """State 0,1"""
    if GetEventFlag(1042369405) == 1:
        """State 8"""
        # talk:10610100:"Oh, again we cross paths."
        assert t106016000_x65(text2=10610100, mode4=1)
    else:
        """State 9"""
        # talk:10610200:"Mm? a Tarnished, here?"
        assert t106016000_x65(text2=10610200, mode4=1)
    """State 2"""
    c1_110()
    """State 3"""
    ClearTalkListData()
    """State 4"""
    # action:21061006:"No particular reason"
    AddTalkListData(1, 21061006, -1)
    """State 5"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 6"""
    if GetTalkListEntryResult() == 1:
        """State 7"""
        if GetEventFlag(1042369406) == 1:
            """State 10"""
            # talk:10612000:"No reason in particular, thou claimest?"
            assert t106016000_x65(text2=10612000, mode4=1)
        else:
            """State 12"""
            # talk:10612050:"No reason in particular, thou claimest?"
            assert t106016000_x65(text2=10612050, mode4=1)
        """State 11"""
        assert t106016000_x14()
    else:
        pass
    """State 13"""
    return 0

def t106016000_x9():
    """State 0,1"""
    if GetEventFlag(1034509410) == 1:
        """State 2"""
        if GetEventFlag(1034509417) == 1:
            """State 5"""
            assert t106016000_x11()
        else:
            """State 4"""
            assert t106016000_x10()
    else:
        """State 3"""
        assert t106016000_x6()
    """State 6"""
    return 0

def t106016000_x10():
    """State 0,1"""
    if GetEventFlag(1034509412) == 1:
        """State 2"""
        assert t106016000_x17()
    else:
        """State 3"""
        assert t106016000_x18()
    """State 4"""
    return 0

def t106016000_x11():
    """State 0,1"""
    if GetEventFlag(1034509416) == 1:
        """State 3"""
        # talk:10614100:"I shall soon enter my slumber."
        assert t106016000_x65(text2=10614100, mode4=1)
    else:
        """State 2"""
        # talk:10614000:"Ah, allow me to forewarn thee."
        assert t106016000_x64(text3=10614000, z5=1034509416, mode5=1)
    """State 4"""
    return 0

def t106016000_x12():
    """State 0,1"""
    if GetEventFlag(1042369405) == 1:
        """State 8"""
        # talk:10610100:"Oh, again we cross paths."
        assert t106016000_x65(text2=10610100, mode4=1)
    else:
        """State 9"""
        # talk:10610200:"Mm? a Tarnished, here?"
        assert t106016000_x65(text2=10610200, mode4=1)
    """State 2"""
    c1_110()
    """State 5"""
    ClearTalkListData()
    """State 3"""
    # action:21061004:"You must be Ranni the Witch, behind the Night of the Black Knives"
    AddTalkListData(1, 21061004, -1)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 7"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 4"""
    if GetTalkListEntryResult() == 1:
        """State 10"""
        # talk:10611000:"I see. Quite the sleuth, aren't we."
        assert t106016000_x64(text3=10611000, z5=1034509432, mode5=1)
        """State 6"""
        SetEventFlag(1034509405, 1)
    else:
        pass
    """State 11"""
    return 0

def t106016000_x13():
    """State 0,1"""
    if not GetEventFlag(1034509409):
        """State 8"""
        # talk:10611100:"And why should I reveal that to thee?"
        assert t106016000_x64(text3=10611100, z5=1034509409, mode5=1)
    else:
        """State 9"""
        # talk:10611200:"The cursemark thou seekest is not here. That is all I will say."
        assert t106016000_x65(text2=10611200, mode4=1)
    """State 2"""
    if GetEventFlag(11109518) == 1:
        """State 3"""
        c1_110()
        """State 4"""
        ClearTalkListData()
        """State 5"""
        # action:21061005:"I wish to serve you"
        AddTalkListData(1, 21061005, -1)
        """State 6"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 7"""
        if GetTalkListEntryResult() == 1:
            """State 10"""
            # talk:10611300:"Oh, is that so?"
            assert t106016000_x64(text3=10611300, z5=1034509410, mode5=1)
        else:
            pass
    else:
        pass
    """State 11"""
    return 0

def t106016000_x14():
    """State 0,1"""
    c1_110()
    """State 2"""
    ClearTalkListData()
    """State 3"""
    # action:21061007:"Serve Ranni the Witch"
    AddTalkListData(1, 21061007, -1)
    # action:21061008:"Do not serve"
    AddTalkListData(2, 21061008, -1)
    """State 4"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 5"""
    if GetTalkListEntryResult() == 1:
        """State 7"""
        # talk:10612100:"I see. A choice well made."
        assert t106016000_x64(text3=10612100, z5=1034509410, mode5=1)
        """State 6"""
        Label('L0')
        SetEventFlag(1034509431, 1)
    elif GetTalkListEntryResult() == 2:
        """State 8"""
        # talk:10612200:"I see. More's the pity."
        assert t106016000_x64(text3=10612200, z5=1034509411, mode5=1)
        Goto('L0')
    else:
        pass
    """State 9"""
    return 0

def t106016000_x15():
    """State 0,1"""
    if GetEventFlag(1034509411) == 1:
        """State 3"""
        assert t106016000_x16()
    else:
        """State 2"""
        assert t106016000_x8()
    """State 4"""
    return 0

def t106016000_x16():
    """State 0,1"""
    # talk:10612300:"Ah, art thou persuaded to my cause?"
    assert t106016000_x65(text2=10612300, mode4=1)
    """State 2"""
    assert t106016000_x14()
    """State 3"""
    return 0

def t106016000_x17():
    """State 0,1"""
    if GetEventFlag(1034509413) == 1:
        """State 2"""
        if GetEventFlag(1034509437) == 1:
            """State 6"""
            # talk:10613700:"Speak with the three who await thee below."
            assert t106016000_x65(text2=10613700, mode4=1)
        else:
            """State 5"""
            # talk:10613100:"Speak with the three who await thee below."
            assert t106016000_x65(text2=10613100, mode4=1)
    else:
        """State 4"""
        # talk:10613000:"Good, then I ask we proceed with haste."
        assert t106016000_x64(text3=10613000, z5=1034509413, mode5=1)
        """State 3"""
        SetEventFlag(1034509418, 1)
    """State 7"""
    return 0

def t106016000_x18():
    """State 0,1"""
    if GetEventFlag(1034509415) == 1:
        """State 4"""
        # talk:10613600:"Ah, yes. Iji, my war counselor, and Seluvis, preceptor in the sorcerous arts, can be found below."
        assert t106016000_x65(text2=10613600, mode4=1)
        """State 2"""
        SetEventFlag(1034509418, 1)
    else:
        """State 3"""
        # talk:10613500:"Good, then I ask we proceed with haste."
        assert t106016000_x64(text3=10613500, z5=1034509415, mode5=1)
    """State 5"""
    return 0

def t106016000_x19():
    """State 0,1"""
    if GetEventFlag(1034509422) == 1:
        """State 3"""
        assert t106016000_x22()
    else:
        """State 2"""
        if GetEventFlag(1034509425) == 1:
            """State 4"""
            assert t106016000_x26()
        else:
            """State 5"""
            assert t106016000_x27()
    """State 6"""
    return 0

def t106016000_x20(actionbutton2=6000, flag15=6001, flag16=6000, flag17=6000, flag18=6000, flag19=6000,
                   flag20=6000, actionbutton3=_):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag15) == 1 or GetEventFlag(flag16) == 1 or GetEventFlag(flag17) == 1 or
                GetEventFlag(flag18) == 1 or GetEventFlag(flag19) == 1)
        """State 4"""
        assert not GetEventFlag(flag20)
        """State 2"""
        if GetEventFlag(flag20) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag15) and not GetEventFlag(flag16) and not GetEventFlag(flag17) and
              not GetEventFlag(flag18) and not GetEventFlag(flag19)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton2):
            """State 5"""
            return 0
        elif CheckActionButtonArea(actionbutton3):
            break
    """State 6"""
    return 1

def t106016000_x21():
    """State 0"""
    while True:
        """State 3"""
        # actionbutton:6000:"Talk", actionbutton:6411:"Administer draught"
        call = t106016000_x20(actionbutton2=6000, flag15=6001, flag16=6000, flag17=6000, flag18=6000,
                              flag19=6000, flag20=6000, actionbutton3=6411)
        if call.Get() == 1:
            """State 1"""
            Label('L0')
            SetEventFlag(1034509422, 1)
        elif call.Done():
            break
        elif GetEventFlag(1034509423) == 1:
            """State 4"""
            # actionbutton:6000:"Talk", actionbutton:6412:"Administer draught"
            call = t106016000_x20(actionbutton2=6000, flag15=6001, flag16=6000, flag17=6000, flag18=6000,
                                  flag19=6000, flag20=6000, actionbutton3=6412)
            if call.Get() == 1:
                Goto('L0')
            elif call.Done():
                break
            elif not GetEventFlag(1034509423):
                continue
        """State 5"""
        Label('L1')
        return 0
    """State 2"""
    SetEventFlag(1034509423, 1)
    Goto('L1')

def t106016000_x22():
    """State 0,1"""
    assert t106016000_x23()
    """State 2"""
    return 0

def t106016000_x23():
    """State 0,1"""
    # talk:10626000:"Well, this is a most unpleasant awakening."
    assert t106016000_x64(text3=10626000, z5=1034509426, mode5=1)
    """State 2"""
    return 0

def t106016000_x24():
    """State 0,1"""
    # talk:10626100:"I have spoken. Away from my sight."
    assert t106016000_x64(text3=10626100, z5=1034509427, mode5=1)
    """State 2"""
    return 0

def t106016000_x25():
    """State 0,1"""
    c1_121(9649)
    GiveSpEffectToPlayer(9711)
    # talk:10626200:"This is the third time, fiend."
    def WhilePaused():
        c1_121(9649)
    def ExitPause():
        c1_121(9649)
    assert (t106016000_x66(text1=10626200, flag9=1034509428, mode3=1) and CheckSpecificPersonTalkHasEnded(0)
            == 1)
    """State 2"""
    return 0

def t106016000_x26():
    """State 0,1"""
    if not GetEventFlag(1034509426):
        """State 3"""
        assert t106016000_x23()
    else:
        """State 2"""
        if not GetEventFlag(1034509427):
            """State 4"""
            assert t106016000_x24()
        else:
            """State 5"""
            assert t106016000_x25()
    """State 6"""
    return 0

def t106016000_x27():
    """State 0,7"""
    # goods:8159:Fingerslayer Blade
    if ComparePlayerInventoryNumber(3, 8159, 4, 1, 0) == 1 or GetEventFlag(1034509420) == 1:
        """State 1"""
        if GetEventFlag(1034509420) == 1:
            """State 2"""
            if GetEventFlag(1034509405) == 1:
                """State 4"""
                if GetEventFlag(1034509421) == 1:
                    """State 11"""
                    # talk:10617200:"What is it?"
                    assert t106016000_x65(text2=10617200, mode4=1)
                else:
                    """State 9"""
                    assert t106016000_x28()
            else:
                """State 5"""
                if GetEventFlag(1034509421) == 1:
                    """State 12"""
                    # talk:10617600:"What is it? You may go."
                    assert t106016000_x65(text2=10617600, mode4=1)
                else:
                    """State 10"""
                    assert t106016000_x29()
        else:
            """State 8"""
            # talk:10617000:"Ahh...It was thee."
            assert t106016000_x64(text3=10617000, z5=1034509420, mode5=1)
            """State 3"""
            SetEventFlag(1034509429, 1)
            """State 6"""
            # goods:8159:Fingerslayer Blade
            PlayerEquipmentQuantityChange(3, 8159, -1)
    else:
        """State 13"""
        # talk:10614100:"I shall soon enter my slumber."
        assert t106016000_x65(text2=10614100, mode4=1)
    """State 14"""
    return 0

def t106016000_x28():
    """State 0,1"""
    # talk:10617100:"Ah, but before I leave, I must entrust thee with this."
    assert t106016000_x64(text3=10617100, z5=1034509421, mode5=1)
    """State 2"""
    # lot:103910:Carian Inverted Statue
    assert t106016000_x37(lot1=103910)
    """State 3"""
    # talk:10617110:"My discarded flesh lieth beyond the seal unlocked by it."
    assert t106016000_x65(text2=10617110, mode4=1)
    """State 4"""
    return 0

def t106016000_x29():
    """State 0,2"""
    # talk:10617500:"Ah, but before I leave, I shall entrust thee with this."
    assert t106016000_x64(text3=10617500, z5=1034509421, mode5=1)
    """State 3"""
    # lot:103910:Carian Inverted Statue
    assert t106016000_x37(lot1=103910)
    """State 1"""
    if GetEventFlag(1042369406) == 1:
        """State 4"""
        # talk:10617510:"My thanks, for thy sterling efforts."
        assert t106016000_x65(text2=10617510, mode4=1)
    else:
        """State 5"""
        # talk:10617520:"My thanks, for thy sterling efforts."
        assert t106016000_x65(text2=10617520, mode4=1)
    """State 6"""
    return 0

def t106016000_x30():
    """State 0,5"""
    # action:21061009:"Administer Amber Draught?"
    call = t106016000_x33(action1=21061009)
    if call.Get() == 0:
        """State 1"""
        SetEventFlag(1034509424, 1)
        SetEventFlag(1034509425, 1)
        """State 4"""
        SetEventFlag(1034502745, 1)
        """State 3"""
        # goods:8166:Amber Draught
        PlayerEquipmentQuantityChange(3, 8166, -1)
        """State 6"""
        return 0
    elif call.Done():
        """State 2"""
        SetEventFlag(1034509423, 1)
        """State 7"""
        return 1

def t106016000_x31():
    """State 0,1"""
    if not GetEventFlag(1034502745) and not GetEventFlag(1034509429):
        """State 3"""
        # talk:10614500:"..."
        assert t106016000_x65(text2=10614500, mode4=1)
    else:
        """State 2"""
        def WhilePaused():
            RequestAnimation(20000, -1)
        assert t106016000_x19()
    """State 4"""
    return 0

def t106016000_x32():
    """State 0"""
    while True:
        """State 1"""
        # actionbutton:6000:"Talk"
        call = t106016000_x34(actionbutton1=6000, flag5=6001, flag11=6000, flag12=6000, flag13=6000,
                              flag14=6000, flag4=6000)
        if call.Done():
            break
        # goods:8166:Amber Draught
        elif (not GetEventFlag(1034509424) and ComparePlayerInventoryNumber(3, 8166, 4, 1, 0) == 1 and
              not GetEventFlag(1034502745)):
            """State 2"""
            call = t106016000_x21()
            if call.Done():
                break
            # goods:8166:Amber Draught
            elif (GetEventFlag(1034509424) == 1 or ComparePlayerInventoryNumber(3, 8166, 0, 0, 0) ==
                  1 or GetEventFlag(1034502745) == 1):
                pass
    """State 3"""
    return 0

def t106016000_x33(action1=21061009):
    """State 0,1"""
    # action:21061009:"Administer Amber Draught?"
    OpenGenericDialog(8, action1, 3, 4, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == 1:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t106016000_x34(actionbutton1=_, flag5=6001, flag11=6000, flag12=6000, flag13=6000, flag14=6000, flag4=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag5) == 1 or GetEventFlag(flag11) == 1 or GetEventFlag(flag12) == 1 or
                GetEventFlag(flag13) == 1 or GetEventFlag(flag14) == 1)
        """State 4"""
        assert not GetEventFlag(flag4)
        """State 2"""
        if GetEventFlag(flag4) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag5) and not GetEventFlag(flag11) and not GetEventFlag(flag12) and not
              GetEventFlag(flag13) and not GetEventFlag(flag14)):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t106016000_x35():
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

def t106016000_x36():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t106016000_x37(lot1=103910):
    """State 0,1"""
    # lot:103910:Carian Inverted Statue
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t106016000_x38(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t106016000_x54()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t106016000_x35()
    else:
        """State 4,7"""
        call = t106016000_x68()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t106016000_x35()
    """State 9"""
    return 0

def t106016000_x39():
    """State 0,1"""
    assert t106016000_x35()
    """State 2"""
    return 0

def t106016000_x40(flag1=3743, flag2=3741, flag3=3742, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t106016000_x57(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t106016000_x56()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t106016000_x41(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                   flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                   mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t106016000_x44(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t106016000_x48(val1=val1, z1=z1)
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
            call = t106016000_x50(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t106016000_x61() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t106016000_x46(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t106016000_x42(val2=10, val3=12):
    """State 0,1"""
    call = t106016000_x52(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t106016000_x38(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t106016000_x43(flag1=3743, val2=10, val3=12):
    """State 0,8"""
    assert t106016000_x70()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t106016000_x55()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t106016000_x35()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t106016000_x44(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t106016000_x45(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t106016000_x34(actionbutton1=actionbutton1, flag5=flag5, flag11=6000, flag12=6000, flag13=6000,
                flag14=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t106016000_x45(z6=_, val6=_):
    """State 0,1"""
    if f203(z6) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z6)
        assert f202() == val6
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t106016000_x46(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t106016000_x35()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t106016000_x47()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t106016000_x62()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t106016000_x47():
    """State 0,1"""
    assert t106016000_x45(z6=1101, val6=1101)
    """State 2"""
    return 0

def t106016000_x48(val1=5, z1=1):
    """State 0,2"""
    assert t106016000_x58()
    """State 1"""
    call = t106016000_x49()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t106016000_x60()
    """State 4"""
    return 0

def t106016000_x49():
    """State 0,1"""
    assert t106016000_x45(z6=1000, val6=1000)
    """State 2"""
    return 0

def t106016000_x50(val5=12):
    """State 0,1"""
    call = t106016000_x51()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t106016000_x61()
    """State 3"""
    return 0

def t106016000_x51():
    """State 0,1"""
    assert t106016000_x45(z6=1100, val6=1100)
    """State 2"""
    return 0

def t106016000_x52(val2=10, val3=12):
    """State 0,5"""
    assert t106016000_x70()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t106016000_x53()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t106016000_x63()
    """Unused"""
    """State 6"""
    return 0

def t106016000_x53():
    """State 0,2"""
    call = t106016000_x45(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t106016000_x54():
    """State 0,1"""
    assert t106016000_x45(z6=1001, val6=1001)
    """State 2"""
    return 0

def t106016000_x55():
    """State 0,1"""
    assert t106016000_x45(z6=1103, val6=1103)
    """State 2"""
    return 0

def t106016000_x56():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t106016000_x57(flag1=3743, flag2=3741, flag3=3742, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t106016000_x41(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                              flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                              z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t106016000_x43(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t106016000_x42(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t106016000_x69() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t106016000_x58():
    """State 0,1"""
    assert t106016000_x59()
    """State 2"""
    return 0

def t106016000_x59():
    """State 0,1"""
    assert t106016000_x45(z6=1104, val6=1104)
    """State 2"""
    return 0

def t106016000_x60():
    """State 0,1"""
    call = t106016000_x45(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t106016000_x39()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t106016000_x61():
    """State 0,1"""
    call = t106016000_x45(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t106016000_x39()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t106016000_x62():
    """State 0,1"""
    call = t106016000_x45(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t106016000_x39()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t106016000_x63():
    """State 0,1"""
    call = t106016000_x45(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t106016000_x39()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t106016000_x64(text3=_, z5=_, mode5=1):
    """State 0,5"""
    assert t106016000_x36() and CheckSpecificPersonTalkHasEnded(0) == 1
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
    SetEventFlag(z5, 1)
    """State 6"""
    return 0

def t106016000_x65(text2=_, mode4=1):
    """State 0,4"""
    assert t106016000_x36() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t106016000_x66(text1=_, flag9=_, mode3=1):
    """State 0,5"""
    assert t106016000_x67() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(flag9, 1)
    """State 1"""
    TalkToPlayer(text1, -1, -1, 1)
    """State 4"""
    if not mode3:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t106016000_x67():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t106016000_x68():
    """State 0,1"""
    assert t106016000_x45(z6=1002, val6=1002)
    """State 2"""
    return 0

def t106016000_x69():
    """State 0,1"""
    assert t106016000_x35()
    """State 2"""
    return 0

def t106016000_x70():
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

