class Menu(object):
    """

    """
    def __init__(self):
        """

        :return:
        """
        self.name = "---Main Menu---"
        self.menuDict = {'1.Single Integration': '1', '2.Many Integrations': '2', '3.History': '3', '4.Help' : '4', "Press 'q' to quit" : 'q'}

    def show(self):
        """

        :return:
        """
        print(self.name)
        for item in sorted(self.menuDict.keys()):
            print("--" + item )
        print("---------------")


    def select(self):
        """

        :return:
        """
        print("Please Select:")
        self.show()
        selection = raw_input()
        if selection in self.menuDict.values():
            return selection
        else:
            print "Unknown Option Selected!"

