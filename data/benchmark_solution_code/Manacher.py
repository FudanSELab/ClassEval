'''
#This is a class that implements a manacher algorithm to find the Longest palindromic substring in a given string.

class Manacher:
    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string

    def palindromic_length(self, center, diff, string):
        """
        Recursively calculates the length of the palindromic substring based on a given center, difference value, and input string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :param string: The string to be searched, str.
        :return: The length of the palindromic substring, int.
        >>> manacher = Manacher('ababa')
        >>> manacher.palindromic_length(2, 1, 'a|b|a|b|a')
        2

        """

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """
'''

class Manacher:
    def __init__(self, input_string) -> None:
        self.input_string = input_string

    def palindromic_length(self, center, diff, string):
        if (center - diff == -1 or center + diff == len(string)
                or string[center - diff] != string[center + diff]):
            return 0
        return 1 + self.palindromic_length(center, diff + 1, string)


    def palindromic_string(self):
        max_length = 0

        new_input_string = ""
        output_string = ""

        for i in self.input_string[:len(self.input_string) - 1]:
            new_input_string += i + "|"
        new_input_string += self.input_string[-1]

        for i in range(len(new_input_string)):

            length =self.palindromic_length(i, 1, new_input_string)

            if max_length < length:
                max_length = length
                start = i

        for i in new_input_string[start - max_length:start + max_length + 1]:
            if i != "|":
                output_string += i

        return output_string