def test_numpy_24_basic_regression():
    """
    Regression test for NumPy 2.4 compatibility (gh-41342).

    This test ensures that basic NumPy array behavior used by Sage
    remains stable.
    """
    import numpy as np

    a = np.array([1, 2, 3], dtype=int)

    assert a.sum() == 6
    assert a.dtype == int
