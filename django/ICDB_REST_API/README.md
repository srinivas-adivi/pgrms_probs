# DealerTrack Python Developer Evaluation

This evaluation consists of a Django project called ICDB, the Internet Car
Database, which is a database of cars exposed through a REST API.

The API is currently able to create and list cars using JSON representations.

## Setup

To install the dependencies, run:
    python setup.py install

Then, create the sqlite database and load sample data:
    python manage.py syncdb
    python manage.py loaddata sample_cars

To complete this evaluation, you need to:

* Add functionality for updating a car through the REST API by sending a JSON
  representation.
* Add functionality for deleting a car through the REST API.
* Add functionality for viewing a JSON representation of a single car.

* Write unit tests, ideally before the code itself.
* Rewrite views as class-based views. Even better: use built-in generic views.
