#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot05'}
dag = DAG('kd_event_source',
          default_args=default_args,
          schedule_interval='*/5 * * * *',
          catchup=False,
          start_date=datetime(2021, 5, 24, 17, 0))

kdevent_source = BashOperator(task_id="kdevent_source",
                              bash_command="sh /usr/lib/carter/kdevent-source/kdevent_source/scripts/sync_kdevent.sh ",
                              dag=dag)
