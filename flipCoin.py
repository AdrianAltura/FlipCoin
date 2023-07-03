from random import choice

def coinFlip(x):
  heads = 0
  tails = 0
  count = x
  prev = 0
  longest = 0
  list = []
  indexend = 0
  while count != 0:
    coin = ['Heads','tails']
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
        longest += 1
    else:            
      if longest > prev:
        prev = longest
        indexend = i
      longest = 0
  print('\n')
  print("The longest sequence of Heads is "+str(prev))
  print("index start at: "+ str(indexend-prev))
  print("index ends at: "+ str(indexend-1))
  print(f'Total heads count: {heads}. Total tails count: {tails}')

coinFlip(100)
  
