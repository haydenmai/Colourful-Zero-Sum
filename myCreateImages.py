#########################
# CMPT 120 - Final Project: Colourful Zero Game
# ########## & Gia Hue Mai
# Aug 1, 2022
# myCreateImages.py

def colourDictCreation():
    colourDict = {}
    colourFile = open ("colorcoding.csv")
    readLine = colourFile.readline()
    for line in colourFile:
        rgbList = []
        linelist = line.split(",")
        number = int(linelist[0])
        rgbR = int(linelist[1])
        rgbG = int(linelist[2])
        rgbB = int(linelist[3])
        rgbList += [rgbR, rgbG, rgbB]
        colourDict[number] = rgbList
    return colourDict

def rgbInvert(number, colourDict):
    if number < 0:
        absNumber = abs(number)
        colour = colourDict[absNumber]
        r = 255 - colour[0]
        g = 255 - colour[1]
        b = 255 - colour[2]
        colour = [r, g, b]
    else:
        colour = colourDict[number]
    return colour

def fillSquare(x, y, image, colour):
    for row in range(x*100, 100+x*100):
        for col in range(y*100, 100+y*100):
            image[row][col] = colour
    return image