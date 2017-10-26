from testmakerlibrary import TestMakerLibrary
import pprint

testmaker = TestMakerLibrary()
question_requests = \
		[
			{
				'question_category': 'linear equations',
				'selected_question': 'Find the integer x intercept of a line in slope intercept form with nonzero slope.',
				'count': 2,
				'points': 10
			},
		]
questions = testmaker.getSelectedQuestions( question_requests )
for q in questions:	
	pprint.pprint(q)
