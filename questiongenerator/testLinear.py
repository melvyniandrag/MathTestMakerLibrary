import questiongenerator.linear as linear

le = linear.LinearEquations()
ret = le.getQuestion( list(le.getQuestionNames())[0], 1, 1 )
print( ret )
