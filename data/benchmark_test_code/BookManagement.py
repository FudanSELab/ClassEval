import unittest


class BookManagementTestAddBook(unittest.TestCase):
    def test_add_book_1(self):
        bookManagement = BookManagement()
        bookManagement.add_book("book1")
        self.assertEqual({"book1": 1}, bookManagement.inventory)

    def test_add_book_2(self):
        bookManagement = BookManagement()
        self.assertEqual({}, bookManagement.inventory)

    def test_add_book_3(self):
        bookManagement = BookManagement()
        bookManagement.add_book("book1")
        bookManagement.add_book("book1", 2)
        self.assertEqual({"book1": 3}, bookManagement.inventory)

    def test_add_book_4(self):
        bookManagement = BookManagement()
        bookManagement.add_book("book1", 2)
        self.assertEqual({"book1": 2}, bookManagement.inventory)

    def test_add_book_5(self):
        bookManagement = BookManagement()
        bookManagement.add_book("book1", 2)
        bookManagement.add_book("book1")
        self.assertEqual({"book1": 3}, bookManagement.inventory)


class BookManagementTestRemoveBook(unittest.TestCase):
    def setUp(self) -> None:
        self.bookManagement = BookManagement()
        self.bookManagement.add_book("book1", 2)
        self.bookManagement.add_book("book2")

    # remove all this title books
    def test_remove_book_1(self):
        self.bookManagement.remove_book("book1", 2)
        self.assertEqual(self.bookManagement.inventory, {"book2": 1})

    # remove part
    def test_remove_book_2(self):
        self.bookManagement.remove_book("book1", 1)
        self.assertEqual(self.bookManagement.inventory, {"book1": 1, "book2": 1})

    # remove the title that doesn't exist
    def test_remove_book_3(self):
        with self.assertRaises(Exception):
            self.bookManagement.remove_book("book3", 1)

    # invalid quantity
    def test_remove_book_4(self):
        with self.assertRaises(Exception):
            self.bookManagement.remove_book("book2", 2)

    def test_remove_book_5(self):
        with self.assertRaises(Exception):
            self.bookManagement.remove_book("book2", 5)


class BookManagementTestViewInventory(unittest.TestCase):
    def test_view_inventory_1(self):
        bookManagement = BookManagement()
        bookManagement.add_book("book1", 2)
        bookManagement.add_book("book2")
        expected = {"book1": 2, "book2": 1}
        self.assertEqual(expected, bookManagement.inventory)

    def test_view_inventory_2(self):
        bookManagement = BookManagement()
        expected = {}
        self.assertEqual(expected, bookManagement.inventory)

    def test_view_inventory_3(self):
        bookManagement = BookManagement()
        bookManagement.add_book("book1", 2)
        bookManagement.add_book("book2")
        expected = {"book1": 2, "book2": 1}
        self.assertEqual(expected, bookManagement.inventory)

    def test_view_inventory_4(self):
        bookManagement = BookManagement()
        bookManagement.add_book("book1", 2)
        bookManagement.add_book("book2")
        bookManagement.remove_book("book1", 2)
        expected = {"book2": 1}
        self.assertEqual(expected, bookManagement.inventory)

    def test_view_inventory_5(self):
        bookManagement = BookManagement()
        bookManagement.add_book("book1", 2)
        bookManagement.add_book("book2", 1)
        bookManagement.remove_book("book1", 2)
        bookManagement.remove_book("book2",1)
        expected = {}
        self.assertEqual(expected, bookManagement.inventory)


class BookManagementTestViewBookQuantity(unittest.TestCase):
    def test_view_book_quantity_1(self):
        bookManagement = BookManagement()
        bookManagement.add_book("book1", 2)
        self.assertEqual(2, bookManagement.view_book_quantity("book1"))

    def test_view_book_quantity_2(self):
        bookManagement = BookManagement()
        self.assertEqual(0, bookManagement.view_book_quantity("book1"))

    def test_view_book_quantity_3(self):
        bookManagement = BookManagement()
        bookManagement.add_book("book1", 2)
        self.assertEqual(2, bookManagement.view_book_quantity("book1"))

    def test_view_book_quantity_4(self):
        bookManagement = BookManagement()
        bookManagement.add_book("book1", 2)
        bookManagement.remove_book("book1", 2)
        self.assertEqual(0, bookManagement.view_book_quantity("book1"))

    def test_view_book_quantity_5(self):
        bookManagement = BookManagement()
        bookManagement.add_book("book1", 3)
        bookManagement.remove_book("book1", 2)
        self.assertEqual(1, bookManagement.view_book_quantity("book1"))


class BookManagementTestMain(unittest.TestCase):
    def test_main(self):
        bookManagement = BookManagement()
        bookManagement.add_book("book1", 2)
        bookManagement.add_book("book2")
        self.assertEqual(bookManagement.view_inventory(), {"book1": 2, "book2": 1})

        bookManagement.remove_book("book2", 1)
        self.assertEqual(bookManagement.view_inventory(), {"book1": 2})
        self.assertEqual(0, bookManagement.view_book_quantity("book2"))