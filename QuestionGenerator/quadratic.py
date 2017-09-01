import utility
from fractions import Fraction
from returnVerifier import returnVerifier

class QuadraticEquations(object):
    
    def __init__(self):
        self.category_name = "quadratic equations"
        import inspect 
        self.all_methods = inspect.getmembers(self, predicate=inspect.ismethod)
        self.questions = dict([(function_tuple[1]()["question_name"], function_tuple[1])for function_tuple in self.all_methods if function_tuple[0][0:2] == "EQ"])

    def get_all_methods(self):
        return self.all_methods

    def get_available_questions(self):
        return list(self.questions)
    
    def get_questions(self, question_count_pairs):
        """
        @param question_count_pairs:
            A list of 2-tuples (question, count). e.g.
            [("find_integral_x_intercept_non_zero_slope_standard_form", 2),
             ("find_decimal_x_intercept_non_zero_slope_standard_form", 1)]
        @return a list of question dictionaries.
            {"name": name, "question_text": question_text, "solution": solution}
        """
        pass

        @returnVerifier
        def EQ_find_single_x_int_open_up_standard_form( self ):
            pass

        @returnVerifier
        def EQ_find_two_x_int_open_up_standard_form( self ):
            pass

        @returnVerifier
        def EQ_find_no_x_int_open_up_standard_form( self ):
            pass

        @returnVerifier
        def EQ_find_single_x_int_open_down_standard_form( self ):
            pass

        @returnVerifier
        def EQ_find_two_x_int_open_down_standard_form( self ):
            pass

        @returnVerifier
        def EQ_find_no_x_int_open_down_standard_form( self ):
            pass

        @returnVerifier
        def EQ_find_single_x_int_open_up_vertex_form( self ):
            pass

        @returnVerifier
        def EQ_find_two_x_int_open_up_vertex_form( self ):
            pass

        @returnVerifier
        def EQ_find_no_x_int_open_up_vertex_form( self ):
            pass

        @returnVerifier
        def EQ_find_single_x_int_open_down_vertex_form( self ):
            pass

        @returnVerifier
        def EQ_find_two_x_int_open_down_vertex_form( self ):
            pass

        @returnVerifier
        def EQ_find_no_x_int_open_down_vertex_form( self ):
            pass

        @returnVerifier
        def EQ_convert_vertex_form_to_standard_form( self ):
            pass

        @returnVerifier
        def EQ_convert_standard_form_to_vertex_form( self ):
            pass
