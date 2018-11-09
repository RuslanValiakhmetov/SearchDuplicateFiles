import os
from sys import argv, exit
from searcher import Searcher
from file_search import SearchByName, SearchByContent


class Main:
    @staticmethod
    def print_with_help(fault_string):
        print(fault_string + "Parameters:\n"
              "1. 1-st directory\n"
              "2. 2-nd directory\n"
              "3. -n - search by name\n"
              "   -c - search by content\n")

    @staticmethod
    def main(args):
        try:
            if len(args) != 3:
                Main.print_with_help("Invalid number of parameters.\n")
                return 1

            dirs = args[:-1]
            for directory in dirs:
                if not os.path.isdir(directory):
                    Main.print_with_help("'{}' is not directory.\n".format(directory))
                    return 1
                elif not len(os.listdir(directory)):
                    print("'{}' directory is empty.\n".format(directory))
                    return 1

            search_type = args[-1]

            # using of strategy pattern
            if search_type == '-n':
                searcher = Searcher(SearchByName())
            elif search_type == '-c':
                searcher = Searcher(SearchByContent())
            else:
                Main.print_with_help("Invalid parameter.\n")
                return 1

            searcher.duplicate_search(dirs)
            searcher.print_results()

        except Exception as exp:
            print("Exception: " + str(exp))
            return -1


if __name__ == "__main__":
    exit(Main.main(argv[1:]))
