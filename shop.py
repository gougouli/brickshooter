highscore = 0
money = 1
defil_speed = 2
shoot_speed = 3
move_speed = 4

# def readFile():
#     try:
#         myFile = open("data.txt", "r")
#         file = myFile.read()
#         myFile.close()
#         return file
#     except:
#         print("Erreur avec l'ouverture du fichier")
#
# def getValueLine(value, line):
#     valeur = value.split("\n")
#     return valeur[line]
#
# def writeFile(line, valeur):
#     value = readFile()
#     myTblo = []
#     myTblo.append(getValueLine(value, highscore))
#     myTblo.append(getValueLine(value, money))
#     myTblo.append(getValueLine(value, defil_speed))
#     myTblo.append(getValueLine(value, shoot_speed))
#     myTblo.append(getValueLine(value, move_speed))
#     file = open("data.txt", "w")
#     for i in range(0,5):
#         if i != line:
#             file.write(str(myTblo[i]))
#             file.write("\n")
#         else:
#             file.write(str(valeur))
#             file.write("\n")

def add(line):
    values =readFile()
    currentValue = int(getValueLine(values, line))
    price = currentValue**2
    money = int(getValueLine(values, 1))
    if money >= price:
        moneyRestant = money - price
        lvl = currentValue + 1
        writeFile(1, moneyRestant)
        writeFile(line, lvl)
        print("Acheté")
        return 1
    print("Pas d'argent")
    return 0

def remove(line):
    values = readFile()
    currentValue = int(getValueLine(values, line))
    returnPrice = currentValue * 2
    money = int(getValueLine(values, 1))
    if currentValue > 0:
        newMoney = money + returnPrice
        lvl = currentValue - 1
        writeFile(1, newMoney)
        writeFile(line, lvl)
        print("Niveau retiré")
        return 1
    print("Vous etes niveau 0 ! Attention")
    return 0
remove(move_speed)