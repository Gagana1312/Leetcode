class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # res=[]
        # for i in range(len(arr)):
        #     i = arr[0]
        #     res.append(max(arr))
        #     if len(arr)==1:
        #         res.append(-1)
        #     del arr[0]
        # del res[0]
        # return res

        # initial max=-1
        #reverse iteration
        #new max = max(old max, prev position in the arr)

        max1= -1

        for i in range(len(arr)-1,-1,-1):
            max2 = max(max1, arr[i])
            arr[i] = max1
            max1=max2
        return arr

        