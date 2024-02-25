'''
How importing in python works

Importing in Python is the process of loading code from a Python module into the current
script. This allown you to use the functions and variables defined in module in your
current script, as well as any additional modules that the imported module any depend on.

To import a module in Python, you use the import statement followed by the name of module.
For example , to import the module, which contais a variety of mathematical funtions, you
would use the follwing statement:

-------------------
import math
-------------------
Once a module is imported, you can use any of the functions and variables defined in the
module by using the dot notation. For example, to use the sqrt function for the math module,
you would write:

'''

import math

result = math.sqrt(4)

print(result)


'''
from keyword

You can also import specific  functions or variables from a module using the from keyword.
For example, to import only the sqrt function from the math module, you would write:

'''

from math import sqrt

result1 = sqrt(9)
print(result1)


'''
You can also import multiple functions or vaariables at once by sparting them with a comma:

from math import ssqrt, pi

result =sqrt(9)

print(result)
print(pi)
-------------------------------------------------------------------------------------------

Importing Everyting

It's also possible to import all functions and variabes from a module using the * wildcard.
However, tihs is generally not recommended as it can lead to confusion and make it harder to
understand where specific functions and variables are coming from.

----------------------------------------------------------------------------------------

from math import *
result = sqrt(9)
print(result)

print(pi)

----------------------------------------------------------------------------------------

Python also allows you to rename imported modules using the as keyword. This can be useful
if you want to use a shorter or more descriptive name for module, or if you want to avoid
conflicts with other modules or variables in your code.

The ''as'' keyword

----------------------------------
import math as m
result = m.sqrt(9)
print(result)
print(m.pi)
----------------------------------------------------------------
The dir function

Finally, Python has a built-in function called dir that you can use to view the names of all
the functions and variables defined in a modules. This can be helpful for exploring and
understanding the contents of a new module.

'''

print(dir(math))


'''
This will output a list of all the manes defined in the math module, including functions like
sqrt and pi, as well as other variabes and constants.



In summary, the import statement in Python allows you to access the functions and vaiables
defined in module from within your current script. You can import the entire module, specific
functions or variables, or use the * wildcard to import everything. You can also use the as
keyword to rename a module, and the dir function to view the contents of module.



'''

from msp import *

welcome()
































