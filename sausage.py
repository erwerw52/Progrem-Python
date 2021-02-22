from random import randint as rint
import json
class game:
    #初始化一次遊戲
    def __init__(self,m,n):
        self.win=self.lose=self.draw=0
        self.round=m
        self.price=n
        self.data={}
        self.data['GameData']=[]
        #產生亂數
        self.runs=[round() for i in range(m)]   
    def game_round(self):
        for i in range(len(self.runs)):
            #設定BOSS是老闆，TEST是玩家
            self.boss,self.test,self.x,self.y,self.wld=self.runs[i].data()
            self.data['GameData'].append({'BOSS DECK':self.x,'PLAYER DECK':self.y,'BOSS':self.boss,'PLAYER':self.test,'result':self.wld})
        print(self.wld)
            #判斷是玩家還是老闆贏，贏的+1
    # def Calculation(self):
    #         if self.boss>self.test:
    #             self.lose+=1
    #         elif self.boss<self.test:
    #             self.win+=1
    #         else:
    #             print(f'*{"draw":^28}*')
    #             self.draw+=1
    # def print_result(self):
    #     spend=self.round*self.price
    #     get=2*self.win*self.price-spend+self.draw*self.price
    #     if(get<0):
    #        get=abs(get)
    #     else:
    #         get=get
        #輸出
class round:
    #初始化一場遊戲
    def __init__(self):
        self.boss=self.test=0
        self.x=self.y=[]
        self.round()
        self.pk()
        self.wld=str
    def rint_array(self):
        #產生亂數
        return [rint(1,6) for i in range(4)]
    def cal(self):
        #計算點數
        total=0
        a=self.rint_array()
        x=sorted(a)
        for i in range(len(x)-1):
            if(x[i]==x[i+1]):
                total=sum(x)-2*x[i]
        return total,x
    def round(self):
        for _ in range(3):
            bossresult=self.cal()
            self.x=bossresult[1]
            self.boss=bossresult[0]
            #print(bossresult)
            if self.boss!=0:
                break
        for _ in range(3):
            testresult=self.cal()
            #print(testresult)
            self.y=testresult[1]
            self.test=testresult[0]
            if self.test!=0:
                break
    def pk(self):
        if(self.boss>self.test):
            self.wld='BOSS WIN'
        elif(self.boss<self.test):
            self.wld='PLAYER WIN'
        elif(self.boss==self.test):
            self.wld='DROW'
    def data(self):
        return self.boss,self.test,self.x,self.y,self.wld
#輸入次數與價錢
game1=game(int(input('玩幾次?')),int(input('一場的錢?')))
game1.game_round()