from random import randint
# 1 = Heads
# 0 = Tails
def coinFlip(x):
  count = x
  heads = 0
  tails = 0
  prevTails = 0
  prevHeads = 0
  headLongest = 0
  tailLongest = 0
  list = []
  indexend = 0
  indexendtails = 0
  
  while count != 0:
    flip = randint(0,1)
    count -= 1
    if flip == 1:
      heads += 1
    else:
      tails += 1
    list.append(flip)
  print('\n')
  print(list)
  
  for i in range(0,len(list)):
    if list[i] == 1:
        headLongest += 1
    else:            
      if headLongest > prevHeads:
        prevHeads = headLongest
        indexend = i
      headLongest = 0
      
    if list[i] == 0:
        tailLongest += 1
    else:            
      if tailLongest > prevTails:
        prevTails = tailLongest
        indexendtails = i
      tailLongest = 0
      
  print('\n')
  print(f'The longest sequence of Heads is {prevHeads}')
  print(f'The longest sequence of Tails is {prevTails}')
  print(f'index start for heads at: {indexend-prevHeads}')
  print(f'index ends at: {indexend-1}')
  print(f'index start for tails at: {indexendtails-prevTails}')
  print(f'index ends at: {indexendtails-1}')
  print(f'Total heads count: {heads}. Total tails count: {tails}')

x = int(input('Enter how many times coin flips: '))
coinFlip(x)
