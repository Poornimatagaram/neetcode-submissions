def print_first_char(word: str) -> None:
    firstchar = word[0:2]
    return firstchar

def print_second_char(word: str) -> None:
    secondchar = word[1:3]
    return secondchar

def print_last_char(word: str) -> None:
    lastchar = word[-3:-1]
    return lastchar


# do not modify below this line
print_first_char("hello")
print_second_char("hello")
print_last_char("hello")

print_first_char("yay")
print_second_char("yay")
print_last_char("yay")
