import urllib2
import datetime
import zipfile
import os
import shutil
import json
import sys 
import StringIO
import contextlib
import pprint


BASE_URL = "http://www.bseindia.com/download/BhavCopy/Equity"
PAST_WORKING_DAYS = 10


def get_urls(past_working_days):
    """ """
    today = datetime.date.today()
    delta_days = 1

    urls = []
    while past_working_days: 
        date = today - datetime.timedelta(delta_days)
        day_date = datetime.datetime.strftime(date, "%a %d%m%y")
        day, date = day_date.split()
        params = {'base_url': BASE_URL, 'date': date}
        if not day in ['Sat', 'Sun']:
            url = "%(base_url)s/EQ%(date)s_CSV.ZIP" %(params)
            urls.append(url)
            past_working_days = past_working_days - 1

        delta_days = delta_days + 1

    return urls
 
def download_urls(urls, path_to_download):
    """ """
    if not os.path.exists(path_to_download):
        os.makedirs(path_to_download)
    else:
        shutil.rmtree(path_to_download)

    for url in urls:
        head, file_name = url.rsplit('/', 1)
        eq_zip = urllib2.urlopen(url)
        zip_file = open(file_name, 'w')
        zip_file.write(eq_zip.read())
        zip_file.close()

        zip_ref = zipfile.ZipFile(file_name, 'r')
        zip_ref.extractall(path_to_download)
        zip_ref.close()

        os.remove(file_name)

def get_data_from_csv(path_to_files):
    """ """
    sample_companies, sample_stocks, company_codes = [], [], []
    for i, file_name in enumerate(os.listdir(path_to_files)):
        date = file_name.split('.')[0][2:]
        date = '20'+date[-2:]+'-'+date[2:4]+'-'+date[:2]
        lines = open(os.path.join(path_to_files, file_name)).readlines()
        for line in lines[1:]:
            details = line.replace("'", "`").split(',')
            code = details[0]
            if not code in company_codes:
                company_field_names = ["code", "name", "group", "type"]
                company = {"model": "companies.company", "fields": dict(zip(company_field_names, details[:4]))}
                sample_companies.append(company)
                company_codes.append(code)

            stock_details = [code, date, details[4], details[7]]
            stock_field_names = ["company", "date", "opening_price", "closing_price"]
            stock = {"model": "stocks.stock", "fields": dict(zip(stock_field_names, stock_details))}
            sample_stocks.append(stock)

    return sample_companies, sample_stocks

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

if __name__ == "__main__":
    urls = get_urls(PAST_WORKING_DAYS)
    download_urls(urls, 'downloads')
    companies, stocks = get_data_from_csv('downloads') 

    with stdoutIO() as c:
        exec "pprint.pprint(companies)"
    f1 = open('companies/fixtures/sample_companies.json', 'w')
    f1.write(c.getvalue().replace("'", '"'))
    f1.close()
    
    with stdoutIO() as s:
        exec "pprint.pprint(stocks)"
    f2 = open('stocks/fixtures/sample_stocks.json', 'w')
    f2.write(s.getvalue().replace("'", '"'))
    f2.close()
