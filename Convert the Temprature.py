class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = float(celsius + 273.15)

        Fahrenheit = float(celsius *1.80+ 32.00)
        return kelvin ,Fahrenheit
