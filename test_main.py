import unittest
import main 

class TddTest(unittest.TestCase):

    aa = 0
    bb = 0
    result = 0

    # 매 테스트 메소드 실행 전 동작
    def setUp(self):
        self.aa = 10
        self.bb = 20

    def testAdd(self):
        self.result = main.add(self.aa, self.bb)

        # 결과 값이 일치 여부 확인
        self.assertEqual(self.result, 31)

    def testSubstract(self):
        self.result = main.substract(self.aa, self.bb)

        if self.result > 10:
            boolval = True
        else:
            boolval = False

        # 결과 값이 True 여부 확인
        self.assertTrue(boolval)

    def testDivision(self):
        # 결과 값이 ZeroDivisionError 예외 발생 여부 확인
        self.assertRaises(ZeroDivisionError, main.division, 4, 1)

    def testMultiply(self):
        nonechk = True

        self.result = main.multiply(10, 9)

        if self.result > 100:
            nonechk = None

        # 결과 값이 None 여부 확인
        self.assertIsNone(nonechk)

    # 매 테스트 메소드 실행 후 동작
    def tearDown(self):
        print(' 결과 값 : ' + str(self.result))

if __name__ == '__main__':
    unittest.main()