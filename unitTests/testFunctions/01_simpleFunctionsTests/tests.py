import unittest
import functionsToTest as funcs

class Tester(unittest.TestCase):
    def test_add_ten(self):
        self.assertEqual(funcs.add_ten(10), 20)
        self.assertEqual(funcs.add_ten(-10),0)

    def test_is_valid_midi_value(self):
        self.assertTrue(funcs.is_valid_midi_value(0))
        self.assertTrue(funcs.is_valid_midi_value(60))
        self.assertTrue(funcs.is_valid_midi_value(127))
        self.assertFalse(funcs.is_valid_midi_value(-1))
        self.assertFalse(funcs.is_valid_midi_value(128))
        self.assertFalse(funcs.is_valid_midi_value(9999))

if __name__ == '__main__':
    unittest.main()
