#created by duknust
#find in https://github.com/Duknust

def parser(fileName):
    dictionary = {
        'a':'2',
        'b':'22',
        'c':'222',
        'd':'3',
        'e':'33',
        'f':'333',
        'g':'4',
        'h':'44',
        'i':'444',
        'j':'5',
        'k':'55',
        'l':'555',
        'm':'6',
        'n':'66',
        'o':'666',
        'p':'7',
        'q':'77',
        'r':'777',
        's':'7777',
        't':'8',
        'u':'88',
        'v':'888',
        'w':'9',
        'x':'99',
        'y':'999',
        'z':'9999',
        ' ':'0',
    }
    fo = open(fileName, "r")
    number = fo.readline()
    res=""
    for it in range(0,int(number)):
        lastnumber=""
        line=fo.readline().rstrip('\n')
        for i in range (0,len(line)):
                char = line[i]
                if lastnumber==(dictionary[char])[0]:
                    res=res+" "
                lastnumber=(dictionary[char])[0]
                res=res+(dictionary[char])
      
        buildingString = "Case #"+str(it+1)
        buildingString = buildingString+": "
        buildingString = buildingString+res
        res = ""
        f = open('output.out','a')
        f.write(buildingString+'\n')
        f.close()