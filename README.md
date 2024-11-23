# Student Performance Tracker

This script is designed to manage and track student performance. It calculates individual and class averages and determines the passing status of students based on their scores.

---

## **Features**

1. **Student Class**  
   Manages individual student data and operations like calculating average scores and determining passing status.
2. **PerformanceTracker Class**  
   Handles multiple students, calculating class averages and displaying performance.

3. **Error Handling**  
   Includes checks for valid score inputs to prevent runtime errors.

4. **Interactive Input**  
   Collects student data interactively, allowing users to manage multiple students efficiently.

---

## **Code Breakdown**

### 1. **Student Class**

#### Methods:

- `__init__(self, name, scores)`  
  Initializes the student instance with a name and a list of scores.

- `calculate_average(self)`  
  Calculates the average score using:

  ```python
  return sum(self.scores.values()) / len(self.scores.values())
  ```

- `is_passing(self, passing_score=40)`  
  Checks if all scores meet or exceed the passing score (default: 40).

---

### 2. **PerformanceTracker Class**

#### Methods:

- `__init__(self)`  
  Initializes an empty dictionary to store student objects.

- `add_student(self, name, scores)`  
  Adds a student to the dictionary:

  ```python
  self.students[name] = Student(name, scores)
  ```

- `calculate_class_average(self)`  
  Computes the average score across all students. Returns `0` if no students are present:

  ```python
  if not self.students:
      return 0
  ```

- `display_student_performance(self)`  
  Prints each student's Name and each book name with score also average score and their passing status.

---

### 3. \*\*Helper Function: `get_student_data()`

- Prompts the user to enter a student's name and scores for three subjects.
- Handles invalid input using a `try...except` block:
  ```python
        try:
            name = input("Enter student's name (or 'done' to finish): ")
            if name.lower() == 'done':
                break
            while True:
                subject=input("Enter subject name (or 'done' to finish): ")
                if subject.lower() == 'done':
                    break
                score = int(input(f"Enter {subject} score: "))
                scores[subject]=score
            return name, scores
        except ValueError:
            print("Invalid input. Please enter numeric values for scores.")
  ```

---

### 4. **Main Function**

- Initializes a `PerformanceTracker` object.
- Repeatedly collects student data using `get_student_data()`.
- Adds valid data to the tracker or exits when the user types "done".
- Displays all student performances and the class average:
  ```python
  tracker.display_student_performance()
  print(f"\nClass Average: {class_avg:.2f}")
  ```

---

## **Error Handling**

1. **Invalid Input**

   - The `get_student_data()` function ensures numeric scores are entered. If not, it catches the `ValueError` and prompts the user to re-enter data.

2. **Empty Class Check**
   - In `calculate_class_average`, the code prevents division by zero by returning `0` if no students are added.

---

## **How to Run**

1. Save the script to a `.py` file.
2. Run the script in your Python environment.
3. Follow prompts to enter student names and scores.
4. Type "done" to finish entering data.
5. View individual performances and the class average.

---

## **Sample Output**

```
Student Performance:

Performance for Umer:
  OOP: 89
  Data Base: 78
  DSA: 98
  Average = 88.33, Status = Passing

Performance for Ali:
  OOp: 97
  DSA: 78
  Average = 87.50, Status = Passing

Class Average: 87.92
```

---

This markdown file explains the purpose, functionality, and error-handling features of your code.
