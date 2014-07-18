## Setup

To install the dependencies, run:
    python setup.py install

Get sample data for companies, stocks:
    python get_sample_data.py

Then, create the sqlite database and load sample data:
    python manage.py syncdb
    python manage.py loaddata sample_companies 
    python manage.py loaddata sample_stocks 
