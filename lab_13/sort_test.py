from sort import bubblesort
import pytest

testdata = [
    ([18, 2, 5, 1, 20, 21, 19], [1, 2, 5, 18, 19, 20, 21]),
    ([1, 3, 2, 5], [1, 2, 3, 5]),
    (['a', 'b', 'c'], ['1']),
    ([60, 20, 30, 80, 21], [1, 2, 3]),
    (1, 3)
]

@pytest.mark.parametrize('test, expected_output', testdata)
def test_bubblesort(test, expected_output):
    assert type(test) == list
    assert type(expected_output) == list
    assert [type(i) for i in test] == [int] * len(test)
    assert [type(i) for i in expected_output] == [int] * len(expected_output)
    assert len(test) == len(expected_output)

    lst = bubblesort(test)[0]
    assert lst == expected_output