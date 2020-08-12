class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        length = len(self.arr)
        if length % 2 == 0:
            if length == 2:
                return (self.arr[0]+self.arr[1])/2
            return (self.arr[length//2]+self.arr[length//2-1])/2
        else:
            return self.arr[length//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()