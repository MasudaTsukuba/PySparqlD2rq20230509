from uri_query import execute_query


def test_q1():
    result = execute_query('query/q1.txt')
    assert len(result) == 801


def test_q2():
    result = execute_query('query/q2.txt')
    assert len(result) == 2146


def test_q3a():
    result = execute_query('query/q3a.txt')
    assert len(result) == 3732


def test_q3b():
    result = execute_query('query/q3b.txt')
    assert len(result) == 3695


def test_q4():
    result = execute_query('query/q4.txt')
    assert len(result) == 19526


def test_q5():
    result = execute_query('query/q5.txt')
    assert len(result) == 43980


def test_q6():
    result = execute_query('query/q6.txt')
    assert len(result) == 219


def test_q7():
    result = execute_query('query/q7.txt')
    assert len(result) == 1


def test_q1pred():
    result = execute_query('query/q1pred.txt')
    assert len(result) == 801