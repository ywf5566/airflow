# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime

default_args = {
    'owner': 'kd01_sync'
}

dag = DAG(
    'sync_l2data',
    default_args=default_args,
    description='sync-l2data-kd03-kd01',
    schedule_interval='*/10 17-18 * * *',
    start_date=datetime(2020, 12, 21, 17, 0)
)
# ==========================================================tasks======================================================
sync_l2data = BashOperator(task_id="sync_l2data",
                           bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/sync_l2data.sh ",
                           dag=dag)
