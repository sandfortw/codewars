def next_smaller(num):
    num_string = str(num)
    length = len(num_string)
    new_num = num
    swappers = num_string[length - 2:length]
    new_num_string = num_string
    counter = 1
    cycle_counter = 0
    while new_num >= num:
        # import ipdb; ipdb.set_trace()
        char_list = list(new_num_string)
        latter = length - counter
        former = length - (1 + counter)
        char_list[latter] = swappers[0]
        char_list[former] = swappers[1]
        new_num_string = ''.join(char_list)
        new_num = int(new_num_string)
        # import ipdb; ipdb.set_trace()
        if length - (2 + counter) >= 0:
            # import ipdb; ipdb.set_trace()
            swappers = new_num_string[length - (2 + counter):length - counter]
        elif new_num < num:
            # import ipdb; ipdb.set_trace()
            return new_num
        elif cycle_counter == length + 1:
            # import ipdb; ipdb.set_trace()
            return -1
        else: 
            cycle_counter += 1
            counter = 0
            swappers = new_num_string[length - 2:length]

        counter += 1
    return new_num
            
import unittest

class TestNextSmaller(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(next_smaller(907), 790)
        self.assertEqual(next_smaller(531), 513)
        self.assertEqual(next_smaller(135), -1)
        self.assertEqual(next_smaller(2071), 2017)
        self.assertEqual(next_smaller(414), 144)
        self.assertEqual(next_smaller(123456798), 123456789)
        self.assertEqual(next_smaller(123456789), -1)
        self.assertEqual(next_smaller(1234567908), 1234567890)
        self.assertEqual(next_smaller(100), -1)

if __name__ == '__main__':
    unittest.main()