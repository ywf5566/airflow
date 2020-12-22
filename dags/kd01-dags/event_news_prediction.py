# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
from datetime import datetime
default_args = {
    'owner': 'keydriver'
}
dag = DAG(
    'kd01_keydriver_event_news_prediction',
    default_args=default_args,
    description='event_news_prediction',
    schedule_interval='*/20 * * * *',
    start_date=datetime(2020, 12, 24, 12, 30)
)
# ==========================================================tasks======================================================
news_event_prediction = SSHOperator(task_id="news_event_prediction", ssh_conn_id="kd01_keydriver",command="source /usr/lib/carter/event-news-scheduler/event-news-scheduler-venv/bin/activate;cd /usr/lib/carter/event-news-scheduler;python BATCH_PREDICTION_EVENT.py ", dag=dag)
