import pytest


@pytest.mark.smoke
def test_1():
    x = 10
    y = 20
    assert x == y   # assert is like comparision if its result is true then test case is passed if false then test case is failed


@pytest.mark.regression
def test_2():
    x = 20
    y = 20
    assert x == y


@pytest.mark.regression
def test_t3():
    x = 10
    y = 20
    result = x + y
    assert result == 30


@pytest.mark.smoke
@pytest.mark.regression
def test_some():
    x = 10
    y = 20
    result = x + y
    assert result == 30

@pytest.mark.smoke
def some_test():             ## invalid test case name
    x = 10
    y = 20
    result = x + y
    assert result == 30


@pytest.mark.bhagyashree
def test_check_in():
    name = "Credence"
    message = "Credence is the best place to learn and also extended family"
    assert name in message      ## in =>  like operator or contains function


@pytest.mark.regression
def test_check_is():
    name = "Credence"
    message = "Credence is the best place to learn and also extended family"
    assert name is message      #  is =>  equal to

