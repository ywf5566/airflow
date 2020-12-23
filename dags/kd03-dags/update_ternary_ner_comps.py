#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('update_ternary_ner_comps',
          default_args=default_args,
          schedule_interval='0 12 * * SAT',
          catchup=False,
          start_date=datetime(2020, 12, 12, 12, 0))

update_ternary_enr_comps = BashOperator(task_id="update_ternary_enr_comps", bash_command=r"source /usr/lib/carter/event-news-scheduler/event-news-scheduler-venv/bin/activate;cd /usr/lib/carter/event-news-scheduler/project/predictor/predictor/scripts/;python BATCH_UPDATE_TERNARY_NER_COMPS.py ", dag=dag)
