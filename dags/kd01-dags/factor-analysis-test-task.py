# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
default_args = {
    'owner': 'afroot01'
}

dag = DAG(
    'factor-analysis-test-task',
    default_args=default_args,
    description='factor-analysis-test-task',
    schedule_interval=None,
    start_date=datetime(2020, 12, 16)
)
# ==========================================================tasks======================================================
fac_daily_kd_deap_factor_1196 = BashOperator(task_id="fac_daily_kd_deap_factor_1196", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3057145 ", dag=dag)
fac_daily_kd_deap_factor_1156 = BashOperator(task_id="fac_daily_kd_deap_factor_1156", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3057105 ", dag=dag)
fac_daily_kd_deap_factor_1157 = BashOperator(task_id="fac_daily_kd_deap_factor_1157", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3057106 ", dag=dag)
fac_daily_kd_deap_factor_1182 = BashOperator(task_id="fac_daily_kd_deap_factor_1182", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3057131 ", dag=dag)
fac_daily_kd_deap_factor_1178 = BashOperator(task_id="fac_daily_kd_deap_factor_1178", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3057127 ", dag=dag)
fac_daily_kd_deap_factor_1165 = BashOperator(task_id="fac_daily_kd_deap_factor_1165", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3057114 ", dag=dag)
fac_daily_kd_deap_factor_1166 = BashOperator(task_id="fac_daily_kd_deap_factor_1166", bash_command="sh /usr/lib/quant/factor/factor-analysis/factor_analysis_service/tool/factor_analysis.sh 3057115 ", dag=dag)
