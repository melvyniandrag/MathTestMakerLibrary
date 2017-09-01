"""
This file contains functions for generating linear equations and a class that
calls the can summarize the available functions and call a selected subset of the functions
based on user input.

As of June 21st 2017, the functions return a dictionary:
{
    "question_name":     "The name of the question", 
    "problem_statement": "The statement of the problem" ,
    "correct_answer":    The solution to the question ,
    "solution":          [
                            (equation1, "first step to solve the problem"),
                            (equation2, "second step to solve the problem"), 
                                ... ,
                            (equationN, "the final solution")
                         ]
}
"""
import random
import utility
import inspect
from fractions import Fraction
from returnVerifier import returnVerifier

class LinearEquations(object):

    def __init__(self):
        self.category_name = "linear equations"
        self.all_class_methods = inspect.getmembers(self, predicate=inspect.ismethod)
        self.question_function_list = [ ( func_name, func ) for ( func_name, func ) in self.all_class_methods if func_name[0:2] == "EQ" ] 
        self.question_names = [ func()["question_name"] for ( func_name, func ) in self.question_function_list ]
        self.index_list = [ func()["question_index"] for (func_name, func ) in self.question_function_list ]
        num_unique_indices = len( set( self.index_list ) )
        print(num_unique_indices)
        print(len(self.question_names))
        assert( len(self.question_names) == num_unique_indices ) 

    def getCategoryName( self ):
        return self.category_name

    def get_all_class_methods(self):
        return self.all_class_methods

    def get_question_names(self):
        return self.question_names

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
    def EQ_find_integral_x_intercept_non_zero_integer_slope_slope_intercept_form(self):
        m = 0
        while(m == 0):
            m = random.randint( -20, 20)
        multiplier = 0
        while(multiplier == 0):
            multiplier = random.randint(-10, 10)
        b = m * multiplier 
        x_intercept = -1 * b // m
        d = {}
        d["question_index"] = 1
        d["question_name"] = "Find the integer x intercept of a line in slope intercept form with nonzero slope."
        d["problem_statement"] = "Find the x intercept of $y = {}x + {}$.".format(m, b) 
        d["correct_answer"] = x_intercept
        d["solution"] = [
                          ("y = {}x + {}".format(m, b), "Find the x intercept."),
                          ("0 = {}x + {}".format(m, b), "Set y to zero."), 
                          ("0 - {} = {}x + {} - {}".format(b, m, b, b), "Subtract b from both sides."),
                          ("{} = {}x".format(-b, m), "Simplify."),
                          ("{} / {} = x".format(-b, m), "Divide both sides by m."),
                          ("{}".format(-b//m), "Simplify.")
                        ]
        return d   
    
    @returnVerifier
    def EQ_find_integral_x_intercept_non_zero_fraction_slope_slope_intercept_form(self):
        m_numerator = 0
        while (m_numerator == 0):
            m_numerator = random.randint( -30, 30)
        m_denominator = 0
        while ((m_denominator == 0) or (m_denominator == m_numerator)):
            m_denominator = random.randint(-30, 30)
        multiplier = 0
        while(multiplier == 0):
            multiplier = random.randint(-10, 10)
        b = m_numerator * multiplier 
        x_intercept = -1 * m_denominator * b // m_numerator
        d = {}
        d["question_index"] = 2
        d["question_name"] = "Find the integer x intercept of a line in slope intercept with nonzero fractional slope."
        d["problem_statement"] = "Find the x intercept of $y = \\frac{{{}}}{{{}}}x + {}$.".format(m_numerator, m_denominator, b) 
        d["correct_answer"] = x_intercept
        d["solution"] = [
                          ("y = \\frac{{{}}}{{{}}}x + {}".format(m_numerator, m_denominator, b), "Find the x intercept."),
                          ("0 = \\frac{{{}}}{{{}}}x + {}".format(m_numerator, m_denominator, b), "Set y to zero."), 
                          ("0 - {} = \\frac{{{}}}{{{}}}x + {} - {}".format(b, m_numerator, m_denominator, b, b), "Subtract b from both sides."),
                          ("{} = \\frac{{{}}}{{{}}}x ".format(-b, m_numerator, m_denominator), "Simplify."),
                          ("{} \\times \\frac{{{}}}{{{}}} = x".format(-b, m_denominator, m_numerator), "Divide both sides by m."),
                          ("{}".format(-1 * m_denominator * b // m_numerator), "Simplify.")
                        ]
        return d   
    
    @returnVerifier
    def EQ_find_integral_x_intercept_zero_slope_slope_intercept_form(self):
        b = 0
        while (b == 0):
            b = random.randint(-30, 30)
        d = {}
        d["question_index"] = 3
        d["question_name"] = "Find the integer x intercept of a line with zero slope." 
        d["problem_statement"] = "Find the y intercept of $y = {}$".format(b)
        d["correct_answer"] = None
        d["solution"] = [
                            ("y = {}".format(b), "Find the x intercept."),
                            ("None", "There is no x intercept."),
                        ]
        return d
    
    @returnVerifier
    def EQ_find_decimal_x_intercept_zero_slope_slope_intercept_form(self):
        precision = 2
        b = 0
        while (b == 0):
            b = round(random.uniform(-30, 30), precision)
        d = {}
        d["question_index"] = 4
        d["question_name"] = "Find the decimal x intercept of a line with zero slope." 
        d["problem_statement"] = "Find the y intercept of $y = {}$".format(b)
        d["correct_answer"] = None
        d["solution"] = [
                            ("y = {}".format(b), "Find the x intercept."),
                            ("None", "There is no x intercept."),
                        ]
        return d
    
    @returnVerifier
    def EQ_find_integral_x_intercept_infinite_slope_slope_intercept_form(self):
        x_intercept = random.randint(-40, 40)
        d = {}
        d["question_index"] = 5
        d["question_name"] = "Find the integer x intercept of a line with infinite slope." 
        d["problem_statement"] = "Find the x intercept of $x = {}$.".format(x_intercept) 
        d["correct_answer"] = x_intercept
        d["solution"] = [
                          ("x = {}".format(x_intercept), "This is a vertical line. The x intercept is {}".format(x_intercept)),
                        ]
        return d   
        
    
    @returnVerifier
    def EQ_find_decimal_x_intercept_infinite_slope_slope_intercept_form(self):
        precision = 2
        x_intercept = round(random.uniform(-40, 40), precision)
        d = {}
        d["question_index"] = 6
        d["question_name"] = "Find the decimal x intercept of a line with infinite slope." 
        d["problem_statement"] = "Find the x intercept of $x = {}$.".format(x_intercept) 
        d["correct_answer"] = x_intercept
        d["solution"] = [
                          ("x = {}".format(x_intercept), "This is a vertical line. The x intercept is {}".format(x_intercept)),
                        ]
        return d   
    
    @returnVerifier
    def EQ_find_integral_y_intercept_non_zero_slope_slope_intercept_form(self):
        m = 0
        while ( m == 0 ):
            m = random.randint(-30, 30)
        b = 0
        while ((b == m) or (b == 0)):
            b = random.randint(-30, 30)
        d = {}
        d["question_index"] = 7
        d["question_name"] = "Find the integer y intercept of a line in slope intercept form with nonzero slope." 
        d["problem_statement"] = "Find the y intercept of $y = {}x + {}$".format(m, b)
        d["correct_answer"] = b
        d["solution"] = [
                            ("y = {}x + {}".format(m, b), "Find the y intercept."),
                            ("{}".format(b), "The y intercept is the 'b' in slope intercept form."),
                        ]
        return d
    
    @returnVerifier
    def EQ_find_decimal_y_intercept_non_zero_slope_slope_intercept_form(self):
        precision = 2
        m = 0
        while ( m == 0 ):
            m = round(random.uniform(-30, 30), precision)
        b = 0
        while ((b == m) or (b == 0)):
            b = round(random.uniform(-30, 30), 2)
        d = {}
        d["question_index"] = 8
        d["question_name"] = "Find the decimal y intercept of a line in slope intercept form with nonzero slope." 
        d["problem_statement"] = "Find the y intercept of $y = {}x + {}$".format(m, b)
        d["correct_answer"] = b
        d["solution"] = [
                            ("y = {}x + {}".format(m, b), "Find the y intercept."),
                            ("{}".format(b), "The y intercept is the 'b' in slope intercept form."),
                        ]
        return d
    
    @returnVerifier
    def EQ_find_integral_y_intercept_zero_slope_slope_intercept_form(self):
        b = 0
        while (b == 0):
            b = random.randint(-30, 30)
        d = {}
        d["question_index"] = 9
        d["question_name"] = "Find the integer y intercept of a line in slope intercept form with zero slope." 
        d["problem_statement"] = "Find the y intercept of $y = {}$".format(b)
        d["correct_answer"] = b
        d["solution"] = [
                            ("y = {}".format(b), "Find the y intercept."),
                            ("{}".format(b), "The y intercept is the 'b' in slope intercept form."),
                        ]
        return d
    
    @returnVerifier
    def EQ_find_integral_slope_non_zero_slope_slope_intercept_form(self):
        m = 0
        while ( m == 0 ):
            m = random.randint(-30, 30)
        b = 0
        while ((b == m) or (b == 0)):
            b = random.randint(-30, 30)
        d = {}
        d["question_index"] = 10
        d["question_name"] = "Find the integer slope of a line in slope intercept form with nonzero slope." 
        d["problem_statement"] = "Find the slope of $y = {}x + {}$".format(m, b)
        d["correct_answer"] = m
        d["solution"] = [
                            ("y = {}x + {}".format(m, b), "Find the slope."),
                            ("{}".format(m), "The slope is the 'm' in slope intercept form."),
                        ]
        return d
    
    @returnVerifier
    def EQ_find_decimal_slope_non_zero_slope_slope_intercept_form(self):
        precision = 2
        m = 0
        while ( m == 0 ):
            m = round(random.uniform(-30, 30), precision)
        b = 0
        while ((b == m) or (b == 0)):
            b = round(random.uniform(-30, 30), 2)
        d = {}
        d["question_index"] = 11
        d["question_name"] = "Find the decimal slope of a line in slope intercept form with nonzero slope." 
        d["problem_statement"] = "Find the slope of $y = {}x + {}$".format(m, b)
        d["correct_answer"] = m
        d["solution"] = [
                            ("y = {}x + {}".format(m, b), "Find the slope."),
                            ("{}".format(b), "The slope is the 'm' in slope intercept form."),
                        ]
        return d
    
    @returnVerifier
    def EQ_find_integral_slope_zero_slope_slope_intercept_form(self):
        b = 0
        while (b == 0):
            b = random.uniform(-30, 30)
        zero_slope = 0
        d = {}
        d["question_index"] = 12
        d["question_name"] = "Find the integer slope of a line in slope intercept form with zero slope."
        d["problem_statement"] = "Find the slope of $y = {}$".format(b)
        d["correct_answer"] = zero_slope
        d["solution"] = [
                            ("y = {}".format(b), "Find the slope."),
                            ("{}".format(zero_slope), "The slope is the 'm' in slope intercept form. There is no 'm' because it is zero."),
                        ]
        return d
    
    @returnVerifier
    def EQ_find_decimal_slope_zero_slope_slope_intercept_form(self):
        b = 0
        while (b == 0):
            b = round(random.uniform(-30, 30), 2)
        zero_slope = 0
        d = {}
        d["question_index"] = 13
        d["question_name"] = "Find the decimal slope of a line in slope intercept form with zero slope."
        d["problem_statement"] = "Find the slope of $y = {}$".format(b)
        d["correct_answer"] = zero_slope
        d["solution"] = [
                            ("y = {}".format(b), "Find the slope."),
                            ("{}".format(zero_slope), "The slope is the 'm' in slope intercept form. There is no 'm' because it is zero."),
                        ]
        return d
    
    @returnVerifier
    def EQ_find_integral_x_intercept_standard_form(self):
        x_int = utility.get_integer_in_range_excluding_specified(low=-5, high=5, exclude_list=[0])
        A = utility.get_integer_in_range_excluding_specified(low=-10, high=10, exclude_list=[0])
        C = x_int * A
        B = utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[0])
        d = {}
        d["question_index"] = 14
        d["question_name"] = "Find the integer x intercept of a line in standard form." 
        d["problem_statement"] = "Find the x intercept of the line ${}x + {}y = {}$".format(A, B, C)
        d["correct_answer"] = x_int
        d["solution"] = [
                            ("{}x + {}y = {}".format(A, B, C), "This is the equation of a line in 'standard form'"),
                            ("{}x + {}(0) = {}".format(A, B, C), "To find the x intercept, plug 0 in for y"),
                            ("{}x = {}".format(A, C), "Simplify."), 
                            ("x = \\frac{{ {} }}{{ {} }}".format(C, A), "Divide both sides by A"), 
                            ("x = {}".format(x_int), "Solve.")
                        ]
        return d
 
    @returnVerifier
    def EQ_find_fraction_x_intercept_slope_standard_form(self):
        A = utility.get_fraction()
        B = utility.get_fraction(den_exclude=[0, 1, A.denominator])
        C = utility.get_fraction(den_exclude=[0, 1, A.denominator, B.denominator])
        y_for_x_intercept = 0
        x_intercept = C / A
        d = {}
        d["question_index"] = 15
        d["question_name"] = "Find the fractional x intercept of a line in standard form."
        d["problem_statement"] = "Find the x intercept of the line $\\frac{{ {} }}{{ {} }}x + \\frac{{ {} }}{{ {} }}y = \\frac{{ {} }}{{ {} }}$".format(A.numerator, A.denominator, B.numerator, B.denominator, C.numerator, C.denominator)
        d["correct_answer"] = (x_intercept.numerator, x_intercept.denominator)
        d["solution"] = [
                            ("Ax + By = C", "This is the equation of a line in slope intercept form."), 
                            ("Ax + B(0) = C", "Remeber that the y coordinate of the x intercept is 0."), 
                            ("\\frac{{ {} }}{{ {} }}x = \\frac{{ {} }}{{ {} }}".format(A.numerator, A.denominator, C.numerator, C.denominator), "Plug in the given values for A and C."), 
                            ("x = \\frac{{ {} }}{{ {} }} \\times \\frac{{ {} }}{{ {} }}".format(C.numerator, C.denominator, A.denominator, A.numerator), "Multiply both sides by the reciprocal of A."), 
                            ("x = \\frac{{ {} }}{{ {} }}".format(C.numerator * A.denominator, C.denominator * A.numerator), "Simplify."), 
                        ]
        if (C.numerator * A.denominator != x_intercept.numerator):
            d["solution"] += [("x = \\frac{{ {} }}{{ {} }}".format(x_intercept.numerator, x_intercept.denominator), "Simplify.")]
        return d
   
    @returnVerifier
    def EQ_find_integral_y_intercept_standard_form(self):
        y_int = utility.get_integer_in_range_excluding_specified(low=-5, high=5, exclude_list=[0])
        A = utility.get_integer_in_range_excluding_specified(low=-10, high=10, exclude_list=[0])
        B = utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[0])
        C = y_int * B
        d = {}
        d["question_index"] = 16
        d["question_name"] = "Find the integer y intercept of a line in standard form."
        d["problem_statement"] = "Find the x intercept of the line ${}x + {}y = {}$".format(A, B, C)
        d["correct_answer"] = y_int
        d["solution"] = [
                            ("{}x + {}y = {}".format(A, B, C), "This is the equation of a line in 'standard form'"),
                            ("{}(0) + {}y = {}".format(A, B, C), "To find the y intercept, plug 0 in for x"),
                            ("{}y = {}".format(B, C), "Simplify."), 
                            ("y = \\frac{{ {} }}{{ {} }}".format(B, A), "Divide both sides by B"), 
                            ("y = {}".format(y_int), "Solve.")
                        ]
        return d
 
    @returnVerifier
    def EQ_find_rational_y_intercept_standard_form(self):
        A = utility.get_fraction()
        B = utility.get_fraction(den_exclude=[0, 1, A.denominator])
        C = utility.get_fraction(den_exclude=[0, 1, A.denominator, B.denominator])
        y_for_x_intercept = 0
        x_intercept = C / A
        d = {}
        d["question_index"] = 17
        d["question_name"] = "Find the fractional y intercept of a line in standard form."
        d["problem_statement"] = "Find the x intercept of the line $\\frac{{ {} }}{{ {} }}x + \\frac{{ {} }}{{ {} }}y = \\frac{{ {} }}{{ {} }}$".format(A.numerator, A.denominator, B.numerator, B.denominator, C.numerator, C.denominator)
        d["correct_answer"] = (x_intercept.numerator, x_intercept.denominator)
        d["solution"] = [
                            ("Ax + By = C", "This is the equation of a line in slope intercept form."), 
                            ("Ax + B(0) = C", "Remeber that the y coordinate of the x intercept is 0."), 
                            ("\\frac{{ {} }}{{ {} }}x = \\frac{{ {} }}{{ {} }}".format(A.numerator, A.denominator, C.numerator, C.denominator), "Plug in the given values for A and C."), 
                            ("x = \\frac{{ {} }}{{ {} }} \\times \\frac{{ {} }}{{ {} }}".format(C.numerator, C.denominator, A.denominator, A.numerator), "Multiply both sides by the reciprocal of A."), 
                            ("x = \\frac{{ {} }}{{ {} }}".format(C.numerator * A.denominator, C.denominator * A.numerator), "Simplify."), 
                        ]
        if (C.numerator * A.denominator != x_intercept.numerator):
            d["solution"] += [("x = \\frac{{ {} }}{{ {} }}".format(x_intercept.numerator, x_intercept.denominator), "Simplify.")]
        return d
   
    @returnVerifier
    def EQ_find_integral_slope_standard_form(self):
        m = utility.get_integer_in_range_excluding_specified(low=-10, high=10, exclude_list=[0])
        b = utility.get_integer_in_range_excluding_specified(low=-10, high=10, exclude_list=[0, m]) 
        #y = mx + b
        # we dont know y or x 
        multiplier = utility.get_integer_in_range_excluding_specified(low = 1, high = 10, exclude_list=[])
        A = multiplier
        B = multiplier * ( -1 * m )
        C = multiplier * ( b )
        d = {}
        d["question_index"] = 18
        d["question_name"] = "Find the integer slope of a line in standard form."
        d["problem_statement"] = "Find the slope of the line {}x + {}y = {}".format(A, B, C)
        d["correct_answer"] = m
        d["solution"] = [
                            ("{}x + {}y = {}".format(A, B, C), "This is the equation of a line in standard form. We will turn it into slope-intercept form to get the slope."), 
                            ("{}y = {}x + {}".format(A, -B, C), "Subtract {}x from both sides.".format(B)),
                            ("y = {}x + {}".format(m, b), "Divide both sides by {}".format(A)),
                            ("m = {}".format(m), "Slope intercept form is $y = mx + b."),
                        ]
        return d
    
    @returnVerifier
    def EQ_find_rational_slope_standard_form(self):
        m = utility.get_fraction(num_low=-10, num_high=10, den_low=-10, den_high=10)
        b = utility.get_fraction(num_low=-10, num_high=10, den_low=-10, den_high=10, den_exclude=[0, 1, m.denominator])
        #y = mx + b
        #multiply through by m_denom * b_denom * constant
        constant = utility.get_integer_in_range_excluding_specified(low=-10, high=10, exclude_list=[0, 1])
        A = -1 * constant * m.numerator * b.denominator
        B = constant * m.denominator * b.denominator
        C = constant * b.numerator * m.denominator
        d = {}
        d["question_index"] = 19
        d["question_name"] = "Find the fractional slope of a line in standard form."
        d["problem_statement"] = "Find the slope of the line given in standard form as {}x + {}y = {}".format(A, B, C)
        d["correct_answer"] = (m.numerator, m.denominator) 
        d["solution"] = [
                            ("{}x + {}y = {}".format(A, B, C), "Find the slope of this line."), 
                            ("{}y = -({}x) + {}".format(A, B, C), "Bring the ${}x$ to the right side".format(A)), 
                            ("y = -\\frac{{ {} }}{{ {} }}x + \\frac{{ {} }}{{ {} }}".format(B, A, C, A), "Divide both sides by {}".format(B)),
                            ("y = \\frac{{ {} }}{{ {} }}x + \\frac{{ {} }}{{ {} }}".format(m.numerator, m.denominator, b.numerator, b.denominator), "Simplify"),
                            ("m = \\frac{{ {} }}{{ {} }}".format(m.numerator, m.denominator), "The slope is given by the slope intercept form."),
                        ]
        return d
    
    @returnVerifier
    def EQ_convert_rational_standard_form_to_slope_intercept_form(self):
        #Get a rational A, B, C
        A = utility.get_fraction(num_low=1, num_high=5, den_low=2, den_high=10)
        B = utility.get_fraction(num_low=1, num_high=5, den_low=2, den_high=15, den_exclude=[0,1,A.denominator])
        C = utility.get_fraction(num_low=1, num_high=5, den_low=2, den_high=15, den_exclude=[0,1,A.denominator, B.denominator])
        An, Ad = A.numerator, A.denominator
        Bn, Bd = B.numerator, B.denominator
        Cn, Cd = C.numerator, C.denominator
        #Convert to slope intercept form
        m = Fraction(-1 * B.denominator * A.numerator, B.numerator * A.denominator)
        mn, md = m.numerator, m.denominator
        b = Fraction(B.denominator * C.numerator, B.numerator * C.denominator) 
        bn, bd = b.numerator, b.denominator
        d = {}
        d["question_index"] = 20
        d["question_name"] = "Convert a line from standard form with fractions to slope intercept form."
        d["problem_statement"] = "Find the slope intercept form of the line $\\frac{{ {} }}{{ {} }}x + \\frac{{ {} }}{{ {} }}y = \\frac{{ {} }}{{ {} }}".format(A.numerator, A.denominator, B.numerator, B.denominator, C.numerator, C.denominator)  
        d["correct_answer"] = (m.numerator, m.denominator, b.numerator, b.denominator)
        d["solution"] = [
                            ("\\frac{{ {} }}{{ {} }}x + \\frac{{ {} }}{{ {} }}y = \\frac{{ {} }}{{ {} }}".format(An, Ad, Bn, Bd, Cn, Cd), "Convert to slope intercept form."),
                            ("\\frac{{ {} }}{{ {} }}y = -\\frac{{ {} }}{{ {} }}x + \\frac{{ {} }}{{ {} }}".format(An, Ad, Bn, Bd, Cn, Cd), "Subtract the x term from both sides."),
                            ("y = -\\frac{{ {} * {} }}{{ {} * {} }}x + \\frac{{ {} * {} }}{{ {} * {} }}".format(Bd, An, Bn, Ad, Bd, Cn, Bn, Cd), "Multiply both sides by the reciprocal of \\frac{{ {} }}{{ {} }}".format(Bn, Bd) ),
                            ("y = \\frac{{ {} }}{{ {} }}x + \\frac{{ {} }}{{ {} }}".format(mn, md, bn, bd), "Simplify"),
                        ]
        return d
    
    @returnVerifier
    def EQ_convert_integral_standard_form_to_slope_intercept_form(self):
        A = utility.get_integer_in_range_excluding_specified(low=-10, high=10, exclude_list=[0,1])
        B = utility.get_integer_in_range_excluding_specified(low=-10, high=10, exclude_list=[0, 1, A])
        C = utility.get_integer_in_range_excluding_specified(low=-10, high=10, exclude_list=[0, 1, A, B])
        m = Fraction(-A, B)
        b = Fraction(C, B)
        d = {}
        d["question_index"] = 21
        d["question_name"] = "Convert a line from standard form with only integers to slope intercept form."
        d["problem_statement"] = "Convert ${}x + {}y={}$ from standard form to slope intercept form.".format(A, B, C)
        d["correct_answer"] = (m.numerator, m.denominator, b.numerator, b.denominator)
        d["solution"] = [
                            ("{}x + {}y = {}".format(A, B, C), "Convert this standard form line into slope intercept form."),
                            ("{}y = -({}x) + {}".format(B, A, C), "Subtract the x term from both sides. We want the y term alone."),
                            ("y = \\frac{{ {} }}{{ {} }}x + \\frac{{ {} }}{{ {} }}".format(-A, B, C, B), "Divide both sides by {}".format(B) ),
                            ("y = \\frac{{ {} }}{{ {} }}x + \\frac{{ {} }}{{ {} }}".format(m.numerator, m.denominator, b.numerator, b.denominator), "Simplify the fractions in the previous step if possible.")
                        ]
        return d
    
    @returnVerifier
    def EQ_convert_rational_slope_intercept_form_to_standard_form(self):
        m = utility.get_fraction(num_low=2, num_high=8, den_low=3, den_high=10)
        b = utility.get_fraction(num_low=2, num_high=8, den_low=3, den_high=10)
        mn, md = m.numerator, m.denominator
        bn, bd = b.numerator, b.denominator
        #y = mx + b
        #m.den * b.den * y = b.den * m.num * x + b.num * m.den
        #Simplify the equation too
        A = -1 * bd * mn
        B = md * bd
        C = bn * md
        ABC_gcd = utility.get_gcd([A, B, C])
        A_simple = A//ABC_gcd
        B_simple = B//ABC_gcd
        C_simple = C//ABC_gcd
        d = {}
        d["question_index"] = 22
        d["question_name"] = "Convert a line from slope intercept form with fractions to standard form."
        d["problem_statement"] = "Convert the line $y = \\frac{{ {} }}{{ {} }}x + \\frac{{ {} }}{{ {} }}$ into standard form.".format(mn, md, bn, bd)
        d["correct_answer"] = (A_simple, B_simple, C_simple)
        d["solution"] = [
                            ("y = \\frac{{ {} }}{{ {} }}x + \\frac{{ {} }}{{ {} }}".format(mn, md, bn, bd), "Convert this line into standard form."),
                            ("{}\\times{}\\times y = {} \\times {} \\times \\frac{{ {} }}{{ {} }}x + {} \\times {} \\times \\frac{{ {} }}{{ {} }}".format(md, bd, md, bd, mn, md, md, bd, bn, bd), "Multiply by the denominators of the fractions."),
                            ("{}y = {}x + {}".format(B,-A, C), "Simplify"),
                            ("-({}x) + {}y = {}".format(-A, B, C), "Bring the x term to the left side."),
                            ("{}x + {}y = {}".format(A, B, C), "Simplify"), 
                        ]
        if (ABC_gcd > 1):
            #simplify
            d["solution"] += [
                                ("{}x + {}y = {}".format(A_simple, B_simple, C_simple), "Simplify by dividing through by {}".format(ABC_gcd))
                             ]
        return d
    
    @returnVerifier
    def EQ_get_integer_slope_from_coordinates(self):
        """
        delta y  must be a multiple of delta x
        """
        x1 = utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[])
        y1 = utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[])
        x2 = utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[x1])
        multiplier = utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[])
        delta_x = x2 - x1
        #y2 - y1 = c(x2 - x1)
        y2 = multiplier * delta_x + y1
        slope = (y2 - y1) // (x2 - x1)
        d = {}
        d["question_index"] = 23
        d["question_name"] = "Get the integer slope of a line from two coordinates."
        d["problem_statement"] = "Find the slope of the line through $({}, {})$ and $({}, {})$".format(x1, y1, x2, y2)
        d["correct_answer"] = slope 
        d["solution"] = [
                            ("m = \\frac{{{y2 - y1}}}{{{x2 - x1}}}", "This is the formula for computing the slope of a line given two points."),
                            ("m = \\frac{{{} -{}}}{{{} - {}}}".format(y2, y1, x2, x1), "Compute the slope"),
                            ("m = \\frac{{{}}}{{{}}}".format(y2 - y1, x2 - x1), "Simplify."),
                            ("m = {}".format(slope), "Done."),
                        ]
        return d
        
    
    @returnVerifier
    def EQ_get_fraction_slope_from_coordinates(self):
        multiplier = utility.get_integer_in_range_excluding_specified(low=-3, high=3, exclude_list=[0])
        modulo = 0
        while (modulo == 0):
            x1 = multiplier*utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[])
            y1 = multiplier*utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[])
            x2 = multiplier*utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[x1])
            y2 = multiplier*utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[y1])
            delta_x = x2 - x1
            if (delta_x == 0):
                continue
            delta_y = y2 - y1
            if (delta_y == 0):
                continue
            modulo = delta_y % delta_x
        slope = Fraction(delta_y, delta_x)
        d = {}
        d["question_index"] = 24
        d["question_name"] = "Get the fractional slope of a line from two coordinates."
        d["problem_statement"] = "Find the slope of the line through $({}, {})$ and $({}, {})$".format(x1, y1, x2, y2)
        d["correct_answer"] = (slope.numerator, slope.denominator)
        d["solution"] = [
                            ("m = \\frac{{{y2 - y1}}}{{{x2 - x1}}}", "This is the formula for computing the slope of a line given two points."),
                            ("m = \\frac{{{} -{}}}{{{} - {}}}".format(y2, y1, x2, x1), "Compute the slope"),
                            ("m = \\frac{{{}}}{{{}}}".format(y2 - y1, x2 - x1), "Simplify."),
                            ("m = \\frac{{{}}}{{{}}}".format(slope.numerator, slope.denominator), "Done."),
                        ]
        return d
    
    
    @returnVerifier
    def EQ_get_integer_y_intercept_from_coordinates(self):
        """
        delta y  must be a multiple of delta x
        """
        x1 = utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[])
        y1 = utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[])
        x2 = utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[x1])
        multiplier = utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[])
        delta_x = x2 - x1
        #y2 - y1 = c(x2 - x1)
        y2 = multiplier * delta_x + y1
        m = (y2 - y1) // (x2 - x1)
        b = y1 - m * x1
        d = {}
        d["question_index"] = 25
        d["question_name"] = "Get the integer y intercept of a line from coordinates."
        d["problem_statement"] = "Find the y intercept of the line through $({}, {})$ and $({}, {})$".format(x1, y1, x2, y2)
        d["correct_answer"] = b 
        d["solution"] = [
                            ("m = \\frac{{{y2 - y1}}}{{{x2 - x1}}}", "This is the formula for computing the slope of a line given two points."),
                            ("m = \\frac{{{} -{}}}{{{} - {}}}".format(y2, y1, x2, x1), "Compute the slope"),
                            ("m = \\frac{{{}}}{{{}}}".format(y2 - y1, x2 - x1), "Simplify."),
                            ("m = {}".format(m), "Now we have the slope."),
                            ("y = mx + b", "You can put a coordinate and the slope into this equation, and solve for the y intercept."),
                            ("{} = {}*{} + b".format(y1, m, x1), "Substitute a coordinate and the slope. We choose the coordinate $(x, y) = ({}, {})".format(x1, y1)),
                            ("{} = {} + b".format(y1, m*x1), "Simplify."), 
                            ("{} - {} = b".format(y1, m * x1), "Simplify"), 
                            ("{} = b".format(y1 - m * x1), "Done. Try using the coordinate $({}, {})$ and you'll get the same answer!".format(x2, y2)),
                        ]
        return d
        
    
    
    @returnVerifier
    def EQ_get_fraction_y_intercept_from_coordinates(self):
        b_numerator = 1
        b_denominator = 1
        while (b_numerator % b_denominator == 0):
            b_numerator = utility.get_integer_in_range_excluding_specified(low=-15, high = 15, exclude_list=[0])
            b_denominator = utility.get_integer_in_range_excluding_specified(low=-15, high=15, exclude_list=[0, b_numerator])
        slope = utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[0])
        x1 = utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[0])
        x1 = Fraction(x1, 1)
        y1 = Fraction(b_denominator * slope * x1 + b_numerator, b_denominator)
        x2_numerator = 1
        x2_denominator = 1
        while ((Fraction(x2_numerator, x2_denominator) == x1) or (Fraction(x2_numerator, x2_denominator) % 1 == 0)):
            x2_numerator = utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[0])
            x2_denominator = utility.get_integer_in_range_excluding_specified(low=-20, high = 20, exclude_list = [0])
        x2 = Fraction(x2_numerator, x2_denominator)
        y2 = Fraction(slope * x2_numerator * b_denominator + b_numerator * x2_denominator, b_denominator * x2_denominator) 
        d = {}
        d["question_index"] = 26
        d["question_name"] = "Get the fractional y intercept of a line from two coordinates."
        d["problem_statement"] = "Find the y intercept of the line through $(\\frac{{{}}}{{{}}}, \\frac{{{}{{{}}})$ and $(\\frac{{{}}}{{{}}}, \\frac{{{}}}{{{}}})$"\
                                .format(x1.numerator, x1.denominator, y1.numerator, y1.denominator, x2.numerator, x2.denominator, y2.numerator, y2.denominator)
        d["correct_answer"] = (b_numerator, b_denominator)
        d["solution"] = [
                            ("m = \\frac{{{y2 - y1}}}{{{x2 - x1}}}", "This is the formula for computing the slope of a line given two points."),
                            ("m = \\frac{{{} -{}}}{{{} - {}}}".format(y2, y1, x2, x1), "Compute the slope"),
                            ("m = \\frac{{{}}}{{{}}}".format(y2 - y1, x2 - x1), "Simplify."),
                            ("m = \\frac{{{}}}{{{}}}".format(slope.numerator, slope.denominator), "Done."),
                        ]
        return d
    
    @returnVerifier
    def EQ_get_integer_x_intercept_from_coordinates(self):
        x_intercept = utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[0])
        y_for_x_intercept = 0
        x1 = utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[x_intercept])
        slope = utility.get_integer_in_range_excluding_specified(low=-10, high=10, exclude_list=[0])
        y1 = slope * (x1 - x_intercept)
        x2 = utility.get_integer_in_range_excluding_specified(low=-20, high=20, exclude_list=[x1, x_intercept])
        y2 = slope * ( x2 - x1 ) + y1
        d = {}
        d["question_index"] = 27
        d["question_name"] = "Get the integer x intercept of a line from two coordinates on it."
        d["problem_statement"] = "Find the x intercept of the line through $({}, {})$ and $({}, {})$.".format(x1, y1, x2, y2)
        d["correct_answer"] = x_intercept
        d["solution"] = [
                            ("m = \\frac{{{} - {}}}{{{} - {}}}".format(y2, y1, x2, x1), "Find the slope through the two points."),
                            ("m = \\frac{{{}}}{{{}}}".format(y2 - y1, x2 - x1), "Simplify."),
                            ("y = {}x + b".format(slope), "Plug the slope into the slope intercept form."), 
                            ("{} = {} \\times {} + b".format(y1, slope, x1), "Plug either one of the two coordinates into the slope intercept equation."), 
                            ("{} - {} = b".format(y1, slope * x1), "Simplify."), 
                            ("{} = b".format(y1 - slope * x1), "Simplify."), 
                            ("y = {}x + {}".format(slope, y1 - slope * x1), "Plug the slope and the y intercept into the slope intercept equation."), 
                            ("0 = {}x + {}".format(slope, y1 - slope * x1), "Set y = 0 to find the x intercept."), 
                            ("{} = {}x".format( slope * x1 - y1, slope ), "Simplify."), 
                            ("\\frac{{{}}}{{{}}} = x".format(slope * x1 - y1, slope), "Simplify."), 
                            ("{} = x".format((slope * x1 - y1 )// slope), "Solve.")
                        ]
        return d;
        
    @returnVerifier
    def EQ_get_integer_x_intercept_from_fraction_coordinates(self):
        """
        Find the x intercept of the equation of a line through two coordinates whose components
        contain fractions.
        x_intercept = (a, 0)
        Other coordinates = (b/c, d/e)
        """
        x_intercept = utility.get_integer_in_range_excluding_specified(low=-5, high=5, exclude_list=[0])
        dx_fracs = set()
        min_numerator = 1
        numerator_up_bd = 5 
        for numerator in range(min_numerator, numerator_up_bd):
            for denominator in range(numerator + 1, numerator_up_bd + 1):
                dx_fracs.add(Fraction(numerator, denominator))
        print(dx_fracs)
        dx_fracs = list(dx_fracs)
        dx_ints = range(2, 5)
        x1_d_int = random.choice(dx_ints)
        x1_d_frac = random.choice(dx_fracs)
        x2_d_int = random.choice([i for i in dx_ints if i != x1_d_int]) 
        x2_d_frac = random.choice([f for f in dx_fracs if f != x1_d_frac]) 
        x1 = x_intercept + x1_d_int + x1_d_frac
        x2 = x_intercept - x2_d_int - x1_d_frac
        m_fracs = dx_fracs[:]
        m = random.choice(m_fracs)
        # y = mx + b
        # 0 = m * x_intercept + b
        b = -m * x_intercept
        y1 = m * x1 + b
        y2 = m * x2 + b
        # Scratchpad for generating values to be used in the answers
        # 1. find the slope
        # 2. find the y intercept
        dy = y2 - y1
        dx = x2 - x1
        m_times_x1 = m * x1
        y1_minus_m_times_x1 = y1 - m_times_x1
        # should have some check here to ensure that b == y1_minus_m_times_x1
        solution = -Fraction(m.denominator * b.numerator, m.numerator * b.denominator)
        # end scratch pad
        d = {}
        d["question_index"] = 28
        d["question_name"] = "Get the integer x intercept of a line from two fractional coordinates on it." 
        d["correct_answer"] = x_intercept
        d["problem_statement"] = """ Find the x_intercept of the line though the coordinates $(\\frac{{ {} }}{{ {} }}, \\frac{{ {} }}{{ {} }})$ and 
                                     $(\\frac{{ {} }}{{ {} }}, \\frac{{ {} }}{{ {} }})$""".format(x1.numerator, x1.denominator, y1.numerator, y1.denominator,
                                                                                             x2.numerator, x2.denominator, y2.numerator, y2.denominator)
        d["solution"] = [
                                    ("m = \\frac{{ y2 - y1 }}{{ x2 - x1 }}", "Find the slope."),
                                    ("m = \\frac{{ \\frac{{ {} }}{{ {} }} - \\frac{{ {} }}{{ {} }} }} \
                                                {{ \\frac{{ {} }}{{ {} }} - \\frac{{ {} }}{{ {} }} }}".format(y2.numerator, y2.denominator, y1.numerator, y1.denominator,\
                                                                                                              x2.numerator, x2.denominator, x1.numerator, x1.denominator ), "Plug in the coordinates."),
                                    ("m = \\frac{{ {} }}{{ {} }}".format(m.numerator, m.denominator), "Simplify"), 
                                    ("y = mx + b", "Now use the slope intercept form to find the y intercept (b)"), 
                                    ("\\frac{{ {} }}{{ {} }} = \\frac{{ {} }}{{ {} }} * \\frac{{ {} }}{{ {} }} + b".format(y1.numerator, y1.denominator, m.numerator, m.denominator,
                                                                                                                           x1.numerator, x1.denominator, b.numerator, b.denominator),
                                     """Plug in either one of your coordinates. We choose to use $(x1, y1) = (\\frac{{ {} }}{{ {} }}, \\frac{{ {} }}{{ {} }}$, 
                                      but you could also use $(x2, y2) = (\\frac{{ {} }}{{ {} }}, \\frac{{ {} }}{{ {} }})$""".format(x1.numerator, x1.denominator, y1.numerator, y1.denominator, 
                                                                                                                                   x2.numerator, x2.denominator, y2.numerator, y2.denominator)), 
                                    ("\\frac{{ {} }}{{ {} }} = \\frac{{ {} }}{{ {} }} + b".format(y1.numerator, y1.denominator, m_times_x1.numerator, m_times_x1.denominator), "Simplify."), 
                                    ("\\frac{{ {} }}{{ {} }} - \\frac{{ {} }}{{ {} }} = b".format(y1.numerator, y1.denominator, m_times_x1.numerator, m_times_x1.denominator), "Simplify."),
                                    ("\\frac{{ {} }}{{ {} }} = b".format(y1_minus_m_times_x1.numerator, y1_minus_m_times_x1.denominator), "Simplify."),
                                    ("y = \\frac{{ {} }}{{ {} }} x + \\frac{{ {} }}{{ {} }}".format(m.numerator, m.denominator, b.numerator, b.denominator), "Plug m and b into the slope intercept equation."),
                                    ("0 = \\frac{{ {} }}{{ {} }} x + \\frac{{ {} }}{{ {} }}".format(m.numerator, m.denominator, b.numerator, b.denominator), "Remember, at the x intercept y = 0"), 
                                    ("\\frac{{ {} }}{{ {} }} = \\frac{{ {} }}{{ {} }} x".format(-b.numerator, b.denominator, m.numerator, m.denominator), "Subtract b from both sides."), 
                                    ("\\frac{{ {} }}{{ {} }} \\times \\frac{{ {} }}{{ {} }} = x".format(m.denominator, m.numerator, -b.numerator, b.denominator), "Multiply both sides by the reciprocal of the slope."),
                                    ("\\frac{{ {} }}{{ {} }} = x".format(solution.numerator, solution.denominator), "Solve."),
                                ]

        return d
                                          
    @returnVerifier
    def EQ_find_decimal_y_intercept_zero_slope_slope_intercept_form(self):
        precision = 2
        b = 0
        while (b == 0):
            b = round(random.uniform(-30, 30), 2)
        d = {}
        d["question_index"] = 29 
        d["question_name"] = "Find the decimal y intercept of a line in slope intercept form with zero slope." 
        d["problem_statement"] = "Find the y intercept of $y = {}$".format(b)
        d["correct_answer"] = b
        d["solution"] = [
                            ("y = {}".format(b), "Find the y intercept."),
                            ("{}".format(b), "The y intercept is the 'b' in slope intercept form."),
                        ]
        return d
    

