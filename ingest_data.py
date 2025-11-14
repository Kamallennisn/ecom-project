import pandas as pd
import sqlite3
import os

# Database file name
db_file = "ecom.db"

# CSV files to ingest
csv_files = {
    "Customers": "Customers.csv",
    "OrderItems": "OrderItems.csv",
    "Orders": "Orders.csv",
    "Products": "Products.csv",
    "Reviews": "Reviews.csv"
}

# Connect to SQLite database (creates if doesn't exist)
conn = sqlite3.connect(db_file)

print("Starting data ingestion...")
print(f"Database: {db_file}\n")

# Process each CSV file
for table_name, csv_file in csv_files.items():
    if not os.path.exists(csv_file):
        print(f"Warning: {csv_file} not found. Skipping...")
        continue
    
    print(f"Processing {csv_file} -> {table_name} table...")
    
    # Read CSV file with pandas (infers types automatically)
    df = pd.read_csv(csv_file)
    
    # Display info about the dataframe
    print(f"  - Rows: {len(df)}")
    print(f"  - Columns: {list(df.columns)}")
    
    # Insert data into SQLite table
    # if_exists='replace' will drop the table if it exists and create a new one
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    print(f"  Successfully imported {len(df)} rows into {table_name} table\n")

# Close the connection
conn.close()

print("Data ingestion complete!")
print(f"Database saved as: {db_file}")

# Verify the database
print("\nVerifying database...")
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Get list of tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print(f"\nTables in database: {len(tables)}")
for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table[0]};")
    count = cursor.fetchone()[0]
    print(f"  - {table[0]}: {count} rows")

conn.close()
print("\nVerification complete!")

