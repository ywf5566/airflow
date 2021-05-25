#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot05'}
dag = DAG('crawler_EmTopNewsUpdate',
          default_args=default_args,
          schedule_interval='*/5 * * * *',
          catchup=False,
          start_date=datetime(2021, 5, 25, 14, 0))


emTopNewsUpdate = BashOperator(task_id="emTopNewsUpdate",
                               bash_command="sh /usr/lib/carter/separateDagobahTask/scripts/CrawlerPortal/crawlerPortal.sh ",
                               dag=dag)
