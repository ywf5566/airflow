#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from monitor.core.send_message import send_message
from monitor.core.send_message import ENV
from monitor.core.send_message import MSG_HEAD
from monitor.core.send_message import MSG_LEVEL
import os
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot05'}


class callBack:
    mesg_head = MSG_HEAD
    msg_level = MSG_LEVEL

    def on_dag_failure(self):
        os['kdconfig'] = '/home/keydriver/airflow/kd_airflow/dags/database.yaml'
        send_message(msg_id='FACTOR_DAILY_RESULT',
                     msg_head=self.mesg_head,
                     msg_level=self.msg_level.CRITICAL.value,
                     service='因子库',
                     msg_type='服务运行结果正确性检查',
                     msg_description='因子库脚本运行失败！',
                     env=ENV.PROD.value,
                     dt=datetime.now(),
                     host_name='kd04',
                     detailed_information='kd04因子任务：Interday_alpha_daily运行异常！')


dag = DAG('Interday_alpha_daily',
          default_args=default_args,
          schedule_interval=None,
          catchup=False,
          start_date=datetime(2021, 3, 10, 18, 0),
          on_failure_callback=callBack.on_dag_failure)

# 不需要进行qsdata和l2data的check了（2021-05-25）
# check_qsdata = BashOperator(task_id="kd05_check_qsdata", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-repo-dep-check.sh check_qsdata ", dag=dag, pool="factor")
# l2_data_check = BashOperator(task_id="kd05_l2_data_check", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-repo-dep-check.sh check_l2_data ", dag=dag, pool="factor")
daily_feature_cal = BashOperator(task_id="kd05_daily_feature_cal", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_daily_cal.sh ", dag=dag, pool="factor")
convert_pkl = BashOperator(task_id="kd05_convert_pkl", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_hdf2pkl.sh ", dag=dag,pool="factor")
save_feature_to_es = BashOperator(task_id="kd05_save_feature_to_es",  bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_pkl2es.sh ", dag=dag, pool="factor")
interday_alpha_universe = BashOperator(task_id="kd05_interday_alpha_universe", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_universe_ti0.sh ", dag=dag, pool="factor")
interday_alpha_ti0 = BashOperator(task_id="kd05_interday_alpha_ti0", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_factor_ti0.sh ", dag=dag, pool="factor")
factor_check_ti0 = BashOperator(task_id="kd05_factor_check_ti0", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/factors_check_ti0.sh ", dag=dag, pool="factor")
""" 午盘因子任务 """
kd05_midday_factor = BashOperator(task_id="kd05_midday_factor",  bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_mid_factor.sh ", dag=dag, pool="factor")
kd05_midday_factor_check = BashOperator(task_id="kd05_midday_factor_check",  bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/factors_check.sh ", dag=dag, pool="factor")

trigger_strategy = TriggerDagRunOperator(task_id="trigger_strategy", trigger_dag_id='Kd_strategy', trigger_rule='all_success', dag=dag)

""" tio任务结束后触发kd05的strategy任务 """
daily_feature_cal >> convert_pkl >> save_feature_to_es >> interday_alpha_universe >> interday_alpha_ti0 >> factor_check_ti0 >> trigger_strategy
interday_alpha_universe >> kd05_midday_factor >> kd05_midday_factor_check >> trigger_strategy