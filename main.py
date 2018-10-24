# coding=utf-8

import pyexcel

records = pyexcel.get_records(file_name="student_scores.xlsx")

math_scores=0
english_scores = 0
student_count = 0

for record in records:
    print(type(record))
    math_scores += record['math_score']
    english_scores += record['english_score']
    student_count += 1

average_math_score= math_scores / student_count
average_english_score= english_scores / student_count

data = [['average_math_score', 'average_english_score'], [average_math_score, average_english_score]]

pyexcel.save_as(array=data, dest_file_name="summary.xlsx")
