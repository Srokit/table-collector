"Code that controls writing dataset to text file"

def write_to_text_file(filename: str, html: str):
    "Write html to text file"
    # Open file for appending
    with open(filename, 'a') as file:
        file.write(html)
        file.write('\n')

