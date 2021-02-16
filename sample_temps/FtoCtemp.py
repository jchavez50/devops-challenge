"""
Formulas used to convert Celsius and Fahrenheit (viceversa)
    f = (celsius * 1.8) + 32
    c = (farenheit - 32) /1.8
"""

def ftoc(ftemp): 
    return(ftemp-32.0)*(5.0/9.0)
def ctof(ctemp): 
    return(ctemp*1.8)+32

def convertFtoC(ftempString): 
    ftemp = 0.0
    try: 
        ftemp = int(round(ftemp, 2))
        ctemp = ftoc(ftemp)
        return  ftempString + str(round(ctemp, 2))
    except ValueError: 
        return "Invalid"

        