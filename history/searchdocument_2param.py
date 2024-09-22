import os
import fnmatch
from tqdm import tqdm
from bs4 import BeautifulSoup

def search_files(root, pattern, content):
    matches = []

    total_files = 0
    processed_files = 0

    # Count the total number of relevant files
    for path, dirs, files in os.walk(root):
        for filename in fnmatch.filter(files, pattern):
            total_files += 1

    # Split the content input into individual search terms
    search_terms = [term.strip().lower() for term in content.split(',')]

    # Search for files and update progress
    with tqdm(total=total_files, unit='file') as pbar:
        for path, dirs, files in os.walk(root):
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

    with open(file_path, 'r') as file:
        file_content = file.read().lower()

        if file_extension == '.html':
            soup = BeautifulSoup(file_content, 'html.parser')
            file_content = soup.get_text()

        if any(term in file_content for term in search_terms):
            return True
    return False


print("""\n
========================NOTICE==========================
THIS IS A TOOL FOR SEARCHING FILES WITH PARAMETERS.

INTENDED FOR SPECIFIC-USE ONLY.
(Such as: Documents with specific file names or content)
========================NOTICE==========================
""")

# Prompt user for directory
directory = input("Enter the directory to search in: ")

# Prompt user for file pattern
file_pattern = input("Enter the file pattern or extension (e.g., *.txt, *.html): ")

# Example usage
search_content = input("Enter the content you want to search for (separated by commas): ")

results = search_files(directory, file_pattern, search_content)

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
