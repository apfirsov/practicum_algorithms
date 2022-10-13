import sys
from io import StringIO
from a import broken_search
from b import Contestant, main


def test_a() -> None:
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    assert broken_search([3, 6, 7], 8) == -1


def test_b() -> None:
    cases = [
        ([['alla', 4, 100], ['gena', 6, 1000], ['gosha', 2, 90],
          ['rita', 2, 90], ['timofey', 4, 80]],
         'gena\ntimofey\nalla\ngosha\nrita\n'),
        ([['alla', 0, 0], ['gena', 0, 0], ['gosha', 0, 0],
          ['rita', 0, 0], ['timofey', 0, 0]],
         'alla\ngena\ngosha\nrita\ntimofey\n'),
    ]

    for data, exp in cases:
        contest_list = [Contestant(*params) for params in data]
        out = StringIO()
        sys.stdout = out
        main(contest_list)
        sys.stdout = sys.__stdout__
        assert out.getvalue() == exp, 'WA'
