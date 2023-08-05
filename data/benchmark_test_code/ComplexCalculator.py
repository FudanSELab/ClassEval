import unittest

class ComplexCalculatorTestAdd(unittest.TestCase):
    def test_add(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.add(1+2j, 3+4j), (4+6j))

    def test_add_2(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.add(-1 - 2j, -3 - 4j), (-4 - 6j))

    def test_add_3(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.add(1-2j, 3-4j), (4-6j))

    def test_add_4(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.add(-1+2j, -3+4j), (-4+6j))

    def test_add_5(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.add(1+2j, -1-2j), (0+0j))

class ComplexCalculatorTestSubtract(unittest.TestCase):
    def test_subtract(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.subtract(1+2j, 3+4j), (-2-2j))

    def test_subtract_2(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.subtract(-1-2j, -3-4j), (2+2j))

    def test_subtract_3(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.subtract(1-2j, 3-4j), (-2+2j))

    def test_subtract_4(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.subtract(-1+2j, -3+4j), (2-2j))

    def test_subtract_5(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.subtract(1+2j, 1+2j), (0+0j))

class ComplexCalculatorTestMultiply(unittest.TestCase):
    def test_multiply(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.multiply(1+2j, 3+4j), (-5+10j))

    def test_multiply_2(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.multiply(-1-2j, -3-4j), (-5+10j))

    def test_multiply_3(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.multiply(1-2j, 3-4j), (-5-10j))

    def test_multiply_4(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.multiply(-1+2j, -3+4j), (-5-10j))

    def test_multiply_5(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.multiply(1+2j, -1-2j), (3-4j))

class ComplexCalculatorTestDivide(unittest.TestCase):
    def test_divide(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.divide(1+2j, 3+4j), (0.44+0.08j))

    def test_divide_2(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.divide(-1-2j, -3-4j), (0.44+0.08j))

    def test_divide_3(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.divide(1-2j, 3-4j), (0.44-0.08j))

    def test_divide_4(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.divide(-1+2j, -3+4j), (0.44-0.08j))

    def test_divide_5(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.divide(1+2j, -1-2j), (-1+0j))

class ComplexCalculatorTestMain(unittest.TestCase):
    def test_main(self):
        complexCalculator = ComplexCalculator()
        self.assertEqual(complexCalculator.add(1+2j, 3+4j), (4+6j))
        self.assertEqual(complexCalculator.subtract(1+2j, 3+4j), (-2-2j))
        self.assertEqual(complexCalculator.multiply(1+2j, 3+4j), (-5+10j))
        self.assertEqual(complexCalculator.divide(1+2j, 3+4j), (0.44+0.08j))