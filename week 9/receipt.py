import csv
from datetime import datetime
print("Python Groceries")

def read_dict (filename, key_column_index):
    csv_dict={}
    with open(filename,'rt') as csv_file:
        reader=csv.reader(csv_file)
        next(reader)
        for list in reader:
            if list != 0:
                key= list[key_column_index]
                csv_dict[key]=list
    return csv_dict

def main():
        
        key_column_index=0
        products_dict= read_dict('week 9/products.csv', key_column_index)
        print(products_dict)
        with open("week 9/request.csv",'rt') as csv_file:
            reader= csv.reader(csv_file)
            next(reader)
            n_itens=0
            subtotal=0
            for list in reader:
                quantity = list[1]
                item= list[0]
                item_info=products_dict[item]
                n_itens+=(int(quantity))
                subtotal+=(int(quantity)*(float(item_info[2])))
                print(f'{item_info[1]}: {quantity} @ {item_info[2]}')
            subtotal=round(subtotal,2)
            tax=round((subtotal*6)/100,2)
            total=(subtotal+tax)
            date_and_time=datetime.now()
            day_of_week=date_and_time.weekday()
            if day_of_week == 1 or day_of_week == 2:
                total=total-(total/10)
            print(f'Number of itens: {n_itens}')
            print(f'Subtotal: {subtotal} $')
            print(f'Sales Tax:{tax}')
            print(f'Total: {total}')
            print('Thank you for shopping in Python Groceries')
            print(f'{date_and_time:%A %I:%M %p}')

main()
        


     