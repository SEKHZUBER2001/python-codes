def sum_of_integers(number):
    if number<1:
        return 0
    else:
        i=1
        sum=0
        while i <= number:
            sum = sum + i
            i+=1
        print(f"Summation of factorial of {number} will be={sum}")

sum_of_integers(8)
sum_of_integers(7)
sum_of_integers(5)
sum_of_integers(10)


