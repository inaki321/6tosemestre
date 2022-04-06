import math
import time
from datetime import date, datetime
from os.path import exists
import os 
import tkinter 
import random as rd

   
def Instrucciones(inputIn):
   if(inputIn == '*'):
       borradofunc()
       if borrado == False:
           print('No hay borrado')
           varResultado["text"] = "No hay borrado"
       elif borrado == True:
           print('Ya hay borrado')
           varResultado["text"] = "Si hay borrado"
       print('var check ',borrado)

   if(inputIn == 'suma'):
       resA = suma()
       print('suma: ',resA)
       varResultado["text"] = "Suma: " + str(resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')

   if(inputIn == 'resta'):
       resA = resta()
       print('resta: ',resA)
       varResultado["text"] = "Resta: " + str(resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')


   if(inputIn == 'multiplicacion'):
       resA = multiplica()
       print('multiplicacion: ',resA)
       varResultado["text"] = "multiplicacion: " + str(resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')

   if(inputIn == 'division'):
       resA = divide()
       print('division: ',resA)
       varResultado["text"] = "division: " + str(resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')

   if(inputIn == 'factorial'):
       resA = factorial()
       print('factorial: ',resA)
       varResultado["text"] = "factorial: " + str(resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')
    
   if(inputIn == 'seno'):
       resA = seno()
       print('seno: ',resA)
       varResultado["text"] = "seno: " + str(resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')

   if(inputIn == 'coseno'):
       resA = coseno()
       print('coseno: ',resA)
       varResultado["text"] = "coseno: " + str(resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')
           
   if(inputIn == 'tangente'):
       resA = tan()
       print('tangente: ',resA)
       varResultado["text"] = "tangente: " + str(resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')

   if(inputIn == 'duplica'):
      duplica()
   if(inputIn == 'duplica n'):
       duplicaN()
   if(inputIn == 'intercambia'):
       intercambia()
   if(inputIn == 'intercambia n'):
       resA = intercambiaN()
       print('intercambia n: ',resA)
       varResultado["text"] = "intercambia n: " + str(resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')
   if(inputIn == 'duerme'):
       duerme()
   if(inputIn == 'duerme n'):
       duermeN()
   if(inputIn == 'muestra'):
       muestra()
   if(inputIn == 'promedio n'):
       resA = promedioN()
       print('promedio: ',resA)
       varResultado["text"] = "promedio: " + str(resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')
           
   if(inputIn == 'comentario'):
       resA = comentario()
       print('memoria: ',resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')
   if(inputIn == 'ecuacion 2 grado'):
       resA,resB = ec2grado()
       print('ecuacion 2do grado: '+resA + ' '+ resB)
       varResultado["text"] = "ecuacion 2do grado: " + str(resA) + " " + str(resB)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')
           f.write(str(resB))
           f.write('\n')
       
   if(inputIn == 'memoria'):
       resA = memoria()
       print('memoria: ',resA)
       varResultado["text"] = "memoria: " + str(resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')
   if(inputIn == 'cls'):
       Cls()
   if(inputIn == 'borra'):
       resA = borra()
       print('borrado: ',resA)
       varResultado["text"] = "borrado: " + str(resA)      
    

   if(inputIn == 'reset'):
       reset()
   if(inputIn == 'signo'):
       resA = signo()
       print('signo: ',resA)
       varResultado["text"] = "signo: " + str(resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')
   if(inputIn == 'raiz'):
       resA = raiz()
       print('Raiz: ',resA)
       varResultado["text"] = "raiz: " + str(resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')

   if(inputIn == 'leer'):
       leerTxt()


def suma():
    if(len(inputNumerico) > 1 ):
        res = 0
        res = inputNumerico[-1] + inputNumerico[-2]
        if(borrado == True):
            del(inputNumerico[-1])
            del(inputNumerico[-1])
        inputNumerico.append(res)
        return(res)
    else:
       return('No se pudo realizar la instruccion')
       
def resta():
    if(len(inputNumerico) > 1 ):
        res = 0
        res = inputNumerico[-1] - inputNumerico[-2]
        if(borrado == True):
            del(inputNumerico[-1])
            del(inputNumerico[-1])
        inputNumerico.append(res)
        return(res)
    else:
        return('no se pudo realizar la instruccion ')

def multiplica():
    if(len(inputNumerico) > 1 ):
        res = 0
        res = inputNumerico[-1] * inputNumerico[-2]
        if(borrado == True):
            del(inputNumerico[-1])
            del(inputNumerico[-1])
        inputNumerico.append(res)
        return(res)
    else:
        return('no se pudo realizar la instruccion ')

def divide():
    if(len(inputNumerico) > 1 ):
        res = 0
        if(inputNumerico[-2] != 0):
            res = inputNumerico[-2] / inputNumerico[-1]
            if(borrado == True):
                del(inputNumerico[-1])
                del(inputNumerico[-1])
            inputNumerico.append(res)
            return(res)
        else:
            return('no se pudo realizar la instruccion "/0" ')
    else:
        return('no se pudo realizar la instruccion ')
    
def factorial():
    n = inputNumerico[-1]
    if(len(inputNumerico) > 0 ):
        factorial = 1
        if int(n) >= 1:
            for i in range(1, int(n)+1):
                factorial = factorial * i
        
        if(borrado == True):
            del(inputNumerico[-1])
        inputNumerico.append(factorial)
        return(factorial)
    else:
        return('no se pudo realizar la instruccion ')

def borradofunc():
    global borrado
    if borrado == False:
        borrado = True
    elif borrado == True:
        borrado = False

def seno(nums = 'default', cicloss = 'default'):
    global borrado
    borrado = False
    

    
    if (len(inputNumerico)>1):
        if(nums == 'default' and cicloss == 'default'):    
            num = inputNumerico[-1] 
            num = (num*math.pi)/180
            ciclos = int(inputNumerico[-2])
        else:
            num = nums
            num = (num*math.pi)/180
            ciclos = int(cicloss)

        
        
        if(ciclos<4 or ciclos>8):
            return 'Dame un numero entre 4 y 8 de ciclos'
        
        with open(dtime, "a") as f:
           f.write('\n')
           f.write('comentario')
           f.write('\n') 
           f.write('Codigo para generar el seno de '+ str(num)+' radianes') 
        inputNumerico.append(num)
        
        with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str(num))
                       f.write('\n')
        
        Instrucciones('*')
        with open(dtime, "a") as f:
               f.write('\n')
               f.write(str('*'))
               f.write('\n')

        for i in range(3,ciclos*2,2):
            for j in range(0,i):
                Instrucciones('duplica')
                with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('duplica'))
                       f.write('\n')
            for j in range(0,i-1):
                Instrucciones('multiplicacion')
                with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('multiplica'))
                       f.write('\n')
            if((i+1) % 4== 0):
                Instrucciones('signo')
                with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('signo'))
                       f.write('\n')
            inputNumerico.append(i)
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str(i))
                       f.write('\n')
            Instrucciones('factorial')
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('factorial'))
                       f.write('\n')
            Instrucciones('division')
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('division'))
                       f.write('\n')
            Instrucciones('intercambia')
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('intercambia'))
                       f.write('\n')
        for i in range(0,ciclos-1):
            Instrucciones('suma')
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('suma'))
                       f.write('\n')
        Instrucciones('muestra')
        with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('muestra'))
                       f.write('\n')
    
        Instrucciones('*')
        with open(dtime, "a") as f:
               f.write('\n')
               f.write(str('*'))
               f.write('\n')
        return inputNumerico[-1]

def coseno(nums = 'default', cicloss = 'default'):   
    #ciclos, valor

    
    if (len(inputNumerico)>1):
        if(nums == 'default' and cicloss == 'default'):    
            num = inputNumerico[-1] 
            num = (num*math.pi)/180
            ciclos = int(inputNumerico[-2])
        else:
            print('mucho antes ',cicloss)
            num = nums
            num = (num*math.pi)/180
            ciclos = int(cicloss)

        if(ciclos<4 or ciclos>8):
            return 'Dame un numero entre 4 y 8 de ciclos'
        
        
        
        with open(dtime, "a") as f:
           f.write('\n')
           f.write('comentario')
           f.write('\n') 
           f.write('Codigo para generar el coseno de '+ str(num)+' radianes') 
        inputNumerico.append(1)
        with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str(1))
                       f.write('\n')
        inputNumerico.append(num)
        with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str(num))
                       f.write('\n')
        
        Instrucciones('*')
        with open(dtime, "a") as f:
               f.write('\n')
               f.write(str('*'))
               f.write('\n')
               
        for i in range(2,ciclos*2-1,2):
            for j in range(0,i):
                Instrucciones('duplica')
                with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('duplica'))
                       f.write('\n')
            for j in range(0,i-1):
                Instrucciones('multiplicacion')
                with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('multiplica'))
                       f.write('\n')
            if((i+2) % 4== 0):
                Instrucciones('signo')
                with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('signo'))
                       f.write('\n')
            inputNumerico.append(i)
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str(i))
                       f.write('\n')
            Instrucciones('factorial')
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('factorial'))
                       f.write('\n')
            Instrucciones('division')
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('division'))
                       f.write('\n')
            Instrucciones('intercambia')
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('intercambia'))
                       f.write('\n')
        Instrucciones('borra')
        with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('borra'))
                       f.write('\n')
        for i in range(0,ciclos-1):
            Instrucciones('suma')
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('suma'))
                       f.write('\n')
        Instrucciones('muestra')
        with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('muestra'))
                       f.write('\n')
        
        Instrucciones('*')
        with open(dtime, "a") as f:
               f.write('\n')
               f.write(str('*'))
               f.write('\n')
        
        return inputNumerico[-1]


def tan():
    #ciclos, valor
    if(inputNumerico[-2]<4 or inputNumerico[-2]>8):
        return 'Dame un numero entre 4 y 8 de ciclos'
    
    ciclos = inputNumerico[-2]
    valor  = inputNumerico[-1]
    
    salida = 0
    sen = seno(valor,ciclos) 
    cos = coseno(valor,ciclos)
    print('res: ',sen)
    print('res2: ',cos)
    salida = sen/cos
    return salida

def raiz():

   if(inputNumerico[-2]<5 or inputNumerico[-2]>15):
        return ('Dame un numero entre 5 y 15 para ciclos')
    
    
   numraizdos = inputNumerico[-1]
   if (len(inputNumerico)>=2):
        num = inputNumerico[-1]
        ciclos = int(inputNumerico[-2])
        with open(dtime, "a") as f:
           f.write('\n')
           f.write('comentario')
           f.write('\n') 
           f.write('Codigo para generar raiz cuadrada de '+ str(num)) 
        with open(dtime, "a") as f:
           f.write('\n')
           f.write(str(num))
           f.write('\n') 
           
        for i in range(0,ciclos+1):
            Instrucciones('duplica')
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('duplica'))
                       f.write('\n')
        n1 =  rd.uniform(0, 1) * num / 2
        with open(dtime, "a") as f:
           f.write('\n')
           f.write(str(n1))
           f.write('\n') 
        inputNumerico.append(n1)
        Instrucciones('*')
        with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('*'))
                       f.write('\n')
        for i in range(0,ciclos):
            with open(dtime, "a") as f:
               f.write('\n')
               f.write('comentario')
               f.write('\n') 
               f.write('inicia el ciclo '+str(i+1))
            Instrucciones('divide')
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('division'))
                       f.write('\n')
            Instrucciones('duplica')
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('duplica'))
                       f.write('\n')
            with open(dtime, "a") as f:
                   f.write('\n')
                   f.write(str(1))
                   f.write('\n') 
            inputNumerico.append(1)
            print(inputNumerico)
            Instrucciones('intercambia n')
            print(inputNumerico)
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('intercambia n'))
                       f.write('\n')
            Instrucciones('duplica')
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('duplica'))
                       f.write('\n')
            with open(dtime, "a") as f:
                   f.write('\n')
                   f.write(str(1))
                   f.write('\n') 
            inputNumerico.append(1)
            Instrucciones('intercambia n')
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('intercambia n'))
                       f.write('\n')
            Instrucciones('divide')
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('division'))
                       f.write('\n')
            with open(dtime, "a") as f:
                   f.write('\n')
                   f.write(str(2))
                   f.write('\n') 
            inputNumerico.append(2)
            Instrucciones('promedio n')
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write(str('promedio n'))
                       f.write('\n')
            with open(dtime, "a") as f:
                       f.write('\n')
                       f.write('comentario')
                       f.write('\n') 
                       f.write('fin del ciclo '+str(i+1))
        Instrucciones('muestra')
        Instrucciones('*')
        with open(dtime, "a") as f:
               f.write('\n')
               f.write(str('*'))
               f.write('\n')
   
   raizuno = inputNumerico[-1]
   
   if(len(inputNumerico)>=1):
       n = math.sqrt(numraizdos)
       raizdos = n
       if(borrado==True):
           inputNumerico.pop()
           inputNumerico.append(n)
       else:
           pass      
   
   return 'raiz1:' + str(raizuno)+' raiz2: '+ str(raizdos)
   

def logaritmo():
    if(len(inputNumerico)>=1):
        n = math.log(inputNumerico[-1]) #logaritmo natural
        if(borrado==True):
            inputNumerico.pop()
        inputNumerico.append(n)
        return n
    else:
        print('Error, faltan datos')    

def duplica():
    if (len(inputNumerico) >= 1):
        dup = inputNumerico[-1]
        print('Duplicando: ' + str(dup))
        inputNumerico.append(dup)
    else:
        print('Faltan datos')
        
def duplicaN():
    if (len(inputNumerico) >= 2):
        n = inputNumerico[-1]
        valor = inputNumerico[-2]
    
        print('Duplicando: {}'.format(valor))
        print('Veces: {}'.format(n))
        
        for i in range(0,math.floor(n)):
            inputNumerico.append(valor)
    else:
        print('Faltan datos')

def intercambia():
    if (len(inputNumerico) >= 2):
        n1 = inputNumerico[-1]
        n2 = inputNumerico[-2]
    
        inputNumerico.pop()
        inputNumerico.pop()
        
        inputNumerico.append(n1)
        inputNumerico.append(n2)
    else:
        print('Faltan datos')

def intercambiaN():
    if (len(inputNumerico) >= 3):
        pos = int(inputNumerico[-1]-1)
        n = inputNumerico[-2]
        inputNumerico.pop()
        
        if (pos >= 0):
            try:
                b = inputNumerico[pos]
                inputNumerico.insert(pos,n)
            except:
                return('N fuera de alcance en la memoria')
        else:
            try:
                b = inputNumerico[len(inputNumerico)+pos]
                inputNumerico.insert(len(inputNumerico)+pos,n)
            except:
                return('N fuera de alcance en la memoria')
        
        inputNumerico.pop()
        inputNumerico.append(b)
        return b
    else:
        print('Error al intercambiar, faltan datos')

def duermeN():
    if(len(inputNumerico) >= 1):
        n = inputNumerico[-1]
        
        print('Durmiendo {} segundos'.format(n))
        time.sleep(math.floor(n))
    else:
        print('Error al dormir, faltan datos')

def duerme():
    try:
        print('Duemriendo 5 segundos')
        time.sleep(5)
    except:
        print('Ocurrio un error al dormir')

def muestra():
    if (borrado==True):
        print('****Con Borrado****')
    else:
        print('****Sin Borrado****')
    
    varResultado["text"] = "Memoria: " + str(inputNumerico)
    print('Memoria: ',inputNumerico)
    with open(dtime, "a") as f:
         f.write(str(inputNumerico))
         f.write('\n')

def promedioN():
    if(len(inputNumerico) >= 1):
        n = inputNumerico[-1]
        if(len(inputNumerico)>=n+1):
            suma = 0
            for i in range(0,round(n)):
                suma += inputNumerico[len(inputNumerico)-1-i]
            if (borrado == True):
                for j in range(0,n+1):
                    inputNumerico.pop()
            inputNumerico.append(suma/n)
            return inputNumerico[-1]
        else: 
            print('No se puede promediar {} numeros'.format(n))
    else:
        print('Error al promediar, faltan datos')


    
def comenGraf(co, ve):
    com = co.get()
    varResultado["text"] = "Comentario: "+ str(com)
    ve.destroy()
    
def comentario():
    try:
        comment = input('Escriba un comentario: ')
        print('Comentario: '+comment)
        return comment
    except:
        print('Ocurrio un error')


def ec2grado():
    if (len(inputNumerico)>=3):
        a=inputNumerico[-3]
        b=inputNumerico[-2]
        c=inputNumerico[-1]
        
        d = b**2 - (4*a*c)
        if (d<0):
            print('No tiene raices reales')
        else:
            x1=(-b+math.sqrt(d))/(2*a)
            x2=(-b-math.sqrt(d))/(2*a)
            if (borrado==True):
                for i in range(0,3):
                    inputNumerico.pop()
            inputNumerico.append(x1)
            inputNumerico.append(x2)
            return x1, x2
    else:
        print('Error al resolver Ec 2 grado, faltan datos')

def memoria():
    if(len(inputNumerico)>0):
        inputNumerico.append(len(inputNumerico))
        return inputNumerico[-1]
    else:
        print('Error, no hay suficientes datos')


def Cls():
    os.system('cls')
    

def borra():
    if(len(inputNumerico)>=1):
        n = inputNumerico[-1]
        inputNumerico.remove(n)
        return n
    else: 
        print('Error al borrar, faltan datos')

def signo():
    if(len(inputNumerico)>=1):
        n = inputNumerico[-1]
        if(borrado==True):
            inputNumerico.pop()
        inputNumerico.append(-n)
        return inputNumerico[-1]
    else:
        print('Error al cambiar signo, faltan datos')

def reset():
    print('Tamaño de memoria = ' +len(inputNumerico))
    print('Borrando memoria')
    if(borrado==True):
        borradofunc()
    inputNumerico.clear()

def leerTxt():
    with open('ejemplo.txt') as f:
        lines = f.readlines()
        
    checkArray=[]
    for k in range(0,len(lines)):
        auxi = lines[k].split()    
        checkArray.append(auxi)
    
    for i in range(0,len(lines)):
        arrayAux = lines[i].split()
        instruccionAux = arrayAux[-1]
        del arrayAux[-1]
        
        check = 1
        if(len(inputNumerico)>0):
            check = inputNumerico[-1]
        
        if check == 0:
            inputNumerico.append(1)
            continue 
        
        if checkArray[i-1][-1]=='salta':
            continue
        
        for j in arrayAux:
            inputNumerico.append(float(j))
        Instrucciones(instruccionAux)


def GetNum():
    return inputNumerosGraf1.get()


#-----------------------MAIN---------------------------------#
now = datetime.now()
dtime = 'Resultado'+now.strftime("%d%m%Y%H%M")
dtime =  dtime+'.txt'
file_exists = exists(dtime)


if not file_exists:
    f= open(dtime,"w+")   
     
inputInstruccion = 'x'
inputNumerico = []
borrado = False
numeros=[]
#       Quite el while que eso solo jala con la logica de la terminal

ventana = tkinter.Tk()
ventana.geometry("1200x350")


    
resp = ["suma","resta", "multiplicacion","division","seno","coseno", "tangente","factorial","ecuacion 2 grado", "signo","salta","salta 0",
        "cls","borra", "reset", "duplica", "duplica n","intercambia","intercambia n","memoria","duerme", 
        "duerme n",'raiz',"comentario","muestra","promedio n","leer", "*"]
def clear_text():
   inputNumerosGraf1.delete(0, 50)
   
   inputInstruccionGraf1.delete(0, 50)
   varResultado["text"] = " "
   labelError["text"] = ""

def pasarVar():

    Num1 = inputNumerosGraf1.get()
    
    inputNumeros = Num1.split()
    for i in range(0, len(inputNumeros)):
        try:
            inputNumerico.append(float(inputNumeros[i]))
        except:
            pass
    
    Instruccion = (inputInstruccionGraf1.get()).lower()
    
    ver = 0
    for i in resp :
        if(i == Instruccion):
            ver = 1
            varResultado["fg"] = "black"
            labelError["text"] = ""
            Instrucciones(Instruccion)
    
            
    
    with open(dtime, "a") as f:
        f.write('\n')
        f.write(str(Instruccion))
        f.write('\n')  
            
    if ver == 0 :
        
        clear_text()
        labelError["text"] = "Error en la instruccion"
            
def on_closing():
    print("A cerrar")
    try:
        
        f.close()
    except NameError:
        pass
    ventana.destroy()
    
inputLabel0 = tkinter.Label(ventana,text = "Inserta los numeros que\n quieres introducir por espacios", font = "Helvetica 13", fg="gray")
inputLabel0.grid(row = 0, column =3, padx = 35, pady = 30)
inputLabel = tkinter.Label(ventana,text = "Ingresa los numeros ",font = "Helvetica 19")
inputLabel.grid(row = 0, column =0, padx = 35, pady = 30)
inputNumerosGraf1 = tkinter.Entry(ventana, font = "Helvetica 19", width = 12)
inputNumerosGraf1.grid(row = 0, column =1, padx = 5, pady = 30)

instruccionLabel = tkinter.Label(ventana,text = "Instruccion:", font = "Helvetica 19")
instruccionLabel.grid(row = 1, column =0, padx = 5, pady = 15)
inputInstruccionGraf1 = tkinter.Entry(ventana, font = "Helvetica 19", width = 12)
inputInstruccionGraf1.grid(row = 1, column =1, padx = 5, pady = 15)
enviarBoton = tkinter.Button(ventana, text = "Enter", padx = 28, pady=5, command = pasarVar)
enviarBoton.grid(row = 3, column = 0, ipadx = 25, pady = 8)
clearBoton = tkinter.Button(ventana, text = "Clear", padx = 28, pady=5, command = clear_text)
clearBoton.grid(row = 3, column = 1, ipadx = 25, pady = 24)
labelResultado = tkinter.Label(ventana, text = "Resultado: ", font = "Helvetica 29")
labelResultado.grid(row = 1, column = 3, pady = 10, padx = 40)
varResultado = tkinter.Label(ventana, font = "Helvetica 19")
varResultado.grid(row = 1, column = 4, pady = 40)
labelError = tkinter.Label(ventana, font = "Helvetica 21", fg = "red")
labelError.grid(row = 2, column = 3, pady = 10, padx = 40)


ventana.protocol("WM_DELETE_WINDOW", on_closing)
ventana.mainloop()