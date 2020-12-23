#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('L2_FACTOR',
          default_args=default_args,
          schedule_interval='0 5 * * *',
          catchup=False,
          start_date=datetime(2020, 12, 17, 5, 0))

task_1440904_1441449 = BashOperator(task_id="task_1440904_1441449", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1440904 1441449 l2_factor ", dag=dag)
task_1442808_1442902 = BashOperator(task_id="task_1442808_1442902", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1442808 1442902 l2_factor ", dag=dag)
task_1442432_1442807 = BashOperator(task_id="task_1442432_1442807", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1442432 1442807 l2_factor ", dag=dag)
task_1098897_1099827 = BashOperator(task_id="task_1098897_1099827", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1098897 1099827 l2_factor ", dag=dag)
task_1327568_1327648 = BashOperator(task_id="task_1327568_1327648", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1327568 1327648 l2_factor ", dag=dag)
task_1100063_1327567 = BashOperator(task_id="task_1100063_1327567", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1100063 1327567 l2_factor ", dag=dag)
task_1441545_1441638 = BashOperator(task_id="task_1441545_1441638", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1441545 1441638 l2_factor ", dag=dag)
task_1441735_1442110 = BashOperator(task_id="task_1441735_1442110", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1441735 1442110 l2_factor ", dag=dag)
task_1098698_1098894 = BashOperator(task_id="task_1098698_1098894", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1098698 1098894 l2_factor ", dag=dag)
task_1441639_1441734 = BashOperator(task_id="task_1441639_1441734", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1441639 1441734 l2_factor ", dag=dag)
task_1441450_1441543 = BashOperator(task_id="task_1441450_1441543", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1441450 1441543 l2_factor ", dag=dag)
task_1327738_1404733 = BashOperator(task_id="task_1327738_1404733", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1327738 1404733 l2_factor ", dag=dag)
task_1404790_1440808 = BashOperator(task_id="task_1404790_1440808", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1404790 1440808 l2_factor ", dag=dag)
task_1440809_1440902 = BashOperator(task_id="task_1440809_1440902", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1440809 1440902 l2_factor ", dag=dag)
task_1099967_1100062 = BashOperator(task_id="task_1099967_1100062", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1099967 1100062 l2_factor ", dag=dag)
task_1060636_1098697 = BashOperator(task_id="task_1060636_1098697", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1060636 1098697 l2_factor ", dag=dag)
task_1442111_1442431 = BashOperator(task_id="task_1442111_1442431", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1442111 1442431 l2_factor ", dag=dag)
task_1442903_1443223 = BashOperator(task_id="task_1442903_1443223", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1442903 1443223 l2_factor ", dag=dag)
task_1099828_1099965 = BashOperator(task_id="task_1099828_1099965", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1099828 1099965 l2_factor ", dag=dag)
task_1327649_1327737 = BashOperator(task_id="task_1327649_1327737", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 1327649 1327737 l2_factor ", dag=dag)
