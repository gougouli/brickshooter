def add(line):
    values = readFile()
    currentValue = int(getValueLine(values, line))
    price = currentValue**2
    money = int(getValueLine(values, line_money))
    if money >= price:
        moneyRestant = money - price
        lvl = currentValue + 1
        writeFile(line_money, moneyRestant)
        writeFile(line, lvl)
        print("Acheté")
        return 1
    print("Pas d'argent")
    return 0

def remove(line):
    values = readFile()
    currentValue = int(getValueLine(values, line))
    returnPrice = currentValue * 2
    money = int(getValueLine(values, line_money))
    if currentValue > 0:
        newMoney = money + returnPrice
        lvl = currentValue - 1
        writeFile(line_money, newMoney)
        writeFile(line, lvl)
        print("Niveau retiré")
        return 1
    print("Vous etes niveau 0 ! Attention")
    return 0