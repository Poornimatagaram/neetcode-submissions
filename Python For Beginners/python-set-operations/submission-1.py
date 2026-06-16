from typing import List

def count_unique_words(words: List[str]) -> int:

    if words is None:
        return 0

    new_set = set(words) 
    return  new_set
    
        
   

       

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
