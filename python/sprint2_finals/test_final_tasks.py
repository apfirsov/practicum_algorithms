import sys
from io import StringIO
from typing import Dict, List, Tuple
import a as task_a
import b as task_b


def test_a() -> None:
    cases: List[Tuple[int, List[List[str]], str]] = [
        (4,
         [['push_front', '861'], ['push_front', '-819'], ['pop_back'],
          ['pop_back']],
         '861\n-819\n'),
        (10,
         [['push_front', '-855'], ['push_front', '0'], ['pop_back'],
          ['pop_back'], ['push_back', '844'], ['pop_back'],
          ['push_back', '823']],
         '-855\n0\n844\n'),
        (6,
         [['push_front', '-201'], ['push_back', '959'], ['push_back', '102'],
          ['push_front', '20'], ['pop_front'], ['pop_back']],
         '20\n102\n'),
        (7,
         [['pop_front'], ['pop_front'], ['push_front', '741'],
          ['push_front', '648'], ['pop_front'], ['pop_back'], ['pop_front']],
         'error\nerror\n648\n741\nerror\n'),
    ]

    for max_size, commands, exp in cases:
        out = StringIO()
        sys.stdout = out
        task_a.main(max_size, commands)
        sys.stdout = sys.__stdout__
        assert out.getvalue() == exp, 'WA'


def test_b() -> None:
    cases: Dict[str, int] = {
        '2 1 + 3 *': 9,
        '7 2 + 4 * 2 +': 38,
    }
    for seq, exp in cases.items():
        assert task_b.main(seq.split()) == exp, 'WA'
