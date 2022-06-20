class ALternateNegativePositive:
    def arrange(self,list):
        i=0
        j=len(list)-1
        while(i<j):
            if(list[i]>0 ):
                i+=1
            elif(list[i]<0 and list[j]>0):
                list[i],list[j] = list[j],list[i]
            elif(list[j]<0):
                j-=1
        # Now list is sorted in such a way where positve elements are first then negative elements
        # Position of i is at start of negative elements
        # Will take new pointer k from start and increment it for negative elements
        # i+=1
        if(i==0 or i==len(list)): return

        k=0
        while(k<len(list) and i<len(list)):
            print("earlier==",list)
            list[k],list[i]=list[i],list[k]
            k+=2
            i+=1

        print(list)
list=[2,3,-4,-1,6,-9 ]
a=ALternateNegativePositive()
a.arrange(list)