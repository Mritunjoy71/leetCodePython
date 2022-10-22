from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        listStr = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                listStr.append("FizzBuzz")
            elif i % 3 == 0:
                listStr.append("Fizz")
            elif i % 5 == 0:
                listStr.append("Buzz")
            else:
                listStr.append(str(i))
        return listStr
