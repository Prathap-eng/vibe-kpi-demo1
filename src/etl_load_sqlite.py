import sqlite3
from pathlib import Path

import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT_DIR / "data" / "raw" / "customers_raw.csv"
DB_PATH = ROOT_DIR / "data" / "db" / "analytics.db"


def load_csv_to_db(csv_path: str | Path = CSV_PATH, db_path: str | Path = DB_PATH) -> Path:
    csv_path = Path(csv_path)
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(csv_path)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS customers_raw")
    cursor.execute(
        """
        CREATE TABLE customers_raw (
            customer_id INTEGER,
            city TEXT,
            monthly_spend REAL,
            churned INTEGER
        )
        """
    )
    df.to_sql("customers_raw", conn, if_exists="append", index=False)
    conn.commit()
    conn.close()

    print(f"Loaded {len(df)} rows into {db_path}")
    return db_path


if __name__ == "__main__":
    load_csv_to_db()
