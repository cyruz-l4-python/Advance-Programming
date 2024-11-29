import tkinter as tk
from tkinter import ttk, messagebox
import os

os.chdir(os.path.dirname(__file__))
file_path = "studentMarks.txt"

class StudentManagerGUI:
    def __init__(self, master, student_data):
        self.master = master
        self.master.title("Student Manager")
        self.master.geometry("600x400")
        self.students = student_data
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Student Manager", font=("Arial", 16, "bold"), fg="purple", bg="lightyellow").pack(pady=10)
        button_frame = tk.Frame(self.master, bg="white")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="View All Student Records", command=self.view_all_records, bg="yellow", fg="black", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Show Highest Score", command=self.show_highest_score, bg="green", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Show Lowest Score", command=self.show_lowest_score, bg="red", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)

        self.student_names = [student['name'] for student in self.students]
        self.selected_student = tk.StringVar(value="Select a student")
        tk.Label(self.master, text="View Individual Student Record:", font=("Arial", 10, "bold"), bg="lightyellow").pack()
        dropdown_frame = tk.Frame(self.master, bg="lightyellow")
        dropdown_frame.pack(pady=5)
        self.student_dropdown = ttk.Combobox(dropdown_frame, textvariable=self.selected_student, values=self.student_names, width=30)
        self.student_dropdown.pack(side=tk.LEFT, padx=5)
        tk.Button(dropdown_frame, text="View Record", command=self.view_individual_record, bg="cyan", fg="black", font=("Arial", 10, "bold")).pack(side=tk.LEFT)

        self.output_box = tk.Text(self.master, height=10, width=70, bg="lightgray", fg="darkblue", font=("Arial", 12))
        self.output_box.pack(pady=10)
        self.output_box.config(state=tk.DISABLED)

        self.output_box.tag_configure("title", foreground="blue", font=("Arial", 12, "bold"))
        self.output_box.tag_configure("data", foreground="green", font=("Arial", 10))
        self.output_box.tag_configure("average", foreground="orange", font=("Arial", 10, "italic"))

    def view_all_records(self):
        self.output_box.config(state=tk.NORMAL)
        self.output_box.delete(1.0, tk.END)
        total_percentage = 0
        self.output_box.insert(tk.END, "Student Records:\n", "title")
        for student in self.students:
            self.output_box.insert(tk.END, self.format_student_data(student) + "\n", "data")
            total_percentage += student['overall_percentage']
        avg = total_percentage / len(self.students)
        self.output_box.insert(tk.END, f"\nTotal Students: {len(self.students)}", "data")
        self.output_box.insert(tk.END, f"\nAverage Percentage: {avg:.2f}%", "average")
        self.output_box.config(state=tk.DISABLED)

    def view_individual_record(self):
        name = self.selected_student.get()
        if name == "Select a student" or name not in self.student_names:
            messagebox.showerror("Error", "Pick a real student!")
            return
        self.output_box.config(state=tk.NORMAL)
        self.output_box.delete(1.0, tk.END)
        for student in self.students:
            if student['name'] == name:
                self.output_box.insert(tk.END, self.format_student_data(student) + "\n", "data")
                break
        self.output_box.config(state=tk.DISABLED)

    def show_highest_score(self):
        highest = max(self.students, key=lambda s: s["overall_percentage"])
        self.output_box.config(state=tk.NORMAL)
        self.output_box.delete(1.0, tk.END)
        self.output_box.insert(tk.END, "Student with Highest Overall Score:\n", "title")
        self.output_box.insert(tk.END, self.format_student_data(highest), "data")
        self.output_box.config(state=tk.DISABLED)

    def show_lowest_score(self):
        lowest = min(self.students, key=lambda s: s["overall_percentage"])
        self.output_box.config(state=tk.NORMAL)
        self.output_box.delete(1.0, tk.END)
        self.output_box.insert(tk.END, "Student with Lowest Overall Score:\n", "title")
        self.output_box.insert(tk.END, self.format_student_data(lowest), "data")
        self.output_box.config(state=tk.DISABLED)

    def format_student_data(self, student):
        return (
            f"Name: {student['name']}\n"
            f"Number: {student['number']}\n"
            f"Coursework Total: {student['coursework_total']}\n"
            f"Exam Mark: {student['exam_mark']}\n"
            f"Overall Percentage: {student['overall_percentage']}%\n"
            f"Grade: {student['grade']}\n"
        )

def load_student_data(file_path):
    students = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line in lines[1:]:
        student_data = line.strip().split(",")
        student_number = int(student_data[0])
        name = student_data[1]
        coursework_marks = list(map(int, student_data[2:5]))
        exam_mark = int(student_data[5])
        coursework_total = sum(coursework_marks)
        overall_percentage = round(((coursework_total + exam_mark) / 160) * 100, 2)
        grade = 'A' if overall_percentage >= 70 else 'B' if overall_percentage >= 60 else 'C' if overall_percentage >= 50 else 'D' if overall_percentage >= 40 else 'F'
        students.append({
            "number": student_number,
            "name": name,
            "coursework_total": coursework_total,
            "exam_mark": exam_mark,
            "overall_percentage": overall_percentage,
            "grade": grade
        })
    return students

if __name__ == "__main__":
    try:
        student_data = load_student_data(file_path)
        root = tk.Tk()
        app = StudentManagerGUI(root, student_data)
        root.mainloop()
    except FileNotFoundError:
        print("Error: File not found.")
