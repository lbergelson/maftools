import csv
import sys
from itertools import ifilterfalse
import os

class Maf:
    
   def __init__(self, filename):
    self.filename = filename
    self.lines = 0
    self.comments = [] 
    self._setup_reader()
    self.fieldnames = self.reader.fieldnames
    self.filters = []
    self.annotators = {}
    
   def _check_and_store_comment(self, row):
        if self.lines % 1000 == 0:
            print "Read %d lines" % self.lines
        self.lines += 1
        if row.startswith('#'):
            self.comments.append( row )
            return True
        else:
            return False
   
   def _setup_reader(self):
        tmp = open(self.filename, "rb")
        tmp_no_comment = ifilterfalse( self._check_and_store_comment, tmp)
        self.reader = csv.DictReader(tmp_no_comment, delimiter='\t')

   def write(self, output_file):
        with open(output_file,"wb", 100000000) as output:
            wd = csv.DictWriter(output ,self.fieldnames,lineterminator=os.linesep, delimiter="\t")
            header_written = False
            for row in self.reader:
             if self.comments:
                 output.write("".join(self.comments))
                 self.comments = []
             if not header_written:
                wd.writeheader()
                header_written = True
             for a in self.annotators:
               f = self.annotators[a]
               row[a] = f(row)
             if len(self.filters) == 0 or all( [f(row) for f in self.filters ] ):
                wd.writerow(row)
            
   def addFilter(self, f):
        self.filters.append(f)
  
   def addAnnotator(self, column, f):
        self.annotators[column] = f
        self.fieldnames.append(column)
