import unittest
import os


class ZipFileProcessorTestReadZipFile(unittest.TestCase):
    def test_read_zip_file_1(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example1.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)

        zip_file = processor.read_zip_file()
        self.assertEqual(zip_file.filename, 'example1.zip')
        self.assertEqual(zip_file.mode, 'r')
        zip_file.close()

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_read_zip_file_2(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example2.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)

        zip_file = processor.read_zip_file()
        self.assertEqual(zip_file.filename, 'example2.zip')
        self.assertEqual(zip_file.mode, 'r')
        zip_file.close()

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_read_zip_file_3(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example3.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)

        zip_file = processor.read_zip_file()
        self.assertEqual(zip_file.filename, 'example3.zip')
        self.assertEqual(zip_file.mode, 'r')
        zip_file.close()

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_read_zip_file_4(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example4.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)

        zip_file = processor.read_zip_file()
        self.assertEqual(zip_file.filename, 'example4.zip')
        self.assertEqual(zip_file.mode, 'r')
        zip_file.close()

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_read_zip_file_5(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example5.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        zip_file = processor.read_zip_file()
        self.assertEqual(zip_file.filename, 'example5.zip')
        self.assertEqual(zip_file.mode, 'r')
        zip_file.close()

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_read_zip_file_6(self):
        processor = ZipFileProcessor("")

        zip_file = processor.read_zip_file()
        self.assertIsNone(zip_file)


class ZipFileProcessorTestExtractAll(unittest.TestCase):
    def test_extract_all_1(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example1.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        success = processor.extract_all(output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example1.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_extract_all_2(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example2.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        success = processor.extract_all(output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example2.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_extract_all_3(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example3.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        success = processor.extract_all(output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example3.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_extract_all_4(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example4.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        success = processor.extract_all(output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example4.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_extract_all_5(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example5.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        success = processor.extract_all(output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example5.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_extract_all_6(self):
        processor = ZipFileProcessor("")

        success = processor.extract_all("")
        self.assertFalse(success)


class ZipFileProcessorTestExtractFile(unittest.TestCase):
    def test_extract_file_1(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example1.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        success = processor.extract_file('example1.txt', output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example1.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_extract_file_2(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example2.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        success = processor.extract_file('example2.txt', output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example2.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_extract_file_3(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example3.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        success = processor.extract_file('example3.txt', output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example3.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_extract_file_4(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example4.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        success = processor.extract_file('example4.txt', output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example4.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_extract_file_5(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example5.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'

        success = processor.extract_file('example5.txt', output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example5.txt')))

        os.remove(zip_file_name)
        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_extract_file_6(self):
        processor = ZipFileProcessor("")

        success = processor.extract_file("", "")
        self.assertFalse(success)


class ZipFileProcessorTestCreateZipFile(unittest.TestCase):
    def test_create_zip_file_1(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example1.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        files_to_zip = [example_file_path]
        success = processor.create_zip_file(files_to_zip, new_zip_file)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(new_zip_file))

        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_create_zip_file_2(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example2.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        files_to_zip = [example_file_path]
        success = processor.create_zip_file(files_to_zip, new_zip_file)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(new_zip_file))

        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_create_zip_file_3(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example3.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        files_to_zip = [example_file_path]
        success = processor.create_zip_file(files_to_zip, new_zip_file)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(new_zip_file))

        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_create_zip_file_4(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example4.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        files_to_zip = [example_file_path]
        success = processor.create_zip_file(files_to_zip, new_zip_file)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(new_zip_file))

        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_create_zip_file_5(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example5.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        new_zip_file = 'new_zip_file.zip'

        files_to_zip = [example_file_path]
        success = processor.create_zip_file(files_to_zip, new_zip_file)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(new_zip_file))

        os.remove(example_file_path)
        os.rmdir(test_folder)

    def test_create_zip_file_6(self):
        processor = ZipFileProcessor("")

        success = processor.create_zip_file("", "")
        self.assertFalse(success)


class ZipFileProcessorTest(unittest.TestCase):
    def test_ZipFileProcessor(self):
        test_folder = 'test_folder'
        os.makedirs(test_folder, exist_ok=True)
        example_file_path = os.path.join(test_folder, 'example1.txt')
        with open(example_file_path, 'w') as file:
            file.write('This is an example file.')

        zip_file_name = 'example.zip'
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.write(example_file_path, os.path.basename(example_file_path))

        processor = ZipFileProcessor(zip_file_name)
        output_directory = 'output_directory'
        new_zip_file = 'new_zip_file.zip'

        zip_file = processor.read_zip_file()
        self.assertEqual(zip_file.filename, 'example.zip')
        self.assertEqual(zip_file.mode, 'r')
        zip_file.close()

        success = processor.extract_all(output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example1.txt')))

        files_to_zip = [example_file_path]
        success = processor.create_zip_file(files_to_zip, new_zip_file)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(new_zip_file))

        success = processor.extract_file('example1.txt', output_directory)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(os.path.join(output_directory, 'example1.txt')))

        files_to_zip = [example_file_path]
        success = processor.create_zip_file(files_to_zip, new_zip_file)
        self.assertTrue(success)
        self.assertTrue(os.path.exists(new_zip_file))

        os.remove(example_file_path)
        os.rmdir(test_folder)
