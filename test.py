"""Student grade management system."""


class Student:
    """Represents a student and their grades."""

    def __init__(self, student_id, name):
        """Initialize a student."""
        if not student_id or not name:
            raise ValueError("Student ID and name cannot be empty.")

        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor_roll = False
        self.letter_grade = "F"

    def add_grade(self, grade):
        """Add a valid grade to the student."""
        if not isinstance(grade, (int, float)):
            print("Error: Grade must be numeric.")
            return

        if grade < 0 or grade > 100:
            print("Error: Grade must be between 0 and 100.")
            return

        self.grades.append(grade)

    def calculate_average(self):
        """Calculate the student's average grade."""
        if not self.grades:
            return 0.0

        return sum(self.grades) / len(self.grades)

    def update_status(self):
        """Update letter grade, pass status, and honor roll status."""
        average = self.calculate_average()

        if average >= 90:
            self.letter_grade = "A"
        elif average >= 80:
            self.letter_grade = "B"
        elif average >= 70:
            self.letter_grade = "C"
        elif average >= 60:
            self.letter_grade = "D"
        else:
            self.letter_grade = "F"

        self.is_passed = average >= 60
        self.honor_roll = average >= 90

    def remove_grade_by_index(self, index):
        """Remove a grade using its index."""
        if not isinstance(index, int):
            print("Error: Index must be an integer.")
            return

        if index < 0 or index >= len(self.grades):
            print("Error: Grade index is out of bounds.")
            return

        self.grades.pop(index)

    def remove_grade_by_value(self, grade):
        """Remove a grade using its value."""
        if grade not in self.grades:
            print("Error: Grade value was not found.")
            return

        self.grades.remove(grade)

    def report(self):
        """Print the student's summary report."""
        self.update_status()
        average = self.calculate_average()

        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Grades Count:", len(self.grades))
        print("Average:", round(average, 2))
        print("Letter Grade:", self.letter_grade)
        print("Status:", "Passed" if self.is_passed else "Failed")
        print("Honor Roll:", self.honor_roll)


def start_run():
    """Run an example of the student grade system."""
    try:
        student = Student("001", "John Doe")

        student.add_grade(100)
        student.add_grade(85)
        student.add_grade(95)

        student.add_grade("Fifty")
        student.add_grade(120)

        student.remove_grade_by_value(85)
        student.remove_grade_by_index(5)

        student.report()

    except ValueError as error:
        print("Error:", error)


start_run()
