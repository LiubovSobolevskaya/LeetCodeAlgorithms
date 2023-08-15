 []class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        map = {}
        def recHelper(str1, str2)-> bool:
            if (str1, str2) in map:
                return map[(str1, str2)]
            if not sorted(str1) == sorted(str2):
                return False
            if len(str1) == 1:
                return True
            
            n = len(str1)
            for i in range(1, n):
                if (recHelper(str1[:i], str2[-i:]) and recHelper(str1[i:], str2[:-i])) or (recHelper(str1[i:], str2[i:]) and recHelper(str1[:i], str2[:i])):
                    map[(str1, str2)] = True
                    return True
            map[(str1, str2)] = False
            return False

        return recHelper(s1, s2)
