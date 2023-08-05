import unittest

class NLPDataProcessorTestConstruct(unittest.TestCase):
    def setUp(self):
        self.processor = NLPDataProcessor()

    def test_construct_stop_word_list(self):
        stop_word_list = self.processor.construct_stop_word_list()
        expected_stop_words = ['a', 'an', 'the']
        self.assertEqual(stop_word_list, expected_stop_words)

class NLPDataProcessorTestRemove(unittest.TestCase):
    def setUp(self):
        self.processor = NLPDataProcessor()

    def test_remove_stop_words(self):
        string_list = ['This is a test', 'This is an apple', 'This is the dog']
        stop_word_list = ['a', 'an', 'the']
        words_list = self.processor.remove_stop_words(string_list, stop_word_list)
        expected_words_list = [['This', 'is', 'test'], ['This', 'is', 'apple'], ['This', 'is', 'dog']]
        self.assertEqual(words_list, expected_words_list)

    def test_remove_stop_words_2(self):
        string_list = ['a', 'an', 'the']
        stop_word_list = ['a', 'an', 'the']
        words_list = self.processor.remove_stop_words(string_list, stop_word_list)
        self.assertEqual(words_list, [[], [], []])

    def test_remove_stop_words_3(self):
        string_list = []
        stop_word_list = ['a', 'an', 'the']
        words_list = self.processor.remove_stop_words(string_list, stop_word_list)
        self.assertEqual(words_list, [])

    def test_remove_stop_words_4(self):
        string_list = ['This is a test', 'This is an apple', 'This is the dog']
        stop_word_list = []
        words_list = self.processor.remove_stop_words(string_list, stop_word_list)
        expected_words_list = [['This', 'is', 'a', 'test'], ['This', 'is', 'an', 'apple'], ['This', 'is', 'the', 'dog']]
        self.assertEqual(words_list, expected_words_list)

    def test_remove_stop_words_5(self):
        string_list = ['This is a test', 'This is an apple', 'This is the dog']
        stop_word_list = ['a', 'an', 'the', 'This', 'is']
        words_list = self.processor.remove_stop_words(string_list, stop_word_list)
        expected_words_list = [['is', 'test'], ['is', 'apple'], ['is', 'dog']]
        self.assertEqual(words_list, expected_words_list)

class NLPDataProcessorTestProcess(unittest.TestCase):
    def setUp(self):
        self.processor = NLPDataProcessor()

    def test_process(self):
        string_list = ['This is a test.', 'This is an apple.', 'This is the dog.']
        words_list = self.processor.process(string_list)
        expected_words_list = [['This', 'is', 'test.'], ['This', 'is', 'apple.'], ['This', 'is', 'dog.']]
        self.assertEqual(words_list, expected_words_list)

    def test_process_with_empty_string_list(self):
        string_list = []
        words_list = self.processor.process(string_list)
        self.assertEqual(words_list, [])

    def test_process_with_single_word_sentences(self):
        string_list = ['Hello aa', 'World']
        words_list = self.processor.process(string_list)
        expected_words_list = [['Hello', 'aa'], ['World']]
        self.assertEqual(words_list, expected_words_list)

    def test_process_with_stop_words_only(self):
        string_list = ['a', 'an', 'the']
        words_list = self.processor.process(string_list)
        self.assertEqual(words_list, [[], [], []])

    def test_process_with_stop_words_only_2(self):
        string_list = ['a', 'an', 'the','This']
        words_list = self.processor.process(string_list)
        self.assertEqual(words_list,[[], [], [], ['This']])


