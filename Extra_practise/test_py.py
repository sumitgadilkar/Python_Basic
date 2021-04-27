import pytest

def test_1():
    x = 89
    y = 89
    assert x==y, "Test Failed as value of x and y not match"


def test_2():
    name = "Selencls"
    title = "Name is Selenium"
    assert name in title, "{name} is not present in Title"


def test_3():
    name = "jenkins"
    title= "Jenkins is CI CD platform"
    assert name in title, "Title not matches"
