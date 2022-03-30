import pytest

import EverorOdd

@pytest.mark.parametrize("a,b",[(10,True),(2,True),(3,True),(6,True),(5,False),(7,False)])
def test_evenorodd(a,b):
    result = EverorOdd.EvenorOdd(a)
    assert result == b


