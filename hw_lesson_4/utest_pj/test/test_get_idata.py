import unittest
from  utest_pj.get_idata import def_index2

class MyTestCase(unittest.TestCase):
    def test_def_index2(self):
        self.assertEqual(
            def_index2([4, 8, -5, 4, 9, 2]),2

        )
    def test_def_index3(self):
        self.assertEqual(
            def_index2([1]),0
        )



# if __name__ == '__main__':
#     unittest.main()


