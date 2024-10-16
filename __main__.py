import os
import sys
sys.path.insert(0, os.path.join( os.getcwd(), "common") ) # so common code is accessible by other folder

import nlp_training
import mail_test
import mail_classify

def nlpt(args):
    if (len(args)<1): raise Exception("nlpt missing example index")
    nlp_training.run_example(int(args[0]))   

#--------
print("JMM toying around with AI...")

args = sys.argv.copy()
script = args.pop(0) # pop first argument (script name)
if (len(args)<1):
    raise Exception("no arguments provided...")

cmd = args.pop(0)
match cmd:
    case "nlpt":    nlpt(args)
    case "mtst":    mail_test.run()
    case "mcls":    mail_classify.run()
    case _:         raise Exception("unknown command '{0}'".format(cmd))

