#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('factor_analysis_0104',
          default_args=default_args,
          schedule_interval='30 3 * * *',
          catchup=False,
          start_date=datetime(2020, 12, 17, 3, 30))

t2 = BashOperator(task_id="t2", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3982311 3982311 task  2010-01-11 ", dag=dag)
t3 = BashOperator(task_id="t3", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3982314 3982316 task  2010-01-11 ", dag=dag)
t1 = BashOperator(task_id="t1", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3982303 3982304 task  2010-01-11 ", dag=dag)
