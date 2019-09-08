class Utils():
    def next_highest_power_of_2(self, num):
        num -= 1
        num |= num >> 1
        num |= num >> 2
        num |= num >> 4
        num |= num >> 8
        num |= num >> 16
        num |= num >> 32
        num += 1
        return num
    
    def pad_to(self, lst, num):
        if len(lst) >= num:
            return lst

        pad_size = num - len(lst)
        
        result = list("0" * pad_size)
        result += lst

        return result

    def pad_binary_str(self, binary_lst):
        pow2 = self.next_highest_power_of_2(len(binary_lst)) 
        while pow2 % 64 != 0:
            pow2 += 1
            pow2 = self.next_highest_power_of_2(pow2)
        
        pad_size = pow2 - len(binary_lst)
        result = list("0" * pad_size)
        result += binary_lst

        return result
