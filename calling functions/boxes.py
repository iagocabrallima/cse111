import math
n=float(input('Enter the number of items: '))
npb=float(input('Enter the number of items per box: ')) 

boxes=math.ceil(n/npb)
print(f'For {round(n)} items, packing {round(npb)} items in each box, you will need {boxes} boxes.')


