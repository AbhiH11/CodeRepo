import unittest
from Crash_course import survey

# class name_test_case(unittest.TestCase):

#     def test_first_last_name(self):

#         formatted_name = get_formatted_name('hari','anu')
#         self.assertEqual(formatted_name,'Hari Anu')

#     def test_first_middle_last_name(self):
#         formatted_name = get_formatted_name('hari','h','abhi')
#         # print(formatted_name)
#         self.assertEqual(formatted_name,'Hari Abhi H')
        
# if __name__ == '__main__':
#     unittest.main()

# class city_name(unittest.TestCase):
#     def test_city_name(self):
#         formatted_name = details('hyderabad','india')
#         self.assertEqual(formatted_name,'Hyderabad India')
    
#     def test_city_country_population(self):
#         formatted_name = details('hyderabad','india',50000)
#         self.assertEqual(formatted_name,'Hyderabad India 50000')
# if __name__ == '__main__':
#     unittest.main()

class verify_survey(unittest.TestCase):

    def test_survey(self):
        question = "What is your fav car brand?".title()
        my_survey = survey(question)

        my_survey.store_response("maruti")
        self.assertIn('maruti',my_survey.response)

    def test_survey_multiple_response(self):
        question = "what is your fav car brand?"
        my_survey = survey(question)
        responses = ['maruti','honda','Suzuki']
        for responce in responses:
            my_survey.store_response(responce)
        for responce in responses:
            self.assertIn(responce,my_survey.response)
            

if __name__ == '__main__':
    unittest.main()