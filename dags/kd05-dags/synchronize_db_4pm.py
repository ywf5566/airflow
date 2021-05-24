#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot05'}
dag = DAG('synchronize_db_4pm',
          default_args=default_args,
          schedule_interval='50 15 * * *',
          catchup=False,
          start_date=datetime(2021, 5, 23, 15, 50))
          
sync_org_id_to_kdcode = BashOperator(task_id="sync_org_id_to_kdcode", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_org_id_to_kdcode.sh ", dag=dag)
sync_kdb_dayquota_at_4pm = BashOperator(task_id="sync_kdb_dayquota_at_4pm", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_kdb_dayquota_at_4pm.sh ", dag=dag)


sync_org_id_to_kdcode >> [sync_kdb_dayquota_at_4pm]
