from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime
from pathlib import Path

# This makes the DAG portable and prevents "wrong folder" issues forever
# dags/stock_pipeline_dag.py -> project root is one folder above /dags
PROJECT_DIR = Path(__file__).resolve().parents[1]
PYTHON_BIN = PROJECT_DIR / "venv" / "bin" / "python"

def cmd(script_name: str) -> str:
    return f"cd '{PROJECT_DIR}' && '{PYTHON_BIN}' scripts/{script_name}"

with DAG(
    dag_id="stock_market_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    extract = BashOperator(task_id="extract", bash_command=cmd("extract.py"))
    transform = BashOperator(task_id="transform", bash_command=cmd("transform.py"))
    upload_s3 = BashOperator(task_id="upload_to_s3", bash_command=cmd("upload_to_s3.py"))
    load_pg = BashOperator(task_id="load_to_postgres", bash_command=cmd("load_to_postgres.py"))

    extract >> transform >> upload_s3 >> load_pg
