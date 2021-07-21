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
    logging.info('Main function ended')

def journal(tod):
    '''
    calls helper functions morning, and evening

    @params
    tod string; will represent Time of Day, am or pm

    '''
    logging.info('Journal function started')
    if tod != 'am':
        morning()
    else:
        evening()
    logging.info('Journal function ended')

def morning():
    '''
    # Morning 
    - I am grateful for: (three lines)
    - What would make today great? (three lines)
    - Daily affirmations
    - my goal
    - My targets (3)
    - Schedule
    '''
    logging.info('Morning function started')

    logging.info('Morning function ended')

def evening():
    '''
    # Night
    - 3 amazing things that happened today
    - How could I have made today even better? (three lines)
    - Lessons learned (3)
    - wins(3)
    - I am grateful for: (three lines)
    '''
    logging.info('Evening function started')

    logging.info('Evening function ended')

def grateful(tod):
    '''
    asks user for three things they are grateful for, stores them in an array which is what it returns
    '''
    logging.info('Grateful function started')
    things = []

    while len(things) < 3:
        if tod != 'am':
            things.append(raw_input('What are you grateful for this morning gorgeous?'))
        else:
            things.append(raw_input('What are you grateful for this evening gorgeous?'))

    logging.info('Grateful function ended')

if __name__ == '__main__':
    main()