#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.ssh_operator import SSHOperator

default_args = {'owner': 'afroot04', 'retries': 2, 'retry_delay': timedelta(minutes=1)}
dag = DAG('synchronize_db_5pm',
          default_args=default_args,
          schedule_interval='0 17 * * *',
          catchup=False,
          start_date=datetime(2020, 12, 24, 16, 0))
          
sync_stock_suspended = BashOperator(task_id="sync_stock_suspended", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_stock_suspended.sh ", dag=dag)
sync_stock_st = BashOperator(task_id="sync_stock_st", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_stock_st.sh ", dag=dag)
em_sw_index = BashOperator(task_id="em_sw_index", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_em_sw_index.sh ", dag=dag)
sync_kdb_sw_industry = BashOperator(task_id="sync_kdb_sw_industry", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_sw_industry.sh ", dag=dag)
check_em_sw_index = BashOperator(task_id="check_em_sw_index", bash_command="sh /usr/lib/carter/dbsync/scripts/sw_industry_check.sh ", dag=dag)
eod_table = BashOperator(task_id="eod_table", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_eod_jydb.sh ", dag=dag)
sync_kdb_dayquota_at_5pm = BashOperator(task_id="sync_kdb_dayquota_at_5pm", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_kdb_dayquota_at_5pm.sh ", dag=dag)
sync_trading_halt_quota = BashOperator(task_id="sync_trading_halt_quota", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_trading_halt_quota.sh ", dag=dag)
sync_org_id_to_kdcode = BashOperator(task_id="sync_org_id_to_kdcode", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_org_id_to_kdcode.sh ", dag=dag)
sync_stock_adjfactor = BashOperator(task_id="sync_stock_adjfactor", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_stock_adjfactor.sh ", dag=dag)

# 加入 sync_minquota 和 qsdata_update
sync_minquota = BashOperator(task_id="sync_minquota",
                             bash_command="sh /usr/lib/carter/dbsync/scripts/sync_minquota.sh ", dag=dag)
update_qsdata = BashOperator(task_id="update_qsdata",
                             bash_command="sh /usr/lib/carter/dbsync/scripts/update_qsdata.sh ", dag=dag)
# 2021-05-19添加fix_adjfactor
fix_adjfactor = BashOperator(task_id="fix_adjfactor",
                             bash_command="sh /usr/lib/carter/dbsync/scripts/fix_kdadjfactor.sh ", dag=dag)

trigger_kd05_factor = SSHOperator(task_id="trigger_05_factor", ssh_conn_id="kd05@keydriver", command="source /home/keydriver/airflow/bin/activate;airflow trigger_dag Factor_level2_and_normal ")
eod_table >> [sync_kdb_dayquota_at_5pm]
sync_kdb_sw_industry >> [check_em_sw_index]
sync_trading_halt_quota >> [sync_org_id_to_kdcode, sync_stock_adjfactor]
sync_kdb_dayquota_at_5pm >> [sync_trading_halt_quota]
sync_stock_st >> [eod_table]
sync_stock_suspended >> [eod_table]
check_em_sw_index >> [eod_table]
em_sw_index >> [check_em_sw_index]

sync_stock_adjfactor >> fix_adjfactor
[sync_stock_adjfactor, sync_org_id_to_kdcode, sync_minquota, fix_adjfactor] >> update_qsdata >> trigger_kd05_factor