from datetime import datetime

date_and_time=datetime.now()
day_of_week=date_and_time.weekday()
subtotal=0
tax=0
total=0
if day_of_week == 3 or day_of_week == 1:
    subtotal=float(input('Pelase enter the subtotal:'))
    if subtotal >= 50:
        discount=(subtotal*0.1)
        tax=(0.06*subtotal)
        total=((subtotal-discount)+tax)
print(f'Sales tax amount: {tax}')
print(f'Total: {total}')




