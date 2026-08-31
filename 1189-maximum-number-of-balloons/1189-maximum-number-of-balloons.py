class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count={}
        i=0
        while i<len(text):
            if text[i] in count:
                count[text[i]]+=1
            else:
                count[text[i]]=1
            i+=1
        balloon_count={}
        j=0
        string="balloon"
        while j<len(string):
            if string[j] in balloon_count:
               balloon_count[string[j]]+=1
            else:
                balloon_count[string[j]]=1
            j+=1
        ans=float("inf")

        for letter in string:
            if letter not in count:
                return 0
            available=count[letter]//balloon_count[letter]
            if available<ans:
                ans=available
        return ans 

