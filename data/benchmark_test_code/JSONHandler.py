import os
import stat
import json
import unittest


class JSONProcessorTestReadJson(unittest.TestCase):
    def setUp(self):
        self.processor = JSONProcessor()
        self.test_data = {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3"
        }
        self.file_path = "test.json"

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    # file exists
    def test_read_json_1(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.test_data, file)
        result = self.processor.read_json(self.file_path)
        self.assertEqual(result, self.test_data)

    # file not exists
    def test_read_json_2(self):
        result = self.processor.read_json(self.file_path)
        self.assertEqual(result, 0)

    # invalid json file
    def test_read_json_3(self):
        with open(self.file_path, 'w') as file:
            file.write("Invalid JSON")
        result = self.processor.read_json(self.file_path)
        self.assertEqual(result, -1)

    def test_read_json_4(self):
        result = self.processor.read_json('wrong')
        self.assertEqual(result, 0)

    def test_read_json_5(self):
        result = self.processor.read_json('abcd')
        self.assertEqual(result, 0)


class JSONProcessorTestWriteJson(unittest.TestCase):
    def setUp(self):
        self.processor = JSONProcessor()
        self.test_data = {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3"
        }
        self.file_path = "test.json"

        # create a read only file
        self.file_path_only_read = 'test_only_read.json'
        with open(self.file_path_only_read, 'w') as f:
            f.write('{"key1": "value1"}')

        # set file only read mode
        os.chmod(self.file_path_only_read, stat.S_IRUSR + stat.S_IRGRP + stat.S_IROTH)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if os.path.exists(self.file_path_only_read):
            # unset file only read mode and remove the file
            os.chmod(self.file_path_only_read,
                     stat.S_IWUSR + stat.S_IRUSR + stat.S_IWGRP + stat.S_IRGRP + stat.S_IWOTH + stat.S_IROTH)
            os.remove(self.file_path_only_read)

    def test_write_json_1(self):
        result = self.processor.write_json(self.test_data, self.file_path)
        self.assertEqual(result, 1)
        with open(self.file_path, 'r') as file:
            written_data = json.load(file)
        self.assertEqual(written_data, self.test_data)

    def test_write_json_2(self):
        # Provide a read-only file path to simulate an exception
        result = self.processor.write_json(self.test_data, self.file_path_only_read)
        self.assertEqual(result, -1)

    def test_write_json_3(self):
        result = self.processor.write_json([], self.file_path_only_read)
        self.assertEqual(result, -1)

    def test_write_json_4(self):
        result = self.processor.write_json(self.test_data, '')
        self.assertEqual(result, -1)

    def test_write_json_5(self):
        result = self.processor.write_json([], '')
        self.assertEqual(result, -1)


class JSONProcessorTestProcessJsonExistingKey(unittest.TestCase):
    def setUp(self):
        self.processor = JSONProcessor()
        self.test_data = {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3"
        }
        self.file_path = "test.json"

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    # key exists
    def test_process_json_1(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.test_data, file)
        remove_key = "key2"
        self.processor.process_json(self.file_path, remove_key)
        with open(self.file_path, 'r') as file:
            processed_data = json.load(file)
        expected_data = {
            "key1": "value1",
            "key3": "value3"
        }
        self.assertEqual(processed_data, expected_data)

    # key not exists
    def test_process_json_2(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.test_data, file)
        remove_key = "nonexistent_key"
        self.processor.process_json(self.file_path, remove_key)
        with open(self.file_path, 'r') as file:
            processed_data = json.load(file)
        self.assertEqual(processed_data, self.test_data)

    # file is empty
    def test_process_json_3(self):
        # Create an empty JSON file
        with open(self.file_path, 'w') as file:
            pass
        remove_key = "key1"
        self.assertEqual(self.processor.process_json(self.file_path, remove_key), 0)

    def test_process_json_4(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.test_data, file)
        remove_key = "aaa"
        self.processor.process_json(self.file_path, remove_key)
        with open(self.file_path, 'r') as file:
            processed_data = json.load(file)
        self.assertEqual(processed_data, self.test_data)

    def test_process_json_5(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.test_data, file)
        remove_key = "bbb"
        self.processor.process_json(self.file_path, remove_key)
        with open(self.file_path, 'r') as file:
            processed_data = json.load(file)
        self.assertEqual(processed_data, self.test_data)


class JSONProcessorTestMain(unittest.TestCase):
    def setUp(self):
        self.processor = JSONProcessor()
        self.test_data = {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3"
        }
        self.file_path = "test.json"

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_main(self):
        # write first
        result = self.processor.write_json(self.test_data, self.file_path)
        self.assertEqual(result, 1)
        with open(self.file_path, 'r') as file:
            written_data = json.load(file)
        self.assertEqual(written_data, self.test_data)

        # read
        result = self.processor.read_json(self.file_path)
        self.assertEqual(result, self.test_data)

        # process
        remove_key = "key2"
        self.processor.process_json(self.file_path, remove_key)
        with open(self.file_path, 'r') as file:
            processed_data = json.load(file)
        expected_data = {
            "key1": "value1",
            "key3": "value3"
        }
        self.assertEqual(processed_data, expected_data)

