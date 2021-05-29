# You are given a table containing assignment scores of students in a class. Write a query that identifies the largest difference in total score of all assignments.
# Output just the difference in total score between the two students.


import pandas as pd

# Start writing code
max(box_scores[['assignment1','assignment2','assignment3']].sum(axis=1)) - \
min(box_scores[['assignment1','assignment2','assignment3']].sum(axis=1))
