import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from invoice_parser import extract_invoice_data
from csv_writer import write_csv
from utils import is_due_or_overdue, wait_for_file


DOWNLOAD_DIR = os.path.abspath("downloads")
CSV_OUTPUT = os.path.abspath("output/result.csv")


def setup_driver():
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
    })
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def main():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    os.makedirs("output", exist_ok=True)

    driver = setup_driver()
    driver.get("https://rpachallengeocr.azurewebsites.net/")

    # iniciando
    driver.find_element(By.ID, "start").click()

    #tentativa primeira linha tabela
    row = driver.find_element(By.CSS_SELECTOR, "tbody tr")
    cells = row.find_elements(By.TAG_NAME, "td")

    invoice_id = cells[0].text.strip()
    due_date = cells[1].text.strip()
    download_button = cells[2].find_element(By.TAG_NAME, "button")

    # pdf
    download_button.click()
    pdf_path = wait_for_file(DOWNLOAD_DIR)


    if is_due_or_overdue(due_date):
        invoice_data = extract_invoice_data(pdf_path)

        write_csv([
            invoice_id,
            due_date,
            invoice_data["invoice_number"],
            invoice_data["invoice_date"],
            invoice_data["company_name"],
            invoice_data["total_due"],
        ], CSV_OUTPUT)

        # tentativa uploud csv
        upload_input = driver.find_element(By.ID, "fileUpload")
        upload_input.send_keys(CSV_OUTPUT)

    driver.quit()


if __name__ == "__main__":
    main()
