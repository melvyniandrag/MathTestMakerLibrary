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
    """
    Class for generating linear equation type questions.
    
    --- Abbreviations ---
    SIF: slope-intercept form
    M: slope
    
    --- Naming Conventions ---
    Function names should indicate the type of question the function generates.
    Concepts are written in camelCase and different concepts in a given function are 
    separated by an underscore.
    e.g. A question about finding an integer x intercept of a linear equation
         in slope-intercept form with a non-zero slope is called findIntegralXIntercept_SIF_NonZeroM

    --- Return Values ---
    All of the methods that generate questions need to return a dictionary containing:
    1. problem_statement
    2. correct_answer
    3. solution

    The problem statement and solution should return strings that can be used by LaTeX to format output.
    The formatting of these strings may change in the future to allow for flexibility, but for now 
    we are just using primitive LaTeX syntax. 
    """
    def __init__(self):
        self.category_name = "linear equations"
        self.questions = dict( [
            ( "Find the integer x intercept of a line in slope intercept form with nonzero slope",
              self.findIntegralXIntercept_SIF_NonZeroM ),
            ( "Find the integer x intercept of a line in slope intercept with nonzero fractional slope.",
              self.findIntegralXIntercept_SIF_NonZeroFracM ),
        ] )

    def getQuestionNames( self ):
        """
        @return: A list of all the questions available
        """
        return self.questions.keys() 

    def getQuestions(self, questionNames ):
        """
        @param questionNames: Desired questions. The names should be keys into the self.questions dict.
        @return: A 2-tuple containing a list of generated questions and a list of questions that couldn't be generated.
        """
        generated = []
        errors = []
        for name in questionNames:
            try:
                generated.append( self.questions[name]() )
            except Exception as e:
                errors.append( name )
        return generated, errors

    def findIntegralXIntercept_SIF_NonZeroM(self):
        m = 0
        while(m == 0):
            m = random.randint( -20, 20)
        multiplier = 0
        while(multiplier == 0):
            multiplier = random.randint(-10, 10)
        b = m * multiplier 
        x_intercept = -1 * b // m
        d = {}
        d["problem_statement"] = "Find the x intercept of $y = {}x + {}$.".format(m, b) 
        d["correct_answer"] = x_intercept
        d["solution"] = [
                          (                "y = {}x + {}".format(m, b), "Find the x intercept."),
                          (                "0 = {}x + {}".format(m, b), "Set y to zero."), 
                          ("0 - {} = {}x + {} - {}".format(b, m, b, b), "Subtract b from both sides."),
                          (                   "{} = {}x".format(-b, m), "Simplify."),
                          (                "{} / {} = x".format(-b, m), "Divide both sides by m."),
                          (                         "{}".format(-b//m), "Simplify.")
                        ]
        return d   
    
    def findIntegralXIntercept_SIF_NonZeroFracM(self):
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
        d["problem_statement"] = "Find the x intercept of $y = \\frac{{{}}}{{{}}}x + {}$.".format(m_numerator, m_denominator, b) 
        d["correct_answer"] = x_intercept
        d["solution"] = [
                          (                "y = \\frac{{{}}}{{{}}}x + {}".format(m_numerator, m_denominator, b), "Find the x intercept."),
                          (                "0 = \\frac{{{}}}{{{}}}x + {}".format(m_numerator, m_denominator, b), "Set y to zero."), 
                          ("0 - {} = \\frac{{{}}}{{{}}}x + {} - {}".format(b, m_numerator, m_denominator, b, b), "Subtract b from both sides."),
                          (                  "{} = \\frac{{{}}}{{{}}}x ".format(-b, m_numerator, m_denominator), "Simplify."),
                          (          "{} \\times \\frac{{{}}}{{{}}} = x".format(-b, m_denominator, m_numerator), "Divide both sides by m."),
                          (                                  "{}".format(-1 * m_denominator * b // m_numerator), "Simplify.")
                        ]
        return d   
