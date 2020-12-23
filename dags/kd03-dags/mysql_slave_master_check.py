#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('mysql_slave_master_check',
          default_args=default_args,
          schedule_interval='*/30 * * * *',
          catchup=False,
          start_date=datetime(2020, 12, 18, 18, 30))


mysql_slave_check = BashOperator(task_id="mysql_slave_check", bash_command="sh /usr/lib/carter/dbsync/scripts/mysql_slave_check.sh ", dag=dag)
