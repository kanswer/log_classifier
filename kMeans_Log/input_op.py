import numpy
def loadDataSet(filename):
    Contents=[]
    fr=open(filename)
    for line in fr.readlines():
        line1=line.strip().split(' ')   #Split log with space
        line2=line1[9:] #Extract log content except content
        num1=0
        num2=0
        for i in range(len(line2[0])):
            num1+=ord(line2[0][i])
        dataset=[]
        dataset.append(num1)    
        for i in range(len(line2)):
            for j in range(len(line2[i])):
                num2+=ord(line2[i][j])
        dataset.append(num2)
        Contents.append(dataset)
    return numpy.array(Contents)