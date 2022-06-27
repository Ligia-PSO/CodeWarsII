
import mysql.connector

def Conectar_SQL(user_:str='root',password_:str='throwaway11', host_:str='127.0.0.1',database_:str='xpto_alimentos')->None:
    cnx = mysql.connector.connect(user=user_, password=password_,host=host_,database=database_)                   
    return cnx.cursor()
