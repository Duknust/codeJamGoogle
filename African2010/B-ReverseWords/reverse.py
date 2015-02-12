def parser(fileName):
    fo = open(fileName, "r")
    number = fo.readline()

    for i in range(0,int(number)):
        line = fo.readline().rstrip('\n')
        ar = line.split(" ")
        reverseAr = ar[::-1]
        stringReverse = ' '.join([str(x) for x in reverseAr])
        buildingString = "Case #"+str(i+1)
        buildingString = buildingString+": "
        buildingString = buildingString+stringReverse

        f = open('output.out','a')
        f.write(buildingString+'\n')
        f.close()

        #print buildingString