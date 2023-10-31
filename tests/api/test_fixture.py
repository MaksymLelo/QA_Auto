import pytest


@pytest.mark.check
def test_change_name(user):
    assert user.name == "Maksym"


@pytest.mark.check
def test_change_secong_name(user):
    assert user.second_name == "Lelo"
