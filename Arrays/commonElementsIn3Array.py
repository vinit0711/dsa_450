import sys


class CommonElments:
    def return_common_list(self, list1, list2, list3):
        result = []
        i = j = k = 0
        prev1 = prev2 = prev3 = -sys.maxsize-1
        while(i < len(list1) and j < len(list2) and k < len(list3)):
            print("i==",i)
            while(list1[i] == prev1 and i < len(list1)):
                i += 1
            while(list2[j] == prev2 and j < len(list2)):
                j += 1
            while(list3[k] == prev3 and k < len(list3)):
                k += 1
            if(list1[i] == list2[j] == list3[k]):
                result.append(list1[i])
                prev1 = list1[i]
                prev2 = list2[j]
                prev3 = list3[k]
                i += 1
                j += 1
                k += 1
            elif(list1[i] < list2[j]):
                prev1=list1[i]
                i += 1
            elif(list2[j] < list3[k]):
                prev2=list1[j]
                j+=1
            else:
                prev3=list1[k]
                k+=1
        return result


list1=[1, 5, 10, 20, 40, 80]
list2=[6, 7, 20, 80, 100]
list3=[3, 4, 15, 20, 30, 70, 80, 120]
a=CommonElments()
ans=a.return_common_list(list1,list2,list3)
print(ans)