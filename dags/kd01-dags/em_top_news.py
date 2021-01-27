# -*- coding: utf-8 -*-
from airflow import DAG
from datetime import datetime
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'afroot01'
}

dag = DAG(
    'kd01_em_top_new',
    default_args=default_args,
    description='kd_news_process[em_top_news]',
    schedule_interval='*/5 * * * *',
    catchup=False,
    start_date=datetime(2021, 1, 27, 17, 10)
)
# ==========================================================tasks======================================================
syncEmWarnings = BashOperator(task_id="syncEmWarnings", bash_command="sh /usr/lib/carter/kd_news_process/scripts/step1/syncEmWarnings.sh ", dag=dag)
syncEmTopNews = BashOperator(task_id="syncEmTopNews", bash_command="sh /usr/lib/carter/kd_news_process/scripts/step1/syncEmTopNews.sh ", dag=dag)
emStock = BashOperator(task_id="emStock", bash_command="sh /usr/lib/carter/kd_news_process/scripts/EmStock/emStock.sh ", dag=dag)
syncTopNewsToEm = BashOperator(task_id="syncTopNewsToEm", bash_command="sh /usr/lib/carter/kd_news_process/scripts/step4/syncTopNewsToEm.sh ", dag=dag)

syncEmTopNews >> syncTopNewsToEm
