from linear import LinearEquations

class TestMakerLibrary( object ):
    def __init__( self ):
        self.linear_equations = LinearEquations()
        self.question_categories = [
                                        self.linear_equations.getCategoryName(),
                                   ]
    def getAllQuestionCategories( self ):
        return self.question_categories

    def getLinearQuestionList( self ):
        return self.linear_equations.get_question_names()
