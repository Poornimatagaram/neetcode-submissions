def add_two_numbers() -> int:
    num1= input()
    add = num1.split(",")
    final_num = 0
    for i in add:
        num2 = int(i)
        final_num += num2
    return final_num

    



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
