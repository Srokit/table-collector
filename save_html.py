"Save table html to html file."

import os

# Set to true to see html files for each table in html out dir
ENABLE_HTML_SAVE = False

HTML_OUT_DIR = 'html_out'

def save_html(table: str, filename: str):
    """Save table html to html file."""
    if ENABLE_HTML_SAVE:
        if os.path.exists(HTML_OUT_DIR):
            os.remove(HTML_OUT_DIR)
        if not os.path.exists(HTML_OUT_DIR):
            os.makedirs(HTML_OUT_DIR)
        with open(os.path.join(HTML_OUT_DIR, filename), 'w') as file:
            file.write(table)

