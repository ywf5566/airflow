#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator

default_args = {'owner': 'afroot04'}
dag = DAG('kd05_level2_from_em_to_kd',
          default_args=default_args,
          schedule_interval='0 17 * * *',
          catchup=False,
          start_date=datetime(2020, 12, 24, 16, 0))

level2_from_em = SSHOperator(task_id="level2_from_em", ssh_conn_id="kd05_keydriver",
                             command="/usr/lib/quant/factor/factor_repo/tools/l2code/l2source_file/sync.sh ", dag=dag)
level2_to_kd = SSHOperator(task_id="level2_to_kd", ssh_conn_id="kd05_keydriver",
                           command="/usr/lib/quant/factor/factor_repo/tools/l2code/parser/parser.sh ", dag=dag)
level2_from_em >> [level2_to_kd]
