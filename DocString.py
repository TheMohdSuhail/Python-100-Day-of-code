'''

Docstrings in python

Python docstrings are the string literals that appear right after the definition of a function, method,class, or module.

'''

# Example
def square(n):
    ''' Takes in a number n returns the square of n '''
    print(n**2)

square(5)
print(__doc__)
# Another example

def add(num1,num2):
    """
    Add up two interger numbers.
    This function simply wraps the ``+``
    operator, and does not
    do anything interesting, except for illustrating  what
    the dicstring of a very simple functon looks like.

    Parameters
    -----------
    num1 : int
    First number to add.
    num2 : int
    Second number to add.
    Returns
    -----------

    int The sum of `` num1`` and `` num2``.
    See Also
    -----------
    Subtract : Subtract one integer from another.
     Examples
     ----------
     >>> add (2,2)
     4
     >>> add (25, 0)
     25
     >>> add (10, -10)
     0

    """
    return num1 + num2
# print(add.__doc__)

'''
PEP 8 
 PEP 8 is a document that provides guidelines and best practices on how to write
  Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and 
  Nick Coghlan. The primary focus of PEP 8 is to improve the readability and 
 consistency  of Python
  
  PEP stands for Python Enhancement Proposal, and there are several of them. 
  A PEP is a document that describes new features proposed for Python and 
  document aspects of Python, like design nd style, for the community.
  
  
The Zen of Python

Long time Pythoneer Tim Peters succinctly channels the BDFL's guiding
 principles for Python's design into 20 aphorisms, only 19 of which have been written down.
 
 '''
import this