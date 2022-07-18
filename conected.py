import mysql.connector
import numpy as np
# querys

def select_users():
  try:
    connection = mysql.connector.connect(
      host='localhost',
      database='zltecnologia',
      user='root',
      password='root')

    sql = """
    SELECT
    id, usuario, fila, cli_id
    FROM api_kentro p
    WHERE EXISTS
    (
    SELECT *
    FROM start_autosend
    WHERE p.id = start_autosend.api_id AND start_autosend.status = 0
    );
    """ 
    cursor = connection.cursor()
    cursor.execute(sql)
    # fetch result
    result = cursor.fetchall()

  except mysql.connector.Error as error:
      return("Error reading data from MySQL table: {}".format(error))

  finally:
     if connection.is_connected():
        connection.close()
        cursor.close()
        # print("MySQL connection is closed")
        return result
    
def select_msg(id):
  try:
    connection = mysql.connector.connect(
      host='localhost',
      database='zltecnologia',
      user='root',
      password='root')

    sql = """select * from start_autosend where api_id = %s and createdAt <= now() and status = 0"""
    cursor = connection.cursor()
     # set variable in query
    cursor.execute(sql, (id,))
    # fetch result
    result = np.array(cursor.fetchall())
    print('quantidade de mensagem: "{}"'.format(len(result)))
    for row in result:
      print([row[0], row[2] ,row[3], row[14]])
    
  except mysql.connector.Error as error:
      return("Failed to get record from MySQL table: {}".format(error))

  finally:
    if connection.is_connected(): 
        cursor.close()
        connection.close()
        return("MySQL connection is closed")