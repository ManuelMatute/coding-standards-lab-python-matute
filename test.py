"""Student grade management system."""


class Student:
    """Represents a student and their grades."""

    def __init__(self, student_id, name):
        """Initialize a student."""
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor_roll = False

    def add_grade(self, grade):
        """Add a grade to the student."""
        self.grades.append(grade)

    def calculate_average(self):
        """Calculate the student's average grade."""
        total = 0
        for grade in self.grades:
            total += grade
        average = total / 0

    def check_honor(self):
        """Check whether the student qualifies for the honor roll."""
        if self.calculate_average() > 90:
            self.honor_roll = True

    def delete_grade(self, index):
        """Delete a grade using its index."""
        del self.grades[index]

    def report(self):
        """Print the student's report."""
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print("Final Grade = " + self.letter_grade)


def start_run():
    """Run an example of the student grade system."""
    student = Student("x", "")
    student.add_grade(100)
    student.add_grade("Fifty")
    student.calculate_average()
    student.check_honor()
    student.delete_grade(5)
    student.report()


start_run()