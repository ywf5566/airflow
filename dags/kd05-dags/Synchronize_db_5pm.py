#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator

default_args = {'owner': 'afroot05', 'retries': 2, 'retry_delay': timedelta(minutes=1)}
dag = DAG('Synchronize_db_5pm',
          default_args=default_args,
          schedule_interval="0 17 * * *",
          catchup=False,
          start_date=datetime(2021, 5, 19, 16, 0))

# 合并l2解析的任务
level2_from_em = BashOperator(task_id="level2_from_em",
                             bash_command="sh /usr/lib/quant/factor/factor_repo/tools/l2code/l2source_file/sync.sh ", dag=dag)
level2_to_kd = BashOperator(task_id="level2_to_kd",
                           bash_command="sh /usr/lib/quant/factor/factor_repo/tools/l2code/parser/parser.sh ", dag=dag)

sync_stock_suspended = BashOperator(task_id="sync_stock_suspended",
                                    bash_command="sh /usr/lib/carter/dbsync/scripts/sync_stock_suspended.sh ", dag=dag)
sync_stock_st = BashOperator(task_id="sync_stock_st",
                             bash_command="sh /usr/lib/carter/dbsync/scripts/sync_stock_st.sh ", dag=dag)
em_sw_index = BashOperator(task_id="em_sw_index", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_em_sw_index.sh ",
                           dag=dag)
sync_kdb_sw_industry = BashOperator(task_id="sync_kdb_sw_industry",
                                    bash_command="sh /usr/lib/carter/dbsync/scripts/sync_sw_industry.sh ", dag=dag)
check_em_sw_index = BashOperator(task_id="check_em_sw_index",
                                 bash_command="sh /usr/lib/carter/dbsync/scripts/sw_industry_check.sh ", dag=dag)
eod_table = BashOperator(task_id="eod_table", bash_command="sh /usr/lib/carter/dbsync/scripts/sync_eod_jydb.sh ",
                         dag=dag)
sync_kdb_dayquota_at_5pm = BashOperator(task_id="sync_kdb_dayquota_at_5pm",
                                        bash_command="sh /usr/lib/carter/dbsync/scripts/sync_kdb_dayquota_at_5pm.sh ",
                                        dag=dag)
sync_trading_halt_quota = BashOperator(task_id="sync_trading_halt_quota",
                                       bash_command="sh /usr/lib/carter/dbsync/scripts/sync_trading_halt_quota.sh ",
                                       dag=dag)
sync_org_id_to_kdcode = BashOperator(task_id="sync_org_id_to_kdcode",
                                     bash_command="sh /usr/lib/carter/dbsync/scripts/sync_org_id_to_kdcode.sh ",
                                     dag=dag)
sync_stock_adjfactor = BashOperator(task_id="sync_stock_adjfactor",
                                    bash_command="sh /usr/lib/carter/dbsync/scripts/sync_stock_adjfactor.sh ", dag=dag)

# 加入 sync_minquota 和 qsdata_update
sync_minquota = BashOperator(task_id="sync_minquota",
                             bash_command="sh /usr/lib/carter/dbsync/scripts/sync_minquota.sh ", dag=dag)
update_qsdata = BashOperator(task_id="update_qsdata",
                             bash_command="sh /usr/lib/carter/dbsync/scripts/update_qsdata.sh ", dag=dag)
trigger_kd04_factor = TriggerDagRunOperator(task_id="trigger_factor_normal",
                                            trigger_dag_id="Factor_level2_and_normal", trigger_rule="all_success",
                                            dag=dag)

eod_table >> [sync_kdb_dayquota_at_5pm]
sync_kdb_sw_industry >> [check_em_sw_index]
sync_trading_halt_quota >> [sync_org_id_to_kdcode, sync_stock_adjfactor]
sync_kdb_dayquota_at_5pm >> [sync_trading_halt_quota]
sync_stock_st >> [eod_table]
sync_stock_suspended >> [eod_table]
check_em_sw_index >> [eod_table]
em_sw_index >> [check_em_sw_index]
level2_from_em >> level2_to_kd >> trigger_kd04_factor
[sync_stock_adjfactor, sync_org_id_to_kdcode, sync_minquota] >> update_qsdata >> trigger_kd04_factor