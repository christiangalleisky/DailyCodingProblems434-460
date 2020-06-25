class Balanced_String():

    def __init__(self, arr):
        self.core_array = []
        for x in arr:
            if x == '(':
                self.core_array.append(1)
            elif x == '*':
                self.core_array.append(0)
            elif x == ')':
                self.core_array.append(-1)

    def count_array(self):
        i = 0
        sum = 0
        while i < len(self.core_array):
            sum += self.core_array[i]
            if sum >= 1 and i == (len(self.core_array)-1):
                success = self.find_zeroes(i, -1)
                if success:
                    sum = 0
                    i = 0
                else:
                    return False
            elif sum == 0 and i == (len(self.core_array)-1):
                return True
            elif sum <= -1:
                success = self.find_zeroes(i, 1)
                if success:
                    sum = 0
                    i = 0
                else:
                    return False
            else:
                i += 1


    def find_zeroes(self, index, looking_for):
        if looking_for == 1:
            i = index
            while i >= 0:
                if self.core_array[i] == 0:
                    self.core_array[i] = 1
                    return True
                i -= 1
            return False
        if looking_for == -1:
            x = self.find_point_of_no_return(index)
            if x > 0:
                self.core_array[x] = -1
                return True
            else:
                return False


    def find_point_of_no_return(self, index):
        index_of_last_zero_sum = 0
        index_of_last_zero = 0
        i = 0
        sum = 0
        while i < len(self.core_array):
            sum += self.core_array[i]
            if sum == 0:
                index_of_last_zero_sum = i
            i += 1
        i = index_of_last_zero_sum
        u = index_of_last_zero
        while i < len(self.core_array):
            if self.core_array[i] == 0:
                u = i
            i += 1
        return u


arr = "()"
obj = Balanced_String(arr)
state = obj.count_array()
print(state)