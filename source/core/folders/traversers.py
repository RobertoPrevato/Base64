import os
import re
from os import listdir
from os.path import isfile, join, isdir

class Traverser:
    def __init__(self, ext):
        self.ext = ext

    def include(self, f):
        p = re.compile("\.{}$".format(self.ext), re.IGNORECASE)
        return p.search(f) is not None

    def get_files(self, path):
        a = [path + os.sep + f for f in listdir(path) if (isfile(join(path, f)) and self.include(f))]
        dr = [f for f in listdir(path) if isdir(join(path, f))]
        for b in dr:
            a = a + self.get_files(path + os.sep + b)
        return a

class PicsTraverser(Traverser):
    def __init__(self):
        self.ext = re.compile("\.jpg$|\.jpeg$|\.jpe$|\.png$|\.gif|\.svg$", re.IGNORECASE)
        
    def include(self, f):
        return self.ext.search(f) is not None
