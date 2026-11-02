# Miguel Viloria Abreu
# Programming Exercise (Módulo de archivos CSV - Calificaciones)

import csv


def write_sales_to_file():
    """Brief description of the function:
    Prompts the instructor for student details and writes them to grades.csv.

    Parameters:
    None

    Variables:
    - num_students (int): Number of students to input.
    - file_name (str): The name of the CSV file.
    - header (list): Column headers for the CSV file.
    - students_data (list): Collected rows of student records.
    - first_name (str): Student's first name.
    - last_name (str): Student's last name.
    - exam1 (int): First exam grade.
    - exam2 (int): Second exam grade.
    - exam3 (int): Third exam grade.

    Logical steps of the function:
    1. Ask the user for the number of students.
    2. Open grades.csv for writing using the csv module and with keyword.
    3. Write the header row.
    4. Loop through the number of students to gather names and 3 exam grades.
    5. Write each student's record into the CSV file.

    Return:
    None
    """
    # Store the filename in a constant or string variable
    file_name = "grades.csv"

    # Define the header for the CSV file
    header = ["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"]

    # Prompt the instructor for how many students to enter
    num_students = int(input("Enter the number of students to enter: "))

    # Open the file in write mode using the with keyword and csv module
    with open(file_name, mode="w", newline="", encoding="utf-8") as csv_file:
        # Create a csv writer object
        writer = csv.writer(csv_file)

        # Write the header row into the csv file
        writer.writerow(header)

        # Loop through the specified number of students
        for i in range(num_students):
            # Print current student index for clarity
            print(f"\nEntering details for student {i + 1}:")

            # Prompt the instructor for the student's first name
            first_name = input("Enter first name: ")

            # Prompt the instructor for the student's last name
            last_name = input("Enter last name: ")

            # Prompt the instructor for the first exam grade as an integer
            exam1 = int(input("Enter grade for Exam 1: "))

            # Prompt the instructor for the second exam grade as an integer
            exam2 = int(input("Enter grade for Exam 2: "))

            # Prompt the instructor for the third exam grade as an integer
            exam3 = int(input("Enter grade for Exam 3: "))

            # Create a list representing the current student record
            student_record = [first_name, last_name, exam1, exam2, exam3]

            # Write the student record into the csv file
            writer.writerow(student_record)

    # Print a confirmation message once writing is complete
    print(f"\nData successfully written to {file_name}.")


def read_and_total_sales():
    """Brief description of the function:
    Reads the grades.csv file and displays the data in tabular format.

    Parameters:
    None

    Variables:
    - file_name (str): The name of the CSV file to read.

    Logical steps of the function:
    1. Open grades.csv for reading using the with keyword and csv module.
    2. Iterate through each row in the CSV file.
    3. Format and display each row nicely in a tabular layout on the console.

    Return:
    None
    """
    # Store the filename in a variable
    file_name = "grades.csv"

    # Print a header for the tabular display output
    print(f"\n--- Reading Data from {file_name} ---")

    # Open the file in read mode using the with keyword
    with open(file_name, mode="r", encoding="utf-8") as csv_file:
        # Create a csv reader object
        reader = csv.reader(csv_file)

        # Loop through each row in the csv reader
        for row in reader:
            # Format and print the row data in a neat tabular layout
            print(
                f"{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<10} {row[4]:<10}"
            )


if __name__ == "__main__":
    # Call the function to write student grades to the CSV file
    write_sales_to_file()

    # Call the function to read and display the student grades in tabular format
    read_and_total_sales()