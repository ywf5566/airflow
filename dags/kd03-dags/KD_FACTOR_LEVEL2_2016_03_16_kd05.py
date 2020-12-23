#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {'owner': 'afroot03'}

dag = DAG('KD-FACTOR-LEVEL2-2016-03-16-kd05',
          default_args=default_args,
          schedule_interval=None,
          start_date=datetime(2020, 12, 18, 18, 30))

fac_daily_l2_actbsdelta_ordercnt = BashOperator(task_id="fac_daily_l2_actbsdelta_ordercnt", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1099895 2016-03-16 2016-03-16 False ", dag=dag)
fac_daily_l2_madl_actntfl_to_proptinall_closecorr10 = BashOperator(task_id="fac_daily_l2_madl_actntfl_to_proptinall_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1442138 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_activebuy_turnover_close_propt = BashOperator(task_id="fac_daily_l2_activebuy_turnover_close_propt", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1327650 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_madlarge_activesell_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_madlarge_activesell_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1440914 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_firstn_mainforce_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_firstn_mainforce_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1441534 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_firstn_mainforce_turnover_netinflow_propt_m10 = BashOperator(task_id="fac_daily_l2_firstn_mainforce_turnover_netinflow_propt_m10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1442809 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_firstn_mainforce_sell_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_firstn_mainforce_sell_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1441492 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_madlarge_activebuy_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_madlarge_activebuy_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1440886 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_actnetinflow_turnover_proptinall_closecorr10 = BashOperator(task_id="fac_daily_l2_actnetinflow_turnover_proptinall_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1442800 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_firstn_mainforce_buy_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_firstn_mainforce_buy_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1441478 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_actbsdelta_volume_proptinall_mptorate = BashOperator(task_id="fac_daily_l2_actbsdelta_volume_proptinall_mptorate", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1384238 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_madlarge_netinflow_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_madlarge_netinflow_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1442082 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_madl_ntfl_to_actntfl_propt_closecorr10 = BashOperator(task_id="fac_daily_l2_madl_ntfl_to_actntfl_propt_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1442124 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_firstn_mf_ntfl_to_proptinall_closecorr10 = BashOperator(task_id="fac_daily_l2_firstn_mf_ntfl_to_proptinall_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1442828 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_madlarge_passivebuy_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_madlarge_passivebuy_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1441422 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_madl_ntfl_to_proptinall_closecorr10 = BashOperator(task_id="fac_daily_l2_madl_ntfl_to_proptinall_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1443180 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_actnetinflow_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_actnetinflow_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1441520 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_activesell_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_activesell_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1441464 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_madlarge_buy_turnover_pertrans_closecorr10 = BashOperator(task_id="fac_daily_l2_madlarge_buy_turnover_pertrans_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1442096 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_madlarge_sell_turnover_pertrans_closecorr10 = BashOperator(task_id="fac_daily_l2_madlarge_sell_turnover_pertrans_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1442462 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_madl_psvntfl_to_proptinall_closecorr10 = BashOperator(task_id="fac_daily_l2_madl_psvntfl_to_proptinall_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1442597 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_activebuy_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_activebuy_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1441450 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_firstn_mainforce_netinflow_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_firstn_mainforce_netinflow_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1441548 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_madlarge_passivesell_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_madlarge_passivesell_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1441254 2016-03-16 2016-04-16 False ", dag=dag)
fac_daily_l2_madl_actntfl_to_proptinall_msdelta = BashOperator(task_id="fac_daily_l2_madl_actntfl_to_proptinall_msdelta", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec-2016-2.sh 1405255 2016-03-16 2016-03-16 False ", dag=dag)

