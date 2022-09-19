
import unittest
from BookPracticepg222 import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    '''Tests for the class AnonymousSurvey'''
    def setUp(self):
        '''Create a survey and a set od responses for use in all test methods.'''
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Filipino']
    def test_store_single_responses(self):
        '''Test that a single response is stored properly.'''
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_responses(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
unittest.main()