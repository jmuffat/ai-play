import sys
import nlp_training
import mail_test

print("JMM toying around with AI...")

if len(sys.argv)>1:
    if sys.argv[1]=="nlpt":
        if len(sys.argv)>2:
            nlp_training.run_example(int(sys.argv[2]))
    elif sys.argv[1]=="mail":
        mail_test.run()
