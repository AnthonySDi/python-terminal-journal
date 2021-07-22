import sys
import logging
import datetime
#from .classmodule import MyClass
#from .funcmodule import my_function
logging.basicConfig(filename='develop.log', encoding='utf-8', level=logging.DEBUG)

def main():
    '''
    - Main is evoked by the keyword 'pilot' at the command line. The keyword and anything after it will be space delimited and stored in an array, which can be accessed by calling sys.argv[1:]

    KEYWORD: pilot

    Params:
        am - starts morning journal
        pm - starts night journal
    '''
    logging.info('Keyword evoked and Main start')
    
    timeDifference = ''
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
    # my_function('hello world')
    
    print(args[0])
    journal(args[0])
    logging.info('Main function ended')

def journal(tod):
    '''
    calls helper functions morning, and evening

    @params
    tod string; will represent Time of Day, am or pm

    '''
    logging.info('Journal function started')
    if tod != 'am':
        morning(tod)
    else:
        evening()
    logging.info('Journal function ended')

def morning(tod):
    '''
    # Morning 
    - I am grateful for: (three lines) 0
    - What would make today great? (three lines) 6
    - Daily affirmations 7
    - my goal 8
    - My targets (3) 9
    - Schedule 10
    '''
    logging.info('Morning function started')
    grateful = getAnswers(0, 3)
    print(grateful)
    #great = getAnswers(6, 3)
    #affirm = getAnswers(7, 3) # only three affirmations or ?
    #goal = getAnswers(8, 1)
    #targets = getAnswers(9, 3)
    #schedule = getAnswers(10, 1)
    logging.info('Morning function ended')

def evening():
    '''
    # Night
    - 3 amazing things that happened today 2
    - How could I have made today even better? (three lines) 3
    - Lessons learned (3) 4
    - wins(3) 5
    - did you hit your goal? 11
    - did you hit your target 12
    - I am grateful for: (three lines) 1
    '''
    logging.info('Evening function started')
    amazing = getAnswers(2, 3)
    better = getAnswers(3, 3)
    learned = getAnswers(4, 3)
    wins = getAnswers(5, 3)
    goal = getAnswers(11, 1)
    targetCheck = getAnswers(12, 3) #take three lines or just long format typing?
    grateful = getAnswers(1, 3)
    logging.info('Evening function ended')

def getAnswers(quest,asknum):

    response = []
    for i in range(0,asknum):
        response.append(raw_input(questions(quest)))

    return response

def questions(quest):
    
    switch={
        0:'What are you grateful for this morning gorgeous?',
        1:'What are you grateful for this evening gorgeous?',
        2:'Tell me about something today that was amazing!',
        3:'How could I have made today better?',
        4:'List a Lesson Learned today.',
        5:'Name a victory from today!',
        6:'What would make today great?',
        7:'Affirm yourself now!',
        8:'what is your goal today?',
        9:'What is a target today?',
        10:'how do you plan on spending your day?',
        11:'Did you hit your goal today?',
        12:'Did you hit your targets today?'
        }
    return switcher.get(quest,"error")

if __name__ == '__main__':
    main()