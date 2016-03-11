from InputValidator import InputValidator


class InputReader(object):
    """
    contains user input methods
    """
    def __init__(self):
        """

        :return:
        """
        self.validator = InputValidator()                       # initialize the validating engine

    def consoleInput(self):
        """
        terminal input method
        :return: list of parameters
        """
        while True:
            usrInput = raw_input("Please provide: polynomial,min,max,dx:")
            usrInput = usrInput[5:].split(',')                  # splitting different parameters
            if self.validator.validateParameters(usrInput):     # run the validation
                return usrInput
            elif self.yesNoInput("Try again?"):                 # if validation fails, ask to try again
                continue
            else:
                return []

    def fileInput(self):
        """
        reading from file method
        :return:
        """
        while True:
            fileName = raw_input("Please enter name of the file: ")
            if self.validator.validateFile(fileName):           # run the validation
                with open(fileName, 'r') as f:                  # open file
                    fileContent = f.readlines()                 # read the contents
                    return fileContent
            elif self.yesNoInput("Try again?"):                 # if validation fails, ask to try again
                    continue
            else:
                return []

    def yesNoInput(self, string):
        """
        simple user decision
        :param string: question displayed
        :return: bool: true or false
        """
        while True :
            usrAction = raw_input(string + " y/n:")
            if usrAction == 'y':
                return True
            elif usrAction == 'n':
                return False
            else:
                print("Cannot Recognize command")
