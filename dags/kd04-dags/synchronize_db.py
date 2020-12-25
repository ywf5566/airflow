#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot04'}
dag = DAG('synchronize_db',
          default_args=default_args,
          schedule_interval='0 20 * * *',
          catchup=False,
          start_date=datetime(2020, 12, 24, 16, 0))

sync_org_id_to_kdcode_test = BashOperator(task_id="sync_org_id_to_kdcode_test",
                                          bash_command="sh /usr/lib/carter/dbsync/scripts/sync_org_id_to_kdcode.sh ",
                                          dag=dag)
sync_db = BashOperator(task_id="sync_db", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_db.sh ", dag=dag)
sync_future_dayquota = BashOperator(task_id="sync_future_dayquota",
                                    bash_command="sh /usr/lib/carter/dbsync/scripts/sync_fdayquota.sh ", dag=dag)
