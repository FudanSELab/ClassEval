import unittest


class IpUtilTestIsValidIpv4(unittest.TestCase):
    def test_is_valid_ipv4_1(self):
        result = IpUtil.is_valid_ipv4('192.168.0.123')
        self.assertEqual(result, True)

    def test_is_valid_ipv4_2(self):
        result = IpUtil.is_valid_ipv4('10.10.10.10')
        self.assertEqual(result, True)

    def test_is_valid_ipv4_3(self):
        result = IpUtil.is_valid_ipv4('0.0.0.0')
        self.assertEqual(result, True)

    def test_is_valid_ipv4_4(self):
        result = IpUtil.is_valid_ipv4('abc.168.0.123')
        self.assertEqual(result, False)

    def test_is_valid_ipv4_5(self):
        result = IpUtil.is_valid_ipv4('256.0.0.0')
        self.assertEqual(result, False)


class IpUtilTestIsValidIpv6(unittest.TestCase):
    def test_is_valid_ipv6_1(self):
        result = IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
        self.assertEqual(result, True)

    def test_is_valid_ipv6_2(self):
        result = IpUtil.is_valid_ipv6('2001:0db8:85a3:::8a2e:0370:7334')
        self.assertEqual(result, False)

    def test_is_valid_ipv6_3(self):
        result = IpUtil.is_valid_ipv6('2001:0db8:85a3:2001:llll:8a2e:0370:7334')
        self.assertEqual(result, False)

    def test_is_valid_ipv6_4(self):
        result = IpUtil.is_valid_ipv6('2001:0db8:85a3:llll:llll:8a2e:0370:7334')
        self.assertEqual(result, False)

    def test_is_valid_ipv6_5(self):
        result = IpUtil.is_valid_ipv6('2001:0db8:85a3::llll:8a2e:0370:7334')
        self.assertEqual(result, False)


class IpUtilTestGetHostname(unittest.TestCase):
    def test_get_hostname_1(self):
        result = IpUtil.get_hostname('110.242.68.3')
        self.assertEqual(result, None)

    def test_get_hostname_2(self):
        result = IpUtil.get_hostname('10.0.0.1')
        self.assertEqual(result, None)

    def test_get_hostname_3(self):
        result = IpUtil.get_hostname('0.0.0.0')
        self.assertEqual(result, 'LAPTOP-2CS86KUM')

    def test_get_hostname_4(self):
        result = IpUtil.get_hostname('0.0.0.1')
        self.assertEqual(result, None)

    def test_get_hostname_5(self):
        result = IpUtil.get_hostname('0.0.0.2')
        self.assertEqual(result, None)


class IpUtilTest(unittest.TestCase):
    def test_IpUtil(self):
        result = IpUtil.is_valid_ipv4('192.168.0.123')
        self.assertEqual(result, True)

        result = IpUtil.is_valid_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
        self.assertEqual(result, True)

        result = IpUtil.get_hostname('110.242.68.3')
        self.assertEqual(result, None)
