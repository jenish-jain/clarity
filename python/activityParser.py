from bs4 import BeautifulSoup
import re
from datetime import datetime

def parse_transaction_info(text):
    text = re.sub(r"\s{2,}", " ", text)
    amount_pattern = r"(₹)([0-9,]+)\.\d{2}"
    title_account_pattern = r"Paid\s+₹[\d\.]+\s+to\s+(.*?)(?: using Bank Account (.*?))?(?=[A-Z][a-z]{2}\s\d{1,2},)"
    time_pattern = r"([A-Z][a-z]{2} \d{1,2}, \d{4}, \d{1,2}:\d{2}:\d{2}\s*(?:PM|AM))"

    amount_match = re.search(amount_pattern, text)
    title_account_match = re.search(title_account_pattern, text)
    time = re.search(time_pattern, text)

    if time:
        time_str = time.group(1).replace("\u202f", " ")
        time = datetime.strptime(time_str, "%b %d, %Y, %I:%M:%S %p")
        time = time.strftime("%d-%m-%Y")
    
    if amount_match:
        amount = int(amount_match.group(2).replace(",", ""))

    return {
        "currency": amount_match.group(1) if amount_match else None,
        "amount": amount if amount_match else None,
        "title": title_account_match.group(1).strip() if title_account_match else None,
        "account": (
            title_account_match.group(2)
            if title_account_match and title_account_match.group(2)
            else None
        ),
        "time": time if time else None,
    }


def parse_product_info(text):
    parts = text.split("\u2003")
    if len(parts) >= 3:
        product = parts[0]
        transactionId = parts[1]
        status = parts[2]
    else:
        product = transactionId = status = None

    return {"product": product, "transactionId": transactionId, "status": status}

def parse_html_to_json(html):
    soup = BeautifulSoup(html, "html.parser")
    outer_cells = soup.find_all(
        "div", {"class": "outer-cell mdl-cell mdl-cell--12-col mdl-shadow--2dp"}
    )
    transaction_list = []
    for outer_cell in outer_cells:

        content_cells = outer_cell.find_all(
            "div",
            {"class": "content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1"},
        )
        transaction_info_raw = content_cells[0].text.replace("\n", "").strip()
        transaction_info = parse_transaction_info(transaction_info_raw)
        product_info = outer_cell.find(
            "div",
            {"class": "content-cell mdl-cell mdl-cell--12-col mdl-typography--caption"},
        ).text.strip()
        product_info = (
            product_info.replace("Products:", "").replace("Details:", "").split("\n")
        )
        products_raw = product_info[0].strip()
        products = parse_product_info(products_raw)

        json_entry = {
            "currency": transaction_info["currency"],
            "amount": transaction_info["amount"],
            "title": transaction_info["title"],
            "account": transaction_info["account"],
            "time": transaction_info["time"],
            "product": products["product"],
            "transactionId": products["transactionId"],
            "status": products["status"],
        }
        transaction_list.append(json_entry)

    return transaction_list
