from typing import List


class CracklePop:

    @staticmethod
    def print() -> List[str]:
        result = []
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                result.append('CracklePop')
            elif i % 3 == 0:
                result.append('Crackle')
            elif i % 5 == 0:
                result.append('Pop')
            else:
                result.append(str(i))

        return result
