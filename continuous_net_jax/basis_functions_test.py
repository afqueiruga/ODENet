import unittest

from .basis_functions import *

class BasisFunctionsTests(unittest.TestCase):

    def test_list_of_floats(self):
        nodes = [1.0, 3.0, 2.0]
        theta_t = params_of_t(nodes, piecewise_constant)
        self.assetEqual(theta_t(0.0), 1.0)
        self.assetEqual(theta_t(0.5), 3.0)
        self.assetEqual(theta_t(1.000001), 2.0)
        self.assetTrue(False)


if __name__ == "__main__":
    unittest.main()
