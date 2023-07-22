class Solution:    
    def optimizescan(self, battcap):
        # Input type: Integer
        # return type: float

        #TODO: Write code below to return a float with the solution to the prompt.


        return float((battcap/500)*(battcap/1000))
#sdist=2*tdist
#tdist=p/4
#A=p-4tdist
#battcap/250=p
#a-tdist *(P-2 tdist)
def main():
    battcap = int(input())

    tc1 = Solution()
    ans = tc1.optimizescan(battcap)
    print("%.2f" % ans)

if __name__ and "__main__":
    main()