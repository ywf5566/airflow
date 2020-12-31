# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'kd01_strategy',
}
dag = DAG(
    'kd_bs_model_training',
    default_args=default_args,
    description='kd_bs_model_training',
    schedule_interval='0 23 30 * *',
    start_date=datetime(2020, 12, 1, 23, 0)
)
# ==========================================================tasks======================================================
dk_training_task = BashOperator(task_id="dk_training_task",
                                bash_command="sh /usr/lib/carter/kd_strategy/script/v3_dk_training_task.sh dev ",
                                dag=dag)

