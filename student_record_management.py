# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 20:28:27 2024

@author: Admin
"""

import csv
import os
import re
import matplotlib.pyplot as plt

class Student:
    def __init__(self, name, branch, semester, section, mobile, email, dbms_marks, python_marks, atcd_marks, java_marks, se_marks):
        self.name = name
        self.branch = branch
        self.semester = semester
        self.section = section
        self.mobile = mobile
        self.email = email
        self.dbms_marks = dbms_marks
        self.python_marks = python_marks
        self.atcd_marks = atcd_marks
        self.java_marks = java_marks
        self.se_marks = se_marks
        self.total_marks = dbms_marks + python_marks + atcd_marks + java_marks + se_marks
        self.average_marks = self.total_marks / 5

    def accept(self):
        self.name = input("Enter Student Name: ")
        self.branch = input("Enter Student Branch: ")
        while True:
            try:
                self.semester = int(input("Enter Student Semester: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer for Semester.")
        self.section = input("Enter Student Section: ")
        while True:
            self.mobile = input("Enter Student Mobile Number (10 digits only): ")
            if self.mobile.isdigit() and len(self.mobile) == 10:
                break
            else:
                print("Invalid input! Mobile number must contain 10 digits and no characters.")
        while True:
            self.email = input("Enter Student Gmail (name@gmail.com): ")
            if re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', self.email):
                break
            else:
                print("Invalid input! Email must be in the format name@gmail.com.")
        self.dbms_marks = int(input("Enter Marks in DBMS: "))
        self.python_marks = int(input("Enter Marks in Python: "))
        self.atcd_marks = int(input("Enter Marks in ATCD: "))
        self.java_marks = int(input("Enter Marks in Java: "))
        self.se_marks = int(input("Enter Marks in Software Engineering: "))
        self.total_marks = self.dbms_marks + self.python_marks + self.atcd_marks + self.java_marks + self.se_marks
        self.average_marks = self.total_marks / 5

        student_info = {'Name': self.name, 'Branch': self.branch, 'Semester': self.semester, 'Section': self.section,
                        'Mobile Number': self.mobile, 'Gmail': self.email, 'Marks in DBMS': self.dbms_marks,
                        'Marks in Python': self.python_marks, 'Marks in ATCD': self.atcd_marks,
                        'Marks in Java': self.java_marks, 'Marks in Software Engineering': self.se_marks,
                        'Total Marks': self.total_marks, 'Average Marks': self.average_marks}
        ls.append(student_info)

        with open('student_details.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=student_info.keys())
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(student_info)

    @staticmethod
    def display(student_info):
        print("Name : ", student_info['Name'])
        print("Branch : ", student_info['Branch'])
        print("Semester : ", student_info['Semester'])
        print("Section : ", student_info['Section'])
        print("Mobile Number : ", student_info['Mobile Number'])
        print("Gmail : ", student_info['Gmail'])
        print("Marks in DBMS : ", student_info['Marks in DBMS'])
        print("Marks in Python : ", student_info['Marks in Python'])
        print("Marks in ATCD : ", student_info['Marks in ATCD'])
        print("Marks in Java : ", student_info['Marks in Java'])
        print("Marks in Software Engineering : ", student_info['Marks in Software Engineering'])
        print("Total Marks : ", student_info['Total Marks'])
        print("Average Marks : ", student_info['Average Marks'])
        print("\n")

    @staticmethod
    def search(name):
        for student_info in ls:
            if student_info['Name'] == name:
                return student_info
        return None

    @staticmethod
    def delete(delete_name):
        for i, student_info in enumerate(ls):
            if student_info['Name'] == delete_name:
                deleted_student = ls.pop(i)
                print("Student '{}' deleted successfully.".format(deleted_student['Name']))

                with open('student_details.csv', mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=student_info.keys())
                    writer.writeheader()
                    writer.writerows(ls)
                return
        print("Student '{}' not found.".format(delete_name))

    @staticmethod
    def load_from_csv():
        if os.path.exists('student_details.csv'):
            with open('student_details.csv', mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    ls.append(row)

    @staticmethod
    def plot_marks():
        dbms_marks = [int(student.get('Marks in DBMS', 0)) for student in ls]
        python_marks = [int(student.get('Marks in Python', 0)) for student in ls]
        atcd_marks = [int(student.get('Marks in ATCD', 0)) for student in ls]
        java_marks = [int(student.get('Marks in Java', 0)) for student in ls]
        se_marks = [int(student.get('Marks in Software Engineering', 0)) for student in ls]

        # Calculate the maximum marks for each subject
        max_dbms = max(dbms_marks)
        max_python = max(python_marks)
        max_atcd = max(atcd_marks)
        max_java = max(java_marks)
        max_se = max(se_marks)

        # Set the maximum value of bins based on the maximum marks obtained
        max_marks = max(max_dbms, max_python, max_atcd, max_java, max_se)

        plt.figure(figsize=(10, 6))
        # Dynamically set the range of bins for each subject
        plt.hist(dbms_marks, bins=max_marks, range=(0, max_dbms), color='blue', alpha=0.5, label='DBMS Marks')
        plt.hist(python_marks, bins=max_marks, range=(0, max_python), color='green', alpha=0.5, label='Python Marks')
        plt.hist(atcd_marks, bins=max_marks, range=(0, max_atcd), color='orange', alpha=0.5, label='ATCD Marks')
        plt.hist(java_marks, bins=max_marks, range=(0, max_java), color='purple', alpha=0.5, label='Java Marks')
        plt.hist(se_marks, bins=max_marks, range=(0, max_se), color='red', alpha=0.5, label='Software Engineering Marks')
        plt.xlabel('Marks')
        plt.ylabel('Frequency')
        plt.title('Distribution of Student Marks')
        plt.legend()
        plt.show()


ls = []

Student.load_from_csv()

while True:
    print("\n********* Welcome to Student Information Management System  **********")
    print("1. Add Student\n2. Search Student\n3. Delete Student\n4. Plot Marks\n5. Exit")
    choice = input("Enter your choice 1, 2, 3, 4, 5: ")

    if choice == '1':
        obj = Student('', '', 0, '', '', '', 0, 0, 0, 0, 0)
        obj.accept()
    elif choice == '2':
        search_name = input("Enter the name of the student to search: ")
        student_info = Student.search(search_name)
        if student_info:
            print("\nStudent Found, Details are:")
            Student.display(student_info)
        else:
            print("Student not found.")
    elif choice == '3':
        delete_name = input("Enter the name of the student to delete: ")
        Student.delete(delete_name)
    elif choice == '4':
        Student.plot_marks()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option.")

print("Thank You for using our SIM system!")
