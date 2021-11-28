command = ''
x = 0
y = 0
n = 0
flg = True

while flg:
  print("список команд: \n 1.left \n 2.right \n 3.up \n 4.dn")
  command = str(input("куда идем: \n"))
  n = int(input("на сколько шагов? \n"))
  
  if command.lower() == "left":
    x -= n
  elif command.lower() == "right":
    x += n
  elif command.lower() == "up":
    y += n
  elif command.lower() == "dn":
    y -= n 
  elif command.lower() == "stop":
    flg = False
  else:
     print("неверная команда")
  
  print(x, y)