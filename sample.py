import pytest


def print1(a):
    val = a
    return val


def test_print1():
    refval = print1(1)
    assert refval == 1