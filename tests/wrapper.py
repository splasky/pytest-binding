import ctypes

# Load the shared library
my_c_lib = ctypes.CDLL('./tests/add.so')

# Define C function prototypes if needed
my_c_lib.my_c_add.argtypes = [ctypes.c_int, ctypes.c_int]
my_c_lib.my_c_add.restype = ctypes.c_int

# Python function wrapping the C function
def my_c_add(x, y):
    return my_c_lib.my_c_add(x, y)
