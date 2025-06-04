import os
import csv
from fpdf import FPDF

# Step 1: Read data from CSV file
def read_csv_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    if not data:
        raise ValueError(f"The file {file_path} is empty.")
    header = data[0]
    rows = data[1:]
    # Check if all rows have the same number of columns as the header
    if any(len(row) != len(header) for row in rows):
        raise ValueError(f"The CSV file has rows with inconsistent number of columns.")
    return header, rows

# Step 2: Analyze data (e.g., calculate total number of records)
def analyze_data(rows):
    total_records = len(rows)
    return total_records

# Step 3: Generate PDF report
def generate_pdf_report(header, rows, total_records):
    # Create FPDF object
    pdf = FPDF()
    pdf.add_page()
    
    # Set effective page width
    epw = pdf.w - 2 * pdf.l_margin
    
    # Add title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(epw, 10, "Sample Report", 0, 1, 'C')
    
    # Add total records
    pdf.set_font("Arial", '', 12)
    pdf.cell(epw, 10, f"Total records: {total_records}", 0, 1)
    
    # Add table header
    pdf.set_font("Arial", 'B', 12)
    num_cols = len(header)
    col_width = epw / num_cols
    for col in header:
        pdf.cell(col_width, 10, col, 1, 0, 'C')
    pdf.ln()
    
    # Add table data
    pdf.set_font("Arial", '', 12)
    for row in rows:
        for i, col in enumerate(row):
            pdf.cell(col_width, 10, str(col), 1, 0, 'L')
        pdf.ln()
    
    # Save PDF
    pdf.output("report.pdf")

# Main function
def main():
    # Specify the CSV file path
    csv_file_path = 'car.csv'
    
    try:
        # Step 1: Read CSV
        header, rows = read_csv_file(csv_file_path)
        
        # Step 2: Analyze data
        total_records = analyze_data(rows)
        
        # Step 3: Generate PDF
        generate_pdf_report(header, rows, total_records)
        
        print("PDF report generated successfully as 'report.pdf'.")
    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the file exists in the correct directory.")
    except ValueError as e:
        print(f"Error: {e}. Please check the CSV file content.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
