import csv
import os


def write_csv(data, output_path):
    headers = [
        "ID",
        "Due Date",
        "Invoice Number",
        "Invoice Date",
        "Company Name",
        "Total Due"
    ]

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerow(data)
