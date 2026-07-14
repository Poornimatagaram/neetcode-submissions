class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_to_open = {
            ")" : "(",
            "}" :"{",
            "]" : "["

        }

        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i) 

            else:

                if  len(stack) == 0:
                    return False

                if stack[-1] == close_to_open[i]:
                     stack.pop()
                else:
                    return False

        return len(stack) == 0                       

                            


        