# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot05', 'retries': 2, 'retry_delay': timedelta(minutes=1), 'start_date': datetime.strptime('2021-06-01 16:40:00', "%Y-%m-%d %H:%M:%S")}

dag = DAG('STAR_sync_data',
          default_args=default_args,
          schedule_interval='0 17 * * *')

sync_kcb_industry = BashOperator(
    task_id='sync_kcb_industry',
    bash_command=r'''sh /usr/lib/carter/dbsync/scripts/sync_kcb_industry.sh  ''',
    dag=dag)

sync_STAR_adjfactor = BashOperator(
    task_id='sync_STAR_adjfactor',
    bash_command=r'''sh /usr/lib/carter/dbsync/scripts/sync_kcb_adjfactor.sh  ''',
    dag=dag)

kcb_quota_check = BashOperator(
    task_id='kcb_quota_check',
    bash_command=r'''sh /usr/lib/carter/dbsync/scripts/sync_kcb_quota_check.sh  ''',
    dag=dag)

