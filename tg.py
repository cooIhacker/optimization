#Метод касательных
#f(x)=exp(0,87x)+exp(0,84x)-144sinx
import numpy as np
import math

corsim=4                   #Кол-во верных цифр в 16 системе счисления
a=0.                         #Интервал поиска минимайзера
b=np.pi
eps=0.5*1/(16**(corsim-1))                      #Погрешность
callf=0
calldf=0
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
f1=f(a)
f2=f(b)
df1=df(a)
df2=df(b)

def tg(a,b,f1,f2,df1,df2):
    global itern
    itern+=1
    #print(f"Итерация номер {callf//2+1},  значение: {str(float.hex((b + a) / 2))[2:3 + corsim:]}, с погрешностью {float.hex((b - a) / 2)}")
    if abs(b-a)<eps:
        print(itern, float.hex(f1), float.hex(f2), float.hex(df1),  float.hex(df2), callf,calldf, sep='   ')
        print(f"Погрешность {float.hex((b-a)/2)}")
        return (b+a)/2
    else:
        c=(f2-b*df2-f1+a*df1)/(df1-df2)
        f3=f(c)
        df3=df(c)
        print(itern,form(a),form(c),form(b),float.hex(f1),float.hex(f3),float.hex(f2),float.hex(df1),float.hex(df3),float.hex(df2),float.hex((b-a)/2),callf,calldf,sep='   ')
        if df3>=0:
            return tg(a,c,f1,f3,df1,df3)
        else:
            return tg(c,b,f3,f2,df3,df2)

minimayzer=tg(a,b,f1,f2,df1,df2)

print(f"Минимайзер = {float.hex(minimayzer)}   в 16-ричной")
s=str(float.hex(minimayzer))
hans=s[2:3+corsim:]


print(f"Функция была вызвана {callf} раз(а)")
print(f"Производная функции была вызвана {calldf} раз(а)")
print(f"Минимайзер = {hans}     16-ричная с {corsim-1} верными цифрами")
print(form(minimayzer))