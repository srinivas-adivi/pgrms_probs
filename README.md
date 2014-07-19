## Setup

To install the dependencies, run:
    python setup.py install

Get sample data for companies, stocks:
    python get_sample_data.py

Then, create the sqlite database and load sample data:
    python manage.py syncdb
    python manage.py loaddata sample_companies 
    python manage.py loaddata sample_stocks 

Eample urls

    To get group of all companies details 

        http://localhost:8000/goc/

    To get specific company details like code, name, group, type for tata motors  

        http://localhost:8000/goc/500570
    
    To get opening and closing price of tata motors for date 4th July 2014
    
        http://localhost:8000/goc/500570/04072014/

    To get the prices of tata motors between 4th July 2014 to 16th July 2014 with graphical output

        http://localhost:8000/goc_range/500570/04072014/16072014/    
