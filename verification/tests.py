"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[6,1,10,5,4]],
            "answer": 2
        },
        {
            "input": [[10,3,3,2,1]],
            "answer": 1
        },
        {
            "input": [[7,3,4,2,9,7,4]],
            "answer": -1
        },
        {
            "input": [[42]],
            "answer": 0
        }
    ],
    "Extra": [
        {
            "input": [[1,1,1,9,1,1,1]],
            "answer": 3
        }
    ]
}
