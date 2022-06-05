
input_intervals=[[1,3],[8,10],[15,18],[2,6]]

class Merge:

    def merge_interval(self,input_intervals):
        x=[]
        if len(input_intervals) == 0:
            return x
        input_intervals.sort()
        print(input_intervals)
        temp=input_intervals[0]
        for i in input_intervals:
                
            if temp[1]>=i[0]:
                temp[1]=max(temp[1],i[1])
            
            else:
                x.append(temp)
                temp=i
                    
            x.append(temp)     
            
        return x


if __name__ == "__main__":
    a=Merge()

    b=a.merge_interval(input_intervals)

    print(b)