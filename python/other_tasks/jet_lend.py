from typing import Dict, List, Set, Tuple


def remove_duplicates(array: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Removes dict-type duplicates from list."""
    unique_values: Set = set()
    result: List[Dict[str, str]] = []

    for dictionary in array:
        content_tuple: Tuple = tuple(dictionary.items())
        if content_tuple not in unique_values:
            unique_values.add(content_tuple)
            result.append(dictionary)

    return result


def main() -> None:
    array: List[Dict[str, str]] = [
        {"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {},
        {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}
    ]
    clear_array = remove_duplicates(array)
    print(clear_array)


def test() -> None:
    cases: List[Tuple] = [
        ([{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {},
          {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}],
         [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {},
          {"key2": "value2"}]),
        ([], []),
        ([{"a": "a"}, {"a": "123"}, {"a": "a"}], [{"a": "a"}, {"a": "123"}]),
        ([{"a": "a"}, {"a": "a"}, {"a": "a"}], [{"a": "a"}])
    ]

    for array, expected in cases:
        assert remove_duplicates(array) == expected, f"Wrong answer {array}"

    print('Tests - OK')


if __name__ == '__main__':
    main()
