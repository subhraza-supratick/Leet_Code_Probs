class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        x= self.fib(n-1)
        y= self.fib(n-2)
        return x+y
        