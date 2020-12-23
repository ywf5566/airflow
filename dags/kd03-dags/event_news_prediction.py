#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('event_news_prediction',
          default_args=default_args,
          schedule_interval='*/20 * * * *',
          catchup=False,
          start_date=datetime(2020, 12, 18, 18, 20))

news_event_prediction = BashOperator(
    task_id="news_event_prediction",
    bash_command="source /usr/lib/carter/event-news-scheduler/event-news-scheduler-env/bin/activate;cd /usr/lib/carter/event-news-scheduler;python BATCH_PREDICTION_EVENT.py ", dag=dag)
