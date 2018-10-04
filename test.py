from mathtestmaker import MathTestMaker
import pprint

testmaker = MathTestMaker()
question_requests = \
		[
			{
				'category': 'linear equations',
				'name': 'Find the integer x intercept of a line in slope intercept form with nonzero slope.',
				'numChoices': 4,
				'points': 10
			},
		]
questions = testmaker.getSelectedQuestions( question_requests )
for q in questions:	
	pprint.pprint(q)
