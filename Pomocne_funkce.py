import random
import time

def pochvala(pocet):
    pochvala = ""
    if pocet <= 2:
        pochvala = "amazing"
    elif pocet > 2 and pocet < 5:
        pochvala = "average"
    else:
        pochvala = "not so good"
    return pochvala


def hra():
    ODDELOVAC = 47 * "-"
    #Vytvoření náhodného listu čísel
    list_cisel = [random.randint(1, 9)]
    while len(list_cisel) != 4:
        pridane = random.randint(0, 9)
        if pridane not in list_cisel:
            list_cisel.append(pridane)

    #print("Solution key = " + str(list_cisel))

    pocet_pokusu = 0
    while True:
        t0 = time.time()
        pocet_pokusu += 1
        print(f"xxx Tip: {pocet_pokusu} xxx")
        print("Please enter 4 digit number: ")
        tip = [int(cislo) for cislo in str(input())]

        while len(tip) != len(list_cisel):
            print("Please enter exactly 4 digit number!")
            tip = [int(cislo) for cislo in str(input())]

        while tip[0] == 0:
            print("First number cannot be 0")
            tip = [int(cislo) for cislo in str(input())]

        kontrola_cisel = []
        for i in tip:
            if i not in kontrola_cisel:
                kontrola_cisel.append(i)
        if len(kontrola_cisel) != len(list_cisel):
            print("Numbers must be unique (no duplicates)")
            tip = [int(cislo) for cislo in str(input())]


        if tip == list_cisel:
            t1 = time.time() - t0
            print(f"Correct, you've guessed the right number.\nIn {pocet_pokusu} guesses!")
            print(ODDELOVAC)
            break

        else:
            cow = 0
            bull = 0

            for odhad in range(len(list_cisel)):
                if tip[odhad] == list_cisel[odhad]:
                    bull += 1
                elif tip[odhad] in list_cisel:
                    cow += 1

        print(f"Cows: {cow} Bulls: {bull}")
        print(ODDELOVAC)

    print(f"That's {pochvala(pocet_pokusu)}")
    print(f"It took you {int(t1)}s to accomplish")
    time.sleep(10)
