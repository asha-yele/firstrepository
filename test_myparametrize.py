import pytest


@pytest.mark.parametrize("username,password",
                             [
                                 ('userid', 'pass123'),
                                 ("abc", 'pwd@123'),
                                 ("abc", 'pwd@123'),
                                 ("xyz", 'xyz@123'),
                                 ("pqr", 'pwd@987')
                             ]
                         )
def test_login(username, password):
    print(f"{username}   {password}")

    if username == 'abc':
        assert False

