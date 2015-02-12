#created by duknust
#find in https://github.com/Duknust

def parser(fileName):
    fo = open(fileName, "r")
    number = fo.readline()
    #print "number:"+number
    for it in range(0,int(number)):
    #for it in range(0,1):
        credit =int(fo.readline().rstrip('\n'))
        numberMoves=int(fo.readline().rstrip('\n'))
        line=fo.readline().rstrip('\n')
        ar = line.split(" ")

        #print "credit"+" "+str(credit)
        #print "numberMoves"+" "+str(numberMoves)
        #print line

        for i in range (0,numberMoves):
            for j in range (i+1,numberMoves):
                #print "i "+str(i)
                #print "j "+str(j)
                if int(ar[i])+int(ar[j])==credit:
                    resI=i+1
                    resJ=j+1
                    break
      
        buildingString = "Case #"+str(it+1)
        buildingString = buildingString+": "
        buildingString = buildingString+str(resI)+" "+str(resJ)

        f = open('output.out','a')
        f.write(buildingString+'\n')
        f.close()