def check_list_empty(my_list) -> bool:
    if my_list:
        print("The list is not empty")
    else:
        print("The list is empty")    


def check_element_in_list(my_list, element) -> bool:
    if element in my_list:
        print(f" {element} is present in the list")
    else:
         print(f" {element} is not present in the list")    


# do not modify below this line
print(check_list_empty([]))
print(check_list_empty([1, 2, 3]))

print(check_element_in_list([1, 2, 3], 1))
print(check_element_in_list([1, 2, 3], 4))

print(check_element_in_list(["Apple", "Banana", "Orange"], "Banana"))
print(check_element_in_list(["Apple", "Banana", "Orange"], "Grape"))
