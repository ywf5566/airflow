# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'afroot01'
}

dag = DAG(
    'beta_info_update',
    default_args=default_args,
    description='beta_info_update',
    schedule_interval='0 8 * * 1,4',
    start_date=datetime(2020, 12, 21, 8, 0)
)
# ==========================================================tasks======================================================
beta_info_update = BashOperator(task_id="beta_info_update",
                                bash_command="source /usr/lib/carter/carter-racker/racker-env/bin/activate;cd "
                                             "/usr/lib/carter/carter-racker/racker/core/update_touyan_task;python "
                                             "beta_update_auto_proc.py  ",
                                dag=dag)
