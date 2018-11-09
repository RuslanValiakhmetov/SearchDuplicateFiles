import os
import hashlib
from base_search import BaseSearch


class FileSearch(BaseSearch):
    def get_file_key(self, path):
        """
        Abstract method - must be implemented by subclasses.
        :param path: path to file
        :return: special key according to context of subclass object.
        """
        raise NotImplementedError()

    def get_all_items(self, directory):
        dict_files = {}
        for dir_name, subdirs, files in os.walk(directory):
            for item in files:
                path = os.path.join(dir_name, item)
                file_key = self.get_file_key(path)
                if file_key in dict_files:
                    dict_files[file_key].append(path)
                else:
                    dict_files[file_key] = [path]

        return dict_files

    def do_search(self, file_dict_lists):
        duplicate_list = []
        for key in file_dict_lists[0]:
            if key in file_dict_lists[1]:
                for dict in file_dict_lists:
                    duplicate_list.extend(dict.get(key))

        return duplicate_list


class SearchByName(FileSearch):
    def get_file_key(self, path):
        return os.path.basename(path)


class SearchByContent(FileSearch):
    def get_file_key(self, path):
        content_hash = 0
        try:
            with open(path, 'rb') as f:
                content_file = f.read()
            content_hash = hashlib.md5(content_file).hexdigest()
        except (IOError, ValueError) as exp:
            print("Can not get content of file - {}.".format(str(exp)))

        return content_hash
