from a import broken_search


def test_a() -> None:
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    assert broken_search([3, 6, 7], 8) == -1


def test_b() -> None:
    pass
