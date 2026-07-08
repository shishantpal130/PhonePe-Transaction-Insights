# 📱 PhonePe Transaction Insights

## Project Overview

PhonePe Transaction Insights is a data analytics project built using the PhonePe Pulse dataset.

The project extracts, processes, stores, analyzes, and visualizes transaction, user, and insurance data to generate meaningful business insights.

The solution uses:

- Python for data extraction and processing
- MySQL for data storage and analysis
- Streamlit for interactive dashboard visualization


---

# 🚀 Project Features

## Data Extraction

Extracted PhonePe Pulse data:

### Aggregated Data
- Transaction data
- User data
- Insurance data

### Map Data
- State-wise transactions
- District-wise users
- Geographical analysis

### Top Data
- Top states
- Top districts
- Top pincodes


---

# 🏗️ Project Architecture

PhonePe Pulse Dataset
|
↓
Python ETL Scripts
|
↓
CSV Files
|
↓
MySQL Database
|
↓
SQL Business Queries
|
↓
Streamlit Dashboard


---

# 📂 Project Structure

PhonePe_Transaction_Insights/

│
├── README.md
├── app.py
│
├── data/
│ ├── transaction.csv
│ ├── user.csv
│ ├── insurance.csv
│ ├── map_transaction.csv
│ ├── map_user.csv
│ ├── map_insurance.csv
│ ├── top_transaction.csv
│ ├── top_user.csv
│ └── top_insurance.csv
│
├── scripts/
│ ├── extract_data.py
│ ├── extract_user.py
│ ├── extract_insurance.py
│ ├── extract_map_transaction.py
│ ├── extract_map_user.py
│ ├── extract_map_insurance.py
│ ├── extract_top_transaction.py
│ ├── extract_top_user.py
│ ├── extract_top_insurance.py
│ └── load_mysql.py
│
└── sql/
└── business_queries.sql



---

# 🛠️ Technologies Used


| Technology | Purpose |
|---|---|
| Python | Data extraction and transformation |
| Pandas | Data processing |
| MySQL | Database management |
| SQL | Business analysis |
| Streamlit | Dashboard development |
| Plotly | Interactive charts |


---

# ⚙️ Installation


Install required libraries:

```bash
pip install pandas mysql-connector-python streamlit plotly

Database Setup

Start MySQL:

mysql -u root

Create database:

CREATE DATABASE phonepe;

USE phonepe;


Data Pipeline
Extract Data

Run:

python3 scripts/extract_data.py

python3 scripts/extract_user.py

python3 scripts/extract_insurance.py

Map Extraction:

python3 scripts/extract_map_transaction.py

python3 scripts/extract_map_user.py

python3 scripts/extract_map_insurance.py

Top Extraction:

python3 scripts/extract_top_transaction.py

python3 scripts/extract_top_user.py

python3 scripts/extract_top_insurance.py



Load Data into MySQL

Run:
python3 scripts/load_mysql.py

Successful output:
ALL DATA LOADED ✅

Dashboard

Run:
streamlit run app.py

Open:
http://localhost:8501

Dashboard Modules
Transaction Analysis

Includes:

* Total transaction count
* Transaction amount
* State-wise performance
* Growth trends
* Transaction categories

User Analytics

Includes:

* Registered users
* User growth
* State ranking

Insurance Analytics

Includes:

* Insurance adoption
* State-wise insurance value

---------

Business Insights Generated

The project answers:

- Which states generate the highest transaction value?
- How has PhonePe usage grown over time?
- Which transaction categories are most popular?
- Which states have the highest registered users?
- Where is insurance adoption strongest?

Future Improvements
- Add interactive India map visualization
- Add ML prediction models
- Deploy dashboard online
- Automate data refresh pipeline

Author

- Shishant Pal
Data Analytics Project


This is the complete README.✅
