import unittest


class UrlPathTestAdd(unittest.TestCase):
    def test_add_1(self):
        url_path = UrlPath()
        url_path.add('foo')
        url_path.add('bar')
        self.assertEqual(url_path.segments, ['foo', 'bar'])

    def test_add_2(self):
        url_path = UrlPath()
        url_path.add('aaa')
        url_path.add('bbb')
        self.assertEqual(url_path.segments, ['aaa', 'bbb'])

    def test_add_3(self):
        url_path = UrlPath()
        url_path.add('123')
        self.assertEqual(url_path.segments, ['123'])

    def test_add_4(self):
        url_path = UrlPath()
        url_path.add('ddd')
        self.assertEqual(url_path.segments, ['ddd'])

    def test_add_5(self):
        url_path = UrlPath()
        url_path.add('eee')
        self.assertEqual(url_path.segments, ['eee'])


class UrlPathTestParse(unittest.TestCase):
    def test_parse_1(self):
        url_path = UrlPath()
        url_path.parse('/foo/bar/', 'utf-8')
        self.assertEqual(url_path.segments, ['foo', 'bar'])
        self.assertEqual(url_path.with_end_tag, True)

    def test_parse_2(self):
        url_path = UrlPath()
        url_path.parse('aaa/bbb', 'utf-8')
        self.assertEqual(url_path.segments, ['aaa', 'bbb'])
        self.assertEqual(url_path.with_end_tag, False)

    def test_parse_3(self):
        url_path = UrlPath()
        url_path.parse('/123/456/', 'utf-8')
        self.assertEqual(url_path.segments, ['123', '456'])
        self.assertEqual(url_path.with_end_tag, True)

    def test_parse_4(self):
        url_path = UrlPath()
        url_path.parse('/123/456/789', 'utf-8')
        self.assertEqual(url_path.segments, ['123', '456', '789'])
        self.assertEqual(url_path.with_end_tag, False)

    def test_parse_5(self):
        url_path = UrlPath()
        url_path.parse('/foo/bar', 'utf-8')
        self.assertEqual(url_path.segments, ['foo', 'bar'])
        self.assertEqual(url_path.with_end_tag, False)

    def test_parse_6(self):
        url_path = UrlPath()
        url_path.parse('', 'utf-8')
        self.assertEqual(url_path.segments, [])
        self.assertEqual(url_path.with_end_tag, False)

    def test_parse_7(self):
        url_path = UrlPath()
        url_path.parse('//', 'utf-8')
        self.assertEqual(url_path.segments, [])
        self.assertEqual(url_path.with_end_tag, True)


class UrlPathTestFixPath(unittest.TestCase):
    def test_fix_path_1(self):
        fixed_path = UrlPath.fix_path('/foo/bar/')
        self.assertEqual(fixed_path, 'foo/bar')

    def test_fix_path_2(self):
        fixed_path = UrlPath.fix_path('/aaa/bbb/')
        self.assertEqual(fixed_path, 'aaa/bbb')

    def test_fix_path_3(self):
        fixed_path = UrlPath.fix_path('/a/b/')
        self.assertEqual(fixed_path, 'a/b')

    def test_fix_path_4(self):
        fixed_path = UrlPath.fix_path('/111/222/')
        self.assertEqual(fixed_path, '111/222')

    def test_fix_path_5(self):
        fixed_path = UrlPath.fix_path('/a/')
        self.assertEqual(fixed_path, 'a')

    def test_fix_path_6(self):
        fixed_path = UrlPath.fix_path('')
        self.assertEqual(fixed_path, '')


class UrlPathTest(unittest.TestCase):
    def test_urlpath(self):
        url_path = UrlPath()
        url_path.add('foo')
        url_path.add('bar')
        self.assertEqual(url_path.segments, ['foo', 'bar'])

        url_path = UrlPath()
        url_path.parse('/foo/bar/', 'utf-8')
        self.assertEqual(url_path.segments, ['foo', 'bar'])
        self.assertEqual(url_path.with_end_tag, True)

        fixed_path = UrlPath.fix_path('/foo/bar/')
        self.assertEqual(fixed_path, 'foo/bar')

