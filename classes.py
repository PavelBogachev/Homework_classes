class Person:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname

	def __str__(self):
		string = f'Имя: {self.name}\nФамилия: {self.surname}'
		return string


class Student(Person):
	def __init__(self, name, surname):
		Person.__init__(self, name, surname)
		self.finished_courses = []
		self.courses_in_progress = []
		self.grades = {}

	def rate_lec(self, lector, course, grade):
		if isinstance(lector, Lector) and course in (
				self.courses_in_progress +
				self.finished_courses) and course in lector.courses_attached:
			lector.grades += [grade]
		else:
			return 'Ошибка'

	def get_average_course_grade(self, course):
		if len(self.grades[course]):
			average_grade = sum(self.grades[course]) / len(self.grades[course])
		else:
			average_grade = 0
		return average_grade

	def get_average_grade(self):
		average_grade = 0
		for course in self.grades:
			average_grade += self.get_average_course_grade(course)
		if len(self.grades):
			average_grade = average_grade / len(self.grades)
		return average_grade

	def __str__(self):
		string = Person.__str__(self)
		string += f'\nСредняя оценка за домашние задания: {self.get_average_grade()}\
			\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\
			\nЗавершенные курсы: {", ".join(self.finished_courses)}'
		return string

	def __eq__(self, other):
		return self.get_average_grade() == other.get_average_grade()

	def __lt__(self, other):
		return self.get_average_grade() < other.get_average_grade()

	def __le__(self, other):
		return self.get_average_grade() <= other.get_average_grade()


class Mentor(Person):
	def __init__(self, name, surname):
		Person.__init__(self, name, surname)
		self.courses_attached = []


class Lector(Mentor):
	def __init__(self, name, surname):
		Mentor.__init__(self, name, surname)
		self.grades = []

	def get_average_grade(self):
		if len(self.grades):
			average_grade = sum(self.grades) / len(self.grades)
		else:
			average_grade = 0
		return average_grade

	def __str__(self):
		string = Person.__str__(self)
		string += f'\nСредняя оценка за лекции: {self.get_average_grade()}'
		return string

	def __eq__(self, other):
		return self.get_average_grade() == other.get_average_grade()

	def __lt__(self, other):
		return self.get_average_grade() < other.get_average_grade()

	def __le__(self, other):
		return self.get_average_grade() <= other.get_average_grade()


class Reviewer(Mentor):
	def rate_hw(self, student, course, grade):
		if isinstance(
				student, Student
		) and course in self.courses_attached and course in student.courses_in_progress:
			if course in student.grades:
				student.grades[course] += [grade]
			else:
				student.grades[course] = [grade]
		else:
			return 'Ошибка'
