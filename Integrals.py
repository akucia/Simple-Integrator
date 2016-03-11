from InputReader import InputReader
from InputValidator import InputValidator
from TrIntegrator import TrIntegrator
from datetime import datetime


class Integrals(object):
    def __init__(self):
        self.reader = InputReader()
        self.validator = InputValidator()
        self.integrator = TrIntegrator()

    def singleIntegral(self):
        log = []
        while True:
            parameters = self.reader.consoleInput()
            if len(parameters) > 0:
                polynomial = eval("lambda x : " + parameters[0])
                result = self.integrator.integrate(polynomial, float(parameters[1]), float(parameters[2]), float(parameters[3]) )
                print("Result: " + str(result))
                log.append(str(datetime.now()) + ", Result: " + str(result) + ", W(x)=" + parameters[0] + ', from:' + parameters[1] + ' to:' + parameters[2] + ', step=' + parameters[3])
            if len(parameters) > 0 and self.reader.yesNoInput("Try again?"):
                continue
            else:
                return log

    def manyIntegrals(self):
        """

        :return:
        """
        log = []
        while True:
            fileContent = self.reader.fileInput()
            for line in fileContent:
                parameters = line[5:]
                parameters = parameters.split(' ')
                parameters[0] = parameters[0].split(',')[0]
                parameters[1] = parameters[1].split(':')[1]
                parameters[2] = parameters[2].split(':')[1]
                parameters[2] = parameters[2].split(',')[0]
                parameters[3] = parameters[3].split('=')[1]
                if self.validator.validateParameters(parameters):
                    polynomial = eval("lambda x : " + parameters[0])
                    result = self.integrator.integrate(polynomial, float(parameters[1]), float(parameters[2]), float(parameters[3]) )
                    print("Result: " + str(result))
                    log.append(str(datetime.now()) + ", W(x)=" + parameters[0] + ', from:' + parameters[1] + ' to:' + parameters[2] + ', step=' + parameters[3])
                else:
                    print("Error in line: " + "'" + line + "'")
            if len(fileContent) > 0 and self.reader.yesNoInput("Try again?"):
                continue
            else:
                return log
