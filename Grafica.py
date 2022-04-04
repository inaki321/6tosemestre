# -*- coding: utf-8 -*-
import math
import time
from datetime import date, datetime
from os.path import exists
import os 
import tkinter 


   
def Instrucciones(inputIn):

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
    
#Aqui hay error        
   if(inputIn == 'seno'):
       resA = seno()
       print('seno: ',resA)
       varResultado["text"] = "seno: " + str(resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')

   if(inputIn == 'coseno'):
       resA = coseno()
       varResultado["text"] = "coseno: " + str(resA)
       print('coseno: ',resA)
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
   if(inputIn == 'duplica n'):  #Hay error
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
   if(inputIn == 'duerme n'):   #hay error
       duermeN()
   if(inputIn == 'muestra '):
       muestra()
   if(inputIn == 'promedio n'): #Hay error
       resA = promedioN()
       print('promedio: ',resA)
       varResultado["text"] = "promedio: " + str(resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')
           
   if(inputIn == 'comentario'):
       comentario()
   if(inputIn == 'ecuacion 2 grado'):
       resA,resB = ec2grado()
       print('ecuacion 2do grado: '+ str(resA) + ' '+ str(resB))
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
   if(inputIn == 'borra'):      #Hay error
       resA = borra()
       print('borrado: ',resA)
       varResultado["text"] = "borrado: " + str(resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')
   if(inputIn == 'reset'):
       reset()
   if(inputIn == 'signo'):
       resA = signo()
       print('signo: ',resA)
       varResultado["text"] = "signo: " + str(resA)
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
       labelError["text"] = "No se pudo realizar la instruccion"
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
        labelError["text"] = "No se pudo realizar la instruccion"
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
        labelError["text"] = "No se pudo realizar la instruccion"
        return('no se pudo realizar la instruccion ')

def divide():
    if(len(inputNumerico) > 1 ):
        res = 0
        if(inputNumerico[-2] != 0):
            res = inputNumerico[-1] / inputNumerico[-2]
            if(borrado == True):
                del(inputNumerico[-1])
                del(inputNumerico[-1])
            inputNumerico.append(res)
            return(res)
        else:
            labelError["text"] = 'no se pudo realizar la instruccion "/0" '
            return('no se pudo realizar la instruccion "/0" ')
    else:
        labelError["text"] = "No se pudo realizar la instruccion"
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
            del(inputNumerico[-1])
        inputNumerico.append(factorial)
        return(factorial)
    else:
        labelError["text"] = "No se pudo realizar la instruccion"
        return('no se pudo realizar la instruccion ')


def borradofunc():
    global borrado
    if borrado == False:
        borrado = True
    elif borrado == True:
        borrado = False

def seno():
    signo=1
    salida=0
    n = (inputNumerico[-1]*math.pi)/180
    for i in range(1,11,2):
        salida = salida +(signo*pow(n,i)/math.factorial(i))
        signo = -signo
    
    return salida

def coseno():
    signo=1
    salida=0
    n = (inputNumerico[-1]*math.pi)/180
    for i in range(0,12,2):
        salida = salida +(signo*pow(n,i)/math.factorial(i))
        signo = -signo
    
    return salida

def tan():
    salida = 0
    salida = seno()/coseno()
    return salida

def raiz():
    if(inputNumerico>=1):
        n = math.sqrt(inputNumerico[-1])
        if(borrado==True):
            inputNumerico.pop()
        inputNumerico.append(n)
        return n
    else:
        labelError["text"] = "Error, faltan datos"
        print('Error, faltan datos')

def logaritmo():
    if(inputNumerico>=1):
        n = math.log(inputNumerico[-1]) #logaritmo natural
        if(borrado==True):
            inputNumerico.pop()
        inputNumerico.append(n)
        return n
    else:
        labelError["text"] = "Error, faltan datos"
        print('Error, faltan datos')    

def duplica():
    if (len(inputNumerico) >= 1):
        dup = inputNumerico[-1]
     
        print('Duplicando: ' + str(dup))
        varResultado["text"] = "Duplicado: " + str(dup)
        inputNumerico.append(dup)
    else:
        labelError["text"] = "Faltan datos"
        print('Faltan datos')
        
def duplicaN():
    if (inputNumerico.len() >= 2):
        n = inputNumerico[-1]
        valor = inputNumerico[-2]
    
        print('Duplicando: ' + valor)
        varResultado["text"] = "Duplicado: "+str(valor)
        print('Veces: ' + n)
        labelError["text"] = "Veces: " + str(n)
        
        for i in range(0,n):
            inputNumerico.append(valor)
        
    else:
        labelError["text"] = "Faltan datos"
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
        labelError["text"] = "Error, faltan datos"
        print('Faltan datos')

def intercambiaN():
    if (len(inputNumerico) >= 3):
        pos = inputNumerico[-1]-1
        n = inputNumerico[-2]
        inputNumerico.pop()
        
        if (pos >= 0):
            b = inputNumerico[pos]
            inputNumerico.insert(pos,n)
        else:
            for i in range(0,pos):
                inputNumerico.append(0)
            inputNumerico.insert(len(inputNumerico)-1+pos,n)
        inputNumerico.pop()
        inputNumerico.append(b)
        return b
    else:
        labelError["text"] = "Error al intercambiar, faltan datos"
        print('Error al intercambiar, faltan datos')

def duermeN():
    if(len(inputNumerico >= 1)):
        n = inputNumerico[-1]
        varResultado["text"] = "Durmiendo " + str(n) + " segundos"
        print('Durmiendo ' + n + 'segundos')
        
        time.sleep(n)
    else:
        labelError["text"] = "Error al intercambiar, faltan datos"
        print('Error al dormir, faltan datos')

def duerme():
    try:
        varResultado["text"] = "Durmiendo 5 segundos"
        print('Duemriendo 5 segundos')
        time.sleep(5)
    except:
        labelError["text"] = "Ocurrio un error al dormir"
        print('Ocurrio un error al dormir')

def muestra():
    mu = []
    if (borrado==True):
        print('****Con Borrado****')
        labelError["text"] = "****Con Borrado****"
    else:
        print('****Sin Borrado****')
        labelError["text"] = "****Sin Borrado****"
    for i, value in enumerate(inputNumerico):
        mu[i] = print(value + '.- ' +inputNumerico)
        
    varResultado["text"] = mu

def promedioN():
    if(len(inputNumerico) >= 1):
        n = inputNumerico[-1]
        if(len(inputNumerico)>=n+1):
            suma = 0
            for i in range(0,n):
                suma += inputNumerico[len(inputNumerico)-2-i]
        if (borrado == True):
            for j in range(0,n):
                inputNumerico.pop()
        inputNumerico.append(suma/n)
        return inputNumerico[-1]
    else:
        labelError["text"] = "Error al promediar, faltan datos"
        print('Error al promediar, faltan datos')


    
def comenGraf(co, ve):
    com = co.get()
    varResultado["text"] = "Comentario: "+ str(com)
    ve.destroy()
    
def  comentario():
    try:
        
        ventanaComm = tkinter.Tk()
        ventanaComm.geometry("1200x350")
        #comment = input('Escriba un comentario: ')
        labelComment = tkinter.Label(ventanaComm,text="Escriba un comentario: ", font = "Helvetica 12", width = 18)
        inputComment = tkinter.Entry(ventanaComm, font = "Helvetica 19", width = 15)
        labelComment.grid(row = 4, column =0, padx = 5, pady = 30)
        inputComment.grid(row = 4, column =1, padx = 15, pady = 30)
        
        
        botonComment = tkinter.Button(ventanaComm, text = "Enter", padx = 18, pady=5, command = lambda:  comenGraf(inputComment, ventanaComm)  )
        botonComment.grid(row = 4, column = 2, ipadx = 10, pady = 8)
        ventanaComm.protocol("WM_DELETE_WINDOW")
        ventanaComm.mainloop()
        print('Comentario: ' + inputComment.get())
        
    except:
        labelError["text"] = "Ocurrio un error"
        print('Ocurrio un error')


    

def ec2grado():
    if (len(inputNumerico)>=3):
        a=inputNumerico[-3]
        b=inputNumerico[-2]
        c=inputNumerico[-1]
        
        d = b**2 - (4*a*c)
        if (d<0):
            labelError["text"] = "No tiene raices reales"
            print('No tiene raices reales')
        else:
            x1=(-b+math.sqrt(d))/(2*a)
            x2=(-b-math.sqrt(d))/(2*a)
            if (borrado==True):
                for i in range(0,3):
                    inputNumerico.pop()
            inputNumerico.append(x1)
            inputNumerico.append(x2)
            return x1,x2
    else:
        labelError["text"] = "Error al resolver Ec 2 grado, faltan datos"
        print('Error al resolver Ec 2 grado, faltan datos')

def memoria():
    if(len(inputNumerico)>0):
        inputNumerico.append(len(inputNumerico))
        return inputNumerico[-1]
    else:
        labelError["text"] = "Error, no hay suficientes datos"
        print('Error, no hay suficientes datos')

def Cls():
    os.system('cls||clear')
    

def borra():
    if(inputNumerico>=1):
        n = inputNumerico[-1]
        inputNumerico.remove(n)
    else: 
        labelError["text"] = "Error al borrar, faltan datos"
        print('Error al borrar, faltan datos')

def signo():
    if(inputNumerico>=1):
        n = inputNumerico[-1]
        if(borrado==True):
            inputNumerico.pop()
        inputNumerico.append(-n)
        return inputNumerico[-1]
    else:
        labelError["text"] = "Error al cambiar signo, faltan datos"
        print('Error al cambiar signo, faltan datos')

def reset():
    varResultado["text"] = "Tamaño de memoria = " + str(len(inputNumerico))
    print('Tamaño de memoria = ' +len(inputNumerico))
    labelError["text"] = "Borrando memoria"
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
dtime = now.strftime("%d%m%Y%H%M")
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
        "duerme n","comentario","muestra","promedio n","leer"]
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
    
    if(Instruccion == '*'):
        borradofunc()
        if borrado == False:
            print('No hay borrado')
        elif borrado == True:
            print('Ya hay borrado')
            
    
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
clearBoton.grid(row = 3, column = 1, ipadx = 25, pady = 8)
labelResultado = tkinter.Label(ventana, text = "Resultado: ", font = "Helvetica 29")
labelResultado.grid(row = 1, column = 3, pady = 10, padx = 40)
varResultado = tkinter.Label(ventana, font = "Helvetica 19")
varResultado.grid(row = 1, column = 4, pady = 15)
labelError = tkinter.Label(ventana, font = "Helvetica 21", fg = "red")
labelError.grid(row = 2, column = 3, pady = 10, padx = 40)


ventana.protocol("WM_DELETE_WINDOW", on_closing)
ventana.mainloop()