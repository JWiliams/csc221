import random
   # The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
    quizFile = open(f'capitalsquiz{quizNum+1}.txt', 'w')
    answerKey = open(f'captialquiz_answers{quizNum+1}.txt', 'w')
    # Writing Headers
    quizFile.write('Name:\n\nDate:\n\nPeriod\n\n')
    quizFile.write(('' *20) + f'State Capitals Quiz (Form{quizNum+1})')
    #This is to give spacing between header and questions
    quizFile.write('\n\n')
    
    #shuffle the order of the states
    states=list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers=list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongChoices = random.sample(wrongAnswers, 3)
        answerOptions = wrongChoices + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write(f'{questionNum +1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"   {'ABCD'[i]}. { answerOptions[i]}\n")
        quizFile.write('\n')

        answerKey.write(f"{questionNum+1}.{'ABCD'[answerOptions.index(correctAnswer)]}")
        answerKey.write('\n')
        #quizFile.close()
        #answerKey.close()

