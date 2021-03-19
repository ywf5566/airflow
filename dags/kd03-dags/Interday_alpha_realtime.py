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
default_args = {'owner': 'afroot03'}


class callBack:
    def on_dag_failure(self):
        os.environ['kdconfig'] = '/home/keydriver/airflow/kd_airflow/dags/database.yaml'
        send_message(msg_id='FACTOR_DAILY_RESULT',
                     msg_head=MSG_HEAD,
                     msg_level=MSG_LEVEL.CRITICAL.value,
                     service='因子库',
                     msg_type='服务运行结果正确性检查',
                     msg_description='因子库脚本运行失败！',
                     env=ENV.PROD.value,
                     dt=datetime.now(),
                     host_name='kd03',
                     detailed_information='kd03因子任务：Interday_alpha_realtime运行异常！')


dag = DAG('Interday_alpha_realtime',
          default_args=default_args,
          schedule_interval='40 10 * * 1-5',
          catchup=False,
          start_date=datetime(2020, 12, 17, 10, 40), on_failure_callback=callBack.on_dag_failure)
realtime_cal_factor = BashOperator(task_id="realtime_cal_factor", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/run_realtime.sh ", dag=dag)
factor_check = BashOperator(task_id="factor_check", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/factors_check.sh ", dag=dag)
# factor_kd05 = BashOperator(task_id="factor_kd05", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/factors_kd05.sh ", dag=dag)
# factors_check_kd05 = BashOperator(task_id="factors_check_kd05", bash_command="sh /usr/lib/quant/factor/interday_alpha/scripts/factors_check_kd05.sh ", dag=dag)
realtime_cal_factor >> factor_check