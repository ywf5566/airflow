#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot05', 'retries': 2, 'retry_delay': timedelta(minutes=1)}
dag = DAG('Level2_from_em_to_kd',
          default_args=default_args,
          schedule_interval='20 17 * * *',
          catchup=False,
          start_date=datetime(2021, 5, 16, 16, 0))

level2_from_em = BashOperator(task_id="level2_from_em",
                             bash_command="sh /usr/lib/quant/factor/factor_repo/tools/l2code/l2source_file/sync.sh ", dag=dag)
level2_to_kd = BashOperator(task_id="level2_to_kd",
                           bash_command="sh /usr/lib/quant/factor/factor_repo/tools/l2code/parser/parser.sh ", dag=dag)

level2_from_em >> level2_to_kd
