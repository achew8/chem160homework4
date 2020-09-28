from cards import *
ngames = 10000
result=[]
for i in range(ngames):
    adeck=deck()
    bdeck=deck()
    adeck.shuffle()
    bdeck.shuffle()
    ascore = 0
    bscore = 0
    while adeck.cardsleft()>0:
        acard=adeck.dealcard()
        bcard=bdeck.dealcard()
        if acard.value()>bcard.value():
            ascore += 2
        if acard.value()<bcard.value():
            bscore += 2
        if acard.value()== bcard.value():
            ascore += 1
            bscore += 1
    if ascore>bscore:
        result.append(ascore-bscore)
    if ascore<bscore:
        result.append(bscore-ascore)
    if ascore==bscore:
        result.append(ascore-bscore)
print("0",result.count(0)/ngames)
print("2",result.count(2)/ngames)
print("4",result.count(4)/ngames)
print("6",result.count(6)/ngames)
print("8",result.count(8)/ngames)
print("10",result.count(10)/ngames)
print("12",result.count(12)/ngames)
print("14",result.count(14)/ngames)
print("16",result.count(16)/ngames)
print("18",result.count(18)/ngames)
print("20",result.count(20)/ngames)
print("22",result.count(22)/ngames)
print("24",result.count(24)/ngames)
print("26",result.count(26)/ngames)
print("28",result.count(28)/ngames)
print("30",result.count(30)/ngames)
print("32",result.count(32)/ngames)
print("34",result.count(34)/ngames)
print("36",result.count(36)/ngames)
print("38",result.count(38)/ngames)
print("40",result.count(40)/ngames)
print("42",result.count(42)/ngames)
print("44",result.count(44)/ngames)
print("46",result.count(46)/ngames)
print("48",result.count(48)/ngames)
print("50",result.count(50)/ngames)
print("52",result.count(52)/ngames)
