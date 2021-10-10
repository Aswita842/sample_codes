# sample_codes
# fibonacci series

fibonacci=[0,1]

no_of_elements=input('enter the number of elements required: ')


for i in range(0,int(no_of_elements)-2):

    fibonacci.append(fibonacci[i]+fibonacci[i+1])

print (fibonacci)
