'''miles = float(input("Enter the value in miles: "))
conversion_factor = 1.60934
kilometers = miles * conversion_factor
print('%.4f miles = %0.4f kilometers' %(miles, kilometers))'''






def function():
    if yes:
        convert_miles_to_kiometres(kms)
    elif no:
        convert_kilometres_to_miles(miles)
def convert_miles_to_kilometres(kms):
    miles = 0.621
    return (kms * miles)


kms = float(input("Enter your distance/ speed in miles"))
result = convert_miles_to_kilometres(kms)
print("The distance in kilometres is :", result)

def convert_kilometres_to_miles(miles):
    kms = 1.6
    return (miles * kms)


miles = float(input("Enter your distance/ speed in kms"))
result = convert_kilometres_to_miles(miles)
print("The distance in miles is :", result)
