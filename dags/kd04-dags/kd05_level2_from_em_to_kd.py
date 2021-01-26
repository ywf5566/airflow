#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from airflow import DAG
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator

default_args = {'owner': 'afroot04', 'retries': 2, 'retry_delay': timedelta(minutes=1)}
dag = DAG('KD05_level2_from_em_to_kd',
          default_args=default_args,
          schedule_interval='0 17 * * *',
          catchup=False,
          start_date=datetime(2020, 12, 24, 16, 0))

level2_from_em = SSHOperator(task_id="level2_from_em", ssh_conn_id="kd05_keydriver",
                             command="/usr/lib/quant/factor/factor_repo/tools/l2code/l2source_file/sync.sh ", dag=dag)
level2_to_kd = SSHOperator(task_id="level2_to_kd", ssh_conn_id="kd05_keydriver",
                           command="/usr/lib/quant/factor/factor_repo/tools/l2code/parser/parser.sh ", dag=dag)

trigger_kd04_factor = TriggerDagRunOperator(task_id="trigger_factor_normal", trigger_dag_id="KD05_FACTOR_LEVEL2_AND_NORMAL", trigger_rule="all_success", dag=dag)
trigger_kd03_factor = SSHOperator(task_id="trigger_kd03_factor", ssh_conn_id="kd03_keydriver",
                                  command="source /home/keydriver/airflow/bin/activate;airflow trigger_dag KD_FACTOR_LEVEL2_AND_NORMAL ", dag=dag)
level2_from_em >> level2_to_kd >> [trigger_kd04_factor, trigger_kd03_factor]
