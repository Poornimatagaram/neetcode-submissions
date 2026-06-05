def concatenate(s1: str, s2: str) -> str:
    concat_str = s1 + s2
    if len(concat_str) > 10:
        print("Too long!") 
    else:
        print("Good Job!")    




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
