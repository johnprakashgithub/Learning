def get_students():
    students_marks = {}
    for _ in range(int(input())):
        name, *line = input().split()
        scores = list(map(float, line))
        students_marks[name] = scores
    return students_marks, input()


def get_marks():
    retries = 3
    for _ in range(retries):
        mark = int(input)
        if 0 <= mark <= 100:
            return mark
        else:
            print("Retry - Enter the mark between 0 to 100 !")
    print("Return the default mark as 0")
    return 0


def calculate_average(scores):
    if scores:
        maths, physics, chemistry = scores
        average = (maths+physics+chemistry)/3
        return average


if __name__ == '__main__':
    students, query_name = get_students()
    for student in students:
        if student == query_name:
            print("{0:.2f}".format(calculate_average(students[student])))

