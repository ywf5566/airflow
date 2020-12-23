#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('kd03_em_top_news_update',
          default_args=default_args,
          schedule_interval='*/5 * * * *',
          catchup=False,
          start_date=datetime(2020, 12, 18, 17, 30))
reinsert_duplicate_em_top_news = BashOperator(
    task_id='reinsert_duplicate_em_top_news',
    bash_command='sh /usr/lib/carter/separateDagobahTask/scripts/CrawlerPortal/crawlerPortal.sh ',
    dag=dag)
