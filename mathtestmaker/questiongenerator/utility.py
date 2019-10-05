import random

def getCorrectAnswerIndex( numChoices ):
    return random.randint( 1, numChoices + 1 )

def generateWrongAnswers( numChoices, correctAnswer, dataType ):
    """
    TBD.
    Wrong answers usually follow some patterns on tests.
    * the negative of the right answer
    * a value close to the right answer
    * < particularly tricky to implement computationally > a deliberately misleading value, perhaps can
      be arrived at through some common miscalculation during problem solution. Maybe this function should take
      a list of deliberately misleading values as a parameter.
    * etc.
    """
    if dataType == "ints":
        return [ correctAnswer + 1 for i in range( numChoices ) ] # TBD put some good logic here.
    else:
        assert( False ) # TBD decide how to handle this elegantly.

def get_integer_in_range_excluding_specified(low=None,  high=None, exclude_list=None):
    """
    random.randint(a, b) is inclusive.        
    low = a
    high = b
    len(exclude_list) = c
    Between b and a there are therefore b - a  + 1 numbers.
    e.g. a=0, b =1, there are 2 numbers.
    must assert that b - a + 1 > len(exclude_list)
    """
    assert( (low  + len(exclude_list)) < high + 1)
    ret = random.randint(low, high)
    while ret in exclude_list:
        ret = random.randint(low, high)
    return ret

def get_float_in_range_excluding_specified(low=None,  high=None, exclude_list=None):
    assert(low < high)
    precision = 2    
    ret = round(random.uniform(low, high), precision)
    while ret in exclude_list:
        ret = round(random.uniform(low, high), precision)
    return ret

def get_fraction(num_low=-10, num_high=10, num_exclude=[0], den_low=-10, den_high=10, den_exclude=[0, 1]):
    """
    Return a fraction that has a denominator != 1
    """
    from fractions import Fraction
    ret = Fraction(1, 1)
    if 0 not in den_exclude:
        print( "In get_fraction(): den_exclude does not contain 0. Adding 0 to prevent the fractions module from crashing.\n")
        den_exclude = den_exclude + [0]
    while (ret.denominator == 1):
        numerator=get_integer_in_range_excluding_specified(low=num_low, high=num_high, exclude_list=num_exclude)
        denominator=get_integer_in_range_excluding_specified(low=den_low, high=den_high, exclude_list=den_exclude)
        ret = Fraction(numerator, denominator)
    return ret

def get_gcd(l):
    """
    Return the gcd of a list of numbers
    """
    from fractions import gcd
    assert(len(l) > 1)
    ret = l[0]
    for val in l[1:]:
        ret = gcd(ret, val)
    return ret
