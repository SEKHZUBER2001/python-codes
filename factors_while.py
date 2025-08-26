def count_factors(number):
    if number == 0:
        print("there is no factors")
    factor=1
    while   number>=factor:
        if  number%factor==0:
            return  factor
    factor+=1

count_factors(8)
