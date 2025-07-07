import unittest
from fields.fieldA import DEMO as DEMO_A
from fields.fieldB import DEMO as DEMO_B
from fields.fieldC import DEMO as DEMO_C
from fields.fieldD import DEMO as DEMO_D
from fields.fieldE import DEMO as DEMO_E
from fields.fieldF import DEMO as DEMO_F
from fields.fieldG import DEMO as DEMO_G
from fields.field_a import FieldA
from fields.field_b import FieldB
from fields.field_c import FieldC
from fields.field_d import FieldD
from fields.field_e import FieldE
from fields.field_f import FieldF
from fields.field_g import FieldG

class TestFields(unittest.TestCase):
    def test_fieldA(self):
        self.assertIsInstance(DEMO_A, dict)
        self.assertIsInstance(FieldA.generate_test()["prompt"], str)
        self.assertIsInstance(FieldA.audit_schema(), dict)
    def test_fieldB(self):
        self.assertIsInstance(DEMO_B, dict)
        self.assertIsInstance(FieldB.generate_test()["prompt"], str)
        self.assertIsInstance(FieldB.audit_schema(), dict)
    def test_fieldC(self):
        self.assertIsInstance(DEMO_C, dict)
        self.assertIsInstance(FieldC.generate_test()["prompt"], str)
        self.assertIsInstance(FieldC.audit_schema(), dict)
    def test_fieldD(self):
        self.assertIsInstance(DEMO_D, dict)
        self.assertIsInstance(FieldD.generate_test()["prompt"], str)
        self.assertIsInstance(FieldD.audit_schema(), dict)
    def test_fieldE(self):
        self.assertIsInstance(DEMO_E, dict)
        self.assertIsInstance(FieldE.generate_test()["prompt"], str)
        self.assertIsInstance(FieldE.audit_schema(), dict)
    def test_fieldF(self):
        self.assertIsInstance(DEMO_F, dict)
        self.assertIsInstance(FieldF.generate_test()["prompt"], str)
        self.assertIsInstance(FieldF.audit_schema(), dict)
    def test_fieldG(self):
        self.assertIsInstance(DEMO_G, dict)
        self.assertIsInstance(FieldG.generate_test()["prompt"], str)
        self.assertIsInstance(FieldG.audit_schema(), dict)

if __name__ == '__main__':
    unittest.main() 