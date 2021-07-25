from area import rect_area
height = 4
width = 5
correct_answer = 20
answer = rect_area(height, width)
if answer == correct_answer:
    print('Test passed')
else:
    print('Test failed')