import logging
import os
import pandas as pd

from niadic_py.data import CSV_FILE, XLSX_FILE


def convert_to_csv():
    xlsx_file_path = XLSX_FILE
    csv_file_path = CSV_FILE
    if os.path.exists(csv_file_path):
        logging.warning("exists.")
        return
    else:
        df = pd.read_excel(xlsx_file_path)
        df.to_csv(csv_file_path, index=False)
        logging.warning("done.")
        return


if __name__ == '__main__':
    convert_to_csv()
