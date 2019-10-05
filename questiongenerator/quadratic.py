import questiongenerator.utility as utility

class QuadraticEquations(object):
    def __init__(self):
        self.questions = dict( [
            ( "Factor the quadratic equation.",
              self.factorIntegers ),
        ] )
        self.codeName = "quadratic_equations"
        self.displayName = "Quadratic Equations"
        self.categoryInformation = "A set of questions involving quadratic equations."

    def getQuestionNames( self ):
        """
        @return: A list of all the questions available
        """
        return self.questions.keys() 

    def getQuestion(self, name, numChoices, points ):
        """
        TBD
        """
        return self.questions[name]( numChoices, points )

    def factorIntegers(self, numChoices, points):
        """
        TBD implement a factorization problem. Make sure that the
        factorization involves integers and is easy to perform.
        """
        a=1
        b=4
        c=4
        d={}
        problemStatement = "Factor the quadratic equation {}x^2 + {}x +{} = 0"
        d["problemStatement"] = problemStatement.format(a, b, c)
        d["correctAnswer"] = "(x+2)(x+2)"
        d["correctAnswerIdx"] = utility.getCorrectAnswerIndex(numChoices)
        d["wrongAnswers"] = utility.generateWrongAnswers(numChoices, 2, "ints") # todo implement  this
        d["points"] = points
        d["solution"] = [("learn to do this", "learn to do this")]
        return d
        


