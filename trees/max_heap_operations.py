class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def max_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc
            #print (self.heap_list)

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)
        #print (self.heap_list)

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while (i > 0):
            self.perc_down(i)
            i = i - 1
        #print(self.heap_list)

    def build_heap_mod(self, a_list):
        print (a_list)
        new_list = self.heap_list
        for item in a_list:
            self.insert(item)
            print (self.heap_list)
        """
        while (i > 0):
            self.perc_down(i)
            i = i - 1
        print(self.heap_list)"""

H = BinHeap()
a_list = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27, 2, 1, 4]
H.build_heap_mod(a_list)
