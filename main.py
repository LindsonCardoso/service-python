import requests
import numpy as np
from conected import select_users, select_msg

def send(nome, msg):

  print(type(msg))

  url = "localhost:3333/message/text?key="+nome

  print("url = ", url)
  # enviando requisição
  

  return print('enviado\n')

def main():

  result = select_users()

  # print(result)

  # print(len(result))

  # enviando pra funciton
  
  if (len(result) != 0):
    for row in (result):
      id = row[0]
      nome = row[1]
      print(id, nome)
      msg = np.array(select_msg(id))
      send(nome, msg)
      print("\n") 
  
  else:
   return("OPS SEM DADOS")


if __name__ == '__main__': main()
