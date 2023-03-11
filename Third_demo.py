
def test_1():
    x = 10
    y = 20
    assert x == y   # assert is like comparision if its result is true then test case is passed if false then test case is failed


def test_2():
    x = 20
    y = 20
    assert x == y


def test_t3():
    x = 10
    y = 20
    result = x + y
    assert result == 30


def some_test_t4():             ## invalid test case name
    x = 10
    y = 20
    result = x + y
    assert result == 30


def some_test():             ## invalid test case name
    x = 10
    y = 20
    result = x + y
    assert result == 30
