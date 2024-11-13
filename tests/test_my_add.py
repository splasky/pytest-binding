# test_my_c_code.py
import pytest
from wrapper import my_c_add

def test_my_c_add():
    assert my_c_add(10, 20) == 30
