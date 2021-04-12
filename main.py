from classes import Student, Reviewer, Lector
from random import randint


def average_students_grade(students, course):
	average_grade = 0
	count_students = 0
	for student in students:
		if isinstance(student, Student) and course in (
				student.finished_courses + student.courses_in_progress):
			average_grade += student.get_average_course_grade(course)
			count_students += 1
	if count_students:
		return average_grade / count_students
	else:
		return 0


def average_lectors_grade(lectors, course):
	average_grade = 0
	count_lectors = 0
	for lector in lectors:
		if isinstance(lector, Lector) and course in lector.courses_attached:
			average_grade += lector.get_average_grade()
			count_lectors += 1
	if count_lectors:
		return average_grade / count_lectors
	else:
		return 0


def main():
	student_1 = Student('One', 'Student')
	student_2 = Student('Two', 'Student')
	students = [student_1, student_2]

	reviewer_1 = Reviewer('One', 'Rewiewer')
	reviewer_2 = Reviewer('Two', 'Rewiewer')
	reviewers = [reviewer_1, reviewer_2]

	lector_1 = Lector('One', 'Lector')
	lector_2 = Lector('Two', 'Lector')
	lectors = [lector_1, lector_2]

	all_persons = students + reviewers + lectors

	student_1.finished_courses += ['Git']
	student_1.courses_in_progress += ['Python']

	student_2.finished_courses += ['Python']
	student_2.courses_in_progress += ['Git']

	reviewer_1.courses_attached += ['Git']
	reviewer_2.courses_attached += ['Python']

	lector_1.courses_attached += ['Git', 'Python']
	lector_2.courses_attached += ['Python']

	for person in all_persons:
		print(person)
		print()

	for student in students:
		for reviewer in reviewers:
			for course in reviewer.courses_attached:
				for _ in range(5):
					reviewer.rate_hw(student, course, randint(1, 10))

	for student in students:
		for course in student.finished_courses:
			student.grades[course] = [randint(1, 10)]
			for _ in range(4):
				student.grades[course] += [randint(1, 10)]

	for student in students:
		for lector in lectors:
			for course in (student.finished_courses + student.courses_in_progress):
				for _ in range(5):
					student.rate_lec(lector, course, randint(1, 10))

	for student in students:
		print(student)
		print(student.grades)
		print()

	for lector in lectors:
		print(lector)
		print(lector.grades)
		print()

	print(average_lectors_grade(lectors, 'Python'))
	print(average_lectors_grade(lectors, 'Git'))
	print(average_students_grade(students, 'Python'))
	print(average_students_grade(students, 'Git'))
	print()

	print(average_lectors_grade(all_persons, 'Python'))
	print(average_lectors_grade(all_persons, 'Git'))
	print(average_students_grade(all_persons, 'Python'))
	print(average_students_grade(all_persons, 'Git'))
	print()

	print(average_students_grade(all_persons, 'Java'))
	print(average_lectors_grade(all_persons, 'Java'))
	print()

	for person in all_persons:
		print(person)
		print()

	print(student_1 > student_2)
	print(lector_1 > lector_2)


if __name__ == '__main__':
	main()
