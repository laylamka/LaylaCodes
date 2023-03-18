
# Create a function with inputs of 2 lists & print which list is bigger.
# Bigger means the highest individual number.
list_of_nums_1 = [1,2,3,14,5,9,8,7,6]
list_of_nums_2 = list_of_nums_1.copy()
list_of_nums_2.extend([i for i in range(1,12)])
print(list_of_nums_1)
print(list_of_nums_2)

def PrintBiggestList(inputa,inputb):
    largest_numberA = max(inputa)
    largest_numberB = max(inputb)

    if largest_numberA >largest_numberB:
        print("Input A had the biggest number:", largest_numberA)
    elif largest_numberB > largest_numberA:
        print("Input B had the biggest number:", largest_numberB)
    else:
        print("Both had the same highest number")



PrintBiggestList(inputa=list_of_nums_1,inputb=list_of_nums_2)