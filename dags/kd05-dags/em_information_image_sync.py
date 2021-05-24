#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot05'}
dag = DAG('em_information_image_sync',
          default_args=default_args,
          schedule_interval='*/5 * * * *',
          catchup=False,
          start_date=datetime(2021, 5, 24, 12, 0))

information_and_image = BashOperator(task_id="information_and_image",
                                     bash_command="sh /usr/lib/carter/dbsync/scripts/sync_em_information_and_image.sh ",
                                     dag=dag)
