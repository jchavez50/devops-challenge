
class Unit(object):

    "A temperature unit that can be linearly converted to or from Kelvins."
    def __init__(self, name, slope, intercept):
        self.name = name
        self.slope = slope
        self.intercept = intercept

    def to_kelvins(self, t):
        return self.intercept + t / self.slope

    def from_kelvins(self, k):
        return (k - self.intercept) * self.slope
          
        # all_units = {
        #     "k": Unit("kelvins", 1.0, 0.0),
        #     "c": Unit("Celsius", 1.0, 273.15),
        #     "r": Unit("rankin", 9.0/5, 0.0),
        #     "f": Unit("Fahrenheit", 9.0/5, 255.37),
        # }
        # if __name__ == '__main__':
        #     for i in [0, 255.37, 273.15, 373.15, 473.15]:
        #         for unit in all_units.values():
        #             print("%.2f K is %.2f %s" % (i, unit.from_kelvins(i), unit.name))
        #         print()