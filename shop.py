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