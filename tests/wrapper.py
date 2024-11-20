import ctypes

# Load the shared library
my_c_lib = ctypes.CDLL('./tests/add.so')

# Define C function prototypes if needed
my_c_lib.my_c_add.argtypes = [ctypes.c_int, ctypes.c_int]
my_c_lib.my_c_add.restype = ctypes.c_int

# Python function wrapping the C function
def my_c_add(x, y):
    return my_c_lib.my_c_add(x, y)

# binding rust shared by ctypes
# Load the shared library
rust_lib = ctypes.CDLL("./tests/librust_shared.so")

# Define argument and return types
rust_lib.add.argtypes = (ctypes.c_int, ctypes.c_int)
rust_lib.add.restype = ctypes.c_int

rust_lib.multiply.argtypes = (ctypes.c_int, ctypes.c_int)
rust_lib.multiply.restype = ctypes.c_int

# binding rust shared by FFI
from cffi import FFI

ffi = FFI()

# Load the shared library
rust_ffi_lib = ffi.dlopen("./tests/librust_shared.so")  # Adjust path and extension for your OS

# Define the function signatures
ffi.cdef("""
    int add(int a, int b);
    int multiply(int a, int b);
""")

