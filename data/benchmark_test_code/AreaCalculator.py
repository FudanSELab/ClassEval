import unittest

class AreaCalculatorTestCalculateCircleArea(unittest.TestCase):
    def test_calculate_circle_area(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(12.56, areaCalculator.calculate_circle_area(), delta=0.01)
    def test_calculate_circle_area_2(self):
        areaCalculator = AreaCalculator(2.5)
        self.assertAlmostEqual(19.63, areaCalculator.calculate_circle_area(), delta=0.01)

    def test_calculate_circle_area_3(self):
        areaCalculator = AreaCalculator(2000)
        self.assertAlmostEqual(12566370.61, areaCalculator.calculate_circle_area(), delta=0.01)

    def test_calculate_circle_area_4(self):
        areaCalculator = AreaCalculator(0)
        self.assertAlmostEqual(0, areaCalculator.calculate_circle_area(), delta=0.01)

    def test_calculate_circle_area_5(self):
        areaCalculator = AreaCalculator(0.1)
        self.assertAlmostEqual(0.031, areaCalculator.calculate_circle_area(), delta=0.01)


class AreaCalculatorTestCalculateSphereArea(unittest.TestCase):
    def test_calculate_sphere_area(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(50.27, areaCalculator.calculate_sphere_area(), delta=0.01)

    def test_calculate_sphere_area_2(self):
        areaCalculator = AreaCalculator(2.5)
        self.assertAlmostEqual(19.63, areaCalculator.calculate_circle_area(), delta=0.01)

    def test_calculate_sphere_area_3(self):
        areaCalculator = AreaCalculator(2000)
        self.assertAlmostEqual(12566370.61, areaCalculator.calculate_circle_area(), delta=0.01)

    def test_calculate_sphere_area_4(self):
        areaCalculator = AreaCalculator(0)
        self.assertAlmostEqual(0, areaCalculator.calculate_circle_area(), delta=0.01)

    def test_calculate_sphere_area_5(self):
        areaCalculator = AreaCalculator(0.1)
        self.assertAlmostEqual(0.031, areaCalculator.calculate_circle_area(), delta=0.01)


class AreaCalculatorTestCalculateCylinderArea(unittest.TestCase):
    def test_calculate_cylinder_area(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(50.27, areaCalculator.calculate_cylinder_area(2), delta=0.01)

    def test_calculate_cylinder_area_2(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(25.13, areaCalculator.calculate_cylinder_area(0), delta=0.01)

    def test_calculate_cylinder_area_3(self):
        areaCalculator = AreaCalculator(0)
        self.assertAlmostEqual(0, areaCalculator.calculate_cylinder_area(2000), delta=0.01)

    def test_calculate_cylinder_area_4(self):
        areaCalculator = AreaCalculator(2.5)
        self.assertAlmostEqual(70.68, areaCalculator.calculate_cylinder_area(2), delta=0.01)

    def test_calculate_cylinder_area_5(self):
        areaCalculator = AreaCalculator(2.5)
        self.assertAlmostEqual(62.83, areaCalculator.calculate_cylinder_area(1.5), delta=0.01)

class AreaCalculatorTestCalculateSectorArea(unittest.TestCase):
    def test_calculate_sector_area(self):
        areaCalculator = AreaCalculator(1.5)
        self.assertAlmostEqual(3.53, areaCalculator.calculate_sector_area(math.pi), delta=0.01)

    def test_calculate_sector_area_2(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(3.14, areaCalculator.calculate_sector_area(math.pi/2), delta=0.01)

    def test_calculate_sector_area_3(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(0, areaCalculator.calculate_sector_area(0), delta=0.01)

    def test_calculate_sector_area_4(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(12.56, areaCalculator.calculate_sector_area(2*math.pi), delta=0.01)

    def test5_calculate_sector_area_5(self):
        areaCalculator = AreaCalculator(0)
        self.assertAlmostEqual(0, areaCalculator.calculate_sector_area(math.pi), delta=0.01)

class AreaCalculatorTestCalculateAnnulusArea(unittest.TestCase):
    def test_calculate_annulus_area(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(25.128, areaCalculator.calculate_annulus_area(1, 3), delta=0.01)

    def test_calculate_annulus_area_2(self):
        areaCalculator = AreaCalculator(2.5)
        self.assertAlmostEqual(0, areaCalculator.calculate_annulus_area(3, 3), delta=0.01)

    def test_calculate_annulus_area_3(self):
        areaCalculator = AreaCalculator(2000)
        self.assertAlmostEqual(3.14, areaCalculator.calculate_annulus_area(0, 1), delta=0.01)

    def test_calculate_annulus_area_4(self):
        areaCalculator = AreaCalculator(0)
        self.assertAlmostEqual(25.13, areaCalculator.calculate_annulus_area(1, 3), delta=0.01)

    def test_calculate_annulus_area_5(self):
        areaCalculator = AreaCalculator(2.5)
        self.assertAlmostEqual(25.13, areaCalculator.calculate_annulus_area(1, 3), delta=0.01)

class AreaCalculatorTestCalculateMain(unittest.TestCase):
    def test_main(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(12.56, areaCalculator.calculate_circle_area(), delta=0.01)
        self.assertAlmostEqual(50.27, areaCalculator.calculate_sphere_area(), delta=0.01)
        self.assertAlmostEqual(50.27, areaCalculator.calculate_cylinder_area(2), delta=0.01)
        self.assertAlmostEqual(6.28, areaCalculator.calculate_sector_area(math.pi), delta=0.01)
        self.assertAlmostEqual(25.128, areaCalculator.calculate_annulus_area(1, 3), delta=0.01)
