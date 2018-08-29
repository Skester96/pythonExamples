import pytest
import functionsToTest as funcs


def test_add_ten():
    assert(funcs.add_ten(10) == 20)
    assert(funcs.add_ten(-10) ==0)

def test_is_valid_midi_value():
    assert(funcs.is_valid_midi_value(0) == True)
    assert(funcs.is_valid_midi_value(60) == True)
    assert(funcs.is_valid_midi_value(127) == True)
    assert(funcs.is_valid_midi_value(-1) == False)
    assert(funcs.is_valid_midi_value(128) == False)
    assert(funcs.is_valid_midi_value(99999) == False)
