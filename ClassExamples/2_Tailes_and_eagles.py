import random

TRIES = 100000
total_eagles = 0
total_tailes = 0

for i in range(TRIES):
   temp_seq = ['Орел', 'Решка']
   x = random.choice(temp_seq)
   if x=='Орел':
      total_eagles += 1
   else:
      total_tailes += 1

eagles_ratio = total_eagles / TRIES * 100
tailes_ratio = total_tailes / TRIES * 100
print("Выпало: " + str(total_eagles) + " Орлов(" + str(eagles_ratio) + "%)" )
print("Выпало: "  + str(total_tailes) + " Решек(" + str(tailes_ratio) + "%)")
