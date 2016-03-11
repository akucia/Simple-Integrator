from InputReader import InputReader
from InputValidator import InputValidator
from TrIntegrator import TrIntegrator
from datetime import datetime


class Integrals(object):
    """
    contains available integration methods
    """
    def __init__(self):
        """
        creates variables used for reading, parsing and calculating
        :return: none
        """
        self.reader = InputReader()                         # reading engine
        self.validator = InputValidator()                   # parsing engine
        self.integrator = TrIntegrator()                    # integration engine

    def singleIntegral(self):
        """
        calculates single integral provided from console input
        :return: list, history of completed calculations
        """
        log = []                                            # create empty log list
        while True:
            parameters = self.reader.consoleInput()         # get data
            if len(parameters) > 0:                         # if there is anything to do
                polynomial = eval("lambda x : " + parameters[0])            # create function of provided equation
                result = self.integrator.integrate(polynomial, float(parameters[1]), float(parameters[2]), float(parameters[3]) )       # run integration
                print("Result: " + str(result))
                log.append(str(datetime.now()) + ", Result: " + str(result) + ", W(x)=" + parameters[0] + ', from:' + parameters[1] + ' to:' + parameters[2] + ', step=' + parameters[3])       # add result to log
            if len(parameters) > 0 and self.reader.yesNoInput("Would you like to begin new integration?"):      #     ask user to try again
                continue
            else:
                return log

    def manyIntegrals(self):
        """
        calculates seres of integrals provided in file
        :return: list, history of completed calculations
        """
        log = []
        while True:
            fileContent = self.reader.fileInput()                   # ask user for input
            for line in fileContent:                                # for each line in file get the parameters
                parameters = line[5:]
                parameters = parameters.split(' ')
                parameters[0] = parameters[0].split(',')[0]
                parameters[1] = parameters[1].split(':')[1]
                parameters[2] = parameters[2].split(':')[1]
                parameters[2] = parameters[2].split(',')[0]
                parameters[3] = parameters[3].split('=')[1]
                if self.validator.validateParameters(parameters):           # parse the parameters
                    polynomial = eval("lambda x : " + parameters[0])        # create function from equation
                    result = self.integrator.integrate(polynomial, float(parameters[1]), float(parameters[2]), float(parameters[3]) )       # do th integration
                    print("Result: " + str(result))
                    log.append(str(datetime.now()) + ", Result: " + str(result) + ", W(x)=" + parameters[0] + ', from:' + parameters[1] + ' to:' + parameters[2] + ', step=' + parameters[3])       # save to log
                else:
                    print("Error in line: " + "'" + line + "'")
            if len(fileContent) > 0 and self.reader.yesNoInput("Would you like to begin new integration?"):         # ask user to try again
                continue
            else:
                return log
