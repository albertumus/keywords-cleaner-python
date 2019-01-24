# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 11:55:10 2019

@author: alberto.camina
"""

import os
import pandas as pd

### SUBPROGRAMAS ###

def cargarCSV(lcsv):
    """PRE: Lista de CSV 
    OBJ: Crear una lista de dataframes por cada csv
    """
    
    ldataframes = []
    for csv in lcsv:
        nuevo_df = pd.read_csv(csv)
        ldataframes.append(nuevo_df)
        
    
    df_keywords = pd.concat(ldataframes, sort=False, ignore_index=True)
    
    return df_keywords
    
def pedirKeywordsAlUsuario():
    """PRE: None
    OBJ: pide keywords al usuario hasta que este introduce 'fin'
    """
    
    listaDeKeywords = []
    print("A continuación escribe las keywords que quieras borrar. Introduce 'fin' para terminar")
    keywordsParaBorrar = input("Keyword: ")  

    
    
    while keywordsParaBorrar != "fin":
        listaDeKeywords.append(keywordsParaBorrar)
        keywordsParaBorrar = input("Keyword: ")  

    return listaDeKeywords

def leerTxt():
    """PRE: None
    OBJ: leer las palabras de un txt, IMPORTANTE: poner "," al final de cada palabra
    """
    
    nombreTxt = input("Introduce el nombre del fichero, junto la extensión. Ej: 'fichero.txt' - ")
    listaDeKeywords = []
    
    txt = open(nombreTxt, "r")
    for palabra in txt:
        palabra = palabra.split(",")[0]
        listaDeKeywords.append(palabra)
        
    return listaDeKeywords
    

def eliminarKeywords(df, metodo):
    """PRE: Dataframe, str
    OBJ: Elimina las filas con keywords donde coincidan los terminos
    """
    terminos_eliminar = []
    
    if metodo == "write":
        terminos_eliminar = pedirKeywordsAlUsuario()
    elif metodo == "txt":
        terminos_eliminar = leerTxt()     
    else:
        print("No se ha podido reconocer su opción de borrado")


    
    for palabra in terminos_eliminar:
        df = df[~df['Keyword'].str.contains(palabra)]
    
    return df    
    
def eliminarRepetidos(df):
    """PRE: Dataframe
    OBJ: elimina las filas con keywords repetidas
    """
    
    df = df.drop_duplicates(subset=["Keyword"])    
        
    return df
    
def exportarDFToCSV(df,nombre):
    """PRE: Dataframe con el formato correcto procedente de "Key Magic Tool" de Semrush y de "Mozarbar SEO"
    OBJ: Eliminar columnas con datos innecesarios
    """
    
    columnas = ["Keyword","Volumne", "Keyword Difficulty", "CPC", "CPC (USD)"]
    
    df_keyword.to_csv("{}.csv".format(nombre), columns=columnas, na_rep="NAN")
    


### MAIN ###

#El script obtiene la ruta donde se encuentra el archivo.py y carga una lista con todos los csvs
try:
    directorio = os.path.dirname(os.path.abspath(__file__))
    lcsv = [csv for csv in os.listdir(directorio) if '.csv' in csv]
except: 
    print("Ha habido un error y no se ha podido encontrar ningún CSV")


#####
print("BIENVENIDO")
print("##########")
####
#Cargan todos los csv de la carpeta
df_keyword = cargarCSV(lcsv)
#se borran las keywords repetidas
borrarRepetidos = input("¿Quieres borrar las Keywords repetidas? [y/n]:  ")
if borrarRepetidos == "y":
    df_keyword = eliminarRepetidos(df_keyword)
    print("##########")
    print("KEYWORDS REPETIDAS BORRADAS")
print("##########")
#se borran las keywords que incluyen palabras que no nos interesan
filtrarKeywords = input("¿Quieres borrar las filas que contengan palabras seleccionadas? [y/n]:  ")
if filtrarKeywords == "y": 
    metodoFiltrado = input("¿Cómo quieres filtrarlas? [txt/write]: ")
    df_keyword = eliminarKeywords(df_keyword, metodoFiltrado)
#exporta el df a un csv
print("##########")
nombreFichero = input("Escribe el nombre del fichero csv que quieres exportar: ")
exportarDFToCSV(df_keyword,nombreFichero)
print("CSV CREADO CON EXITO")

    