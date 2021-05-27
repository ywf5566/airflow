# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'afroot01'
}
dag = DAG(
    'kd01_mina',
    default_args=default_args,
    description='mina',
    schedule_interval='*/4 * * * *',
    start_date=datetime(2020, 12, 22, 13, 30)
)
# ==========================================================tasks======================================================
infoPoolSummary = BashOperator(task_id="infoPoolSummary",
                               bash_command="sh /usr/lib/carter/kd_news_process/scripts/Mina/infoPoolSummary.sh ",
                               dag=dag)
infoPoolWebSummary = BashOperator(task_id="infoPoolWebSummary",
                                  bash_command="sh /usr/lib/carter/kd_news_process/scripts/Mina/infoPoolWebSummary.sh ",
                                  dag=dag)
