#!/bin/bash
export AIRFLOW_HOME="$HOME/Desktop/stock-market-data-pipeline"
export AIRFLOW__CORE__DAGS_FOLDER="$AIRFLOW_HOME/dags"
export AIRFLOW__CORE__LOAD_EXAMPLES=False
airflow standalone

