# MathTestMaker

## Introduction
Alot of wasted time goes into making tests for your class! Some teachers have access to a test generator 
of some sort that's often associated with the testbook manufacturer. That's fine, but there ought to be 
a free solution for everyone to use. This library provides an API that allows the user to request a number
of questions of certain types, and then spits out some fresh questions and solutions matching the request.

## Benefits
* It's free
* It can quickly generate a massive amount of unique tests
* You can make a unique test for each student! NO MORE CHEATING!
* All math teachers can work together to create a pool of great questions
* etc.

## Where We're At Now
Right now I have an older version of this library hosted at [Calisto Studios](www.calistostudios.com). 
I'm working out a POC now. Over there you'll see that you can select questions, a number of tests, and 
it spits out a pretty PDF formatted in [LaTeX](https://www.latex-project.org/)! I'm in the process of getting
a new domain name now and enhancing the site, but been bogged down with work.

## The Future
The project will have a few libraries
1. A library for generating test questions
2. A library for generating wrong answers
3. A library for generating LaTeX docs from the input of 1&2
4. ( Maybe )  A computer-vision-based bubble sheet grader for quick grading!

## Code Overview

### Question Generator
The APIs aren't written in stone yet, but the current APIs are specified below.

The question generator will take a user input in the form of a list of dictionaries:
```python
input = [
    { 
      'category':      XXXX,
      'question_type': XXXX,
      'count':         XXXX,
    },

    { 
      'category':      XXXX,
      'question_type': XXXX,
      'count':         XXXX,
    },

    ... 

]
```

And output a list of dictionaries of the form:
```python
[
    {
        'question_name':     'A description of the type of question',
        'problem_statement': 'The statement of the problem',
        'correct_answer':    'The correct answer to the problem specified in the problem_statement',
        'solution':          [
                                ( 'Equation for solution step 1', 'Text for solution step 1' ),
                                ...
                                ( 'Equation for solution final solution step', 'Text for final solution step' )
                             ]
    },
    {
        'question_name':     'A description of the type of question',
        'problem_statement': 'The statement of the problem',
        'correct_answer':    'The correct answer to the problem specified in the problem_statement',
        'solution':          [
                                ( 'Equation for solution step 1', 'Text for solution step 1' ),
                                ...
                                ( 'Equation for solution final solution step', 'Text for final solution step' )
                             ]
    },
    ...
]
```

### Sample API usage
For example, suppose that you, the teacher, just taught about finding x intercepts of linear equations. Perhaps 
you want one question about finding the x intercept of a line that doesn't go through the origin, and another quesion
about finding the y intercept of a line through the origin. The input will be:

```python
input  = [
    {
        'category':      'linear_equations',
        'question_type': 'find_non_zero_x_intercept_std_form',
        'count':          1
    },
    {
        'category':       'linear_equations',
        'question_type':  'find_zero_y_intercept',
        'count':          1
    },
]
```

And then the output will be something like:

```
[
    {
        'question_name': 'Find the x intercept',
        'problem_statement': 'Find the x intercept of the line y = 5x + 5'
        'correct_answer': -1,
        'solution': [
                        ( 'y = 5x + 5', 'Find the x intercept.' ),
                        ( '0 = 5x + 5', 'Set y to zero'),
                        ( '-5 = 5x',    'Subtract 5 from both sides.'),
                        ( '-1 = x'),    'Divide both sides by 5. Done.')
                    ]
    },
    {
        'question_name': 'Find the y intercept',
        'problem_statement': 'Find the y intercept of the line y = -6x'
        'correct_answer': 0,
        'solution': [
                        ( 'y = -6x', 'Find the y intercept.' ),
                        ( 'y = 6*0', 'Set x to zero'),
                        ( 'y = 0' ,  'Done.')
                    ]
    },
]
```

The solution set in the output can be run through the LaTeX generator ( the strings will be more complicated than they appear here so 
they will generate valid LaTeX markup ) and a solution manual can be automatically generated for each question to be handed out after the 
test is completed by the student! Because the solution steps are generated procedurally along with the question, every student can have an
individualized solution sheet! 

### The LaTeX Generator
Documentation to come. The issue with this now is that we'll ultimately need to support images for questions that involve pictures, e.g. graphing problems and word problems with doodles. I haven't decided on the best way to support images and other complications yet.

### The Wrong Number Generator 
Documentation to come. The wrong answers for a multiple choice question can't always follow the same pattern. You might want to choose wrong answers uniformly from around the right answer, you might want to throw in some crazy outliers as freebies to the kids, and how to handle the generation of wrong answers for graphical problems? These considerations and more require some thought before deciding on how wrong number generation happens.

### Grader
We will have a bubble sheet grader. There are alot of free ones out there. [OMR](https://en.wikipedia.org/wiki/Optical_mark_recognition) has been solved pretty thoroughly and professionally by alot of people. We'll need to look at what's out there and choose which one to use, or spin our own. [Adrian Rosebrock](https://www.pyimagesearch.com/2016/10/03/bubble-sheet-multiple-choice-scanner-and-test-grader-using-omr-python-and-opencv/) has a great blog post laying out a barebones not-quite-ready-for-production bubble sheet grader. It might be worthwhile to build on that code, or maybe find one that already works and is tested. I'm not even sure it's worthwhile to have a vision based grader, because the time it takes to take a picture and upload it to a server might exceed the time it would take to just manually look at a bubble sheet of right answers and compare them to the student's submission.

A big plus to taking pictures, though, is that the teacher then has a copy of paper as it was handed in and solves the perennial problem of sly foxes changing answers when the test is returned and arguing that they had in fact already put the right answer. If there is a fun, fast way for teachers to take pictures of a bunch of bubble sheets ( maybe just stick the stack in a copier with email capabilities and blast them over en masse to our server ) then this is a reasonable direction to go in.

## Contributing
Feel free to contribute! The code in the library will hopefully stay relatively simple so that math teachers who aren't professional programmers can learn the basics of Python and start contributing / tweaking the code quickly. Hopefully DigitalOcean and Hacktoberfest run [Hacktoberfest](https://hacktoberfest.digitalocean.com/?2018) again this year and we get a flood of contributions! I've slapped the GPL3 license on this project to keep it [free as in freedom](https://en.wikipedia.org/wiki/Free_as_in_Freedom). If this thing takes off maybe we can slap a donation button on the website and to cover server costs and maybe do this as a full time job for a bit.
