import unittest


class OrderTestAddDish(unittest.TestCase):
    def setUp(self):
        self.order = Order()

        self.order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        self.order.menu.append({"dish": "dish2", "price": 15, "count": 3})
        self.order.menu.append({"dish": "dish3", "price": 20, "count": 7})
        self.order.sales = {"dish1": 0.9, "dish2": 1, "dish3": 0.8}

    # add dish in menu
    def test_add_dish_1(self):
        result = self.order.add_dish({"dish": "dish3", "price": 15, "count": 4})
        self.assertTrue(result)

        # test the status of self.menu and self.selected_dishes
        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 5)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 3)
        self.assertEqual(self.order.selected_dishes, [{"dish": "dish3", "price": 15, "count": 4}])

    # add dish when dish count exceeds the remaining count
    def test_add_dish_2(self):
        result = self.order.add_dish({"dish": "dish3", "price": 15, "count": 8})
        self.assertFalse(result)

        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 5)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 7)
        self.assertEqual(self.order.selected_dishes, [])

    def test_add_dish_3(self):
        result = self.order.add_dish({"dish": "dish3", "price": 15, "count": 7})
        self.assertTrue(result)

        # test the status of self.menu and self.selected_dishes
        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 5)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 0)
        self.assertEqual(self.order.selected_dishes, [{"dish": "dish3", "price": 15, "count": 7}])

    def test_add_dish_4(self):
        result = self.order.add_dish({"dish": "dish3", "price": 15, "count": 6})
        self.assertTrue(result)

        # test the status of self.menu and self.selected_dishes
        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 5)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 1)
        self.assertEqual(self.order.selected_dishes, [{"dish": "dish3", "price": 15, "count": 6}])

    def test_add_dish_5(self):
        result = self.order.add_dish({"dish": "dish3", "price": 15, "count": 5})
        self.assertTrue(result)

        # test the status of self.menu and self.selected_dishes
        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 5)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 2)
        self.assertEqual(self.order.selected_dishes, [{"dish": "dish3", "price": 15, "count": 5}])

    def test_add_dish_6(self):
        self.order.menu = []
        result = self.order.add_dish({})
        self.assertTrue(result)


class OrderTestCalculateTotal(unittest.TestCase):
    def setUp(self):
        self.order = Order()
        self.order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        self.order.menu.append({"dish": "dish2", "price": 15, "count": 3})
        self.order.menu.append({"dish": "dish3", "price": 20, "count": 7})
        self.order.sales = {"dish1": 0.9, "dish2": 1, "dish3": 0.8}

    def test_calculate_total_1(self):
        self.order.add_dish({"dish": "dish1", "price": 10, "count": 2})
        self.order.add_dish({"dish": "dish3", "price": 20, "count": 2})
        result = self.order.calculate_total()
        self.assertEqual(50, result)

    def test_calculate_total_2(self):
        self.order.add_dish({"dish": "dish1", "price": 10, "count": 2})
        self.order.add_dish({"dish": "dish2", "price": 15, "count": 2})
        result = self.order.calculate_total()
        self.assertEqual(48, result)

    def test_calculate_total_3(self):
        self.order.add_dish({"dish": "dish1", "price": 10, "count": 1})
        self.order.add_dish({"dish": "dish3", "price": 20, "count": 1})
        result = self.order.calculate_total()
        self.assertEqual(25, result)

    def test_calculate_total_4(self):
        self.order.add_dish({"dish": "dish1", "price": 10, "count": 3})
        self.order.add_dish({"dish": "dish3", "price": 20, "count": 3})
        result = self.order.calculate_total()
        self.assertEqual(75, result)

    def test_calculate_total_5(self):
        self.order.add_dish({"dish": "dish1", "price": 10, "count": 4})
        self.order.add_dish({"dish": "dish3", "price": 20, "count": 4})
        result = self.order.calculate_total()
        self.assertEqual(100, result)


class OrderTestCheckout(unittest.TestCase):
    def setUp(self):
        self.order = Order()
        self.order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        self.order.menu.append({"dish": "dish2", "price": 15, "count": 3})
        self.order.menu.append({"dish": "dish3", "price": 20, "count": 7})
        self.order.sales = {"dish1": 0.9, "dish2": 1, "dish3": 0.8}

    # as test_main
    def test_checkout_1(self):
        self.order.add_dish({"dish": "dish1", "price": 10, "count": 2})
        self.order.add_dish({"dish": "dish3", "price": 20, "count": 2})
        result = self.order.checkout()
        self.assertEqual(50, result)

        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 5)
        self.assertEqual([], self.order.selected_dishes)

    # haven't ordered dishes.
    # self.selected_dishes is empty
    def test_checkout_2(self):
        result = self.order.checkout()
        self.assertFalse(result)

    def test_checkout_3(self):
        self.order.add_dish({"dish": "dish1", "price": 10, "count": 1})
        self.order.add_dish({"dish": "dish3", "price": 20, "count": 1})
        result = self.order.checkout()
        self.assertEqual(25, result)

        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 4)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 6)
        self.assertEqual([], self.order.selected_dishes)

    def test_checkout_4(self):
        self.order.add_dish({"dish": "dish1", "price": 10, "count": 3})
        self.order.add_dish({"dish": "dish3", "price": 20, "count": 3})
        result = self.order.checkout()
        self.assertEqual(75, result)

        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 2)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 4)
        self.assertEqual([], self.order.selected_dishes)

    def test_checkout_5(self):
        self.order.add_dish({"dish": "dish1", "price": 10, "count": 5})
        self.order.add_dish({"dish": "dish3", "price": 20, "count": 5})
        result = self.order.checkout()
        self.assertEqual(125, result)

        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 0)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 2)
        self.assertEqual([], self.order.selected_dishes)


class OrderTest(unittest.TestCase):
    def setUp(self):
        self.order = Order()

        self.order.menu.append({"dish": "dish1", "price": 10, "count": 5})
        self.order.menu.append({"dish": "dish2", "price": 15, "count": 3})
        self.order.menu.append({"dish": "dish3", "price": 20, "count": 7})
        self.order.sales = {"dish1": 0.9, "dish2": 1, "dish3": 0.8}

    def test_order(self):
        self.order.add_dish({"dish": "dish1", "price": 10, "count": 2})
        self.order.add_dish({"dish": "dish3", "price": 20, "count": 2})
        result = self.order.checkout()
        self.assertEqual(50, result)

        menu = self.order.menu
        for menu_dish in menu:
            if menu_dish["dish"] == "dish1":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish2":
                self.assertEqual(menu_dish["count"], 3)
            if menu_dish["dish"] == "dish3":
                self.assertEqual(menu_dish["count"], 5)
        self.assertEqual([], self.order.selected_dishes)

