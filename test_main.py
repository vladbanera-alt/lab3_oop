import pytest
from main import Block, Program


def test_block_creation():
    block = Block("Stone", "rock", 5, 10, True)

    assert block.name == "Stone"
    assert block.material == "rock"
    assert block.hardness == 5
    assert block.weight == 10
    assert block.isSolid is True


def test_block_equality():
    b1 = Block("Wood", "organic", 3, 5, True)
    b2 = Block("Wood", "organic", 3, 5, True)

    assert b1 == b2


def test_block_inequality():
    b1 = Block("Wood", "organic", 3, 5, True)
    b2 = Block("Stone", "rock", 5, 10, True)

    assert b1 != b2


def test_sorting_blocks():
    blocks = [
        Block("A", "m1", 3, 10, True),
        Block("B", "m2", 1, 5, False),
        Block("C", "m3", 3, 7, True),
    ]

    sorted_blocks = sorted(blocks, key=lambda b: (b.hardness, -b.weight))

    assert sorted_blocks[0].name == "B"
    assert sorted_blocks[1].name == "C"
    assert sorted_blocks[2].name == "A"

def test_find_object_logic():
    blocks = [
        Block("Stone", "rock", 5, 10, True),
        Block("Wood", "organic", 3, 5, True),
        Block("Glass", "sand", 1, 3, False),
    ]

    target = Block("Wood", "organic", 3, 5, True)

    found = None
    for b in blocks:
        if b == target:
            found = b
            break

    assert found is not None
    assert found.name == "Wood"

def test_program_main_runs(capsys):
    Program.main()
    captured = capsys.readouterr()

    assert "C11" in captured.out
