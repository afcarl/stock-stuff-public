import numpy

from src.Indicators import *


class BollingerBand(Indicator):

    def __init__(self, data_points, period):
        assert isinstance(data_points, list), "moving average must take a list, not an iterator"
        self.data_points = data_points
        self.period = period

    def calculate(self):
        for i, dp in enumerate(self.data_points):
            yield dp.minutes, self.calculate_point(i)

    def calculate_point(self, index):
        points = self.data_points[- self.period:]
        period = len(points)
        closes = [p.close for p in points]
        average = sum(closes) / float(period)
        std_deviation = numpy.std([x.close for x in points])

        high = average + std_deviation * 2
        low = average - (std_deviation * 2)
        return low, average, high

