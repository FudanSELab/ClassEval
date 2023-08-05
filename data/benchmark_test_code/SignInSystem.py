import unittest


class SignInSystemTestAddUser(unittest.TestCase):
    def test_add_user_1(self):
        signin_system = SignInSystem()
        result = signin_system.add_user("user1")
        self.assertTrue(result)

    def test_add_user_2(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        result = signin_system.add_user("user1")
        self.assertFalse(result)

    def test_add_user_3(self):
        signin_system = SignInSystem()
        result = signin_system.add_user("aaa")
        self.assertTrue(result)

    def test_add_user_4(self):
        signin_system = SignInSystem()
        result = signin_system.add_user("bbb")
        self.assertTrue(result)

    def test_add_user_5(self):
        signin_system = SignInSystem()
        result = signin_system.add_user("ccc")
        self.assertTrue(result)


class SignInSystemTestSignIn(unittest.TestCase):
    def test_sign_in_1(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        result = signin_system.sign_in("user1")
        self.assertTrue(result)

    # user not exist
    def test_sign_in_2(self):
        signin_system = SignInSystem()
        result = signin_system.sign_in("user1")
        self.assertFalse(result)

    def test_sign_in_3(self):
        signin_system = SignInSystem()
        signin_system.add_user("aaa")
        result = signin_system.sign_in("aaa")
        self.assertTrue(result)

    def test_sign_in_4(self):
        signin_system = SignInSystem()
        signin_system.add_user("bbb")
        result = signin_system.sign_in("bbb")
        self.assertTrue(result)

    def test_sign_in_5(self):
        signin_system = SignInSystem()
        result = signin_system.sign_in("ccc")
        self.assertFalse(result)


class SignInSystemTestCheckSignIn(unittest.TestCase):
    # has signed in
    def test_check_sign_in_1(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        signin_system.sign_in("user1")
        result = signin_system.check_sign_in("user1")
        self.assertTrue(result)

    # hasn't signed in 
    def test_check_sign_in_2(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        result = signin_system.check_sign_in("user1")
        self.assertFalse(result)

    # not exist
    def test_check_sign_in_3(self):
        signin_system = SignInSystem()
        result = signin_system.check_sign_in("user1")
        self.assertFalse(result)

    def test_check_sign_in_4(self):
        signin_system = SignInSystem()
        signin_system.add_user("aaa")
        signin_system.sign_in("aaa")
        result = signin_system.check_sign_in("aaa")
        self.assertTrue(result)

    def test_check_sign_in_5(self):
        signin_system = SignInSystem()
        signin_system.add_user("bbb")
        signin_system.sign_in("bbb")
        result = signin_system.check_sign_in("bbb")
        self.assertTrue(result)


class SignInSystemTestAllSignedIn(unittest.TestCase):
    def test_all_signed_in_1(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        signin_system.sign_in("user1")
        result = signin_system.all_signed_in()
        self.assertTrue(result)

    def test_all_signed_in_2(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        result = signin_system.all_signed_in()
        self.assertFalse(result)

    def test_all_signed_in_3(self):
        signin_system = SignInSystem()
        signin_system.add_user("aaa")
        signin_system.sign_in("aaa")
        result = signin_system.all_signed_in()
        self.assertTrue(result)

    def test_all_signed_in_4(self):
        signin_system = SignInSystem()
        signin_system.add_user("bbb")
        signin_system.sign_in("bbb")
        result = signin_system.all_signed_in()
        self.assertTrue(result)

    def test_all_signed_in_5(self):
        signin_system = SignInSystem()
        signin_system.add_user("aaa")
        signin_system.add_user("bbb")
        signin_system.sign_in("aaa")
        result = signin_system.all_signed_in()
        self.assertFalse(result)


class SignInSystemTestAllNotSignedIn(unittest.TestCase):
    def test_all_not_signed_in_1(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        signin_system.sign_in("user1")
        result = signin_system.all_not_signed_in()
        self.assertEqual([], result)

    def test_all_not_signed_in_2(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        signin_system.add_user("user2")
        result = signin_system.all_not_signed_in()
        self.assertEqual(["user1", "user2"], result)

    def test_all_not_signed_in_3(self):
        signin_system = SignInSystem()
        signin_system.add_user("aaa")
        signin_system.sign_in("aaa")
        result = signin_system.all_not_signed_in()
        self.assertEqual([], result)

    def test_all_not_signed_in_4(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        signin_system.add_user("aaa")
        signin_system.sign_in("user1")
        result = signin_system.all_not_signed_in()
        self.assertEqual(['aaa'], result)

    def test_all_not_signed_in_5(self):
        signin_system = SignInSystem()
        result = signin_system.all_not_signed_in()
        self.assertEqual([], result)


class SignInSystemTestMain(unittest.TestCase):
    def setUp(self):
        self.signin_system = SignInSystem()

    def test_main(self):
        result = self.signin_system.add_user("user1")
        result = self.signin_system.add_user("user2")
        self.assertTrue(result)

        result = self.signin_system.sign_in("user1")
        self.assertTrue(result)

        result = self.signin_system.check_sign_in("user1")
        self.assertTrue(result)

        result = self.signin_system.all_signed_in()
        self.assertFalse(result)

        result = self.signin_system.all_not_signed_in()
        self.assertEqual(["user2"], result)
