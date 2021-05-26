# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'afroot01'
}
# 每个月1号执行---0 0 1 */1 *
dag = DAG(
    'kd01_keydriver_train_tfidf_model',
    default_args=default_args,
    schedule_interval='	0 0 1 */1 *',
    start_date=datetime(2020, 12, 1, 0, 0)
)
# ==========================================================tasks======================================================
train_tfidf_model = BashOperator(task_id="train_tfidf_model", bash_command="source /usr/lib/carter/event-news-scheduler/event-news-scheduler-venv/bin/activate;cd /usr/lib/carter/event-news-scheduler;python BATCH_TRAIN_TFIDF_MODEL.py ", dag=dag)
