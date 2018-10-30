

class Calculator():

    def is_power_of_two(self, number):
        if ((number - 1) & number) == 0:
            return True
        return False
