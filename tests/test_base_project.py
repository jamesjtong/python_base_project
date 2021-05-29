from src.base_project import *


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


def test_import_from_src():
    assert calc_a() == 89
