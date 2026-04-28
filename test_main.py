from main import Block, Program


def test_block_equality():
    b1 = Block("Stone", "rock", 5, 10, True)
    b2 = Block("Stone", "rock", 5, 10, True)

    assert b1 == b2


def test_block_inequality():
    b1 = Block("Stone", "rock", 5, 10, True)
    b2 = Block("Glass", "sand", 1, 3, False)

    assert b1 != b2


def test_sorting_order():
    blocks = [
        Block("A", "m1", 3, 10, True),
        Block("B", "m2", 1, 50, True),
        Block("C", "m3", 1, 20, True),
    ]

    sorted_blocks = sorted(blocks, key=lambda b: (b.hardness, -b.weight))

    # спочатку hardness=1 (C потім B через weight ↓)
    assert sorted_blocks[0].name == "C"
    assert sorted_blocks[1].name == "B"
    assert sorted_blocks[2].name == "A"


def test_search_found():
    blocks = [
        Block("Stone", "rock", 5, 10, True),
        Block("Wood", "organic", 3, 5, True),
    ]

    target = Block("Wood", "organic", 3, 5, True)

    found = None
    for b in blocks:
        if b == target:
            found = b
            break

    assert found is not None
    assert found.name == "Wood"


def test_search_not_found():
    blocks = [
        Block("Stone", "rock", 5, 10, True),
        Block("Wood", "organic", 3, 5, True),
    ]

    target = Block("Iron", "metal", 7, 15, True)

    found = None
    for b in blocks:
        if b == target:
            found = b
            break

    assert found is None
