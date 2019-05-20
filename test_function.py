from my_function import four, three


def test_three_returns_3():
    assert 3 == three()



def test_three_returns_3_wrong_order():
    assert three() == 3

def test_failing_three_returns_4():
    assert 4 == three()

def test_failing_three_returns_5():
    assert 5 == three()

def test_failing_three_returns_4_wrong_order():
    assert three() == 4

def test_four_returns_4():
    assert 4 == four()