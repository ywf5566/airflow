#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot05'}
dag = DAG('sync_em_information',
          default_args=default_args,
          schedule_interval='*/5 * * * * ',
          catchup=False,
          start_date=datetime(2021, 5, 24, 12, 0))

sync_information_to_kd02 = BashOperator(task_id="sync_information_to_kd02",
                                        bash_command="/usr/lib/carter/dbsync/scripts/sync_information.sh ", dag=dag)
sync_information_to_kd03 = BashOperator(task_id="sync_information_to_kd03",
                                        bash_command="/usr/lib/carter/dbsync/scripts/sync_information_to_kd03.sh ",
                                        dag=dag)
