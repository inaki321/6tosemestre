import time
from datetime import date, datetime
from os.path import exists
import os 
   
def Instrucciones(inputIn):

   if(inputIn == 'suma'):
       resA = suma()
       print('suma: ',resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')

   if(inputIn == 'resta'):
       resA = resta()
       print('resta: ',resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')


   if(inputIn == 'multiplicacion'):
       resA = multiplica()
       print('multiplicacion: ',resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')

   if(inputIn == 'division'):
       resA = divide()
       print('division: ',resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')

   if(inputIn == 'factorial'):
       resA = factorial()
       print('factorial: ',resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')
    
#Aqui hay error        
   if(inputIn == 'seno'):
       resA = seno()
       print('factorial: ',resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')

   if(inputIn == 'coseno'):
       resA = coseno()
       print('factorial: ',resA)
       with open(dtime, "a") as f:
           f.write(str(resA))
           f.write('\n')
           
   if(inputIn == 'tangente'):
       resA = tan()
       print('factorial: ',resA)
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
       intercambiaN()
   if(inputIn == 'duerme'):
       duerme()
   if(inputIn == 'duerme n'):
       duermeN()
   if(inputIn == 'muestra '):
       muestra()
   if(inputIn == 'promedio n'):
       promedioN()
   if(inputIn == 'comentario '):
       comentario()
   if(inputIn == 'ecuacion 2 grado'):
       ec2grado()
   if(inputIn == 'memoria'):
       memoria()
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
            res = inputNumerico[-1] / inputNumerico[-2]
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

def seno():
    signo=1
    salida=0
    for i in range(1,11,2):
        salida = salida +(signo*pow(inputNumerico[-1],i)/math.factorial(i))
        signo = -signo
    
    return salida

def coseno():
    signo=1
    salida=0
    for i in range(0,12,2):
        salida = salida +(signo*pow(inputNumerico[-1],i)/math.factorial(i))
        signo = -signo
    
    return salida

def tan():
    salida = 0
    salida = seno(inputNumerico[-1])/coseno(inputNumerico[-1])
    return salida

def raiz():
    if(inputNumerico>=1):
        n = math.sqrt(inputNumerico[-1])
        if(borrado==True):
            inputNumerico.pop()
        inputNumerico.append(n)
    else:
        print('Error, faltan datos')

def logaritmo():
    if(inputNumerico>=1):
        n = math.log(inputNumerico[-1]) #logaritmo natural
        if(borrado==True):
            inputNumerico.pop()
        inputNumerico.append(n)
    else:
        print('Error, faltan datos')    

def duplica():
    if (len(inputNumerico) >= 1):
        dup = inputNumerico[-1]
    
        print('Duplicando: ' + dup)
        inputNumerico.append(dup)
    else:
        print('Faltan datos')
        
def duplicaN():
    if (inputNumerico.len() >= 2):
        n = inputNumerico[-1]
        valor = inputNumerico[-2]
    
        print('Duplicando: ' + valor)
        print('Veces: ' + n)
        
        for i in range(0,n):
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
    else:
        print('Error al intercambiar, faltan datos')

def duermeN():
    if(len(inputNumerico >= 1)):
        n = inputNumerico[-1]
        
        print('Durmiendo ' + n + 'segundos')
        time.sleep(n)
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
    for i, value in enumerate(inputNumerico):
        print(value + '.- ' +inputNumerico)

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
    else:
        print('Error al promediar, faltan datos')

def comentario():
    try:
        comment = input('Escriba un comentario: ')
        print('Comentario: '+comment)
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
    else:
        print('Error al resolver Ec 2 grado, faltan datos')

def memoria():
    if(len(inputNumerico)>0):
        inputNumerico.append(len(inputNumerico))
    else:
        print('Error, no hay suficientes datos')

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

while inputInstruccion != 'salir' :
   
   numeros=[]
   checkInput = input('deseas introducir numeros? ')
   if(checkInput == 'si'):
       inputNumeros = input('Dame los numeros que quieres introducir por espacios: ') 
       inputNumeros = inputNumeros.split()
       for i in range(0, len(inputNumeros)):
           try:
               inputNumerico.append(float(inputNumeros[i]))
           except:
               pass
   inputInstruccion = input('Dame tu instruccion a realizar: ')
   
           
   if(inputInstruccion == '*'):
       borradofunc()
       if borrado == False:
           print('No hay borrado')
       elif borrado == True:
           print('Ya hay borrado')
           
   
   with open(dtime, "a") as f:
       f.write('\n')
       f.write(str(inputInstruccion))
       f.write('\n')      
   
   Instrucciones(inputInstruccion)
   if(inputInstruccion=='salir'):
       f.close()