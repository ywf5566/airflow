# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'afroot01'
}
dag = DAG(
    'kd_event_performance',
    default_args=default_args,
    schedule_interval='50 10 * * *',
    start_date=datetime(2020, 12, 21, 10, 50)
)
# ==========================================================tasks======================================================
performance = BashOperator(task_id="performance", bash_command="sh /usr/lib/carter/kdevent-source/kdevent_source/scripts/sync_performance.sh ", dag=dag)

