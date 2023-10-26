import pytest

# skudd år
# delig med 4
# delig med 400

# ikke skudd år
# ikke delig med 4
# delig med 100
# ikke delig med 400



def is_Leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False



