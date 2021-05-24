#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot05'}
dag = DAG('factor_dependent_data',
          default_args=default_args,
          schedule_interval='*/5 * * * *',
          catchup=False,
          start_date=datetime(2021, 5, 24, 12, 0))

em_sw_index = BashOperator(task_id="em_sw_index", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_em_sw_index.sh ",
                           dag=dag)
EM_QUOTE_STOCK_DAILY = BashOperator(task_id="EM_QUOTE_STOCK_DAILY",
                                    bash_command="sh /usr/lib/carter/dbsync/scripts/sync_em_daily_quote.sh ", dag=dag)
