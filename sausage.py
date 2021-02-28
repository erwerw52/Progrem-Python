from random import randint as rint
import json
class game:
    def __init__(self,m,n):#初始化
        self.win=self.lose=self.drow=self.spend=self.i=0
        self.round=m# 玩多少場
        self.price=n# 多少錢
        self.get=0# 賺或虧
        self.com=0# 獎勵
        self.runs=[]# 場次
        self.data={}# 字典
        self.data['GameData'] = []
        self.Calculation()
    # 產生每一個場次(round)
    def round_game(self):
        return [round()for self.i in range(self.round)]
    def Calculation(self):# 計算所有場次的輸贏以及賺錢或虧錢
        self.runs=self.round_game()
        for i in range(len(self.runs)):
            self.boss,self.player,self.x,self.y,self.wld=self.runs[i].data()
                # 設定boss是老闆，player是玩家
            if (self.boss>self.player):
                self.lose+=1
            elif (self.boss<self.player):
                self.com+=2# 獎勵+2
                self.win+=1
            elif(self.boss==self.player):
                self.drow+=1
            self.data['GameData'].append({'Boss Deck':self.x,'Player Deck':self.y,'Boss':self.boss,'Player':self.player,'Result':self.wld})
        if(self.com<2):
            self.com=0
        self.spend=self.round*self.price# 總共花費
        get=2*self.win*self.price-self.spend+self.drow*self.price#算出得到多少
        if(get<0):#如果結果<0
            self.get=abs(get)#虧了，錢為負所以加絕對值
        else:
            self.get=get#賺了不動
        self.data['Round']=[{'WIN':self.win,'LOSE':self.lose,'DROW':self.drow}]
        self.data['Spend']=self.spend
        self.data['REWARD']=self.com
        self.data['Get']=self.get
    def print_all(self):#印出所有資料
        print(json.dumps(self.data,indent=4))
        
class round:
    def __init__(self):
        self.dicesum=0
        self.wld=str# 判斷輸贏以字串方式
        self.x=self.y=[]
        self.boss=self.player=0
        self.round() 
        self.pk()      
    def rint_array(self):#產生 4 個亂數的陣列
        return [rint(1,6) for _ in range(4)]
    def cal(self):#計算骰子點數
        total=0#定義total
        a=self.rint_array()
        x=sorted(a)
        for i in range(len(x)-1):
            if(x[i]==x[i+1]):
                total=sum(x)-2*x[i]
        return total,x
    def round(self):#產生老闆與顧客
        for _ in range(3):
            bossresult=self.cal()
            self.x=bossresult[1]
            self.boss=bossresult[0]
            #print(bossresult)
            if self.boss!=0:
                break
        for _ in range(3):
            playerresult=self.cal()
            #print(testresult)
            self.y=playerresult[1]
            self.player=playerresult[0]
            if self.player!=0:
                break
    def pk(self):#判斷輸贏
        if (self.boss>self.player):
            self.wld='BOSS WIN'
        elif (self.boss<self.player):
            self.wld='PLAYER WIN'
        elif(self.boss==self.player):
            self.wld='DROW'
    def data(self):#資料回傳
        return self.boss,self.player,self.x,self.y,self.wld
game1=game(int(input('玩幾次?')),int(input('一場的錢?')))
game1.print_all()
