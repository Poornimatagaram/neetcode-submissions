
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if op == "+":
                add = record[-1] + record[-2]
                record.append(add)

            elif op == "C":
                record.pop()

            elif op == "D":
                mul = record[-1] * 2
                record.append(mul)    

            else:
                record.append(int(op))

        return (sum(record))         

                
        