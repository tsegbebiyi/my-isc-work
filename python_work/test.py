course = "python"
>>> rating = 8
>>> print rating,course
8 python
>>> b = 5
>>> c = 6
>>> a = (5**2 + 6**2)**0.5
>>> a
7.810249675906654
>>> import math
>>> sqrt(a)
type(a)
<type 'float'>
>>> type(b)
<type 'int'>
>>> type(c)
<type 'int'>
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'a', 'b', 'c', 'course', 'math', 'python', 'rating']
>>> import math
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'a', 'b', 'c', 'course', 'math', 'python', 'rating']
>>> dir(math)
['__doc__', '__file__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'hypot', 'isinf', 'isnan', 'ldexp', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> a=math.sqrt(b**2 + c**2)
>>> a
7.810249675906654
>>> int()
0
>>> int(a)
7
>>> a
7.810249675906654
>>> a = int(a)
>>> a
7
>>> print str(a) + "squared equals" + str(b) + " squared" + str(c) + "squared."
7squared equals5 squared6squared.
>>> print str(a) + " squared equals " + str(b) + " squared " + str(c) + " squared."
7 squared equals 5 squared 6 squared.
>>> 
>>> num = 24
>>> a=34.999
>>> result=num*(13-a**2)+1.0
>>> print result
-29085.320024
>>> print "Result:",result
Result: -29085.320024

