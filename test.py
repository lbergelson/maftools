from maf_utils import *

m = Maf("test.maf")
m.addAnnotator("ends in n", lambda x: x['sample'].endswith('n'))
m.addFilter(lambda x: x["gender"] in ["male","female"])
m.write("new_test.maf")
