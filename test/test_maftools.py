from unittest import TestCase
from maftools.maftools import *
import os
    

class TestMafTools(TestCase):
    
    #thanks to Ned Batcheldar 
    #http://stackoverflow.com/questions/3942820/how-to-do-unit-testing-of-functions-writing-files-using-python-unittest
    def assertMultiLineEqual(self, first, second, msg=None):
        """Assert that two multi-line strings are equal.

        If they aren't, show a nice diff.

        """
        self.assertTrue(isinstance(first, str),
                'First argument is not a string')
        self.assertTrue(isinstance(second, str),
                'Second argument is not a string')

        if first != second:
            message = ''.join(difflib.ndiff(first.splitlines(True),
                                                second.splitlines(True)))
            if msg:
                message += " : " + msg
            self.fail("Multi-line strings are unequal:\n" + message)


    def test_read_write_no_filter(self):
        infile = "test/testdata/test.maf"
        outfile = "test/testoutput/no_filter_no_add.maf"

        assert(os.path.exists(infile))
        m = Maf(infile)
        m.write(outfile)
        assert(os.path.exists(outfile))
        
        self.assertMultiLineEqual("".join(open(infile).readlines()), "".join(open(outfile).readlines()))
        
            
    
