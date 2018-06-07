import random


def getYa():
    tries = 0
    ya = False
    while (not yaheze):
         rolls = []
         rolls.append(random.randint(1, 6))
         rolls.append(random.randint(1, 6))
         rolls.append(random.randint(1, 6))
         rolls.append(random.randint(1, 6))
         rolls.append(random.randint(1, 6))
 
         count = [0, 0, 0, 0, 0, 0]

         for i in rolls:
    count[i - 1] += 1
    
    tries +=1
    ya = (5 in count)
    
print ('Number of tries:', tries)
return tries

yas = []
for i in range(1000):
    yas.append(getYa())
    
print (yas)
print ('min = ', min(yas))
print ('max = ', max(yas))
print ('avg = ', sum(yas) / len(yas))


