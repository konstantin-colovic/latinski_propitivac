import csv

# Read the files

csvfile = open('imenice.csv', newline='')
imenice = csv.reader(csvfile)

csvfile = open('glagoli.csv', newline='')
glagoli = csv.reader(csvfile)

csvfile = open('pridevi.csv', newline='')
pridevi = csv.reader(csvfile)

csvfile = open('nepromenljive.csv', newline='')
nepromenljive = csv.reader(csvfile)

# Ask the user if they want to be quizzed on verbs, nouns etc.

print(".csv FLASHCARD TESTER ZA LATINSKI\n")
mod = input("Koji mod zelite?\n1.imenice\n2.glagole\n3.prideve\n4.nepromenljive\n\n")

# If the user selected nouns

if mod == "1":
    for row in imenice:
        print("Mora sva mala slova i sa zapetama izmedju komponenata, takodje NE SME razmak posle zapete, takodje ne ide tacka posle oznake za rod")
        print(f"Kako ova rec glasi na latinskom: {row[0]}") # Ask the user
        nom = row[1]
        gen = row[2]
        rod = row[3]
        ges = input("Kako glasi na latinskom?\n")
        spl = ges.split(",")
        if spl[0] == nom and spl[1] == gen and spl[2] == rod:
            print("To je tacno !\n.....idemo dalje")              # If correct
        else:
            print(f"Netacno, tacno je {nom}, {gen}, {rod}.\n")    # If incorrect

# Same philosophy applies for the other word types            
            
elif mod == "2":
    for row in glagoli:
        print("Mora sva mala slova i sa zapetama izmedju komponenata, takodje NE SME razmak posle zapete.")
        print(f"Kako ova rec glasi na latinskom: {row[0]}")
        prv = row[1]
        inf = row[2]
        ges = input("Kako glasi na latinskom?\n")
        spl = ges.split(",")
        if spl[0] == prv and spl[1] == inf:
            print("To je tacno !\n.....idemo dalje")
        else:
            print(f"Netacno, tacno je {prv}, {inf}.\n")

elif mod == "3":
    for row in pridevi:
        print("Mora sva mala slova i sa zapetama izmedju rodova, takodje NE SME razmak posle zapete.")
        print(f"Kako ova rec glasi na latinskom: {row[0]}")
        mus = row[1]
        zen = row[2]
        sre = row[3]
        ges = input("Kako glasi na latinskom?\n")
        spl = ges.split(",")
        if spl[0] == mus and spl[1] == zen and spl[2] == sre:
            print("To je tacno !\n.....idemo dalje")
        else:
            print(f"Netacno, tacno je {mus}, {zen}, {sre}.\n")

elif mod == "4":
    for row in nepromenljive:
        print("Mora sva mala slova i sa slashovima (/) izmedju znacenja, takodje NE SME razmak posle slesha.")
        print(f"Kako ova rec glasi na latinskom: {row[0]}")
        zna = row[1]
        ges = input("Kako glasi na latinskom?\n")
        if ges == zna:
            print("To je tacno !\n.....idemo dalje")
        else:
            print(f"Netacno, tacno je {zna}.\n")

else:
    print("Ne vazeci input, restartujte program !!!") # If the input is invalid
