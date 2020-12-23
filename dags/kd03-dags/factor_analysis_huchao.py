#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('huchao_factor_analysis',
          default_args=default_args,
          schedule_interval='30 4 * * *',
          catchup=False,
          start_date=datetime(2020, 12, 17, 4, 30))

t2 = BashOperator(task_id="t2", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 5226000 5226261 factor ", dag=dag)
t1 = BashOperator(task_id="t1", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 5225784 5226000 factor ", dag=dag)
