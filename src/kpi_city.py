import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DB_PATH = ROOT_DIR / "data" / "db" / "analytics.db"


def city_kpi(city: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """
        SELECT COUNT(*), ROUND(AVG(monthly_spend), 2), ROUND(AVG(churned), 4)
        FROM customers_raw
        WHERE city = ?
    """

    cursor.execute(query, (city,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        result = {
            "city": city,
            "customer_count": 0,
            "avg_monthly_spend": None,
            "churn_rate": None,
        }
    else:
        customer_count, avg_monthly_spend, churn_rate = row
        result = {
            "city": city,
            "customer_count": customer_count,
            "avg_monthly_spend": avg_monthly_spend,
            "churn_rate": churn_rate,
        }

    print(
        f"city={city} | customer_count={result['customer_count']} | "
        f"avg_monthly_spend={result['avg_monthly_spend']} | churn_rate={result['churn_rate']}"
    )
    return result


if __name__ == "__main__":
    city_kpi("Mumbai")
    city_kpi("Mumbai' OR 1=1 --")
