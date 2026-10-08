# Applied Analytics Mini Project

This project loads a small customer dataset into SQLite and calculates a simple city KPI using parameterized SQL.

## Run commands

```bash
python -m pip install -r requirements.txt
python src/etl_load_sqlite.py
python src/kpi_city.py
pytest -q
```
