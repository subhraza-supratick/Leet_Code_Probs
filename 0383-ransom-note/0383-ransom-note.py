class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count={}
        i=0
        while i < len(magazine):
            if magazine[i] in count:
                count[magazine[i]]+=1
            else:
                count[magazine[i]]=1
            i+=1
        j=0
        while j<len(ransomNote):
            if ransomNote[j] in count:
                count[ransomNote[j]]-=1
                if count[ransomNote[j]]==0:
                    del count[ransomNote[j]]

            else:
                return False
            j+=1
        return True
        