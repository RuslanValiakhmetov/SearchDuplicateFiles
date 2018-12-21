import unittest
from file_search import SearchByName, SearchByContent

DIRECTORY_LIST = ["test/testfolder1",
                  "test/testfolder2"]

TEST_DUPLICATE_LIST_BY_NAME = ['test/testfolder1/testfile2',
                               'test/testfolder1/subtestfolder1/testfile2',
                               'test/testfolder2/testfile2',
                               'test/testfolder1/testfile1',
                               'test/testfolder2/testfile1',
                               'test/testfolder1/subtestfolder2/testfile123',
                               'test/testfolder2/subtestfolder1/testfile123']

TEST_DUPLICATE_LIST_BY_CONTENT = ['test/testfolder1/testfile2',
                                  'test/testfolder1/subtestfolder1/testfile11',
                                  'test/testfolder2/subtestfolder1/testfile123']


class TestFileSearch(unittest.TestCase):
    def test_do_search_by_name(self):
        searcher_by_name = SearchByName()
        file_dict_lists = [searcher_by_name.get_all_items(directory) for directory in DIRECTORY_LIST]
        duplicate_list = searcher_by_name.do_search(file_dict_lists)

        self.assertListEqual(duplicate_list, TEST_DUPLICATE_LIST_BY_NAME)

    def test_do_search_by_content(self):
        searcher_by_content = SearchByContent()
        file_dict_lists = [searcher_by_content.get_all_items(directory) for directory in DIRECTORY_LIST]
        duplicate_list = searcher_by_content.do_search(file_dict_lists)

        self.assertListEqual(duplicate_list, TEST_DUPLICATE_LIST_BY_CONTENT)


if __name__ == "__main__":
    unittest.main()
