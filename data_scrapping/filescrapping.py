import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "https://kmpdc.go.ke/Registers/General_Practitioners.php"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}

response = requests.get(url,headers=headers)


soup = BeautifulSoup(response.text, "html.parser")


table = soup.find("table")


workbook = Workbook()
worksheet = workbook.active
if table:
    for row_num, row in enumerate(table.find_all("tr")):
        for col_num, cell in enumerate(row.find_all(["th", "td"])):
            worksheet.cell(row=row_num + 1, column=col_num + 1, value=cell.text)
else:

    print("Table element not found.")
workbook.save("generalpractitioners.xlsx")
print("Data has been saved")
