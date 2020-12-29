#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('sync_minquota',
          default_args=default_args,
          schedule_interval='15,55 17 * * *',
          catchup=False,
          start_date=datetime(2020, 12, 17, 17, 0))

sync_minquota = BashOperator(task_id="sync_minquota",
                             bash_command="sh /usr/lib/carter/dbsync/scripts/sync_minquota.sh ", dag=dag)
update_qsdata = BashOperator(task_id="update_qsdata",
                             bash_command="sh /usr/lib/carter/dbsync/scripts/update_qsdata.sh ", dag=dag)
statistic_daily_basic_data = BashOperator(task_id="statistic_daily_basic_data",
                                          bash_command="sh /usr/lib/carter/dbsync/scripts/statistic_daily_basic_data"
                                                       ".sh ",
                                          dag=dag)

sync_minquota >> update_qsdata >> statistic_daily_basic_data
