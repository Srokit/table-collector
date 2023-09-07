"Validator for the table html text."

NUMERIC_PERCENTAGE = 0.25
MIN_TDS = 6

import re

import bs4

def table_is_valid(table_html: str) -> bool:
    """Return True iff table_html is a valid table.

    Valid tables fit these rules:
    1. The table has NUMERIC_PERCENTAGE % of td tags
        filled w/ only numeric values.
    2. Table has atleast MIN_TDS td tags.
    """
    numeric_pattern = r"-*\$*\d+\.*\:*\d*\-*\d*\.*\:*\d*\%*"
    # Iterate through all td tags and count the number of numeric ones.
    soup = bs4.BeautifulSoup(table_html, "html.parser")
    td_tags = soup.find_all("td")
    num_numeric = 0
    for td_tag in td_tags:
        td_tag_text = td_tag.text.strip().replace(",", "")
        td_tag_text = re.sub(r"\s+", "", td_tag_text)
        if re.fullmatch(numeric_pattern, td_tag.text.strip()) is not None:
            num_numeric += 1
    has_min_tds = len(td_tags) >= MIN_TDS
    # So that below line does not trigger a divide by zero error.
    if len(td_tags) == 0:
        return False
    has_numeric_percentage = num_numeric / len(td_tags) >= NUMERIC_PERCENTAGE
    return has_min_tds and has_numeric_percentage
