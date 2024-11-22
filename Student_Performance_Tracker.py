class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores.values()) / len(self.scores.values())

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores.values())
class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        if not self.students:
            return 0
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)

    def display_student_performance(self):
        for student in self.students.values():
            average_score = student.calculate_average()
            status = "Passing" if student.is_passing() else "Failing"
            print(f"{student.name}: Average = {average_score:.2f}, Status = {status}")
def get_student_data():
    while True:
        scores={}
        try:
            name = input("Enter student's name (or 'done' to finish): ")
            if name.lower() == 'done':
                break
            subject=input("Enter subject name (or 'done' to finish): ")
            if subject.lower() == 'done':
                break
            scores = int(input(f"Enter {subject} score: "))
            scores[subject]=scores 
            return name, scores
        except ValueError:
            print("Invalid input. Please enter numeric values for scores.")
def main():
    tracker = PerformanceTracker()
    try:

        while True:
            student_data = get_student_data()
            if student_data:
                name, scores = student_data
                tracker.add_student(name, scores)
            else:
                break

        print("\nStudent Performance:")
        tracker.display_student_performance()

        class_avg = tracker.calculate_class_average()
        print(f"\nClass Average: {class_avg:.2f}")
    except ValueError as e:
        print (f"Error {str(e)}")

if __name__ == "__main__":
    main()
