class Solution:
    def firstUniqChar(self, s: str) -> int:
        i=0
        count={}
        curr_min_index=[]
        while i < len(s):
            if s[i] in count:
                count[s[i]]+=1
            else:
                count[s[i]]=1
            i+=1
        j=0
        while j<len(s):
            if count[s[j]]==1:
                return j
            j+=1
        return -1

        