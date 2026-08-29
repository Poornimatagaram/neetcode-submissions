from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    j=scores[0][1]
    for i,j in scores:
        print(f"i: {i}")
        print(f"j:{j}")
    




# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
