from account import account

acc = account()

def test_login() :
    assert acc.login("a", "1234") == True
    assert acc.login("", "") == False
    assert acc.login("a", "") == False
    assert acc.login("", "1234") == False
    assert acc.login("b", "5678") == False

def test_register() :
    assert acc.register("a", "1234", "a@a.com", "1234567890") == True
    assert acc.register("", "1234", "a@a.com", "1234567890") == False
    assert acc.register("a", "", "a@a.com", "1234567890") == False
    assert acc.register("a", "1234", "", "1234567890") == False
    assert acc.register("a", "1234", "a@a.com", "") == False
    assert acc.register("a", "1", "a@a.com", "1234567890") == False
    assert acc.register("a", "1234", "a.com", "1234567890") == False
    assert acc.register("a", "1234", "a@a", "1234567890") == False
    assert acc.register("a", "1234", "a@a.com", "123456789") == False
    
