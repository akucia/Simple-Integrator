class Help(object):
    """

    """
    def __init__(self):
       """

       :return:
       """
    def show(self):
        """
        prints on screen instructions
        :return:
        """
        print("Available functionalities:")
        print("1.Single Integral")
        print("---Program ask user for input in the following form:")
        print("---polynomial,min,max,dx")
        print("---for example:")
        print("---w(x)=1+x+x**2+x**3,0,2,0.001")
        print("---Please don't use any spaces here!")
        print("---Please remember, that max must be greater then min and dx cannot be less of equal to zero!")
        print("2.Many Integrations")
        print("---Program ask user for name of the file, which contains separate lines of dat for calculations in exctly the following form:")
        print("---W(x)='polynomial', from:'min' to:'max', step='step'")
        print("---for example:")
        print("---W(x)=x+1, from:0 to:1, step=0.001")
        print("3.History")
        print("---Program shows list of previous calculations done in this session")