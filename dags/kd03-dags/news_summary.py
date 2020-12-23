#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('news_summary',
          default_args=default_args,
          schedule_interval='*/5 * * * *',
          catchup=False,
          start_date=datetime(2020, 12, 18, 17, 30))

news_summary = BashOperator(task_id="news_summary",
                            bash_command="source /usr/lib/carter/abstract-inserter/env/bin/activate;python /usr/lib/carter/abstract-inserter/do_abstract/database_summary/execute.py ",
                            dag=dag)
