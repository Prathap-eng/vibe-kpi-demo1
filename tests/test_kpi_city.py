from src.etl_load_sqlite import load_csv_to_db
from src.kpi_city import city_kpi


def setup_module():
    load_csv_to_db()


def test_city_kpi_happy_path():
    result = city_kpi("Mumbai")

    assert result["city"] == "Mumbai"
    assert result["customer_count"] == 3
    assert result["avg_monthly_spend"] == 6700.0
    assert result["churn_rate"] == 0.6667


def test_city_kpi_injection_attempt():
    result = city_kpi("Mumbai' OR 1=1 --")

    assert result["city"] == "Mumbai' OR 1=1 --"
    assert result["customer_count"] == 0
    assert result["avg_monthly_spend"] is None
    assert result["churn_rate"] is None
