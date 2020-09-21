# AN APPLICATION WHICH TELLS FUTURE BASED UPON ZODIAC SIGN.

next = True
while next == True:
    print(''' From all the mentioned zodiac signs
    1] Aries
    2] Tauras
    3] Gemini
    4] Cancer
    5] Leo
    6] Virgo
    7] Libra
    8] Scorpio
    9] Sagittiarius
    10] Capricorn
    11] Aquarius
    12] Pisces
    ''')

    a = int(input("Select your zodiac sign number and press enter to know future: "))
    print(a)

    if a == 1:
        print("You are going to rich.")
    elif a == 2:
        print("You are going to troubleshoot all the problems.")
    elif a == 3:
        print("Try and relax so that your mind and body are rejuvenated.")
    elif a == 4:
        print("Your romantic relationship may have to face the trials of misunderstandings.")
    elif a == 5:
        print("You might have to undertake a sudden short trip today.")
    elif a == 6:
        print("You might suffer from some minor physical illness today.")
    elif a == 7:
        print("There might be some embarrassing moments  you may face today.")
    elif a == 8:
        print("You may feel drained of all your energy as you it gets wasted on an unsuccessful project you've taken up.")
    elif a == 9:
        print("Today you might have to face a conflict between your public life and your domestic life. ")
    elif a == 10:
        print("Today your dream project will get the approval from the authorities")
    elif a == 11:
        print("You will be active and intensely alive today. You will also be generous and at your witty best.")
    elif a == 12:
        print("Nothing will bring you out of the dull, melancholic state you have enveloped yourself in today.")
    else:
        print("Please select only from 1 to 12")

    next = True if input("\nShall we do it again? (Y/N) ") == "Y" else False

    
