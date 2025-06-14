import os
import pandas as pd
from sqlalchemy import create_engine

#configurar la conexion mysql
user='sbrito'
password='Sb40222538585'
host='localhost'
database='oulad_db'

#conexion a mysql

engine= create_engine(f'mysql+pymysql://{user}:{password}@localhost/{database}')

#ruta de los archivos
csv_folder=r'C:\Users\sbrito\Documents\Maestria CD-IA\Ciencia de Datos I\Caso practivo 3\OULAD'

#iterar los archivos del directorio

for file in os.listdir(csv_folder):
    if file.endswith('.csv'):
        table_name=file.replace('.csv','').lower()
        try:
            df=pd.read_csv(os.path.join(csv_folder,file))
            df.to_sql(name=table_name,con=engine,index=False,if_exists='replace')
            print(f'Tabla Importada: {table_name}')
        except Exception as e:
            print(f'error importando:{e}')