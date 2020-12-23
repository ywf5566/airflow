#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('analysis_static_service',
          default_args=default_args,
          schedule_interval='0 14 * * FRI',
          catchup=False,
          start_date=datetime(2020, 12, 11, 14, 0))

analysis_static_service = BashOperator(task_id="analysis_static_service", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/analysis_static_service.sh  ", dag=dag)
