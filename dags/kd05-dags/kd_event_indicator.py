#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot05'}
dag = DAG('kd_event_indicator',
          default_args=default_args,
          schedule_interval='0 18 * * *',
          catchup=False,
          start_date=datetime(2021, 5, 23, 18, 0))

a_stock_week = BashOperator(task_id="a_stock_week",
                            bash_command="source /usr/lib/carter/kdevent-source/env/bin/activate;cd /usr/lib/carter/kdevent-source/kdevent_source/indicator_change;python a_stock_chg_week.py ",
                            dag=dag)
a_stock_day = BashOperator(task_id="a_stock_day",
                           bash_command="source /usr/lib/carter/kdevent-source/env/bin/activate;cd /usr/lib/carter/kdevent-source/kdevent_source/indicator_change;python a_stock_chg_day.py ",
                           dag=dag)
a_stock_month = BashOperator(task_id="a_stock_month",
                             bash_command="source /usr/lib/carter/kdevent-source/env/bin/activate;cd /usr/lib/carter/kdevent-source/kdevent_source/indicator_change;python a_stock_chg_month.py ",
                             dag=dag)
sw_index_chg = BashOperator(task_id="sw_index_chg",
                            bash_command="source /usr/lib/carter/kdevent-source/env/bin/activate;cd /usr/lib/carter/kdevent-source/kdevent_source/indicator_change;python sw_index_chg_day.py ",
                            dag=dag)
