#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('Interday_alpha_daily',
          default_args=default_args,
          schedule_interval='0 18 * * 1-5',
          catchup=False,
          start_date=datetime(2020, 12, 17, 18, 0))

daily_feature_cal = BashOperator(task_id="daily_feature_cal", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_daily_cal.sh ", dag=dag)
convert_pkl = BashOperator(task_id="convert_pkl", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_hdf2pkl.sh ", dag=dag)
save_feature_to_es = BashOperator(task_id="save_feature_to_es", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_pkl2es.sh ", dag=dag)

daily_feature_cal >> [convert_pkl]
convert_pkl >> [save_feature_to_es]