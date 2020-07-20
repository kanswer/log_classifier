import numpy
def loadDataSet(filename):
    Contents=[]
    fr=open(filename)
    for line in fr.readlines():
        line1=line.strip().split(' ')   #Split log with space
        line2=line1[9:] #Extract log content except content
        dataset=[] 
        first=0
        second=0
        flag1=0
        flag2=0
        for i in range(len(line2)):
            flag=0
            for j in range(10):
                if line2[i].find(str(j))!=-1:
                    flag=1
                    break
            if flag==1:
                continue
            else:
                he=0
                for k in range(len(line2[i])):
                    he+=ord(line2[i][k])
                if flag1==0 and flag2==0:
                    first=he
                    flag1=1
                elif flag1==1 and flag2==0:
                    second=he
                    flag2=1
                else:
                    break
        dataset.append(first)          
        dataset.append(second)
        Contents.append(dataset)
    print(Contents)
    return numpy.array(Contents)

loadDataSet('E:\保研资料\project\log_classifier\kMeans_Log\BGL_2k.log')