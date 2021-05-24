#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot05'}
dag = DAG('kdevent_source_national_economy',
          default_args=default_args,
          schedule_interval='0 23 * * *',
          catchup=False,
          start_date=datetime(2021, 5, 23, 23, 0))

national_economy = BashOperator(task_id="national_economy",
                                bash_command="sh /usr/lib/carter/kdevent-source/kdevent_source/scripts/sync_national_economy.sh ",
                                dag=dag)
