"""
created matt_dumont 
on: 29/02/24
"""
from komanawa.bugdescribe.parent_class import ParentClassExample

class ChildClassExample(ParentClassExample):

    def __init__(self):
        """
        a simple child class to prove my point

        """
        super().__init__()
        self.value = 2

    def print_value(self):
        """
        print the value of the class
        :param self:
        :return:
        """
        print(self.value)


if __name__ == '__main__':
    c = ChildClassExample()
    c.print_value()
    c._test_value()
    c.add_to_value(2)
    c.print_value()
    c._test_value()
    print('done')