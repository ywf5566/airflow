# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
from datetime import datetime

default_args = {
    'owner': 'keydriver'
}

dag = DAG(
    'kd01_keydriver_em_top_new',
    default_args=default_args,
    description='kd_news_process[em_top_news]',
    schedule_interval='*/5 * * * *',
    start_date=datetime(2020, 12, 24, 12, 50)
)
# ==========================================================tasks======================================================
syncEmWarnings = SSHOperator(task_id="syncEmWarnings", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_news_process/scripts/step1/syncEmWarnings.sh ", dag=dag)
syncEmTopNews = SSHOperator(task_id="syncEmTopNews", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_news_process/scripts/step1/syncEmTopNews.sh ", dag=dag)
emStock = SSHOperator(task_id="emStock", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_news_process/scripts/EmStock/emStock.sh ", dag=dag)
syncTopNewsToEm = SSHOperator(task_id="syncTopNewsToEm", ssh_conn_id="kd01_keydriver",command="sh /usr/lib/carter/kd_news_process/scripts/step4/syncTopNewsToEm.sh ", dag=dag)

syncEmTopNews >> syncTopNewsToEm
