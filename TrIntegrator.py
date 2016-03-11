class TrIntegrator(object):
    def __init__(self):
        """
        should be merged with "integrate" method
        :param :
        :return:
        """
    def integrate(self, function, minVal, maxVal, dx):
        """

        :param function:
        :param minVal:
        :param maxVal:
        :param dx:
        :return:
        """
        result = 0
        print("calculating integral...")
        while minVal < maxVal:
            result += dx*(function(minVal)+function(minVal + dx))/2
            minVal += dx
        return result
