class Error(Exception):
    """

    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

    def handler(self):
        if self.value == "dx":
            print("Wrong input - The step must be greater then 0")
        elif self.value == "minmax":
            print("Wrong input - The length od interval must be greater then 0")
        elif self.value == "NAN":
            print("Please enter a valid numbers as parameters")
        elif self.value == "polynomial":
            print("Please enter a valid polynomial. Read help to see how a valid polynomial looks like.")
        elif self.value == "tooFew":
            print("Please enter all parameters")
        elif self.value == "smalldx":
            print("Please use step bigger than '0.00000001' ")


