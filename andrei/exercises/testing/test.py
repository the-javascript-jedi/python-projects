import unittest
# main is the file name i.e main.py
import main

# to run each file separately run  >python test.py
# to run all test files >python -m unittest
# to run all test files with comments >python -m unittest -v

# goal is to break the code
class TestMain(unittest.TestCase):
    # the setup code is run before each call on the
    def setUp(self):
        print("about to test a function")

    def test_do_stuff(self):
        '''test_do_stuff'''
        test_param=10
        result=main.do_stuff(test_param)
        self.assertEqual(result,15)

    # check if code accepts string
    # fix the code by adding try and catch block
    def test_do_stuff2(self):
        '''test_do_stuff2'''
        test_param='aaaa'
        result=main.do_stuff(test_param)
        self.assertIsInstance(result,ValueError)

    #  no test param
    def test_do_stuff3(self):
        '''test_do_stuff3'''
        test_param=None
        result=main.do_stuff(test_param)
        # we expect a value error when no value is passed
        # check if num is passed in code using if condition
        self.assertEqual(result,'please enter number')

    def test_do_stuff4(self):
        '''test_do_stuff4'''
        test_param=''
        result=main.do_stuff(test_param)
        # we expect a value error when no value is passed
        # check if num is passed in code using if condition
        self.assertEqual(result,'please enter number')

    # tear down - run after test is completed for each method
    def tearDown(self):
        print('cleaning up')


# if we add this below if condition we can run  python -m unittest
if __name__ == "__main__":
    unittest.main()