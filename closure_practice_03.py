def car(car_brand):
    def brand():
        # print(f'The brand name of the car is {car_brand}')
        str_b = f'The brand name of the car is {car_brand}'
        return str_b
    return brand

a = car('Beetle')
b = car('Golf')
c = car('Sagitar')
d = car('Jetta')
for i in [a,b,c,d]:
    print (i())

