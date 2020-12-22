# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
from datetime import datetime

default_args = {
    'owner': 'keydriver'
}
dag = DAG(
    'kd_event_performance',
    default_args=default_args,
    description='kd_event_performance',
    schedule_interval='50 10 * * *',
    start_date=datetime(2020, 12, 21, 10, 50)
)
# ==========================================================tasks======================================================
performance = SSHOperator(task_id="performance", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kdevent-source/kdevent_source/scripts/sync_performance.sh ", dag=dag)

