import random
lehetoseg = ["kő", "papír", "olló"]
def jatek():
    db = 3
    jatekosNyert = 0
    gepNyert = 0
    while True:
        if db > 0 and jatekosNyert < 2 and gepNyert < 2:
            print(f"Jelenlegi állás: \nJátékos:{jatekosNyert}\nGép:{gepNyert}\n ")
            while True:
                beValasztas = input("Add meg, hogy mit szeretnél választani: ")
                beValasztas = beValasztas.lower()
                if lehetoseg.__contains__(beValasztas):
                    break
                else:
                    print("Kérem a három lehetőségből válasszon!")
            randomValasztas = lehetoseg[random.randint(0, len(lehetoseg)-1)]
            print(f"A gép választása {randomValasztas}")
            if beValasztas == randomValasztas:
                print("Döntetlen!\n")
            elif beValasztas == "kő" and randomValasztas == "olló":
                jatekosNyert += 1
                db -= 1
            elif beValasztas == "kő" and randomValasztas == "papír":
                gepNyert += 1
                db -=1
            elif beValasztas == "papír" and randomValasztas == "kő":
                jatekosNyert += 1
                db -= 1
            elif beValasztas == "papír" and randomValasztas == "olló":
                gepNyert += 1
                db -= 1
            elif beValasztas == "olló" and randomValasztas == "papír":
                jatekosNyert += 1
                db -= 1
            elif beValasztas == "olló" and randomValasztas == "kő":
                gepNyert += 1
                db -= 1
        else:
            if jatekosNyert > gepNyert:
                print("A játékos nyert!\n")
                break
            else:
                print("Sajnos a játékos vesztett!\n")
                break

jatek()