import math

old = 22        #現在の年齢
amount = 20000  #月に入れる金額
year = 18       #何年間投資するか
par = 3         #年率何％か（３％）
a = 0           #投資した場合
b = 0           #投資してない場合

y_amount = amount * 12 #12か月
par100 = par / 100 + 1 #100%表記から小数表記に

for i in range(0,year):
    a += y_amount
    a *= par100
    b += y_amount

print(str(old + year) + "歳では毎月" + str(amount) + "円を" + str(year) +"年間毎年" + str(par) + "%で運用すると")
print("投資あり：" + str(math.floor(a)) + "円")
print("投資なし：" + str(b) + "円")
print(str(year) + "年間の投資益は[" + str(math.floor(a-b)) + "円]です。")