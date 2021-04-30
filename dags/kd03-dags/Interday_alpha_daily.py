#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from monitor.core.send_message import send_message
from monitor.core.send_message import ENV
from monitor.core.send_message import MSG_HEAD
from monitor.core.send_message import MSG_LEVEL
import os
from airflow.contrib.operators.ssh_operator import SSHOperator


default_args = {'owner': 'afroot03'}


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
                     host_name='kd03',
                     detailed_information='kd03因子任务：Interday_alpha_daily运行异常！')


dag = DAG('Interday_alpha_daily',
          default_args=default_args,
          schedule_interval=None,
          catchup=False,
          start_date=datetime(2020, 12, 17, 18, 0),
          on_failure_callback=callBack.on_dag_failure)


check_qsdata = BashOperator(task_id="check_qsdata", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-repo-dep-check.sh check_qsdata ", dag=dag)
l2_data_check = BashOperator(task_id="l2_data_check", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-repo-dep-check.sh check_l2_data ", dag=dag)
daily_feature_cal = BashOperator(task_id="daily_feature_cal", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_daily_cal.sh ", dag=dag)
convert_pkl = BashOperator(task_id="convert_pkl", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_hdf2pkl.sh ", dag=dag)
save_feature_to_es = BashOperator(task_id="save_feature_to_es", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_pkl2es.sh ", dag=dag)
interday_alpha_universe = BashOperator(task_id="interday_alpha_universe", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_universe_ti0.sh ", dag=dag)
interday_alpha_ti0 = BashOperator(task_id="interday_alpha_ti0", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_factor_ti0.sh ", dag=dag)
factor_check_ti0 = BashOperator(task_id="factor_check_ti0", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/factors_check_ti0.sh ", dag=dag)
# 添加午盘因子的task
realtime_cal_factor = BashOperator(task_id="realtime_cal_factor", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_mid_factor.sh ", dag=dag)
factor_check = BashOperator(task_id="factor_check", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/factors_check.sh ", dag=dag)


# trigger_kd04_strategy = SSHOperator(task_id="trigger_kd04_strategy", ssh_conn_id="kd04_keydriver", command="source /home/keydriver/airflow/bin/activate;airflow trigger_dag KD05_kd_strategy ", dag=dag)

check_qsdata >> l2_data_check >> daily_feature_cal >> convert_pkl >> save_feature_to_es >> interday_alpha_universe >> interday_alpha_ti0 >> factor_check_ti0
interday_alpha_universe >> realtime_cal_factor >> factor_check