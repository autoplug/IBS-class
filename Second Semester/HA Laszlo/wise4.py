#!/bin/python3

import math
import os
import random
import re
import sys
import requests


import requests
import json
#
# Complete the 'maximumTransfer' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING name
#  2. STRING city
# API URL: https://jsonmock.hackerrank.com/api/transactions?page={page_no}
#


def maximumTransfer(name, city):
    # Write your code here
    page = requests.get("https://jsonmock.hackerrank.com/api/transactions")
    data = json.loads(page.content)
    pages = data["total_pages"]
    debit_str = ""
    credit_str = ""
    debit = 0
    credit = 0
    for i in range(pages):
        page = requests.get(
            f"https://jsonmock.hackerrank.com/api/transactions?page={i}")
        data = json.loads(page.content)
        data = data["data"]

        for item in data:
            # print(item["userName"], "---", item["location"]["city"])
            if item["userName"].strip() == name and item["location"]["city"].strip() == city:
                if item["txnType"] == "debit" and float(item['amount'][1:].replace(",", "")) > debit:
                    debit = float(item['amount'][1:].replace(",", ""))
                    debit_str = item['amount']
                if item["txnType"] == "credit" and float(item["amount"][1:].replace(",", "")) > credit:
                    credit = float(item["amount"][1:].replace(",", ""))
                    credit_str = item["amount"]
    return credit_str, debit_str


print(maximumTransfer("Bob Martin", "Bourg"))
# maximumTransfer("Helena Fernandez", "Ilcheste")
