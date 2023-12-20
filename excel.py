import openpyxl

# Function to read conversation from a file and write to Excel
def extract_from_file_and_write_to_excel(file_path):
    # Initialize Excel workbook and sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Write headers to Excel sheet
    sheet["A1"] = "Employee ID"
    sheet["B1"] = "Name"
    sheet["C1"] = "Tech Stack"
    sheet["D1"] = "Result"

    # Read conversation from file
    with open(file_path, 'r') as file:
        lines = file.readlines()
        employee_id = lines[4].strip().split(": ")[1]
        user_name = lines[6].strip().split(": ")[1]
        tech_stack = lines[8].strip().split(": ")[1]
        result = lines[-1].strip().split(": ")[1]

        # Write responses to Excel sheet
        sheet.append([employee_id, user_name, tech_stack, result])

    # Save Excel file
    workbook.save("interview_responses.xlsx")
    print("Interview responses saved to interview_responses.xlsx")

# Specify the path to your text file (user_input.txt)
file_path = "user_input.txt"

# Run the extraction and write to Excel
extract_from_file_and_write_to_excel(file_path)
