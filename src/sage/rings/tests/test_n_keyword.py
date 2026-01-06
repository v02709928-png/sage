def test_n_keyword_prec_digits():
    """
    Regression test for keyword handling in numerical approximation.
    """
    from sage.all import QQ

    x = QQ(2) / QQ(3)

    a = x.n(digits=10)
    b = x.n(prec=34)

    assert a is not None
    assert b is not None
    assert x.n(digits=10) == a
def test_n_keyword_prec_digits():
    """
    Regression test for keyword handling in numerical approximation.
    """
    from sage.all import QQ

    x = QQ(2) / QQ(3)

    a = x.n(digits=10)
    b = x.n(prec=34)

    assert a is not None
    assert b is not None
    assert x.n(digits=10) == a

