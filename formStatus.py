import requests
import json
import time
import pandas as pd
import subprocess
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import OrderedDict

ggov_forms_status_url = "https://www.grants.gov/web/grants/forms/forms-status-report.html"

# get currect form status page table
browser = webdriver.Chrome()
browser.get(ggov_forms_status_url)
time.sleep(5)
sel_html = browser.page_source
sel_table = BeautifulSoup(sel_html, 'lxml').find("div",{"id":"formsDataDiv"}).find("table")

# drill down into rows and transform table into list
t_body = sel_table.contents[0]
rows = t_body.contents
header = [[th.text for th in rows[0]('th')]]
row_cells = [[cell.text for cell in r('td')] for r in rows if rows.index(r) != 0]
total_data = header + row_cells

# transform list into json
print(json.dumps(OrderedDict(total_data)))

browser.quit()
