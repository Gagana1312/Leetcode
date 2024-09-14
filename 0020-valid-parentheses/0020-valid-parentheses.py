class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # stack = {  "{":"}","["::"]","(":")"}
        # count1, count2, count3 = 0,0,0
        # for c in s:
        #     if c == "{":
        #         count1+=1
        #     elif c == "[":
        #         count2+=1
        #     elif c == "(":
        #         count3+=1
        # for c in s:
        #     if c == "}" and count1>=1:
        #         count1-=1
        #     elif c == "]" and count2>=1:
        #         count2-=1
        #     elif c == ")" and count3>=1:
        #         count3-=1
        # if count1==0 and count2==0 and count3==0:
        #     return True
        # return False

        hashMap = {  "}":"{","]":"[",")":"("}
        res =[]
        for c in s:
            if c not in hashMap:
                res.append(c)
            else:
                if not res:
                    return False
                else:
                    out = res.pop()
                    if out != hashMap[c]:
                        return False
        return not res




                
