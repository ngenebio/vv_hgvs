import unittest

import hgvs.variant

class Test_Variant(unittest.TestCase):
    def test_variant(self):
        var = hgvs.variant.Variant(seqref='AC',type='B',posedits='1234DE>FG')
        self.assertEqual( str(var) , 'AC:B.1234DE>FG' )

if __name__ == '__main__':
    unittest.main()
