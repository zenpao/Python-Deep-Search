import os
import fnmatch
from tqdm import tqdm
from bs4 import BeautifulSoup
import PyPDF2
import textract

def search_files(root, pattern, content, folders=None):
    matches = []

    total_files = 0
    processed_files = 0

    # Count the total number of relevant files
    for path, dirs, files in os.walk(root):
        if folders is None or any(folder in path for folder in folders):
            for filename in fnmatch.filter(files, pattern):
                total_files += 1

    # Split the content input into individual search terms
    search_terms = [term.strip().lower() for term in content.split(',')]

    # Search for files and update progress
    with tqdm(total=total_files, unit='file') as pbar:
        for path, dirs, files in os.walk(root):
            if folders is None or any(folder in path for folder in folders):
                for filename in fnmatch.filter(files, pattern):
                    file_path = os.path.join(path, filename)

                    # Check if content exists in file name or file content
                    if any(term in filename.lower() for term in search_terms) or contains_content(file_path, search_terms):
                        matches.append(file_path)
                        print(file_path)  # Print file path as soon as a match is found
                        print("\nMatched files found so far:")
                        for i, matched_file in enumerate(matches, 1):
                            print(f"{i}. {matched_file}")
                        print("=" * 50)  # Print separator for clarity

                    processed_files += 1
                    pbar.update(1)  # Update the progress bar

    return matches

def contains_content(file_path, search_terms):
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    with open(file_path, 'rb') as file:
        file_content = None

        if file_extension == '.pdf':
            pdf_reader = PyPDF2.PdfReader(file)
            file_content = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                file_content += page.extract_text()

        elif file_extension in ['.docx', '.doc', '.pptx', '.ppt', '.xlsx', '.xls']:
            try:
                file_content = textract.process(file_path).decode('utf-8')
            except Exception as e:
                print(f"Error extracting text from {file_path}: {e}")

        elif file_extension == '.html':
            file_content = BeautifulSoup(file, 'html.parser').get_text()

        else:
            file_content = file.read().decode('utf-8').lower()

        if file_content and any(term in file_content for term in search_terms):
            return True

    return False



print("""\n
========================NOTICE==========================
THIS IS A TOOL FOR SEARCHING FILES WITH PARAMETERS.

INTENDED FOR SPECIFIC-USE ONLY.
(Such as: Documents with specific file names or content)
=========================V3.2===========================
""")

# Prompt user for directory
directory = input("Enter the directory to search in: ")

# Prompt user for file pattern
file_pattern = input("Enter the file pattern or extension (e.g., *.txt, *.html, *.docx, *.pdf): ")

# Prompt user for folder names to search in
folder_input = input("Enter the folder names to search in (separated by commas) or leave empty to search in all folders: ")
folders = [folder.strip() for folder in folder_input.split(',')] if folder_input else None

# Example usage
search_content = input("Enter the content you want to search for (separated by commas): ")

results = search_files(directory, file_pattern, search_content, folders)

if results:
    print("\n[!] Search completed. Documents containing the specified content or matching file name:")
    for file_path in results:
        print(file_path)
else:
    print("\nNo matching documents found.")

# Save results to a text file in the same directory as the program
output_file = os.path.join(os.getcwd(), "search_results.txt")
with open(output_file, 'w') as file:
    if results:
        file.write(f"Search results ({search_content}, {file_pattern}):\n")
        for file_path in results:
            file.write(file_path + "\n")
    else:
        file.write(f"No matching documents found ({search_content}, {file_pattern}).")

print(f"\nSearch results saved to {output_file}")
print(f"Output file directory: {os.path.dirname(os.path.abspath(output_file))}")

# Prompt user to press any key to continue
input("Press any key to continue...")
