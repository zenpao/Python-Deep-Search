def convert_to_hyperlinks(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    formatted_content = ""
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespaces and newlines
        formatted_content += f'<a href="{line}">{line}</a><br>\n'

    return formatted_content

def save_as_html(output_file, content):
    with open(output_file, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    input_file_name = "search_results.txt"  # Replace with the name of your input file
    output_file_name = "search_results.html"

    print("""\n
========================NOTICE==========================
THIS IS A TOOL FOR CONVERTING RESULTS INTO HYPERLINKS.

INTENDED FOR SPECIFIC-USE ONLY.
========================NOTICE==========================
""")

    formatted_content = convert_to_hyperlinks(input_file_name)
    save_as_html(output_file_name, formatted_content)

    print(f"Conversion successful! Output saved to '{output_file_name}'")

# Prompt user to press any key to continue
input("Press any key to continue...")