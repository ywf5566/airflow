#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot05'}
dag = DAG('sync_em_im_info',
          default_args=default_args,
          schedule_interval='0 3,4,5 * * *',
          catchup=False,
          start_date=datetime(2021, 5, 24, 1, 0))

sync_em_im_info = BashOperator(task_id="sync_em_im_info",
                               bash_command="sh /usr/lib/carter/dbsync/scripts/sync_em_im_info.sh ", dag=dag)
sync_em_im_info_to_kd03 = BashOperator(task_id="sync_em_im_info_to_kd03",
                                       bash_command="sh /usr/lib/carter/dbsync/scripts/sync_em_im_info_to_kd03.sh ",
                                       dag=dag)
