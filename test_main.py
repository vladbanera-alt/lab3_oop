import pytest
from main import Block, Program, calculate_c_values

def test_c11_calculation():
    c11 = 5202 % 11
    assert c11 == 10


def test_block_equality():
    b1 = Block("Stone", "rock", 5, 10, True)
    b2 = Block("Stone", "rock", 5, 10, True)

    assert b1 == b2


def test_block_inequality():
    b1 = Block("Stone", "rock", 5, 10, True)
    b2 = Block("Glass", "sand", 1, 3, False)

    assert b1 != b2

def test_program_output(capsys):
    Program.main()

    captured = capsys.readouterr().out

    assert "C11 = 10" in captured
    assert "Sorted array" in captured
    assert "Search result" in captured


def test_search_found(capsys):
    Program.main()

    captured = capsys.readouterr().out

    assert "Found:" in captured
