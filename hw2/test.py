# Verify that we can make a call to the MediaCloud API successfully
import unittest
from main import MediaCloud

# source: https://github.com/mitmedialab/MediaCloud-API-Client/blob/master/mediacloud/test/apitest.py
class MediaCloudTest(unittest.TestCase):

    def test_handle_request(self):
        self.response = MediaCloud().handle_request(('Trump'), (2016, 9, 1), (2016, 9, 30))
        assert self.response['count'] > 0

# if this file is run directly, run the tests
if __name__ == "__main__":
    unittest.main()
