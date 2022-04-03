# -*- coding: utf-8 -*-
import math
import time

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

def seno(x):
    signo=1
    salida=0
    for i in range(1,11,2):
        salida = salida +(signo*pow(x,i)/math.factorial(i))
        signo = -signo
    
    return salida

def coseno(x):
    signo=1
    salida=0
    for i in range(0,12,2):
        salida = salida +(signo*pow(x,i)/math.factorial(i))
        signo = -signo
    
    return salida

def tan(x):
    salida = 0
    salida = seno(x)/coseno(x)
    return salida

def duplica(array):
    if (len(array) >= 1):
        dup = array[-1]
    
        print('Duplicando: ' + dup)
        array.append(dup)
    else:
        print('Faltan datos') 
        
def duplicaN(array):
    if (array.len() >= 2):
        n = array[-1]
        valor = array[-2]
    
        print('Duplicando: ' + valor)
        print('Veces: ' + n)
        
        for i in range(0,n):
            array.append(valor)
        
    else:
        print('Faltan datos')

def intercambia(array):
    if (len(array) >= 2):
        n1 = array[-1]
        n2 = array[-2]
    
        array.pop()
        array.pop()
        
        array.append(n1)
        array.append(n2)
    else:
        print('Faltan datos')

def intercambiaN(array):
    if (len(array) >= 3):
        pos = array[-1]-1
        n = array[-2]
        array.pop()
        
        if (pos >= 0):
            b = array[pos]
            array.insert(pos,n)
        else:
            for i in range(0,pos):
                array.append(0)
            array.insert(len(array)-1+pos,n)
        array.pop()
        array.append(b)
    else:
        print('Error al intercambiar, faltan datos')

def duermeN(array):
    if(len(array >= 1)):
        n = array[-1]
        
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

def muestra(array):
    if (borrado==True):
        print('*Con Borrado*')
    else:
        print('*Sin Borrado*')
    for i, value in enumerate(array):
        print(value + '.- ' +array)

def promedioN(array):
    if(len(array) >= 1):
        n = array[-1]
        if(len(array)>=n+1):
            suma = 0
            for i in range(0,n):
                suma += array[len(array)-2-i]
        if (borrado == True):
            for j in range(0,n):
                array.pop()
        array.append(suma/n)
    else:
        print('Error al promediar, faltan datos')

def comentario():
    try:
        comment = input('Escriba un comentario: ')
        print('Comentario: '+comment)
    except:
        print('Ocurrio un error')


def ec2grado(array):
    if (len(array)>=3):
        a=array[-3]
        b=array[-2]
        c=array[-1]
        
        d = b**2 - (4*a*c)
        if (d<0):
            print('No tiene raices reales')
        else:
            x1=(-b+math.sqrt(d))/(2*a)
            x2=(-b-math.sqrt(d))/(2*a)
            if (borrado==True):
                for i in range(0,3):
                    array.pop()
            array.append(x1)
            array.append(x2)
    else:
        print('Error al resolver Ec 2 grado, faltan datos')

def memoria(array):
    if(len(array)>0):
        array.append(len(array))
    else:
        print('Error, no hay suficientes datos')


inputInstruccion = 'x'
inputNumerico = []
borrado = False


while inputInstruccion != 'salir' :
    
   inputInstruccion = input('Dame tu instruccion a realizar: ')
   
   salir = 'No'
   
   noNumInstrucciones = ['salir', '*','duplica'] #instrucciones que no necesitan input de numero
   
   if(inputInstruccion in noNumInstrucciones):
       while(salir != 'si'):
           try:
               aux = float(input('Dame los numeros: '))
               inputNumerico.append(aux)
           except:
               pass
           salir = input('¿Quieres terminar de guardar numeros? ')
           
   if(inputInstruccion == '*'):
       borradofunc()
       if borrado == False:
           print('No hay borrado')
       elif borrado == True:
           print('Ya hay borrado')

   if(inputInstruccion == 'suma'):
       print('la suma fue: ',suma())
   if(inputInstruccion == 'resta'):
       print('la resta fue: ',resta())
   if(inputInstruccion == 'multiplicacion'):
       print('la multiplicacion fue: ',multiplica())
   if(inputInstruccion == 'division'):
       print('la division fue: ',divide())
   if(inputInstruccion == 'factorial'):
       print('el factorial fue: ',factorial())
   if(inputInstruccion == 'seno'):
       print('el seno fue: ',seno())
   if(inputInstruccion == 'coseno'):
       print('el coseno fue: ',coseno())
   if(inputInstruccion == 'tangente'):
       print('el tangente fue: ',tan())
   if(inputInstruccion == 'duplica'):
      duplica()
   if(inputInstruccion == 'duplica n'):
       duplicaN()
   if(inputInstruccion == 'intercambia'):
       intercambia()
   if(inputInstruccion == 'intercambia n'):
       intercambiaN()
   if(inputInstruccion == 'duerme'):
       duerme()
   if(inputInstruccion == 'duerme n'):
       duermeN()
   if(inputInstruccion == 'muestra '):
       muestra()
   if(inputInstruccion == 'promedio n'):
       promedioN()
   if(inputInstruccion == 'comentario '):
       comentario()
   if(inputInstruccion == 'ecuacion 2 grado'):
       ec2grado()
   if(inputInstruccion == 'memoria'):
       memoria()

    
   
   
   
   