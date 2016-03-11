from InputValidator import InputValidator


class InputReader:
    def __init__(self):
        """

        :return:
        """
        self.validator = InputValidator()

    def consoleInput(self):
        """
        needs docs
        :return: function, imported polynomial
        """
        while True:
            usrInput = raw_input("Please provide: polynomial,min,max,dx:")
            usrInput = usrInput[5:].split(',')
            if self.validator.validateParameters(usrInput):
                return usrInput
            elif self.yesNoInput("Try again?"):
                continue
            else:
                return []

    def fileInput(self):
        """
        this function needs... everything
        :return:
        """
        while True:
            fileName = raw_input("Please enter name of the file: ")
            if self.validator.validateFile(fileName):
                with open(fileName, 'r') as f:
                    fileContent = f.readlines()
                    return fileContent
            elif self.yesNoInput("Try again?"):
                    continue
            else:
                return []

    def yesNoInput(self, string):
        """
        needs docs
        :param string:
        :return:
        """
        while True :
            usrAction = raw_input(string + " y/n:")
            if usrAction == 'y':
                return True
            elif usrAction == 'n':
                return False
            else:
                print("Cannot Recognize command")
