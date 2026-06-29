from typing import List

def read_integers() -> List[int]:
    new_integers =input()
    new_list = new_integers.split(",")

    int_list =[]
    for i in new_list:
        num = int(i)
        int_list.append(num)
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
