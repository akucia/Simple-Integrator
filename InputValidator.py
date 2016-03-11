from Error import Error


class InputValidator:
    """
    document this...
    """

    def __init__(self):
        pass

    def validateParameters(self, parameters):
        try:
            try:
                try:
                    if len(parameters) != 4:
                        raise Error("tooFew")
                    polynomial = parameters[0]
                    eval("lambda x : " + polynomial)
                    min = float(parameters[1])
                    max = float(parameters[2])
                    dx = float(parameters[3])
                    if dx <= 0:
                        raise Error("dx")
                    elif max <= min:
                        raise Error("minmax")
                    elif len(polynomial) <= 0:
                        raise Error("polynomial")
                    elif 'z' in polynomial or 'y' in polynomial:
                        raise Error("polynomial")
                except ValueError:
                    raise Error("NAN")
            except SyntaxError:
                raise Error("polynomial")
        except Error as er:
            er.handler()
        else:
            return True

        return False

    def validateParametersFromFile(self, parameters):
        pass

    def validateFile(self,fileName):
        try:
            f = open(fileName, "r")
        except IOError:
            print("Wrong name of the file!")
            return False

        f.close()
        return True
