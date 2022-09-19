def get_formatted_name(first, last):
    '''Generate a neatly formatted full name.'''
    full_name = first + ' ' + last
    return full_name.title()

def get_formatted_name2(first, middle, last):
    '''Generate a neatly formatted full name.'''
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else: 
        full_name = first + ' ' + last
    return full_name.title()

def get_formatted_city(city, country, population):
    if population:
        formatted_city = city + ', ' + country + ', Population = ' + str(population)
    else: 
        formatted_city = city + ', ' + country
    return formatted_city.title()

class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []
    def show_questions(self):
        print(self.question)
    def store_responses(self, new_response):
        self.responses.append(new_response)
    def show_results(self):
        print('Survey results:')
        for response in self.responses:
            print('- ' + response)
        
