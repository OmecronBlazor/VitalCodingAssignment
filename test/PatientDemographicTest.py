import sys
import unittest

sys.path.append('../src')

from PatientDemographic import PatientInfoList


class PatientDemographicTest(unittest.TestCase):
    def __PatientDemographicHelper(self, _input, actual, expected):

        result = PatientInfoList()
        for line in _input:
            result.add(line)

        assert_flag = True
        if result.len() != len(actual):
            assert_flag = False

        for patient_key in actual:
            if result.exists(patient_key):
                if len(actual[patient_key]) != len(result.get(patient_key)):
                    assert_flag = False
            else:
                assert_flag = False

        self.assertEqual(assert_flag, expected)
        result.clear()

    def test_1(self):
        _input = []
        actual = {}
        self.__PatientDemographicHelper(_input, actual, True)

    def test_2(self):
        _input = ["PID1,POND^AMY,F,19890224", "PID2,WILLIAMS^RORY,F,19881102"]
        actual = {"pond^amy": ["PID1,POND^AMY,F,19890224"], "williams^rory": ["PID2,WILLIAMS^RORY,F,19881102"]}
        self.__PatientDemographicHelper(_input, actual, True)

    def test_3(self):
        _input = ["PID1,POND^AMY,F,19890224", "PID2,WILLIAMS^RORY,F,19881102", "PID3,POND^AMY,F,19890224"]
        actual = {"pond^amy": ["PID1,POND^AMY,F,19890224", "PID3,POND^AMY,F,19890224"],
                  "williams^rory": ["PID2,WILLIAMS^RORY,F,19881102"]}
        self.__PatientDemographicHelper(_input, actual, True)

    def test_4(self):
        _input = ["PID1,POND^AMY,F,19890224", "PID2,WILLIAMS^RORY,F,19881102", "PID3,pond^amy,F,19890224"]
        actual = {"pond^amy": ["PID1,POND^AMY,F,19890224", "PID3,pond^amy,F,19890224"],
                  "williams^rory": ["PID2,WILLIAMS^RORY,F,19881102"]}
        self.__PatientDemographicHelper(_input, actual, True)

    def test_5(self):
        _input = ["PID1,POND^AMY,F,19890224", "PID2,WILLIAMS^RORY,F,19881102", "PID3,POND^amy^MARIA,F,19890224"]
        actual = {"pond^amy": ["PID1,POND^AMY,F,19890224", "PID3,POND^amy^MARIA,F,19890224"],
                  "williams^rory": ["PID2,WILLIAMS^RORY,F,19881102"]}
        self.__PatientDemographicHelper(_input, actual, True)

    def test_6(self):
        _input = ["PID1,POND^AMY,F,19890224", "PID2,WILLIAMS^RORY,F,19881102", "PID3,POND^AMARIA,F,19890224"]
        actual = {"pond^amy": ["PID1,POND^AMY,F,19890224"],
                  "williams^rory": ["PID2,WILLIAMS^RORY,F,19881102"],
                  "pond^amaria": ["PID3,POND^AMARIA,F,19890224"]}
        self.__PatientDemographicHelper(_input, actual, True)

    def test_7(self):
        _input = ["PID1,POND^AMY,F,19890224", "PID2,WILLIAMS^RORY,F,19881102", "PID3,PONDER^AMY,F,19890224"]
        actual = {"pond^amy": ["PID1,POND^AMY,F,19890224"],
                  "williams^rory": ["PID2,WILLIAMS^RORY,F,19881102"],
                  "ponder^amy": ["PID3,PONDER^AMY,F,19890224"]}
        self.__PatientDemographicHelper(_input, actual, True)
