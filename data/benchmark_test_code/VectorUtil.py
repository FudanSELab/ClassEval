import unittest


class VectorUtilTestSimilarity(unittest.TestCase):
    def test_similarity_1(self):
        vector_1 = np.array([1, 1])
        vector_2 = np.array([1, 0])
        similarity = VectorUtil.similarity(vector_1, vector_2)
        self.assertAlmostEqual(similarity, 0.7071067811865475)

    def test_similarity_2(self):
        vector_1 = np.array([1, 1])
        vector_2 = np.array([0, 0])
        similarity = VectorUtil.similarity(vector_1, vector_2)
        self.assertAlmostEqual(similarity, 0.0)

    def test_similarity_3(self):
        vector_1 = np.array([1, 1])
        vector_2 = np.array([1, 1])
        similarity = VectorUtil.similarity(vector_1, vector_2)
        self.assertAlmostEqual(similarity, 1.0)

    def test_similarity_4(self):
        vector_1 = np.array([1, 1, 0, 1, 0, 1, 0, 1])
        vector_2 = np.array([1, 0, 0, 1, 0, 1, 0, 1])
        similarity = VectorUtil.similarity(vector_1, vector_2)
        self.assertAlmostEqual(similarity, 0.8944271909999159)

    def test_similarity_5(self):
        vector_1 = np.array([1, 1, 1, 1, 1, 1, 1, 1])
        vector_2 = np.array([0, 0, 0, 0, 0, 0, 0, 0])
        similarity = VectorUtil.similarity(vector_1, vector_2)
        self.assertAlmostEqual(similarity, 0.0)


class VectorUtilTestCosineSimilarities(unittest.TestCase):
    def test_cosine_similarities_1(self):
        vector1 = np.array([1, 1])
        vectors_all = [np.array([1, 0]), np.array([1, 1])]
        similarities = VectorUtil.cosine_similarities(vector1, vectors_all)
        res = [0.7071067811865475, 1.0]
        for index, item in enumerate(similarities):
            self.assertAlmostEqual(item, res[index])

    def test_cosine_similarities_2(self):
        vector1 = np.array([1, 1, 0, 0, 1, 0, 1, 0])
        vectors_all = [np.array([1, 0, 0, 0, 1, 0, 1, 0]), np.array([1, 1, 0, 1, 1, 1, 1, 0])]
        similarities = VectorUtil.cosine_similarities(vector1, vectors_all)
        res = [0.8660254037844387, 0.8164965809277261]
        for index, item in enumerate(similarities):
            self.assertAlmostEqual(item, res[index])

    def test_cosine_similarities_3(self):
        vector1 = np.array([1, 1, 0, 0, 1, 0, 1, 0])
        vectors_all = [np.array([1, 0, 0, 0, 1, 0, 1, 0]), np.array([1, 1, 1, 1, 1, 1, 1, 0])]
        similarities = VectorUtil.cosine_similarities(vector1, vectors_all)
        res = [0.8660254037844387, 0.7559289460184544]
        for index, item in enumerate(similarities):
            self.assertAlmostEqual(item, res[index])

    def test_cosine_similarities_4(self):
        vector1 = np.array([1, 1, 0, 0, 1, 0, 1, 0])
        vectors_all = [np.array([1, 0, 0, 0, 1, 0, 1, 0]), np.array([1, 1, 1, 1, 1, 1, 1, 1])]
        similarities = VectorUtil.cosine_similarities(vector1, vectors_all)
        res = [0.8660254037844387, 0.7071067811865475]
        for index, item in enumerate(similarities):
            self.assertAlmostEqual(item, res[index])

    def test_cosine_similarities_5(self):
        vector1 = np.array([1, 1, 0, 0, 1, 0, 1, 0])
        vectors_all = [np.array([1, 0, 0, 0, 1, 0, 1, 0]), np.array([0, 1, 1, 1, 1, 1, 1, 1])]
        similarities = VectorUtil.cosine_similarities(vector1, vectors_all)
        res = [0.8660254037844387, 0.5669467095138409]
        for index, item in enumerate(similarities):
            self.assertAlmostEqual(item, res[index])


class VectorUtilTestNSimilarity(unittest.TestCase):
    def test_n_similarity_1(self):
        vector_list1 = [np.array([1, 0]), np.array([0, 1])]
        vector_list2 = [np.array([0, 0]), np.array([1, 1])]
        similarity = VectorUtil.n_similarity(vector_list1, vector_list2)
        self.assertAlmostEqual(similarity, 1.0)

    def test_n_similarity_2(self):
        vector_list1 = [np.array([1, 1]), np.array([0, 1])]
        vector_list2 = [np.array([0, 0]), np.array([1, 1])]
        similarity = VectorUtil.n_similarity(vector_list1, vector_list2)
        self.assertAlmostEqual(similarity, 0.9486832980505137)

    def test_n_similarity_3(self):
        vector_list1 = [np.array([1, 0]), np.array([1, 1])]
        vector_list2 = [np.array([0, 0]), np.array([1, 1])]
        similarity = VectorUtil.n_similarity(vector_list1, vector_list2)
        self.assertAlmostEqual(similarity, 0.9486832980505137)

    def test_n_similarity_4(self):
        vector_list1 = [np.array([1, 0]), np.array([0, 1])]
        vector_list2 = [np.array([1, 0]), np.array([1, 1])]
        similarity = VectorUtil.n_similarity(vector_list1, vector_list2)
        self.assertAlmostEqual(similarity, 0.9486832980505137)

    def test_n_similarity_5(self):
        vector_list1 = [np.array([1, 0]), np.array([0, 1])]
        vector_list2 = [np.array([0, 1]), np.array([1, 1])]
        similarity = VectorUtil.n_similarity(vector_list1, vector_list2)
        self.assertAlmostEqual(similarity, 0.9486832980505137)

    def test_n_similarity_6(self):
        try:
            vector_list1 = []
            vector_list2 = []
            similarity = VectorUtil.n_similarity(vector_list1, vector_list2)
        except:
            pass


class VectorUtilTestComputeIdfWeightDict(unittest.TestCase):
    def test_compute_idf_weight_dict_1(self):
        num_dict = {'key1': 0.1, 'key2': 0.5}
        res = VectorUtil.compute_idf_weight_dict(2, num_dict)
        self.assertAlmostEqual(res['key1'], 1.0033021088637848)
        self.assertAlmostEqual(res['key2'], 0.6931471805599453)

    def test_compute_idf_weight_dict_2(self):
        num_dict = {'key1': 0.2, 'key2': 0.5}
        res = VectorUtil.compute_idf_weight_dict(2, num_dict)
        self.assertAlmostEqual(res['key1'], 0.9162907318741551)
        self.assertAlmostEqual(res['key2'], 0.6931471805599453)

    def test_compute_idf_weight_dict_3(self):
        num_dict = {'key1': 0.3, 'key2': 0.5}
        res = VectorUtil.compute_idf_weight_dict(2, num_dict)
        self.assertAlmostEqual(res['key1'], 0.8362480242006185)
        self.assertAlmostEqual(res['key2'], 0.6931471805599453)

    def test_compute_idf_weight_dict_4(self):
        num_dict = {'key1': 0.4, 'key2': 0.5}
        res = VectorUtil.compute_idf_weight_dict(2, num_dict)
        self.assertAlmostEqual(res['key1'], 0.7621400520468967)
        self.assertAlmostEqual(res['key2'], 0.6931471805599453)

    def test_compute_idf_weight_dict_5(self):
        num_dict = {'key1': 0.5, 'key2': 0.5}
        res = VectorUtil.compute_idf_weight_dict(2, num_dict)
        self.assertAlmostEqual(res['key1'], 0.6931471805599453)
        self.assertAlmostEqual(res['key2'], 0.6931471805599453)


class VectorUtilTest(unittest.TestCase):
    def test_vectorutil(self):
        vector_1 = np.array([1, 1])
        vector_2 = np.array([1, 0])
        similarity = VectorUtil.similarity(vector_1, vector_2)
        self.assertAlmostEqual(similarity, 0.7071067811865475)

        vector1 = np.array([1, 1])
        vectors_all = [np.array([1, 0]), np.array([1, 1])]
        similarities = VectorUtil.cosine_similarities(vector1, vectors_all)
        res = [0.7071067811865475, 1.0]
        for index, item in enumerate(similarities):
            self.assertAlmostEqual(item, res[index])

        vector_list1 = [np.array([1, 0]), np.array([0, 1])]
        vector_list2 = [np.array([0, 0]), np.array([1, 1])]
        similarity = VectorUtil.n_similarity(vector_list1, vector_list2)
        self.assertAlmostEqual(similarity, 1.0)

        num_dict = {'key1': 0.1, 'key2': 0.5}
        res = VectorUtil.compute_idf_weight_dict(2, num_dict)
        self.assertAlmostEqual(res['key1'], 1.0033021088637848)
        self.assertAlmostEqual(res['key2'], 0.6931471805599453)
