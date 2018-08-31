from linear import LinearEquations
from quadratic import QuadraticEquations

class MathTestMaker( object ):
    def __init__( self ):
        self.linear_equations = LinearEquations()
        self.quadratic_equations = QuadraticEquations()
        self.question_categories = [
                                        self.linear_equations.getCategoryName(),
                                        self.quadratic_equations.getCategoryName(),
                                   ]
    def getAllQuestionCategories( self ):
        return self.question_categories

    def getLinearQuestionList( self ):
        return self.linear_equations.get_question_names()

    def getQuadraticQuestionList( self ):
        return self.quadratic_equations.get_question_names()

    
    def getSelectedQuestions( self, question_requests ):
        """
        selected_questions_with_options - a list of the form:
            [ 
                {
                  category_name: xxx,
                          selected_question: xxx,
                  count: xxx,
                  points: xxx
                }
        return a list of the form 
            [
                {     
                    category_name: xxx
                    question: question json from library
                    points : points
                }
            ]
                
        """
        ret = []
        for question_request in question_requests:
            if(question_request[ "question_category" ] == self.linear_equations.getCategoryName()):
                for question_instance in range( question_request[ "count" ] ):
                    ret_json = {
                            "category_name": question_request[ "question_category" ],
                            "points": question_request[ "points" ],
                            "question": self.linear_equations.get_question( question_request[ "selected_question" ] ),
                           }
                    ret.append( ret_json )
            elif(question_request[ "question_category" ] == self.quadratic_equations.getCategoryName()):
                for question_instance in range( question_request[ "count" ] ):
                    ret_json = {
                            "category_name": question_request[ "question_category" ],
                            "points": question_request[ "points" ],
                            "question": self.quadratic_equations.get_question( question_request[ "selected_question" ] ),
                           }
                    ret.append( ret_json )
            else:
                print( question_request[ "question_category" ] )
                assert(false) # this should be handled otherwise. Prob not bring down the application.

        return ret
