#Метод Ньютона-Рафсона
#f(x)=exp(0,87x)+exp(0,84x)-144sinx
import numpy as np
import math

corsim=4                   #Кол-во верных цифр в 16 системе счисления
a=0.                         #Интервал поиска минимайзера
b=np.pi
eps=0.5*1/(16**(corsim-1))                      #Погрешность
callf=0
calldf=0
callddf=0
itern=0

def form(x):
    return str(float.hex(x))[2:10]+' '+str(float.hex(x))[-3:]
def f(x):
    global  callf
    callf+=1
    return math.exp(0.87*x)+math.exp(0.84*x)-144*math.sin(x)

def df(x):
    global calldf
    calldf+=1
    return 0.87*math.exp(0.87*x)+0.84*math.exp(0.84*x)-144*math.cos(x)

def ddf(x):
    global callddf
    callddf += 1
    return 0.87*0.87 * math.exp(0.87 * x) + 0.84*0.84 * math.exp(0.84 * x) + 144 * math.sin(x)

start=1.
def new_raf(x):
    global itern
    itern+=1
    df1=df(x)
    if abs(df1)<eps:
        return x
    else:
        ddf1=ddf(x)
        print(itern,form(x),float.hex(df1),float.hex(ddf1))
        return new_raf(x-df1/ddf1)

minimayzer=new_raf(start)

print(f"Минимайзер = {float.hex(minimayzer)}   в 16-ричной")
s=str(float.hex(minimayzer))
hans=s[2:3+corsim:]


print(f"Функция была вызвана {calldf} раз(а)")
print(f"Вторая производная функции была вызвана {callddf} раз(а)")
print(f"Минимайзер = {hans}     16-ричная с {corsim-1} верными цифрами")
