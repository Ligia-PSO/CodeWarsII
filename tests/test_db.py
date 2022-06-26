import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='root', password='throwaway11',
                              host='127.0.0.1',
                              database='xpto_alimentos')

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    print('Base de dados acessada')



    cursor = cnx.cursor()
    cursor.execute("SHOW DATABASES")

for x in cursor:
  print(x)
  
cnx.close()