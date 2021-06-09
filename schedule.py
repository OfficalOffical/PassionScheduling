import req

"""
Arrival Time: Time at which the process arrives in the ready queue.
Completion Time: Time at which process completes its execution.
Burst Time: Time required by a process for CPU execution.
Turn Around Time: Time Difference between completion time and arrival time.
Turn Around Time = Completion Time – Arrival Time

Waiting Time(W.T): Time Difference between turn around time and burst time.
Waiting Time = Turn Around Time – Burst Time
"""





#Turnaround time = Exit time - Arrival time
#Turnaround time = Burst time + Waiting time
#Waiting time = Turnaround time - Burst time
#Througput = waiting time /3


class process:
    def __init__(self,ID, start, end,):
        self.ID = ID
        self.start = start
        self.end = end


def MLFQ(x,y):
    print(x)
    print(y)
    temp = req.reqTime(y)
    global pList
    pList = []
    pList.append(process(0, -1, -1))
    pList.append(process(1, -1, -1))
    pList.append(process(2, -1, -1))

    tempY = highPriority(x,y,(temp*0.5))#SJF  hoca hepsine ayrı time derse buraya tempx
    tempY = medPriority(x,tempY,(temp*0.3),(temp*0.5)) # buraya da x yerine tempX yaz

    printList()



def highPriority(x, y, ratio):#SJF
    global idleTime #May i put waiting time to other scheduling algo's
    idleTime=0
    tempX = x
    tempY = y
    temp = 0
    for i in range(int(ratio)):
        temp = req.findShortest(tempX,tempY)
        if (temp != -1):
            tempY[temp] -=1
            checkStartEnd(i,temp,tempY[temp])
        else:
            idleTime += 1
    return tempY #Buraya temp X ekleyebilirsin

def medPriority(x,tempY, ratio,realTime):
    realTime = int(realTime)
    ratio = int(ratio)

    time = 0
    temp = 0
    print(ratio)
    k=0
    while True:
        if((tempY[temp]/4)>1.0): #Az beynini zorlasan olcak sanki
            for i in range(4):
                if(time == ratio):
                    print("karo")
                    break;
                else:
                    if((tempY[temp]-1) == 0):
                        checkStartEnd((realTime+time),temp,0)

                    tempY[temp]-=1
                    time+=1

        else:
            for i in range(tempY[temp]):
                if(time == ratio):
                    print("paro")
                    break
                else:
                    if ((tempY[temp] - 1) == 0):
                        checkStartEnd((realTime+time), temp, 0)
                    tempY[temp]-=1
                    time+=1

        temp = ((temp+1)%3)
        if(time == ratio):
            print("taro")
            break


def checkStartEnd(time,ID,var):
    for p in pList:
        if(p.ID == ID):
            if(p.start == -1):
                p.start = time
            elif(p.end == -1 and var == 0):
                p.end = (time+1)


def printList():
    for obj in pList:
        print(obj.ID, obj.start,obj.end, sep=' ')


