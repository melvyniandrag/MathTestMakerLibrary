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
The project will have three libraries
1. A library for generating test questions
2. A library for generating wrong answers
3. A library for generating LaTeX docs from the input of 1&2

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

For example, if a user wants a test with one question about finding the x intercept of a linear equation, the input will be:

```python
```


## Contributing
Feel free to 
