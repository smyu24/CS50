from ctypes import *
libCalc = CDLL("./libcalci.so")

#call C function to check connection
libCalc.connect()

#calling randNum() C function
