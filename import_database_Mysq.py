import pandas as pd
import mysql.connector
from tqdm import tqdm
import math

# Connect to MySQL server
db = mysql.connector.connect(
    host="localhost",  # update with your server IP
    user="root",  # update with your username
    password="",  # update with your password
    database="espaceo_db_master"  # your database name
)

cursor = db.cursor()



# Load data from CSV file into DataFrame
data = pd.read_csv('E:/MyREST AI/Splite_csv/agencies.csv')

# SQL query string
sql_query = """
INSERT INTO `agencies1` (
  id, agency_name, agency_social_name, agency_email, agency_tel, mobile, street, 
  city, zip_code, city_code, latitude, longitude, agency_website,
  agency_description, agency_image, social_media, type_agence, city_concerned,
  juridique, cci, know_interimo, category, establishment_nature,
  establishment_number, activity_agency, siret, siren, card_t_code, services, 
  secteur_activite, effectif, siege, creation_date, capital, tva, dirigeant, 
  first_name, last_name, code_naf, created_at, updated_at, is_deleted, is_updated, 
  is_verified, img_checked)
VALUES (
  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
  %s, %s, %s, %s, %s, %s, %s)
"""

# Check the number of fields in the dataframe and SQL query
print(f"Number of fields in a row: {len(data.columns)}")
print(f"Number of fields in the SQL query: {sql_query.count('%s')}")

if len(data.columns) != sql_query.count('%s'):
    print("The number of fields in the rows does not match the number of fields in the SQL query.")
else:
    # Insert data into the table with progress bar
    for i, row in tqdm(data.iterrows(), total=len(data)):
        row = row.to_dict()
        for key in row:
            if pd.isnull(row[key]):
                row[key] = None
        cursor.execute(sql_query, tuple(row.values()))
        db.commit()

    print("Data imported successfully")
