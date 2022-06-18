
input_intervals = [[1, 3], [8, 10], [15, 18], [2, 6]]


class Merge:

    def merge_interval(self, intervals):
        intervals.sort()
        print("intervals sort==", intervals)
        a = intervals[0]
        result = []
        for i in range(len(intervals)):
            loop = intervals[i]
            if(a[1] >= intervals[i][0]):
                a[1] = max(a[1], intervals[i][1])
                print("intervals[i]==", intervals[i])
                print("a==", a)
            else:
                result.append(a)
                a = intervals[i]
        result.append(a)
        return result


if __name__ == "__main__":
    a = Merge()

    b = a.merge_interval(input_intervals)

    print(b)
