def remove_fourth_character(word: str) -> str:
    first_word = word[:3]
    second_word = word[4:]
    full_word = first_word + second_word
    return full_word


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
