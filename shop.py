def readFile():
    try:
        myFile = open("data.txt", "r")
        file = myFile.read()
        myFile.close()
        return file
    except:
        print("Erreur avec l'ouverture du fichier")

def getValueLine(value, line):
    valeur = value.split("\n")
    return valeur[line]

def writeFile(line, valeur):
    value = readFile()
    myTblo = []
    myTblo.append(getValueLine(value, 0))
    myTblo.append(getValueLine(value, 1))
    myTblo.append(getValueLine(value, 2))
    myTblo.append(getValueLine(value, 3))
    myTblo.append(getValueLine(value, 4))
    file = open("data.txt", "w")
    for i in range(0,5):
        if i != line:
            file.write(str(myTblo[i]))
            file.write("\n")
        else:
            file.write(str(valeur))

