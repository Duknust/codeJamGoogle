#created by duknust
#find in https://github.com/Duknust

def parser(fileName):
    
    fo = open(fileName, "r")
    number = fo.readline()
    res=""
    for it in range(0,int(number)):
        vectorSize=int(fo.readline().rstrip('\n'))
        line1=fo.readline().rstrip('\n')
        line2=fo.readline().rstrip('\n')

        vect1=map(int, line1.split(" "))
        vect2=map(int, line2.split(" "))

        sumScalar = 0;
      
        sumScalar= sum([x * y for x, y in zip(sorted(vect1), sorted(vect2, reverse=True))])

        buildingString = "Case #"+str(it+1)
        buildingString = buildingString+": "
        buildingString = buildingString+str(sumScalar)
        f = open('output.out','a')
        f.write(buildingString+'\n')
        f.close()