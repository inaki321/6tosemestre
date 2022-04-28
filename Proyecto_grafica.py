# -*- coding: utf-8 -*-
import tkinter
import pymysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.layers import Input, SimpleRNN, GRU, LSTM, Dense, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import SGD, Adam
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
db = pymysql.connect(host='localhost',user='root',passwd='',database='proyectobda')


ventana = tkinter.Tk()
ventana.geometry("1200x350")

monedas = ['Argentine_Peso','Australian_Dollar','Bahraini_Dinar','Botswana_Pula','Brazilian_Real',
'British_Pound','Bruneian_Dollar','Bulgarian_Lev','Canadian_Dollar','Chilean_Peso','Chinese_Yuan_Renminbi',
'Colombian_Peso','Croatian_Kuna','Czech_Koruna','Danish_Krone','Emirati_Dirham','Euro','Hong_Kong_Dollar',
'Hungarian_Forint','Icelandic_Krona','Indian_Rupee','Indonesian_Rupiah','Iranian_Rial','Israeli_Shekel','Japanese_Yen',
'Kazakhstani_Tenge','Kuwaiti_Dinar','Libyan_Dinar','Malaysian_Ringgit','Mauritian_Rupee','Mexican_Peso',
'Nepalese_Rupee','New_Zealand_Dollar','Norwegian_Krone','Omani_Rial','Pakistani_Rupee','Philippine_Peso',
'Polish_Zloty','Qatari_Riyal','Romanian_New_Leu','Russian_Ruble','Saudi_Arabian_Riyal',
'Singapore_Dollar','South_African_Rand','South_Korean_Won','Sri_Lankan_Rupee','Swedish_Krona','Swiss_Franc',
'Taiwan_New_Dollar','Thai_Baht','Trinidadian_Dollar','Turkish_Lira','Venezuelan_Bolivar']
monedasCheck = ['Argentina','Australia','Bahraini','Botswana','Brasil',
'Inglaterra','Bruneian','Bulgaria','Canada','Chile','China','Colombia','Croacia','Republica Checa',
'Danish','Emiratos','Euro','Hong Kong','Hungria','Islandia','India','Indonesia','Iran','Israel','Japon',
'Kazajistan','Kuwait','Libia','Malaysia','Mauritian','Mexico','Nepal','Nueva Zelanda','Noruega','Omani','Pakistan','Filipinas',
'Polonia','Qatar','Romania','Rusia','Arabia Saudita','Singapur','Sudafrica','Corea del Sur','Sri Lanka','Suecia','Suiza',
'Taiwan','Thai','Trinidad y Tobago','Turquia','Venezuela']    

def GetNum():
    return inputNumerosGraf1.get()

def on_closing():
    print("A cerrar")
    try:
        
        f.close()
    except NameError:
        pass
    ventana.destroy()
 
def graphSola():
    pred = inputNumerosGraf1.get()
    idx = monedasCheck.index(pred)
    monedas[idx]
    sql = "SELECT {},dateymd FROM mytable".format(monedas[idx])
    print(sql)
    df_graph = pd.read_sql(sql, db)
    x_axis = df_graph['dateymd']
    
    x_axis = np.array(x_axis, dtype='datetime64[D]')
    print(x_axis)

    
    window = tkinter.Tk()
    window.title('Grafica')
    window.geometry("700x500")
    fig = plt.Figure(figsize=(5,5), dpi=100)
    fig.add_subplot(111).plot(x_axis,df_graph[monedas[idx]])
    chart = FigureCanvasTkAgg(fig,window)
    chart.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand = True)

def clear_text():
   inputNumerosGraf1.delete(0, 50)
   

    
def Prediccion():
    print('Iniciando prediccion') 
    
    pred = inputNumerosGraf1.get()
    idx = monedasCheck.index(pred)
    monedas[idx]
    
    sql = "SELECT "+monedas[idx]+" FROM mytable"
    df = pd.read_sql(sql, db)
    series = df.values.reshape(-1,1)
    
    query = "CALL CheckTables"
    #DELIMITER //
    
    # CREATE PROCEDURE Checktables()
    # BEGIN
    #     CREATE TABLE IF NOT EXISTS results( returnFormula double, PrevClose double );
    # END //
    
    # DELIMITER ;
    cursor = db.cursor()
    cursor.execute(query)
    
    query = "DELETE FROM results"
    cursor = db.cursor()
    cursor.execute(query)
    
    cont=0
    x =[]
    for i in range(0,len(df)-10):
        sql = "SELECT " +monedas[idx]+" FROM mytable LIMIT {0},10".format(cont)
        df_data = pd.read_sql(sql, db)
        df_data = df_data.values.tolist()
        cont+=1
        x.append(df_data)
    
    cont=10
    y =[]
    for i in range(0,len(df)-10):
        sql = "SELECT " +monedas[idx]+" FROM mytable LIMIT {0},1".format(cont)
        df_data = pd.read_sql(sql, db)
        df_data = df_data.values.tolist()
        cont+=1
        y.append(df_data)
    
    x = np.array(x)
    
    y = np.array(y)
    
    
    y = y.transpose(2,0,1).reshape(-1,y.shape[1])

        # #Normalizar datos
    scaler = StandardScaler() #STANDARIZA LOS DATOS
    scaler.fit(series[:len(series) // 2]) #Divido los datos entre 2, porque no quiero incluir test data en un inicio
    # Test data es de la mitad al final y training data es del inicio a la mitad
    # print(series.shape)#se normalizan y dividen los datos para tener una matriz de (4061,1)
    series = scaler.transform(y).flatten()
    vals = df.values.tolist()
    
    for i in range(0,len(vals)):
        if (i==0):
            num = 0
        else:
            num=vals[i-1][0]
        nums=vals[i][0]
        query2 = "INSERT INTO results (PrevClose,moneda) VALUES ({0},{1})".format(num,nums)
        cursor = db.cursor()
        cursor.execute(query2)
    
    
    query = "UPDATE results SET returnFormula = ((moneda - PrevClose)/PrevClose)"
    cursor = db.cursor()
    cursor.execute(query)
    
    sql = "SELECT returnFormula FROM results"
    df['Return'] = pd.read_sql(sql, db)
    series = df['Return'].values[1:].reshape(-1, 1)
    scaler = StandardScaler()
    # print('SERIES', series)
    scaler.fit(series[:len(series) // 2])
    series = scaler.transform(series).flatten()
    # print(series.shape)
    
    T = 10
    D = 1
    x = []
    y = []
    for t in range(len(series) - T):
      X = series[t:t+T]
      x.append(X)
      Y = series[t+T]
      y.append(Y)
    
    x = np.array(x).reshape(-1, T, 1) # Now the data should be N x T x D
    y = np.array(y)
    N=len(df)-10
    # RED NEURONAL
    #La misma red del modelo anterior, solo cambio de 'Close' a 'Return'
    i = Input(shape=(T, 1)) 
    xn = LSTM(5)(i)
    xn = Dense(1)(xn)
    model = Model(i, xn)
    model.compile( loss='mse', optimizer=Adam(lr=0.01) )
    y = y.flatten()
    x_train = x[:-N//2]
    y_train = y[:-N//2]
    x_test = x[-N//2:]
    y_test = y[-N//2:]
    
    r = model.fit( x_train, y_train, epochs=40, validation_data=(x_test, y_test), verbose=2 )
    # #Comparacion de perdidas
    # #Se acomoda el modelo al noise=> fitting to the noise, no va muy bien el modelo
    # plt.plot(r.history['loss'], label='Perdidas')
    # plt.plot(r.history['val_loss'], label='val_Perdidas')
    # plt.legend()
    # #Comparacion de los valores verdaderos con las predicciones
    # #One-step forecast
    outputs = model.predict(x) #se manda X porque se evalua todo el modelo, no train ni test
    predictions = outputs[:,0]
    
    window = tkinter.Tk()
    window.title('Grafica')
    window.geometry("700x500")
    fig = plt.Figure(figsize=(5,5), dpi=100)
    a = fig.add_subplot(111)
    a.plot(y, label='Valor Verdadero')
    a.plot(predictions, label='Prediccion')
    
    chart = FigureCanvasTkAgg(fig,window)
    chart.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand = True)
    
    
    plt.plot(y, label='Valor Verdadero')
    plt.plot(predictions, label='Prediccion')
    plt.legend()
    plt.show()


inputLabel0 = tkinter.Label(ventana,text = "Inserte el país ", font = "Helvetica 13", fg="gray")
inputLabel0.grid(row = 0, column =3, padx = 35, pady = 30)
inputLabel = tkinter.Label(ventana,text = "Que moneda quieres su predicción? ",font = "Helvetica 19")
inputLabel.grid(row = 0, column =0, padx = 35, pady = 30)
inputNumerosGraf1 = tkinter.Entry(ventana, font = "Helvetica 19", width = 12)
inputNumerosGraf1.grid(row = 0, column =1, padx = 5, pady = 30)
enviarBoton = tkinter.Button(ventana, text = "Ver gráfica actual", padx = 28, pady=5, command = graphSola)
enviarBoton.grid(row = 3, column = 0, ipadx = 25, pady = 8)
enviarBotonTwo = tkinter.Button(ventana, text = "Prediccion de la moneda", padx = 28, pady=5, command = Prediccion)
enviarBotonTwo.grid(row = 4, column = 0, ipadx = 25, pady = 8)
clearBoton = tkinter.Button(ventana, text = "Borrar", padx = 28, pady=5, command = clear_text)
clearBoton.grid(row = 3, column = 1, ipadx = 25, pady = 24)
ventana.protocol("WM_DELETE_WINDOW", on_closing)
ventana.mainloop()


