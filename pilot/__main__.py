import sys
import logging
import datetime
#from .classmodule import MyClass
#from .funcmodule import my_function

def main():
    start = datetime.datetime.now()
    stop = ''
    timeDifference = ''
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
    # my_function('hello world')
    
    print(args[0])
#    if (args[0].lower() == 'read'):
#        stop = readAction(args)
#    elif (args[0].lower() == 'write'):
#        stop = writeAction(args)
#    else:
#        print('Command not found read or write will be accepted')

#    timeDifference = stop - start

#    print("Total time took ")
#    print(timeDifference)

def readAction(args):
    print("Read Action Function accessed")
    fileName = open("stock.txt", "r")
    sentence = fileName.readline()
    print(sentence)
    count = 0
    index = 0
    print("**Index is ")
    print(index)
    print('*****************')
    print("**len(sentence) is ")
    print(len(sentence))
    print('*************')
    while index < len(sentence):
        index = sentence.find('imperdiet', index)
        
        if index != -1:
            print('imperdiet', index)
            count += 1
            index += 9
        else:
            break

    fileName.close()
    return datetime.datetime.now()

    
def writeAction(arges):
    fileName = open("stock.txt", "r")

    fileName.close()
    return datetime.datetime.now()

if __name__ == '__main__':
    main()