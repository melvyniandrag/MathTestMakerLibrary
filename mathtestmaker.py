from QuestionGenerator.linear import LinearEquations

class MathTestMaker( object ):
    def __init__( self ):
        self.questionGenerators = { 
                "linear equations": LinearEquations(),
        }

    def getQuestionCategories( self ):
        return self.questionGenerators.keys()

    def getSelectedQuestions( self, Requests ):
        """
        @param Requests: A list of dictionaries with the following keys:
            * category: the category of question
            * name: the name of the question, a key into the question generator
            * numChoices: the total number of answer choices for the indicated question
            * points: the number of points to be assigned to the particular question
        @return: A list of questions ready to be processed by the LaTeX generator
        @return: A list of errors encountered during question generation
        """
        ret = []
        errors = []
        for r in Requests:
            if r["category"] in self.getQuestionCategories():
                generator = self.questionGenerators[ r["category"] ]
                try:
                    ret.append( generator.getQuestion( r["name"], r["numChoices"], r["points"] ) )
                except Exception as e:
                    errors.append( ( r["category"], r["name"], str(e) ) )
            else:
                errors.append( ( r["category"], None, "category '{}' is not implemented".format( r["category"] ) ) )
        return ret, errors
