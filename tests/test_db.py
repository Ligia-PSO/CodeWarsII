from mysql.connector import errorcode,connect,Error
import pytest

def test_connect_to_database():
  try:
    cnx = connect(user='root', password='throwaway11',
                                host='127.0.0.1',
                                database='xpto_alimentos')
    connected=True
  except Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
    connected=False
  else:
    connected=True
  cnx.close()
  assert connected==True  
