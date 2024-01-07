import pytest
import numpy as np
from src.epsilon_algorithm import epsilon_algorithm
from src.series import gregory_series, pi_gregory_series


@pytest.mark.parametrize(
    "x, n",
    [
        (x, n)
        for x in np.linspace(0.5, 10, num=10)
        for n in [32, 64, 128]
    ],
)
def test_gregory_series(x, n):
    series = gregory_series(x, n)
    y = np.arctan(np.sum(x))
    y_pred = epsilon_algorithm(series)
    np.testing.assert_allclose(y, y_pred, atol=1e-4, rtol=1e-4)


