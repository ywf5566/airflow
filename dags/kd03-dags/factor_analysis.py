#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('factor_analysis',
          default_args=default_args,
          schedule_interval='30 3 * * *',
          atchup=False,
          start_date=datetime(2020, 12, 17, 3, 30))

t8 = BashOperator(task_id="t8", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3982320 3982322 task ", dag=dag)
t9 = BashOperator(task_id="t9", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3982323 3982325 task ", dag=dag)
t7 = BashOperator(task_id="t7", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3982317 3982319 task ", dag=dag)
t4 = BashOperator(task_id="t4", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3982306 3982309 task ", dag=dag)
t5 = BashOperator(task_id="t5", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3982312 3982313 task ", dag=dag)
t2 = BashOperator(task_id="t2", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3982302 3982302 task ", dag=dag)
t3 = BashOperator(task_id="t3", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3982305 3982305 task ", dag=dag)
t1 = BashOperator(task_id="t1", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3977424 3977425 task ", dag=dag)
t14 = BashOperator(task_id="t14", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3982310 3982310 task ", dag=dag)
t10 = BashOperator(task_id="t10", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3982326 3982328 task ", dag=dag)
t11 = BashOperator(task_id="t11", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3982329 3982331 task ", dag=dag)
t12 = BashOperator(task_id="t12", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3982335 3982337 task ", dag=dag)
t13 = BashOperator(task_id="t13", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3982335 3982337 task ", dag=dag)
