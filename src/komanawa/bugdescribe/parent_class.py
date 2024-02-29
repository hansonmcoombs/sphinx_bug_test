"""
This is a long doc string





a;sldkfa;sl d






salkdjf





aslkdfj





asldkfj



aslkdfjskl dfjkla

sad;flk
sladkfj

created matt_dumont 
on: 29/02/24
"""


class ParentClassExample():
    def __init__(self):
        """
        a base class to prove my point
        :param self:
        :return:
        """
        self.value = 1

    def _test_value(self):
        print(f'value == 1? --> {self.value == 1}')

    def print_value(self):
        """
        print the value of the class

        :param self:
        :return:
        """

        print(self.value)

    def add_to_value(self, value):
        """
        add a value to the class

        :param value:
        :return:
        """
        self.value += value
        print(self.value)
