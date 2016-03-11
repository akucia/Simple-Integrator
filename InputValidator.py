from Error import Error


class InputValidator(object):
    """
    contains various validation methods used in program
    """
    def __init__(self):
        """
        constructor
        :return: none
        """
        pass

    def validateParameters(self, parameters):
        """
        checks if given values are correct, raises exceptions if otherwise
        :param parameters: list: ["polynomial","min","max","step"]
        :return: bool: True if everything is correct, False otherwise
        """
        try:
            try:
                try:
                    if len(parameters) != 4:            # are there enough parameters?
                        raise Error("tooFew")
                    polynomial = parameters[0]
                    eval("lambda x : " + polynomial)    # is the polynomial a valid expression?
                    min = float(parameters[1])          # are the parameters valid numbers?
                    max = float(parameters[2])
                    dx = float(parameters[3])
                    if dx <= 0:                         # is the step a positive number?
                        raise Error("dx")
                    elif max <= min:                    # is the interval positive number?
                        raise Error("minmax")
                    elif len(polynomial) <= 0:          # does the polynomial contain any characters?
                        raise Error("polynomial")
                except ValueError:                      # catch the conversion error
                    raise Error("NAN")
            except SyntaxError:                         # catching the errors raised by eval()
                raise Error("polynomial")
        except Error as er:                             # catch all errors
            er.handler()
        else:
            return True                                 # exit if there are no problems

        return False                                    # exit otherwise

    def validateFile(self, fileName):
        """
        method tests if file of a given name can be reached
        :param fileName: string, name of the file
        :return: bool: True if file exists and can be opened, False otherwise
        """
        try:                                            # try to open a file
            f = open(fileName, "r")
        except IOError:                                 # catch error
            print("Wrong name of the file!")
            return False                                # exit

        f.close()
        return True                                     # exit when no problems found
