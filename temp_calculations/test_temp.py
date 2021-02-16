
class Temperature(object):
    def __init__(self, temp): 
        self.temp = temp

    def checkconversion(self, ):
        return
    def temperature_C_to_K(self, temp_C):
        return temp_C + 273.15

    def temperature_K_to_C(self, temp_K):
        return temp_K - 273.15

    def temperature_F_to_K(self, temp_F):
        return 5./9 * (temp_F - 32) + 273.15

    def temperature_K_to_F(self, temp_K):
        return 1.8 * (temp_K - 273.15) + 32

    to_K_from = {"c": temperature_C_to_K,
                "f": temperature_F_to_K,
                "k": lambda t: t}
    from_K_to = {"c": temperature_K_to_C,
                "f": temperature_K_to_F,
                "k": lambda t: t}

    def convert(self, temperature, from_unit, to_unit):
        return from_K_to[to_unit](to_K_from[from_unit](temperature))

        if __name__ == "__main__":
            kelvin = to_K_from["c"]
            fahrenheit = from_K_to["f"]
            temperature = 33
            print(fahrenheit(kelvin(temperature)))