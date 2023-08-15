class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def isPermutation(s: str, words: List[str])-> bool:
            length = len(words[0])
            substrings = [s[i:i+length] for i in range(0, len(s), length)]
    
            mapping = {}
            for word in words:
                if mapping.get(word) == None:
                    mapping[word] = 1
                else:
                    mapping[word] += 1

            for substring in substrings:
        
                if mapping.get(substring) == None:
                    return False
                mapping[substring] -=1
                if mapping.get(substring)<0:
                    return False
            for key in mapping.keys():
                if mapping[word]!=0:
                    return False
            return True
        output = []
        for i in range (len(s)-len(words[0])*len(words)+1):
            if isPermutation(s[i:i+len(words[0])*len(words)], words):
                output.append(i)
        return output
