class Menu(object):
    """
    contains methods for displaying menu
    """
    def __init__(self):
        """
        creates variables containing name and dictionary of avilable actions
        :return: none
        """
        self.name = "---Main Menu---"
        self.menuDict = {'1.Single Integration': '1', '2.Many Integrations': '2', '3.History': '3', '4.Help' : '4', "Press 'q' to quit" : 'q'}

    def show(self):
        """
        prints menu on screen
        :return: none
        """
        print(self.name)
        for item in sorted(self.menuDict.keys()):
            print("--" + item )
        print("---------------")


    def select(self):
        """
        allows selections of item from displayed menu
        :return: int, selected number
        """

        self.show()
        selection = raw_input("Please select number:")
        if selection in self.menuDict.values():
            return selection
        else:
            print "Unknown Option Selected!"

