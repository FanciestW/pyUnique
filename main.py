import sys
import collections

def main():
    """ Main function """
    try:
        filepath = sys.argv[1]
        open_file = open(filepath, 'r')

        string_list = open_file.read().splitlines()
        
        string_collection = collections.Counter(string_list)
        for entry in string_collection:
            if string_collection[entry] == 1: 
                print(entry)

    except IndexError:
        printUsage()

    except:
        print("Exception: ", sys.exc_info()[0])
        raise


def printUsage():
    print("Usage: cmd [Input filename]")

main()
