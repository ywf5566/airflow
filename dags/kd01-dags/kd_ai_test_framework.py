# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'afroot01'
}

dag = DAG(
    'kd_ai_test_framework',
    default_args=default_args,
    description='kd-ai-test-framework',
    schedule_interval='0 5 * * *',
    start_date=datetime(2020, 12, 21, 5, 0)
)
# ==========================================================tasks======================================================
kd_ai_test_framework = BashOperator(task_id="kd_ai_test_framework", bash_command="/usr/lib/mina/kd-ai-test-framework/performance/script/run.sh ", dag=dag)
