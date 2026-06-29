from typing import List

def read_integers() -> List[int]:
    new_integers =input()
    new_list = new_integers.split(",")
    return new_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
