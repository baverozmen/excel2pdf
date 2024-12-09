# PDF-Excel Search Tool

This is a Python-based GUI application that allows you to search for specific terms in a PDF file and compare them against data in an Excel file. It uses the **Tkinter** library for the graphical interface, **PyPDF2** for extracting text from PDF files, and **pandas** for working with Excel files.

---

## Features

- Load a PDF file and extract its text content.
- Load an Excel file and search specific columns for a term.
- Compare terms found in the Excel file with the content of the PDF.
- Displays results directly in the application.

---

## Requirements

### Python Version

- Python 3.x

### Required Libraries

Install the necessary dependencies by running the following command:

```bash
pip install pandas PyPDF2 tkinter
```
---

## How to Use
1. Run the Application Run the script with the following command:
2. Load the PDF File
- Click the "Browse" button next to the PDF file field.
- Select a PDF file from your system.
### 3. Load the Excel File
- Click the "Browse" button next to the Excel file field.
- Select an Excel file (.xlsx) from your system.

### 4. Enter Column Name

- Enter the name of the column in the Excel file to search for terms.

### 5. Enter Search Term

- Specify the term to search for in the Excel file.
### 6. Additional Searches (Optional)

- If additional searches are required, specify the relevant column or field.
### 7. Start Search

- Click the "Search" button to start the process.
- Results will be displayed in the results section.
## File Structure
- ` main.py `: The main script containing the application logic and GUI implementation.
- Dependencies: The application relies on the following Python libraries:
      -`pandas`
      -`PyPDF2`
      -`tkinter`
---

## Example Usage
1. PDF File: sample.pdf
2. Excel File: data.xlsx
3. Column Name: Name
4. Search Term: John Doe
5. Additional Searches: Leave empty or provide a specific column name.
Result:

```Copy code
 
Found! John Doe
Found! Jane Smith
John Wick not found.

```
--- 

## Acknowledgements
- Tkinter: For creating the graphical user interface.
- PyPDF2: For extracting text from PDF files.
- pandas: For working with Excel files efficiently.

---

## License
This project is licensed under the  [MIT Lisansı](LICENSE).
