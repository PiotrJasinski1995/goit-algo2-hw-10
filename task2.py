# Definition of the Teacher class
class Teacher:
    def __init__(self, first_name, last_name, age, email, subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.subjects = set(subjects)
        self.assigned_subjects = set()

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


def create_schedule(subjects, teachers):
    """
    Assign teachers to cover all required subjects using a greedy strategy:
    - At each step, pick the teacher who can cover the largest number
      of still-uncovered subjects.
    - If there is a tie, pick the youngest teacher.
    """
    uncovered = set(subjects)
    final_schedule = []

    while uncovered:
        # Choose the best teacher for this step
        best_teacher = max(
            teachers,
            key=lambda t: (len(t.subjects & uncovered), -t.age)
        )

        # Determine which subjects they can cover right now
        subjects_covered = best_teacher.subjects & uncovered
        if not subjects_covered:
            # No teacher can cover remaining subjects
            return None

        best_teacher.assigned_subjects = subjects_covered
        final_schedule.append(best_teacher)

        # Remove covered subjects from the uncovered set
        uncovered -= subjects_covered

    return final_schedule


if __name__ == '__main__':
    # Set of subjects
    subjects = {"Mathematics", "Physics", "Chemistry", "Informatics", "Biology"}
    # Creating a list of teachers
    teachers = [
        Teacher("Alexander", "Evans", 45, "a.evans@example.com", {"Mathematics", "Physics"}),
        Teacher("Maria", "Peterson", 38, "m.peterson@example.com", {"Chemistry"}),
        Teacher("George", "Collins", 50, "g.collins@example.com", {"Informatics", "Mathematics"}),
        Teacher("Natalie", "Stevens", 29, "n.stevens@example.com", {"Biology", "Chemistry"}),
        Teacher("Daniel", "Brown", 35, "d.brown@example.com", {"Physics", "Informatics"}),
        Teacher("Helen", "Grant", 42, "h.grant@example.com", {"Biology"}),
    ]
    # Calling the function to create the schedule
    schedule = create_schedule(subjects, teachers)

    # Outputting the schedule
    if schedule:
        print("Class Schedule:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} years old, email: {teacher.email}")
            print(f"   Teaches subjects: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("It is impossible to cover all subjects with the available teachers.")
