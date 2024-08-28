import pytest
from account import account


@pytest.fixture
def setup_account():
    acc = account()
    yield acc


def test_login(setup_account) :
    acc = setup_account
    
    assert acc.login("a", "1234") == True
    assert acc.login("", "") == False
    assert acc.login("a", "") == False
    assert acc.login("", "1234") == False
    assert acc.login("b", "5678") == False

def test_register(setup_account) :
    acc = setup_account
    
    assert acc.register("new_account", "1234", "a@a.com", "1234567890") == True
    acc.unregister("new_account")
    assert acc.register("", "1234", "a@a.com", "1234567890") == False
    assert acc.register("b", "", "a@a.com", "1234567890") == False
    assert acc.register("c", "1234", "", "1234567890") == False
    assert acc.register("d", "1234", "a@a.com", "") == False
    assert acc.register("e", "1", "a@a.com", "1234567890") == False
    assert acc.register("f", "1234", "a.com", "1234567890") == False
    assert acc.register("g", "1234", "a@a", "1234567890") == False
    assert acc.register("h", "1234", "a@a.com", "123456789") == False

