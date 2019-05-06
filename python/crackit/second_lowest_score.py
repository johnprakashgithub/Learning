def enter_students():
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    return students


def second_lowest(students):
    results = []
    if 2 <= len(students) <= 5:
        low = students[0][1]
        second = students[1][1]
        if low > second:
            results.append(students[0][0])
            t = low
            low = second
            second = t
        else:
            results.append(students[1][0])
        if len(students) == 2:
            return results
        else:
            results = []
        for i in range(2, len(students)):
            if students[i][1] < low:
                second = low
                low = students[i][1]
            elif low < students[i][1] < second or (low == second and second < students[i][1]):
                second = students[i][1]
        for student, score in students:
            if score == second:
                results.append(student)
    return results


if __name__ == '__main__':
    students = enter_students()
    for name in sorted(second_lowest(students)):
        print(name)
