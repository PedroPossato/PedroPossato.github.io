import numpy as np

file = open("numbers.txt", "r")
a = np.array([])
b = np.array([])
strapoio = []
sinal = 1
novo = ''
for line in file:
  apoio2 = line
  i = 0
  while apoio2[i-1] != ']':
    novo+=apoio2[i]
    i+=1
  apoio = novo
  apoio2 = apoio2[len(apoio)+1:]
vertical = (int)(apoio2[0])
horizontal = (int)(apoio2[2])
if apoio2[4] == '-':
  constante = -1
else:
  constante = 1
nums = ['1','2','3','4','5','6','7','8','9','0']
i = 1
while i<len(apoio)-1:
  if apoio[i] in nums and apoio[i+1] not in nums:
    strapoio.append(((int)(apoio[i]))*sinal)
  if apoio[i] in nums and apoio[i+1] in nums:
    addlater=""
    while(apoio[i] in nums):
      addlater+=apoio[i]
      i+=1
    try:
      strapoio.append(((int)(addlater))*sinal)
    except:
      print "oops em",i
  if apoio[i] == '-':
    sinal = -1
  else:
    sinal = 1
  i+=1
a = strapoio
#print a

if constante > 0:
  A = np.array([[1,1,0,0],[-1,0,1,0],[0,1,0,-1],[0,0,1,1]])
  b = np.array([a[0]+a[2],a[1]-a[3],a[6]-a[4],a[5]+a[7]])
else:
  A = np.array([[1,-1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,-1]])
  b = np.array([a[2]-a[0],a[1]+a[3],a[6]+a[4],a[7]-a[5]])

x = np.linalg.lstsq(A,b,None)
if np.allclose(np.dot(A,x[0]),b):
  for i in range(4):
    print "X{} = {}".format(i+8,x[0][i])
else:
  print "Solucao impossivel! Nenhuma combinacao de X's pode satifazer esse sistema!"
end = raw_input()
