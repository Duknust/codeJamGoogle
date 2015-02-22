#created by duknust
#find in https://github.com/Duknust

def parser(fileName):
    fo = open(fileName, "r")
    firstLine = fo.readline().rstrip('\n')
    arInt = firstLine.split(" ")
    lSize = int(arInt[0])
    dSize = int(arInt[1])
    nSize = int(arInt[2])


        f = open('output.out','a')
        f.write(buildingString+'\n')
        f.close()