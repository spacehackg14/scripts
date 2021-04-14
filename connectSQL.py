# Importaciones
import pyodbc
import pandas as pd 
import json

# Crear conexión con la base de datos
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
				      'Server=spacehackgrupo14.database.windows.net;'
				      'Database=spacehack;'
				      'UID=spacehackgrupo14;'
				      'PWD=Spacehack2021;')

#cursor = conn.cursor()
sql_user = """SELECT * FROM users"""
sql_bef = """SELECT * FROM beneficios"""
sql_user_bef = """SELECT * FROM usuario_beneficio"""
sql_prueba = """SELECT CONCAT(u.first_name,' ', u.last_name)Cliente , des_beneficio Beneficio 
				FROM users u, beneficios b , usuario_beneficio ub
				WHERE u.id_user=ub.id_usuario AND ub.id_beneficio=b.id_beneficio;"""

dataset = pd.read_csv('C:/Users/alvar/Desktop/BBVA HACKATON/dataset_hack.csv')
dataset.head()

# Lectura de data en DataFrames Pandas

df_user = pd.read_sql(sql_user, conn)
df_bef = pd.read_sql(sql_bef, conn)
df_user_bef = pd.read_sql(sql_user_bef, conn)
'''df_user_lang = pd.read_sql(sql_user_languages, conn)
df_lang = pd.read_sql(sql_languages, conn)
df_doc = pd.read_sql(sql_documento_iden, conn)
df_doc_iden = pd.read_sql(sql_doc_identidad, conn)
df_user_pag = pd.read_sql(sql_usuario_pagina_facebook, conn)
df_user_pag_fb =pd.read_sql(sql_pagina_facebook, conn)
df_user_art = pd.read_sql(sql_artist, conn)
df_art = pd.read_sql(sql_user_artist, conn)
df_viajes = pd.read_sql(sql_viajes_usuario, conn)'''

print(pd.merge(df_user, df_user_bef, on="id_user"))

#print(pd.concat(left=df_user, right=df_user_bef, left_on='id_user', right_on='id',how='inner'))



'''
# Lectura de data en json
re_user = df_user.to_json(orient="split")
re_bef = df_bef.to_json(orient="split")
re_user_bef = df_user_bef.to_json(orient="split")

parseo_user = json.loads(re_user)
parseo_bef = json.loads(re_bef)
parseo_user_bef = json.loads(re_user_bef)

# Imprimido en json
print(parseo_user)
print(parseo_bef)
print(parseo_user_bef)

print(df_user.head())
print(df_bef.head())
print(df_user_bef.head())'''
	
# Analítica de datos (Pandas)


# Mostrar información

