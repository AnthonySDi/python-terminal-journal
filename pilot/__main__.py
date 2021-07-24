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
    args = sys.argv[1:]
    logging.debug('First argument received {} and number of arguments {}'.format(args, len(args)))

    for arg in args:
        logging.debug('Command(s) received :: {}'.format(arg))
    # my_function('hello world')
    
    journal(args[0].lower())
    logging.info('Main function ended')

def journal(tod):
    '''
    calls helper functions morning, and evening

    @params
    tod string; will represent Time of Day, am or pm

    '''
    logging.info('Journal function started')
    logging.debug('Journal function received argument: {}'.format(tod))
    if tod != 'am':
        evening()
    else:
        morning(tod)
    logging.info('Journal function ended')

def morning(tod):
    '''
    # Morning uses helper function getAnswers to ask morning questions for journal entries. 
    #
    # @params tod: string; 
    # Below is the questions for morning and their corresponding numbers?
    - I am grateful for: (three lines) 0
    - What would make today great? (three lines) 6
    - Daily affirmations 7
    - my goal 8
    - My targets (3) 9
    - Schedule 10
    '''
    logging.info('Morning function started')
    logging.debug('morning function received argument: {}'.format(tod))
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
    # Night uses helper function to getAnswers to ask Evening questions and collect answers for journal entries
    #
    # Below are the questions for the Evening and their corresponding numbers. 
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
    '''
    # getAnswers is a helper function that collects responses to journaling questions. Uses helper function questions to get the 
    # questions based on the parameters received. 
    # 
    # @params quest: int; represents the questions key in the dictionary in the helper function
    # @params asknum: int; the number of times the question will be asked. 
    '''
    logging.info('getAnswers function started')
    logging.debug('getAnswers function received argument: quest = {}; asknum = {}'.format(quest,asknum))
    response = []
    for i in range(0,asknum):
        response.append(input(questions(quest)))

    logging.info('getAnswers function ended')
    return response

def questions(quest):
    '''
    # is a helper function to getAnswers and returns a question based on the arguement received. 
    #
    # @params quest: int; is the key in the dictionary to a question
    # @returns: string, which is the question to be asked. 
    '''
    logging.info('questions function started')
    logging.debug('questions function received argument: {}'.format(quest))
    switch={
        0:'What are you grateful for this morning gorgeous? ',
        1:'What are you grateful for this evening gorgeous? ',
        2:'Tell me about something today that was amazing! ',
        3:'How could I have made today better? ',
        4:'List a Lesson Learned today. ',
        5:'Name a victory from today! ',
        6:'What would make today great? ',
        7:'Affirm yourself now! ',
        8:'what is your goal today? ',
        9:'What is a target today? ',
        10:'how do you plan on spending your day? ',
        11:'Did you hit your goal today? ',
        12:'Did you hit your targets today? '
        }
    question = switch.get(quest,"error")
    if question == 'error':
        logging.error('ERROR: Switch does not contain question. Received question number:: {}'.format(quest))

    logging.debug('questions function will return this result: {}'.format(question))
    logging.info('questions function ended')
    return question

if __name__ == '__main__':
    main()