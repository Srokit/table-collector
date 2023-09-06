"Clean the table data module"

import re

def clean_table(table_text: str):
    """Clean the table text data.

    Cleaning steps:
    - Remove all newline chars
    """
    # Remove all whitespace characters
    table_text = re.sub(r"\n", "", table_text)
    return table_text

