import os
from trie import *

class FileTrie(object):

    def __init__(self):
        self.root_path = os.getcwd()
        self.files = self.read(self.root_path, self.root_path)
        self.trie = Trie()       
        for rel_path in self.files:
            self.trie.insert(rel_path)

    def read(self, folder, base=None):
        """return all files in folder"""
        folder_cache = {}

        # ressources
        for ressource in os.listdir(folder):
            current_path = os.path.join(folder, ressource)

            # files: add to cache as path: path
            if (os.path.isfile(current_path)):

                relative_path = os.path.relpath(current_path, self.root_path)
                folder_cache[relative_path] = current_path

            # recurse for lower directories
            elif (not ressource.startswith('.') and os.path.isdir(current_path)):
                folder_cache.update(self.read(current_path, os.path.join(base, current_path)))

        return folder_cache

    def get_all(self):
        return self.trie.get_all()

    def get_all_with_prefix(self, prefix):
        return self.trie.get_all_with_prefix(prefix)


if __name__ == '__main__':
    file_trie = FileTrie()
    for path in file_trie.get_all():
        print path

    prefix = "env/lib/python2.7/site-packages/wh"
    for path in file_trie.get_all_with_prefix(prefix):
        print path