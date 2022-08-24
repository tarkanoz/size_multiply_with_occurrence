'''
Problem:
t and z are strings consist of lowercase English letters.

Find all substrings for t, and return the maximum value of [ len(substring) x [how many times the substring occurs in z] ]

Example:
t = acldm1labcdhsnd
z = shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa

Solution:
abcd is a substring of t, and it occurs 5 times in Z, len(abcd) x 5 = 20 is the solution

'''


import re
b = ""
aFound = []
aText1 =[]
# sText1 = "acldm1labcdhsnd"
# sText2 = "shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa"
def find_max(sText1,sText2):
    for i in range(0,len(sText1)):
        aText1.append(sText1[i])
    # print(aText1)    
    sCheck = " "
    iCount = 0
    ne = ""
    j = 0 
    for i in range(0,len(aText1)):
       j=i
       sCheck = aText1[i]
       ne = re.search(sCheck,sText2)
       if ne :
           iCount = len(ne.regs)
       
       while (iCount > 0):
           
        #    oFound = {}
         
        #    oFound["string"] = sCheck
        #    oFound["count"] = iCount
        #    aFound.update(oFound)
        #    aFound.append[oFound]
           aFound.append([sCheck,iCount])
           j+=1
           if j>=len(aText1):
             sCheck = aText1[i] + "null"
           else:
               sCheck = aText1[i] + aText1[j]
             
           ne = re.search(sCheck,sText2)
           if ne :
               iCount = len(ne.regs)
           else:
               iCount = 0
           
           aText1[i]=sCheck
    # print(aFound) 
    # print(len(aFound))
    for i in range(0,len(aFound)):
       end_text= str(aFound[i][0])
    #    print(end_text)
       a = end_text
       a=str(a)
    #    print(type(b))
    #    print(a)
    #    print(len(a))
    #    print(len(b))
       global b
       if len(a) >len(b):
           b = a
           print(b)
       else:
            pass   
    print(b)      
    again = sText2.count(b)
    print(again)
    answer = int(len(b))* int(again)
    print(answer)
    return answer
if __name__ == '__main__':    
 resolve =find_max("acldm1labcdhsnd", "shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa")
 print(resolve)
    
    
    
    
    
            
        