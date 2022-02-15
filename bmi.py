name1 = "joe"
height_m1 = 2
weight_kg1 = 90

name2 = "doe"
height_m2 = 1.8
weight_kg2 = 70

name3 = "cisse"
height_m3 = 2.6
weight_kg3 = 60

def bmi_calculate(name, height_m, weight_kg):
    bmi=(weight_kg/(height_m**2))
    print("bmi is : ")
    print(bmi)
    if(bmi <26):
        return name + " is not overweight"
    else:
        return name + " is overweight"

result1= bmi_calculate(name1,height_m1,weight_kg1)
result2= bmi_calculate(name2,height_m2,weight_kg2)
result3 = bmi_calculate(name3,height_m3,weight_kg3)
print(result1)
print(result2)
print(result3)