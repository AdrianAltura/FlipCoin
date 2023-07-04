from random import choice

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
    coin = ['Heads','Tails']
    flip = choice(coin)
    count -= 1
    if flip == 'Heads':
      heads += 1
    else:
      tails += 1
    list.append(flip)
  print(list)
  
  for i in range(0,len(list)):
    if list[i] == 'Heads':
        headLongest += 1
    else:            
      if headLongest > prevHeads:
        prevHeads = headLongest
        indexend = i
      headLongest = 0
      
    if list[i] == 'Tails':
        tailLongest += 1
    else:            
      if tailLongest > prevTails:
        prevTails = tailLongest
        indexendtails = i
      tailLongest = 0
      
  print('\n')
  print("The longest sequence of Heads is "+str(prevHeads))
  print("The longest sequence of Tails is "+str(prevTails))
  print("index start for heads at: "+ str(indexend-prevHeads))
  print("index ends at: "+ str(indexend-1))
  print("index start for tails at: "+ str(indexendtails-prevTails))
  print("index ends at: "+ str(indexendtails-1))
  print(f'Total heads count: {heads}. Total tails count: {tails}')

x = int(input('Enter how many times coin flips: '))
coinFlip(x)
  
