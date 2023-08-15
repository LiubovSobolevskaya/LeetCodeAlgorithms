class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        friendSets = [{i} for i in range(n)]
        logs.sort(key = lambda x :x[0])
        print(logs)
        for i in range(len(logs)):
            time = logs[i][0]
            fr1 = logs[i][1]
            fr2 = logs[i][2]
            for frSet in friendSets: 
                if fr1 in frSet:
                    fr1Set = frSet
                if fr2 in frSet:
                    fr2Set = frSet
            print(friendSets)
            if fr1Set!=fr2Set:
                fr1Set.update(fr2Set)
                friendSets.remove(fr2Set)
                if len(fr1Set) == n:
                    return time
        return -1
            
        










