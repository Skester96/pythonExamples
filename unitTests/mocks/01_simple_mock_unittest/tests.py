import playSound as ps

import unittest
import unittest.mock as mock

class Sample():
    def play():
        print("played")

class playSound_test(unittest.TestCase):
    @mock.patch('playSound.sa')
    def test_ps(self, mock_sa):
        # set up the mock
        mock_sa.WaveObject.from_wave_file.return_Value = Sample()
        ps.play_the_sample("any path")
        mock_sa.WaveObject.from_wave_file.assert_called_with("any path")

if __name__ == '__main__':
    unittest.main()
