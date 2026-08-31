import unittest
from pathlib import Path
class ContractPolicyTests(unittest.TestCase):
    def test_contract_contains_required_enums_and_bounds(self):
        s=Path('contracts/endline.py').read_text()
        for x in ('ACTIVE','DEPRECATED','SECURITY_ONLY','END_OF_LIFE','REPLACED','UNKNOWN','run_nondet_unsafe','source_version'):
            self.assertIn(x,s)
    def test_specs_are_present(self):
        self.assertTrue(Path('contracts/endline.py').exists())
if __name__=='__main__': unittest.main()
