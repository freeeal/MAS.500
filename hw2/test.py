import unittest

class MediaCloudTest(unittest.TestCase):

    def setUp(self):
        self.response = ElectionResults('election_results_test_file.csv')

    def testLoad(self):
        self.results.load()
        assert self.results is not None
        assert self.results.file is not None
        assert len(self.results.all_lines) > 0

    def testStateCount(self):
        self.results.load()
        state_count = self.results.state_count()
        assert state_count==2

    def testStates(self):
        self.results.load()
        names = self.results.states()
        assert len(names)==2
        assert names[0]=='Alaska'
        assert names[1]=='Alabama'

# if this file is run directly, run the tests
if __name__ == "__main__":
    unittest.main()
