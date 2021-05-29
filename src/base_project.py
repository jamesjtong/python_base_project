from src.helper import hello
from src.subpackage.nested_helper import helper_b


def calc_a():
    return hello() + helper_b()
