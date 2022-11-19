import csv


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
            for list in reader:
                quantity = list[1]
                item= list[0]
                item_info=products_dict[item]
                print(f'{item_info[1]}: {quantity} @ {item_info[2]}')

main()
        


     