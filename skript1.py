def left(n):
  return x - n, y

def right(n):
  return x + n, y

def up(n):
  return x, y + n

def dn(n):
  return x, y - n

x = 0
y = 0
command = str(input("куда идем: \n 1 - left\n 2 - right \n 3 - dn \n 4 - up \n"))
n = int(input("на сколько шагов? \n"))


if command.lower() == "left":
  print(left(n)) 
elif command.lower() == "right":
  print(right(n)) 
elif command.lower() == "up":
  print(up(n))
elif command.lower() == "dn":
  print (dn(n))
else: print("Неверное движение")