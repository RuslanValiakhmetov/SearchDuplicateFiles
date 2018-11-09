class Searcher:
    def __init__(self, searcher):
        self._searcher = searcher
        self._duplicate_list = []

    def duplicate_search(self, dirs):
        self._duplicate_list = self._searcher.search_duplicate(dirs)

    def print_results(self):
        if self._duplicate_list:
            print("Duplicate files:")
            for item in self._duplicate_list:
                print(item)
        else:
            print("No duplicate files found!\n")
