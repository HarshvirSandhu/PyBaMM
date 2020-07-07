import pybamm
import unittest
import numpy as np


class TestPlot(unittest.TestCase):
    def test_plot(self):
        x = pybamm.Array(np.array([0, 3, 10]))
        y = pybamm.Array(np.array([6, 16, 78]))
        pybamm.plot(x, y, xlabel="x", ylabel="y", title="title", testing=True)

    def test_plot_fail(self):
        x = pybamm.Array(np.array([0]))
        with self.assertRaisesRegex(TypeError, "x must be 'pybamm.Array'"):
            pybamm.plot("bad", x)
        with self.assertRaisesRegex(TypeError, "y must be 'pybamm.Array'"):
            pybamm.plot(x, "bad")

    def test_plot2D(self):
        x = pybamm.Array(np.array([0, 3, 10]))
        y = pybamm.Array(np.array([6, 16, 78]))
        X, Y = pybamm.meshgrid(x, y)

        # plot with array directly
        pybamm.plot2D(x, y, Y, xlabel="x", ylabel="y", title="title", testing=True)

        # plot with meshgrid
        pybamm.plot2D(X, Y, Y, xlabel="x", ylabel="y", title="title", testing=True)

    def test_plot2D_fail(self):
        x = pybamm.Array(np.array([0]))
        with self.assertRaisesRegex(TypeError, "x must be 'pybamm.Array'"):
            pybamm.plot2D("bad", x, x)
        with self.assertRaisesRegex(TypeError, "y must be 'pybamm.Array'"):
            pybamm.plot2D(x, "bad", x)
        with self.assertRaisesRegex(TypeError, "z must be 'pybamm.Array'"):
            pybamm.plot2D(x, x, "bad")


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    pybamm.settings.debug_mode = True
    unittest.main()
