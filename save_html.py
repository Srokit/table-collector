"Save table html to html file."

import os

# Set to true to see html files for each table in html out dir
ENABLE_HTML_SAVE = False

HTML_OUT_DIR = 'html_out'

def save_html(table: str, filename: str):
    """Save table html to html file."""
    if ENABLE_HTML_SAVE:
        with open(os.path.join(HTML_OUT_DIR, filename), 'w') as file:
            file.write(table)

