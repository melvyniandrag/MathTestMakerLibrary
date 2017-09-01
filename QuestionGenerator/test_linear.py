import linear
import pprint

le = linear.LinearEquations()
d = le.EQ_find_rational_slope_standard_form()
pprint.pprint(d, width=200)

d = le.EQ_convert_rational_slope_intercept_form_to_standard_form()
pprint.pprint(d, width=200)

#questions = le.get_available_questions()
#print(len(questions))
#pprint.pprint(questions)
#
#pprint.pprint(le.questions)
