grades = [0, 6, 12, 18] 

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / len(grades)
    return average

def grades_variance(scores,average):
    s = 0
    for i in scores:
        s = s + (average - i)**2

    return float(s)/len(grades)

print grades_variance(grades,grades_average(grades))
