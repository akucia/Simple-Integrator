class TrIntegrator(object):
    """
    contains integration engine
    """
    def __init__(self):
       """

       :return: none
       """
    def integrate(self, function, minVal, maxVal, dx):
        """
        simple integration using trapezes method
        :param function: any function, that returns float
        :param minVal: float, begining of the interval
        :param maxVal: float, end of the interval
        :param dx: float, integration step
        :return: float, result of calculations
        """
        result = 0
        print("calculating integral...")
        while minVal < maxVal:                                  # calculate integral using trapezes method
            result += dx*(function(minVal)+function(minVal + dx))/2
            minVal += dx
        result = round(x, len(dx))                              # round the result
        return result
