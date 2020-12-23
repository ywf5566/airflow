#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('kd_ai_test_framework',
          default_args=default_args,
          schedule_interval='0 5 * * *',
          catchup=False,
          start_date=datetime(2020, 12, 17, 5, 0))


kd_ai_test_framework = BashOperator(task_id="kd_ai_test_framework", bash_command="/usr/lib/mina/kd-ai-test-framework/script/run.sh ", dag=dag)
