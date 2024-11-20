# test_my_c_code.py
import pytest
from wrapper import my_c_add, rust_lib, rust_ffi_lib

def test_my_c_add(benchmark):
    assert benchmark(my_c_add, 10, 20) == 30

def test_my_rust_add(benchmark):
    assert benchmark(rust_lib.add, 3, 5) == 8

def test_my_rust_multiply(benchmark):
    assert benchmark(rust_lib.multiply, 3, 10) == 30

def test_my_rust_ffi_add(benchmark):
    assert benchmark(rust_ffi_lib.add, 3, 5) == 8

def test_my_rust_ffi_multiply(benchmark):
    assert benchmark(rust_ffi_lib.multiply, 3, 10) == 30 

def test_py_add(benchmark):
    # Benchmark the function execution
    def add(a, b):
        return a + b

    result = benchmark(add, 3, 5)
    assert result == 8

def test_py_multiply(benchmark):
    # Benchmark the function execution
    def multiply(a, b):
        return a * b

    result = benchmark(multiply, 3, 10)
    assert result == 30

