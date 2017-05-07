from random import randint


class Template:

    table = []
    n = 0

    def init(self, n):
        self.n = n
        for i in range(0, n):
            self.table.append(randint(0, 100))

    def function(self):
        # self.quicksort(self.table, 0, self.n - 1)

        for i in range(0, self.n):
            for j in range(0, self.n):
                for k in range(0, self.n):
                    self.table.append(123)

    def quicksort(self, myList, start, end):
        if start < end:
            # partition the list
            pivot = self.partition(myList, start, end)
            # sort both halves
            self.quicksort(myList, start, pivot - 1)
            self.quicksort(myList, pivot + 1, end)
        return myList

    def partition(self, myList, start, end):
        pivot = myList[start]
        left = start + 1
        right = end
        done = False
        while not done:
            while left <= right and myList[left] <= pivot:
                left = left + 1
            while myList[right] >= pivot and right >= left:
                right = right - 1
            if right < left:
                done = True
            else:
                # swap places
                temp = myList[left]
                myList[left] = myList[right]
                myList[right] = temp
        # swap start with myList[right]
        temp = myList[start]
        myList[start] = myList[right]
        myList[right] = temp
        return right

    def clean_up(self):
        self.table = []
