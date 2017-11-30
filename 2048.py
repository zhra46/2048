import random,os,time
class Field(object):
    def __init__(self):
        # self.fieldList=[[0]*4]*4
        self.fieldList=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    def showField(self):
        os.system('clear')
        for row in self.fieldList:
            print('-' * 17)
            print('|',end='')
            for item in row:
                print(' %s |'%item,end='')
            print('')
        print('-' * 17)
    def produceNew(self):
        element2choose =[]
        for i in range(4):
            for j in range(4):
                if self.fieldList[i][j] == 0:
                    element2choose.append([i,j])
        choice=random.choice(element2choose)
        print (choice)
        self.fieldList[choice[0]][choice[1]]=random.choice([2,4])
        print(self.fieldList)
    def tighten(self):
        for rownum in range(len(self.fieldList)):
            newRow=[]
            for i in self.fieldList[rownum]:
                if i:
                    newRow.append(i)
            for i in range(4-len(newRow)):
                newRow.append(0)
            self.fieldList[rownum]=newRow
    def merge(self):
        for row in self.fieldList:
            for inum in range(len(row)-1):
                if row[inum]==row[inum+1]:
                    row[inum]=row[inum]+row[inum+1]
                    row[inum+1]=0
    def moveLeft(self):
        self.tighten()
        self.merge()
        self.tighten()
    def moveUp(self):
        self.turnRight()
        self.turnRight()
        self.turnRight()
        self.moveLeft()
        self.turnRight()
    def moveRight(self):
        self.mirror()
        self.moveLeft()
        self.mirror()
    def moveDown(self):
        self.turnRight()
        self.moveLeft()
        self.turnRight()
        self.turnRight()
        self.turnRight()
    def turnRight(self):
        result=[]
        for i in range(len(self.fieldList)):
            li=[]
            for row in self.fieldList:
                li.append(row[i])
            result.append(li)
        self.fieldList=result
        self.mirror()
    def mirror(self):
        result=[]
        for row in self.fieldList:
            result.append(row[::-1])
        self.fieldList=result



if __name__=='__main__':
    a = Field()
    i=0
    while True:
        a.showField()
        a.moveRight()
        a.produceNew()
        time.sleep(0.1)
        i+=1