import pytest
from main import Block, Program


def test_calculate_variant():
    assert Program.calculate_variant(5202) == 10


def test_block_equality():
    b1 = Block("Wood", "organic", 3, 5, True)
    b2 = Block("Wood", "organic", 3, 5, True)
    b3 = Block("Stone", "rock", 5, 10, True)

    assert b1 == b2
    assert b1 != b3


def test_create_blocks():
    blocks = Program.create_blocks()

    assert len(blocks) == 5
    assert isinstance(blocks[0], Block)


def test_sort_blocks():
    blocks = Program.create_blocks()
    sorted_blocks = Program.sort_blocks(blocks)

    assert sorted_blocks[0].hardness <= sorted_blocks[1].hardness

    for i in range(len(sorted_blocks) - 1):
        b1 = sorted_blocks[i]
        b2 = sorted_blocks[i + 1]

        if b1.hardness == b2.hardness:
            assert b1.weight >= b2.weight


def test_find_block_found():
    blocks = Program.create_blocks()
    sorted_blocks = Program.sort_blocks(blocks)

    target = Block("Wood", "organic", 3, 5, True)
    result = Program.find_block(sorted_blocks, target)

    assert result is not None
    assert result == target


def test_find_block_not_found():
    blocks = Program.create_blocks()
    sorted_blocks = Program.sort_blocks(blocks)

    target = Block("Gold", "metal", 10, 20, True)
    result = Program.find_block(sorted_blocks, target)

    assert result is None
