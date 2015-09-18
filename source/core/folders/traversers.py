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

class JsTraverser(Traverser):
    def __init__(self):
        self.ext = "js"
        
    def include(self, f):
        p = re.compile("\.{}$".format(self.ext), re.IGNORECASE)
        return p.search(f) is not None and not "main.built.js" in f.lower()

class TxtTraverser(Traverser):
    def __init__(self):
        self.ext = "txt"
        
    def include(self, f):
        p = re.compile("\.txt$", re.IGNORECASE)
        return p.search(f) is not None

class CsvTraverser(Traverser):
    def __init__(self):
        self.ext = "csv"

    def include(self, f):
        p = re.compile("\.csv$", re.IGNORECASE)
        return p.search(f) is not None

class HtmlTraverser(Traverser):
    def __init__(self):
        self.ext = "html"

    def include(self, f):
        p = re.compile("\.html$|\.htm$", re.IGNORECASE)
        return p.search(f) is not None

class HbsTraverser(Traverser):
    def __init__(self):
        self.ext = "hbs"

    def include(self, f):
        p = re.compile("\.hbs", re.IGNORECASE)
        return p.search(f) is not None

class PicsTraverser(Traverser):
    def __init__(self):
        self.ext = ";".join(['jpg', 'jpeg', 'jpe', 'png'])
        
    def include(self, f):
        p = re.compile("\.jpg$|\.jpeg$|\.jpe$|\.png$|\.gif$", re.IGNORECASE)
        return p.search(f) is not None
        
