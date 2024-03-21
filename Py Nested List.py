# Given the names and grades for each student in a class of  students, 
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, 
# order their names alphabetically and print each name on a new line.


if __name__ == '__main__':
    students = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        score_list.append(score)

        
    sorted_score_list = sorted(list(set(score_list)))
    second_lowest_score = sorted_score_list[1]

    students.sort(key=lambda x: x[0])

    for i in students:
        if i[1] == second_lowest_score:
            print(i[0])