import questiongenerator.quadratic as quadratic

qe = quadratic.QuadraticEquations()
ret = qe.getQuestion(list(qe.getQuestionNames())[0], 1, 1)
print(ret)
