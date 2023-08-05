import unittest
import os


class CSVProcessorTestReadCSV(unittest.TestCase):
    def test_read_csv_1(self):
        self.file = 'read_test.csv'

        with open(self.file, 'w') as f:
            f.write('a,b,c,d\nhElLo,YoU,ME,LoW')

        expected_title = ['a', 'b', 'c', 'd']
        expected_data = [['hElLo', 'YoU', 'ME', 'LoW']]
        csvProcessor = CSVProcessor()
        title, data = csvProcessor.read_csv(self.file)
        self.assertEqual(expected_data, data)
        self.assertEqual(expected_title, title)

    def test_read_csv_2(self):
        self.file = 'read_test.csv'
        with open(self.file, 'w') as f:
            f.write('1234\nhElLo,YoU,ME,LoW')

        expected_title = ['1234']
        expected_data = [['hElLo', 'YoU', 'ME', 'LoW']]
        csvProcessor = CSVProcessor()
        title, data = csvProcessor.read_csv(self.file)
        self.assertEqual(expected_data, data)
        self.assertEqual(expected_title, title)

    def test_read_csv_3(self):
        self.file = 'read_test.csv'

        with open(self.file, 'w') as f:
            f.write('title\nhElLo,YoU,ME,LoW')

        expected_title = ['title']
        expected_data = [['hElLo', 'YoU', 'ME', 'LoW']]
        csvProcessor = CSVProcessor()
        title, data = csvProcessor.read_csv(self.file)
        self.assertEqual(expected_data, data)
        self.assertEqual(expected_title, title)

    def test_read_csv_4(self):
        self.file = 'read_test.csv'

        with open(self.file, 'w') as f:
            f.write('title4\nhElLo,YoU,ME,LoW')

        expected_title = ['title4']
        expected_data = [['hElLo', 'YoU', 'ME', 'LoW']]
        csvProcessor = CSVProcessor()
        title, data = csvProcessor.read_csv(self.file)
        self.assertEqual(expected_data, data)
        self.assertEqual(expected_title, title)

    def test_read_csv_5(self):
        self.file = 'read_test.csv'

        with open(self.file, 'w') as f:
            f.write('title5\nhElLo,YoU,ME,LoW')

        expected_title = ['title5']
        expected_data = [['hElLo', 'YoU', 'ME', 'LoW']]
        csvProcessor = CSVProcessor()
        title, data = csvProcessor.read_csv(self.file)
        self.assertEqual(expected_data, data)
        self.assertEqual(expected_title, title)


class CSVProcessorTestWriteCSV(unittest.TestCase):
    def test_write_csv_1(self):
        self.file = 'read_test.csv'

        file_path = self.file
        csvProcessor = CSVProcessor()
        data = [['a', 'b', 'c', 'd'], ['1', '2', '3', '4']]
        # assert return value
        self.assertEqual(1, csvProcessor.write_csv(data, file_path))

        # read to test if write correctly
        read_title, read_data = csvProcessor.read_csv(file_path)
        self.assertEqual(read_title, data[0])
        self.assertEqual(read_data[0], data[1])
        os.remove(file_path)

    def test_write_csv_2(self):
        self.file = 'read_test.csv'

        file_path = self.file
        csvProcessor = CSVProcessor()
        data = [['aa', 'bb', 'cc', 'dd'], ['1', '2', '3', '4']]
        # assert return value
        self.assertEqual(1, csvProcessor.write_csv(data, file_path))

        # read to test if write correctly
        read_title, read_data = csvProcessor.read_csv(file_path)
        self.assertEqual(read_title, data[0])
        self.assertEqual(read_data[0], data[1])
        os.remove(file_path)

    def test_write_csv_3(self):
        self.file = 'read_test.csv'

        file_path = self.file
        csvProcessor = CSVProcessor()
        data = [['a', 'b', 'c', 'd'], ['11', '22', '33', '44']]
        # assert return value
        self.assertEqual(1, csvProcessor.write_csv(data, file_path))

        # read to test if write correctly
        read_title, read_data = csvProcessor.read_csv(file_path)
        self.assertEqual(read_title, data[0])
        self.assertEqual(read_data[0], data[1])
        os.remove(file_path)

    def test_write_csv_4(self):
        self.file = 'read_test.csv'

        file_path = self.file
        csvProcessor = CSVProcessor()
        data = [['e', 'f', 'g', 'h'], ['1', '2', '3', '4']]
        # assert return value
        self.assertEqual(1, csvProcessor.write_csv(data, file_path))

        # read to test if write correctly
        read_title, read_data = csvProcessor.read_csv(file_path)
        self.assertEqual(read_title, data[0])
        self.assertEqual(read_data[0], data[1])
        os.remove(file_path)

    def test_write_csv_5(self):
        self.file = 'read_test.csv'

        file_path = self.file
        csvProcessor = CSVProcessor()
        data = [['a', 'b', 'c', 'd'], ['5', '6', '7', '8']]
        # assert return value
        self.assertEqual(1, csvProcessor.write_csv(data, file_path))

        # read to test if write correctly
        read_title, read_data = csvProcessor.read_csv(file_path)
        self.assertEqual(read_title, data[0])
        self.assertEqual(read_data[0], data[1])
        os.remove(file_path)

    def test_write_csv_6(self):
        self.file = ''
        file_path = self.file
        csvProcessor = CSVProcessor()
        # assert return value
        self.assertEqual(0, csvProcessor.write_csv([], file_path))


class CSVProcessorTestProcessCSVData(unittest.TestCase):
    def setUp(self) -> None:
        self.file = 'read_test.csv'
        self.file_process = 'read_test_process.csv'
        with open(self.file, 'w') as f:
            f.write('a,b,c,d\nhElLo,YoU,ME,LoW,aBc')

    def test_process_csv_data_1(self):
        title = ['a', 'b', 'c', 'd']
        data = ['HELLO']
        csvProcessor = CSVProcessor()
        self.assertEqual(1, csvProcessor.process_csv_data(0, self.file))

        read_title, read_data = csvProcessor.read_csv(self.file_process)
        self.assertEqual(read_title, title)
        self.assertEqual(read_data[0], data)

    def test_process_csv_data_2(self):
        title = ['a', 'b', 'c', 'd']
        data = ['YOU']
        csvProcessor = CSVProcessor()
        self.assertEqual(1, csvProcessor.process_csv_data(1, self.file))

        read_title, read_data = csvProcessor.read_csv(self.file_process)
        self.assertEqual(read_title, title)
        self.assertEqual(read_data[0], data)

    def test_process_csv_data_3(self):
        title = ['a', 'b', 'c', 'd']
        data = ['ME']
        csvProcessor = CSVProcessor()
        self.assertEqual(1, csvProcessor.process_csv_data(2, self.file))

        read_title, read_data = csvProcessor.read_csv(self.file_process)
        self.assertEqual(read_title, title)
        self.assertEqual(read_data[0], data)

    def test_process_csv_data_4(self):
        title = ['a', 'b', 'c', 'd']
        data = ['LOW']
        csvProcessor = CSVProcessor()
        self.assertEqual(1, csvProcessor.process_csv_data(3, self.file))

        read_title, read_data = csvProcessor.read_csv(self.file_process)
        self.assertEqual(read_title, title)
        self.assertEqual(read_data[0], data)

    def test_process_csv_data_5(self):
        title = ['a', 'b', 'c', 'd']
        data = ['ABC']
        csvProcessor = CSVProcessor()
        self.assertEqual(1, csvProcessor.process_csv_data(4, self.file))

        read_title, read_data = csvProcessor.read_csv(self.file_process)
        self.assertEqual(read_title, title)
        self.assertEqual(read_data[0], data)


class CSVProcessorTestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.file = 'test.csv'
        self.file_process = 'test_process.csv'
        with open(self.file, 'w') as f:
            f.write('a,b,c,d\nhElLo,YoU,ME,LoW')

    def test_main(self):
        csvProcessor = CSVProcessor()
        data = [['a', 'b', 'c', 'd'], ['hElLo', 'YoU', 'ME', 'LoW']]
        # assert return value
        self.assertEqual(1, csvProcessor.write_csv(data, self.file))
        expected_title = ['a', 'b', 'c', 'd']
        expected_data = [['hElLo', 'YoU', 'ME', 'LoW']]
        title, data = csvProcessor.read_csv(self.file)
        self.assertEqual(expected_data, data)
        self.assertEqual(expected_title, title)

        title = ['a', 'b', 'c', 'd']
        data = ['HELLO']
        self.assertEqual(1, csvProcessor.process_csv_data(0, self.file))

        read_title, read_data = csvProcessor.read_csv(self.file_process)
        self.assertEqual(read_title, title)
        self.assertEqual(read_data[0], data)
