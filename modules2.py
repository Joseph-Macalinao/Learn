
#using import keyword will take all functions form other file and will make them into modules able
#to be called from dot-notation
import modules1
#Or, use form file import func to call, after typing import, hold ctrl and space to see funtion options
from modules1 import square

#to access a function from a whole file, use file(module) name and then call func after a '.'
modules1.square(3)

#from the from statement, you can call the function directly

square(2)

