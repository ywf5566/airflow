#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from monitor.core.send_message import send_message
from monitor.core.send_message import ENV
from monitor.core.send_message import MSG_HEAD
from monitor.core.send_message import MSG_LEVEL
import os
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator


default_args = {'owner': 'afroot04'}


class callBack:
    def on_dag_failure(self):
        os['kdconfig'] = '/home/keydriver/airflow/kd_airflow/dags/database.yaml'
        send_message(msg_id='FACTOR_DAILY_RESULT',
                     msg_head=MSG_HEAD,
                     msg_level=MSG_LEVEL.CRITICAL.value,
                     service='因子库',
                     msg_type='服务运行结果正确性检查',
                     msg_description='因子库脚本运行失败！',
                     env=ENV.PROD.value,
                     dt=datetime.now(),
                     host_name='kd04',
                     detailed_information='kd04因子任务：Interday_alpha_daily运行异常！')


dag = DAG('KD05_Interday_alpha_daily',
          default_args=default_args,
          schedule_interval=None,
          catchup=False,
          start_date=datetime(2021, 3, 10, 18, 0),
          on_failure_callback=callBack.on_dag_failure)

check_qsdata = SSHOperator(task_id="kd05_check_qsdata", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-repo-dep-check.sh check_qsdata ", dag=dag, pool="factor")
l2_data_check = SSHOperator(task_id="kd05_l2_data_check", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-repo-dep-check.sh check_l2_data ", dag=dag, pool="factor")
daily_feature_cal = SSHOperator(task_id="kd05_daily_feature_cal", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_daily_cal.sh ", dag=dag, pool="factor")
convert_pkl = SSHOperator(task_id="kd05_convert_pkl", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_hdf2pkl.sh ", dag=dag,pool="factor")
save_feature_to_es = SSHOperator(task_id="kd05_save_feature_to_es", ssh_conn_id="kd05_keydriver", command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_pkl2es.sh ", dag=dag, pool="factor")
interday_alpha_universe = SSHOperator(task_id="kd05_interday_alpha_universe", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_universe_ti0.sh ", dag=dag, pool="factor")
interday_alpha_ti0 = SSHOperator(task_id="kd05_interday_alpha_ti0", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_factor_ti0.sh ", dag=dag, pool="factor")
factor_check_ti0 = SSHOperator(task_id="kd05_factor_check_ti0", ssh_conn_id="kd05_keydriver",command="sh /usr/lib/quant/factor/interday_alpha/scripts/factors_check_ti0.sh ", dag=dag, pool="factor")
""" 午盘因子任务 """
kd05_midday_factor = SSHOperator(task_id="kd05_midday_factor", ssh_conn_id="kd05_keydriver", command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_mid_factor.sh ", dag=dag, pool="factor")
kd05_midday_factor_check = SSHOperator(task_id="kd05_midday_factor_check", ssh_conn_id="kd05_keydriver", command="sh /usr/lib/quant/factor/interday_alpha/scripts/factors_check.sh ", dag=dag, pool="factor")

trigger_kd04_strategy = TriggerDagRunOperator(task_id="trigger_kd04_strategy", trigger_dag_id='KD05_kd_strategy', trigger_rule='all_success', dag=dag)

""" tio任务结束后触发kd04的strategy任务 """
check_qsdata >> l2_data_check >> daily_feature_cal >> convert_pkl >> save_feature_to_es >> interday_alpha_universe >> interday_alpha_ti0 >> factor_check_ti0 >> trigger_kd04_strategy
interday_alpha_universe >> kd05_midday_factor >> kd05_midday_factor_check >> trigger_kd04_strategy