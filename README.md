# Al Nour Rubber

This is a Django API built with Django Rest Framework. The API includes several models and endpoints for managing users, suppliers, products, clients, and daily reports.

## Models

The API includes the following models:

- `User`: Represents a user in the system. Users can have different levels, such as 'owner' and 'supervisor'.
- `Supplier`: Represents a supplier in the system.
- `ProductType`: Represents a type of product.
- `MaterialType`: Represents a type of material.
- `Client`: Represents a client in the system.
- `Configuration`: Represents the global configuration of the system.
- `MeasurementUnit`: Represents a measurement unit.
- `DailyReport`: Represents a daily report.
- `ProductionRecord`: Represents a production record.
- `RawMaterialRecord`: Represents a raw material record.
- `SoldProductRecord`: Represents a sold product record.

## Endpoints

The API includes the following endpoints:

- `/configurations`: For managing configurations.
- `/measurementunits`: For managing measurement units.
- `/dailyreports`: For managing daily reports.
- `/productionrecords`: For managing production records.
- `/rawmaterialrecords`: For managing raw material records.
- `/soldproductrecords`: For managing sold product records.

## Setup

To set up the API, follow these steps:

1. Clone the repository: `git clone <repository_url>`
2. Navigate to the project directory: `cd <project_directory>`
3. Install the requirements: `pip install -r requirements.txt`
4. Run the migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`

Now, you can access the API at `http://localhost:8000`