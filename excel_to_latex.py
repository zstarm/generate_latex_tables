import pandas as pd
import os

def excel_to_latex(excel_file):
    # Read the Excel file
    xls = pd.ExcelFile(excel_file)
    
    # Create an output directory for LaTeX files
    output_dir = 'latex_tables'
    os.makedirs(output_dir, exist_ok=True)
    
    # Iterate over each sheet in the Excel file
    for sheet_name in xls.sheet_names:
        # Read the sheet into a DataFrame
        df = pd.read_excel(xls, sheet_name=sheet_name)

        # Convert the DataFrame to LaTeX format
        latex_code = df.to_latex(index=False)

        # Create a filename for the LaTeX file
        latex_file_name = os.path.join(output_dir, f"{sheet_name}.tex")

        # Write the LaTeX code to the file
        with open(latex_file_name, 'w') as f:
            f.write(latex_code)

        print(f"Generated LaTeX file: {latex_file_name}")

# Example usage
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Generate LaTex table files from excel spreadsheet')
    parser.add_argument('excel_fname', type=str, help='file name of spreadsheet to convert to LaTex')
    args = parser.parse_args()
    excel_to_latex(args.excel_filename)

