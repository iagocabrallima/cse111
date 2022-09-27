def miles_per_gallons(start_miles,end_miles,amount_gallons):
    mpg=((end_miles-start_miles)/amount_gallons)
    return(mpg)

def lp100k_from_mpg(mpg):
    lp100k=(235.215/mpg)
    return(lp100k)

def main():
    start_miles=int(input('Enter the first odometer reading (miles): '))
    end_miles=int(input('Enter the last odometer reading (miles): '))
    amount_gallons=float(input('Enter the amount of fuel used (gallons): '))
    
    print(miles_per_gallons(start_miles,end_miles,amount_gallons),'miles per gallon.')
    print(lp100k_from_mpg(miles_per_gallons(start_miles,end_miles,amount_gallons)),'liters per 100 kilometers')
main()