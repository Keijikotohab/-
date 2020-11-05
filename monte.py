import random
import math
import numpy as np
import matplotlib.pyplot as plt

def monte_method(N):#モンテカルロ法関数
    point = 0
    for i in range(N):
        x = random.random()
        y = random.random()
        if x*x+y*y < 1.0:
            point += 1
    pi = 4.0 * point / N#円周率の近似値の計算
    return pi

count=0#i回目計算のためのカウンタ
monte_method_1=0#18~27行目　i回目の計算結果の変数
monte_method_2=0
monte_method_3=0
monte_method_4=0
monte_method_5=0
monte_method_6=0
monte_method_7=0
monte_method_8=0
monte_method_9=0
monte_method_10=0
In_1=0#27~34行目　グラフ出力のための変数
In_3=0
In_5=0
In_7=0
σn_1=0
σn_3=0
σn_5=0
σn_7=0

def In():#πの推定値の算出関数
    sum=(monte_method_1+monte_method_2+monte_method_3+monte_method_4+monte_method_5\
    +monte_method_6+monte_method_7+monte_method_8+monte_method_9+monte_method_10)/10
    return sum

def σn():#πの推定値の標準偏差の算出関数
    sum2=math.sqrt(((((monte_method_1-In())**2)+((monte_method_2-In())**2)+((monte_method_3-In())**2)\
    +((monte_method_4-In())**2)+((monte_method_5-In())**2)+((monte_method_6-In())**2)\
    +((monte_method_7-In())**2)+((monte_method_8-In())**2)+((monte_method_9-In())**2)\
    +((monte_method_10-In())**2))/9))
    return sum2

N=10#乱数の数　１０個
print("乱数の数:", 10)

for a in range(10):#独立に10回計算、出力
    b = monte_method(N)
    count+=1
    if count==1:
        monte_method_1=b
    elif count==2:
        monte_method_2=b
    elif count==3:
        monte_method_3=b
    elif count==4:
        monte_method_4=b
    elif count==5:
        monte_method_5=b
    elif count==6:
        monte_method_6=b
    elif count==7:
        monte_method_7=b
    elif count==8:
        monte_method_8=b
    elif count==9:
        monte_method_9=b
    elif count==10:
        monte_method_10=b
    print(str(count)+"回目：π =",b)

print("πの推定値:",round(In(),4))
print("πの推定値の標準偏差:",round(σn(),4))
In_1=In()
σn_1=σn()

print("-------------------------------")

N=10**3#乱数の数　１０**3個
count=0#カウンタの初期化
print("乱数の数:", 10**3)

for a in range(10):#独立に10回計算、出力
    b = monte_method(N)
    count+=1
    if count==1:
        monte_method_1=b
    elif count==2:
        monte_method_2=b
    elif count==3:
        monte_method_3=b
    elif count==4:
        monte_method_4=b
    elif count==5:
        monte_method_5=b
    elif count==6:
        monte_method_6=b
    elif count==7:
        monte_method_7=b
    elif count==8:
        monte_method_8=b
    elif count==9:
        monte_method_9=b
    elif count==10:
        monte_method_10=b
    print(str(count)+"回目：π =",b)

print("πの推定値:",round(In(),4))
print("πの推定値の標準偏差:",round(σn(),4))
In_3=In()
σn_3=σn()

print("-------------------------------")

N=10**5#乱数の数　１０**5個
count=0#カウンタの初期化
print("乱数の数:", 10**5)

for a in range(10):#独立に10回計算、出力
    b = monte_method(N)
    count+=1
    if count==1:
        monte_method_1=b
    elif count==2:
        monte_method_2=b
    elif count==3:
        monte_method_3=b
    elif count==4:
        monte_method_4=b
    elif count==5:
        monte_method_5=b
    elif count==6:
        monte_method_6=b
    elif count==7:
        monte_method_7=b
    elif count==8:
        monte_method_8=b
    elif count==9:
        monte_method_9=b
    elif count==10:
        monte_method_10=b
    print(str(count)+"回目：π =",b)
print("πの推定値:",round(In(),4))
print("πの推定値の標準偏差:",round(σn(),4))
In_5=In()
σn_5=σn()

print("-------------------------------")

N=10**7#乱数の数　１０**７個
count=0#カウンタの初期化
print("乱数の数:", 10**7) # 乱数の数: 10

for a in range(10):#独立に10回計算、出力
    b = monte_method(N)
    count+=1
    if count==1:
        monte_method_1=b
    elif count==2:
        monte_method_2=b
    elif count==3:
        monte_method_3=b
    elif count==4:
        monte_method_4=b
    elif count==5:
        monte_method_5=b
    elif count==6:
        monte_method_6=b
    elif count==7:
        monte_method_7=b
    elif count==8:
        monte_method_8=b
    elif count==9:
        monte_method_9=b
    elif count==10:
        monte_method_10=b
    print(str(count)+"回目：π =",b)
print("πの推定値:",round(In(),4))
print("πの推定値の標準偏差:",round(σn(),4))
In_7=In()
σn_7=σn()



"""
left = np.array([10,10**3,10**5,10**7])#乱数の数と推定値の関係グラフ
height = np.array([In_1,In_3,In_5,In_7])
plt.plot(left, height)
plt.title('Relationship between random numbers and E-π')
plt.xlabel('Number of random numbers')
plt.ylabel('Estimated value of π')
plt.show()

left = np.array([10,20,30,40])#間隔を一定にしたバージョン
height = np.array([In_1,In_3,In_5,In_7])
plt.plot(left, height)
plt.title('Relationship between random numbers and E-π')
plt.xlabel('Number of random numbers')
plt.ylabel('Estimated value of π')
plt.show()
"""

"""
left = np.array([10,10**3,10**5,10**7])##乱数の数と推定値の標準偏差の関係グラフ
height = np.array([σn_1,σn_3,σn_5,σn_7])
plt.plot(left, height)
plt.title('Relationship between random numbers and S-π')
plt.xlabel('Number of random numbers')
plt.ylabel('Standard deviation of π')
plt.show()

left = np.array([10,20,30,40])#間隔を一定にしたバージョン
height = np.array([σn_1,σn_3,σn_5,σn_7])
plt.plot(left, height)
plt.title('Relationship between random numbers and S-π')
plt.xlabel('Number of random numbers')
plt.ylabel('Standard deviation of π')
plt.show()
"""
