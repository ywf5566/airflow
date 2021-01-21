#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator

default_args = {'owner': 'afroot03',
                'retries': 1,
                'retry_delay': timedelta(minutes=1)
                }

dag = DAG('KD_FACTOR_LEVEL2_AND_NORMAL',
          default_args=default_args,
          schedule_interval='40 17 * * *',
          catchup=False,
          start_date=datetime(2020, 12, 21, 17, 50))

check_qsdata = BashOperator(task_id="check_qsdata", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-repo-dep-check.sh check_qsdata ", dag=dag)
fac_daily_alpha_zs_8 = BashOperator(task_id="fac_daily_alpha_zs_8", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 89070 ", dag=dag)
fac_daily_fastmadivslowma_20_60 = BashOperator(task_id="fac_daily_fastmadivslowma_20_60", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2615 ", dag=dag)
fac_quarter_s_fa_assetsturn = BashOperator(task_id="fac_quarter_s_fa_assetsturn", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2782 ", dag=dag)
fac_daily_netprofit_grow_rate = BashOperator(task_id="fac_daily_netprofit_grow_rate", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3654324 ", dag=dag)
fac_daily_close = BashOperator(task_id="fac_daily_close", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3757480 ", dag=dag)
fac_daily_alpha_zs_1 = BashOperator(task_id="fac_daily_alpha_zs_1", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 60733 ", dag=dag)
fac_daily_alpha_zs_2 = BashOperator(task_id="fac_daily_alpha_zs_2", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 63798 ", dag=dag)
fac_daily_alpha_zs_5_31 = BashOperator(task_id="fac_daily_alpha_zs_5_31", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 56086 ", dag=dag)
fac_daily_alpha_zs_4 = BashOperator(task_id="fac_daily_alpha_zs_4", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 78983 ", dag=dag)
fac_daily_alpha_zs_6 = BashOperator(task_id="fac_daily_alpha_zs_6", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 78980 ", dag=dag)
fac_daily_alpha_zs_7 = BashOperator(task_id="fac_daily_alpha_zs_7", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 88257 ", dag=dag)
fac_daily_con_npcgrate_2y_roll = BashOperator(task_id="fac_daily_con_npcgrate_2y_roll", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2705 ", dag=dag)
fac_daily_hc2cl_5_d = BashOperator(task_id="fac_daily_hc2cl_5_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773791 ", dag=dag)
fac_daily_h2c_120_d = BashOperator(task_id="fac_daily_h2c_120_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2605 ", dag=dag)
fac_daily_l2c_3_d = BashOperator(task_id="fac_daily_l2c_3_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773794 ", dag=dag)
fac_daily_l2c_120_d = BashOperator(task_id="fac_daily_l2c_120_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2614 ", dag=dag)
fac_daily_l2c_20_d = BashOperator(task_id="fac_daily_l2c_20_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2612 ", dag=dag)
fac_daily_h2c_20_d = BashOperator(task_id="fac_daily_h2c_20_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2603 ", dag=dag)
fac_daily_kd_negative_score = BashOperator(task_id="fac_daily_kd_negative_score", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3949907 ", dag=dag)
fac_daily_alpha_zs_5_31_daily = BashOperator(task_id="fac_daily_alpha_zs_5_31_daily", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 59096 ", dag=dag)
fac_daily_h2c_3_d = BashOperator(task_id="fac_daily_h2c_3_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773782 ", dag=dag)
fac_daily_hc2cl_3_d = BashOperator(task_id="fac_daily_hc2cl_3_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773790 ", dag=dag)
fac_daily_h2l_3_d = BashOperator(task_id="fac_daily_h2l_3_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773786 ", dag=dag)
fac_daily_h2l_120_d = BashOperator(task_id="fac_daily_h2l_120_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2608 ", dag=dag)
fac_daily_hc2cl_15_d = BashOperator(task_id="fac_daily_hc2cl_15_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773793 ", dag=dag)
fac_daily_hc2cl_10_d = BashOperator(task_id="fac_daily_hc2cl_10_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773792 ", dag=dag)
fac_daily_h2c_10_d = BashOperator(task_id="fac_daily_h2c_10_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773784 ", dag=dag)
fac_daily_h2c_5_d = BashOperator(task_id="fac_daily_h2c_5_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773783 ", dag=dag)
fac_daily_beta = BashOperator(task_id="fac_daily_beta", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 418415 ", dag=dag)
fac_daily_rtn_20 = BashOperator(task_id="fac_daily_rtn_20", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3691464 ", dag=dag)
fac_daily_h2l_20_d = BashOperator(task_id="fac_daily_h2l_20_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2606 ", dag=dag)
fac_daily_hc2cl_60_d = BashOperator(task_id="fac_daily_hc2cl_60_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2610 ", dag=dag)
fac_quarter_net_profit_excl_min_int_inc = BashOperator(task_id="fac_quarter_net_profit_excl_min_int_inc", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2858 ", dag=dag)
fac_daily_lnrtn = BashOperator(task_id="fac_daily_lnrtn", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 11377 ", dag=dag)
fac_daily_alpha_zs_3 = BashOperator(task_id="fac_daily_alpha_zs_3", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 78988 ", dag=dag)
fac_quarter_tot_cur_assets = BashOperator(task_id="fac_quarter_tot_cur_assets", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2795 ", dag=dag)
fac_daily_con_eps = BashOperator(task_id="fac_daily_con_eps", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5597631 ", dag=dag)
fac_daily_h2l_10_d = BashOperator(task_id="fac_daily_h2l_10_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773788 ", dag=dag)
fac_daily_l2c_10_d = BashOperator(task_id="fac_daily_l2c_10_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773796 ", dag=dag)
fac_daily_l2c_5_d = BashOperator(task_id="fac_daily_l2c_5_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773795 ", dag=dag)
fac_daily_fastmadivslowma_20_90 = BashOperator(task_id="fac_daily_fastmadivslowma_20_90", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2616 ", dag=dag)
fac_daily_interday_close = BashOperator(task_id="fac_daily_interday_close", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3982302 ", dag=dag)
fac_daily_random_daily_factor = BashOperator(task_id="fac_daily_random_daily_factor", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1055903 ", dag=dag)
fac_daily_h2l_60_d = BashOperator(task_id="fac_daily_h2l_60_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2607 ", dag=dag)
fac_daily_h2c_60_d = BashOperator(task_id="fac_daily_h2c_60_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2604 ", dag=dag)
fac_daily_hc2cl_120_d = BashOperator(task_id="fac_daily_hc2cl_120_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2611 ", dag=dag)
fac_daily_l2c_60_d = BashOperator(task_id="fac_daily_l2c_60_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2613 ", dag=dag)
fac_daily_l2c_15_d = BashOperator(task_id="fac_daily_l2c_15_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773797 ", dag=dag)
fac_daily_hc2cl_20_d = BashOperator(task_id="fac_daily_hc2cl_20_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2609 ", dag=dag)
fac_daily_volume_ratio_d_5 = BashOperator(task_id="fac_daily_volume_ratio_d_5", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3977425 ", dag=dag)
fac_quarter_s_qfa_yoynetprofit = BashOperator(task_id="fac_quarter_s_qfa_yoynetprofit", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2794 ", dag=dag)
fac_daily_fastmadivslowma_20_120 = BashOperator(task_id="fac_daily_fastmadivslowma_20_120", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2617 ", dag=dag)
fac_daily_alpha_ZS_5_daily = BashOperator(task_id="fac_daily_alpha_ZS_5_daily", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 51947 ", dag=dag)
fac_daily_h2c_15_d = BashOperator(task_id="fac_daily_h2c_15_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773785 ", dag=dag)
fac_daily_nextday_close = BashOperator(task_id="fac_daily_nextday_close", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3982320 ", dag=dag)
fac_daily_smart_money = BashOperator(task_id="fac_daily_smart_money", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3977424 ", dag=dag)
fac_daily_h2l_5_d = BashOperator(task_id="fac_daily_h2l_5_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773787 ", dag=dag)
fac_daily_nw_abs_netbuyshares = BashOperator(task_id="fac_daily_nw_abs_netbuyshares", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5579926 ", dag=dag)
l2_data_check = BashOperator(task_id="l2_data_check", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-repo-dep-check.sh check_l2_data ", dag=dag)
fac_daily_alpha_ZS_5 = BashOperator(task_id="fac_daily_alpha_ZS_5", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 56085 ", dag=dag)
fac_daily_ln_s_dq_mv = BashOperator(task_id="fac_daily_ln_s_dq_mv", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2806 ", dag=dag)
fac_daily_tf_alpha_1 = BashOperator(task_id="fac_daily_tf_alpha_1", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 415365 ", dag=dag)
fac_daily_h2l_15_d = BashOperator(task_id="fac_daily_h2l_15_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773789 ", dag=dag)
fac_daily_delta_rd_kurt = BashOperator(task_id="fac_daily_delta_rd_kurt", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 460253 ", dag=dag)
fac_daily_std_5_d = BashOperator(task_id="fac_daily_std_5_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773772 ", dag=dag)
fac_daily_ret_10_d = BashOperator(task_id="fac_daily_ret_10_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773780 ", dag=dag)
fac_daily_std_15_d = BashOperator(task_id="fac_daily_std_15_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773774 ", dag=dag)
fac_daily_std_20_d = BashOperator(task_id="fac_daily_std_20_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2910 ", dag=dag)
fac_daily_ret_20_d = BashOperator(task_id="fac_daily_ret_20_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3830157 ", dag=dag)
fac_daily_alpha_regbench_HS300_252_63_1 = BashOperator(task_id="fac_daily_alpha_regbench_HS300_252_63_1", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2883 ", dag=dag)
fac_daily_barradastd_252_42_0 = BashOperator(task_id="fac_daily_barradastd_252_42_0", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2904 ", dag=dag)
fac_daily_ret_120_d = BashOperator(task_id="fac_daily_ret_120_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3830159 ", dag=dag)
fac_daily_alpha_regbench_ZZ500_252_63_1 = BashOperator(task_id="fac_daily_alpha_regbench_ZZ500_252_63_1", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2886 ", dag=dag)
fac_daily_std_3_d = BashOperator(task_id="fac_daily_std_3_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773771 ", dag=dag)
fac_daily_barramom_252_126_21 = BashOperator(task_id="fac_daily_barramom_252_126_21", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2896 ", dag=dag)
fac_daily_dastd_252_42_True = BashOperator(task_id="fac_daily_dastd_252_42_True", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 11378 ", dag=dag)
fac_daily_std_60_d = BashOperator(task_id="fac_daily_std_60_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2911 ", dag=dag)
fac_daily_barrasduse3_63_21 = BashOperator(task_id="fac_daily_barrasduse3_63_21", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2895 ", dag=dag)
fac_daily_cmra_21_12_True = BashOperator(task_id="fac_daily_cmra_21_12_True", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 29988 ", dag=dag)
fac_daily_ret_60_d = BashOperator(task_id="fac_daily_ret_60_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3830158 ", dag=dag)
fac_daily_alpha_regbench_ZZ800_252_63_1 = BashOperator(task_id="fac_daily_alpha_regbench_ZZ800_252_63_1", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2889 ", dag=dag)
fac_daily_std_10_d = BashOperator(task_id="fac_daily_std_10_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773773 ", dag=dag)
fac_daily_ret_15_d = BashOperator(task_id="fac_daily_ret_15_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773781 ", dag=dag)
fac_daily_ret_3_d = BashOperator(task_id="fac_daily_ret_3_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773778 ", dag=dag)
fac_daily_std_120_d = BashOperator(task_id="fac_daily_std_120_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2912 ", dag=dag)
fac_daily_barracmra_21_12 = BashOperator(task_id="fac_daily_barracmra_21_12", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2892 ", dag=dag)
fac_daily_ret_5_d = BashOperator(task_id="fac_daily_ret_5_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773779 ", dag=dag)
fac_quarter_debt2ncassets = BashOperator(task_id="fac_quarter_debt2ncassets", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2931 ", dag=dag)
fac_daily_interday_dq_turn = BashOperator(task_id="fac_daily_interday_dq_turn", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3982305 ", dag=dag)
fac_daily_interday_close_vol_corr_d10 = BashOperator(task_id="fac_daily_interday_close_vol_corr_d10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3982303 ", dag=dag)
fac_daily_nextday_close_vol_corr_d10 = BashOperator(task_id="fac_daily_nextday_close_vol_corr_d10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3982321 ", dag=dag)
fac_daily_nextday_dq_turn = BashOperator(task_id="fac_daily_nextday_dq_turn", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3982323 ", dag=dag)
fac_daily_l2_actbsdelta_ordercnt = BashOperator(task_id="fac_daily_l2_actbsdelta_ordercnt", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1099895 ", dag=dag)
fac_daily_level2_act = BashOperator(task_id="fac_daily_level2_act", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 516213 ", dag=dag)
fac_daily_l2_activebuy_turnover_close_propt = BashOperator(task_id="fac_daily_l2_activebuy_turnover_close_propt", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1327650 ", dag=dag)
fac_daily_l2v2_close_madlarge_netinflow_turnover = BashOperator(task_id="fac_daily_l2v2_close_madlarge_netinflow_turnover", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3892744 ", dag=dag)
fac_daily_level2_m_13_16_high = BashOperator(task_id="fac_daily_level2_m_13_16_high", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3982319 ", dag=dag)
fac_daily_l2_madlarge_buy_madlarge_sell_turnover = BashOperator(task_id="fac_daily_l2_madlarge_buy_madlarge_sell_turnover", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3724827 ", dag=dag)
fac_daily_to_10_d = BashOperator(task_id="fac_daily_to_10_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773769 ", dag=dag)
fac_daily_pegcon = BashOperator(task_id="fac_daily_pegcon", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2810 ", dag=dag)
fac_daily_barraliquidity_21 = BashOperator(task_id="fac_daily_barraliquidity_21", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2900 ", dag=dag)
fac_daily_irff_60 = BashOperator(task_id="fac_daily_irff_60", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2841 ", dag=dag)
fac_daily_irff_120 = BashOperator(task_id="fac_daily_irff_120", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2843 ", dag=dag)
fac_daily_to_120_d = BashOperator(task_id="fac_daily_to_120_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2920 ", dag=dag)
fac_daily_to_60_d = BashOperator(task_id="fac_daily_to_60_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2919 ", dag=dag)
fac_daily_ncasset2mv = BashOperator(task_id="fac_daily_ncasset2mv", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2809 ", dag=dag)
fac_daily_to_20_d = BashOperator(task_id="fac_daily_to_20_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2918 ", dag=dag)
fac_daily_to_3_d = BashOperator(task_id="fac_daily_to_3_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773767 ", dag=dag)
fac_daily_irff_20 = BashOperator(task_id="fac_daily_irff_20", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2839 ", dag=dag)
fac_daily_to_15_d = BashOperator(task_id="fac_daily_to_15_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773770 ", dag=dag)
fac_daily_to_5_d = BashOperator(task_id="fac_daily_to_5_d", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3773768 ", dag=dag)
fac_daily_barra_residvltl_1 = BashOperator(task_id="fac_daily_barra_residvltl_1", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 2929 ", dag=dag)
fac_daily_l2_madsmall_netinflow_turnover_proptinall_m10 = BashOperator(task_id="fac_daily_l2_madsmall_netinflow_turnover_proptinall_m10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1443217 ", dag=dag)
fac_daily_l2_madsmall_passivebuy_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_madsmall_passivebuy_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441436 ", dag=dag)
fac_daily_l2_madl_actntfl_to_proptinall_closecorr10 = BashOperator(task_id="fac_daily_l2_madl_actntfl_to_proptinall_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442138 ", dag=dag)
fac_daily_l2_mainforce_psvnetinflow_turnover_proptinall_m10 = BashOperator(task_id="fac_daily_l2_mainforce_psvnetinflow_turnover_proptinall_m10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441823 ", dag=dag)
fac_daily_l2_small_passivesell_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_small_passivesell_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1440830 ", dag=dag)
fac_daily_l2_madlarge_turnover_netinflow_propt_closecorr10 = BashOperator(task_id="fac_daily_l2_madlarge_turnover_netinflow_propt_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1443166 ", dag=dag)
fac_daily_l2_small_netinflow_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_small_netinflow_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441576 ", dag=dag)
fac_daily_l2_mf_ntfl_to_actntfl_propt_closecorr10 = BashOperator(task_id="fac_daily_l2_mf_ntfl_to_actntfl_propt_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441702 ", dag=dag)
fac_daily_l2_mainforce_turnover_active_propt_closecorr10 = BashOperator(task_id="fac_daily_l2_mainforce_turnover_active_propt_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441688 ", dag=dag)
fac_daily_l2_madsmall_turnover_netinflow_propt_closecorr10 = BashOperator(task_id="fac_daily_l2_madsmall_turnover_netinflow_propt_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1443208 ", dag=dag)
fac_daily_l2_mainforce_activebuy_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_mainforce_activebuy_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1440788 ", dag=dag)
fac_daily_l2_actnetinflow_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_actnetinflow_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441520 ", dag=dag)
fac_daily_l2_small_buy_turnover_pertrans_closecorr10 = BashOperator(task_id="fac_daily_l2_small_buy_turnover_pertrans_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441590 ", dag=dag)
fac_daily_l2_ceil_board_seconds = BashOperator(task_id="fac_daily_l2_ceil_board_seconds", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3856872 ", dag=dag)
fac_daily_l2_madlarge_activesell_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_madlarge_activesell_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1440914 ", dag=dag)
fac_daily_l2_small_psvnetinflow_turnover_proptinall_m10 = BashOperator(task_id="fac_daily_l2_small_psvnetinflow_turnover_proptinall_m10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441795 ", dag=dag)
fac_daily_l2_mainforce_passivebuy_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_mainforce_passivebuy_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1440872 ", dag=dag)
fac_daily_l2_madsmall_turnover_active_propt_closecorr10 = BashOperator(task_id="fac_daily_l2_madsmall_turnover_active_propt_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442222 ", dag=dag)
fac_daily_l2_small_netinflow_turnover_proptinall_closecorr10 = BashOperator(task_id="fac_daily_l2_small_netinflow_turnover_proptinall_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442870 ", dag=dag)
fac_daily_l2_small_passivebuy_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_small_passivebuy_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1440858 ", dag=dag)
fac_daily_l2_firstn_mainforce_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_firstn_mainforce_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441534 ", dag=dag)
fac_daily_l2_firstn_mainforce_turnover_netinflow_propt_m10 = BashOperator(task_id="fac_daily_l2_firstn_mainforce_turnover_netinflow_propt_m10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442809 ", dag=dag)
fac_daily_l2_madlarge_passivesell_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_madlarge_passivesell_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441254 ", dag=dag)
fac_daily_l2_firstn_mainforce_sell_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_firstn_mainforce_sell_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441492 ", dag=dag)
fac_daily_l2_activebuy_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_activebuy_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441450 ", dag=dag)
fac_daily_l2_madlarge_activebuy_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_madlarge_activebuy_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1440886 ", dag=dag)
fac_daily_l2_activesell_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_activesell_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441464 ", dag=dag)
fac_daily_l2_actnetinflow_turnover_proptinall_closecorr10 = BashOperator(task_id="fac_daily_l2_actnetinflow_turnover_proptinall_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442800 ", dag=dag)
fac_daily_l2_firstn_mainforce_buy_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_firstn_mainforce_buy_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441478 ", dag=dag)
fac_daily_l2_actbsdelta_volume_proptinall_mptorate = BashOperator(task_id="fac_daily_l2_actbsdelta_volume_proptinall_mptorate", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1384238 ", dag=dag)
fac_daily_l2_madsmall_activesell_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_madsmall_activesell_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1440928 ", dag=dag)
fac_daily_l2_firstn_mf_ntfl_to_proptinall_closecorr10 = BashOperator(task_id="fac_daily_l2_firstn_mf_ntfl_to_proptinall_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442828 ", dag=dag)
fac_daily_l2_turnover_mainforce_propt_closecorr10 = BashOperator(task_id="fac_daily_l2_turnover_mainforce_propt_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442884 ", dag=dag)
fac_daily_l2_small_activesell_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_small_activesell_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1440802 ", dag=dag)
fac_daily_l2_madl_ntfl_to_actntfl_propt_closecorr10 = BashOperator(task_id="fac_daily_l2_madl_ntfl_to_actntfl_propt_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442124 ", dag=dag)
fac_daily_l2_madlarge_netinflow_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_madlarge_netinflow_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442082 ", dag=dag)
fac_daily_l2_mainforce_sell_turnover_pertrans_closecorr10 = BashOperator(task_id="fac_daily_l2_mainforce_sell_turnover_pertrans_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441744 ", dag=dag)
fac_daily_l2_madlarge_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_madlarge_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441842 ", dag=dag)
fac_daily_l2_madsmall_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_madsmall_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442152 ", dag=dag)
fac_daily_l2_madlarge_passivebuy_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_madlarge_passivebuy_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441422 ", dag=dag)
fac_daily_l2_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1440760 ", dag=dag)
fac_daily_l2_madl_ntfl_to_proptinall_closecorr10 = BashOperator(task_id="fac_daily_l2_madl_ntfl_to_proptinall_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1443180 ", dag=dag)
fac_daily_l2_small_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_small_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441562 ", dag=dag)
fac_daily_l2_mainforce_activesell_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_mainforce_activesell_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1440816 ", dag=dag)
fac_daily_l2_mainforce_netinflow_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_mainforce_netinflow_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441660 ", dag=dag)
fac_daily_l2_mainforce_buy_turnover_pertrans_closecorr10 = BashOperator(task_id="fac_daily_l2_mainforce_buy_turnover_pertrans_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441674 ", dag=dag)
fac_daily_l2_madsmall_netinflow_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_madsmall_netinflow_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442166 ", dag=dag)
fac_daily_l2_turnover_small_propt_closecorr10 = BashOperator(task_id="fac_daily_l2_turnover_small_propt_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442842 ", dag=dag)
fac_daily_l2_madlarge_buy_turnover_pertrans_closecorr10 = BashOperator(task_id="fac_daily_l2_madlarge_buy_turnover_pertrans_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442096 ", dag=dag)
fac_daily_l2_madlarge_sell_turnover_pertrans_closecorr10 = BashOperator(task_id="fac_daily_l2_madlarge_sell_turnover_pertrans_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442462 ", dag=dag)
fac_daily_l2_turnover_madlarge_propt_closecorr10 = BashOperator(task_id="fac_daily_l2_turnover_madlarge_propt_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1443152 ", dag=dag)
fac_daily_l2_madsmall_buy_turnover_pertrans_closecorr10 = BashOperator(task_id="fac_daily_l2_madsmall_buy_turnover_pertrans_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442180 ", dag=dag)
fac_daily_l2_madsmall_ntfl_to_actntfl_propt_closecorr10 = BashOperator(task_id="fac_daily_l2_madsmall_ntfl_to_actntfl_propt_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442434 ", dag=dag)
fac_daily_l2_mainforce_actnetinflow_turnover_proptinall_m10 = BashOperator(task_id="fac_daily_l2_mainforce_actnetinflow_turnover_proptinall_m10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441711 ", dag=dag)
fac_daily_l2_mainforce_passivesell_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_mainforce_passivesell_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1440844 ", dag=dag)
fac_daily_l2_turnover_madsmall_propt_closecorr10 = BashOperator(task_id="fac_daily_l2_turnover_madsmall_propt_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1443194 ", dag=dag)
fac_daily_l2_small_sell_turnover_pertrans_closecorr10 = BashOperator(task_id="fac_daily_l2_small_sell_turnover_pertrans_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441730 ", dag=dag)
fac_daily_l2_madlarge_turnover_active_propt_closecorr10 = BashOperator(task_id="fac_daily_l2_madlarge_turnover_active_propt_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442110 ", dag=dag)
fac_daily_l2_mainforce_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_mainforce_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441646 ", dag=dag)
fac_daily_l2_contrade_tunrover_activebuy_propt = BashOperator(task_id="fac_daily_l2_contrade_tunrover_activebuy_propt", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3885602 ", dag=dag)
fac_daily_l2_madsmall_sell_turnover_pertrans_closecorr10 = BashOperator(task_id="fac_daily_l2_madsmall_sell_turnover_pertrans_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442476 ", dag=dag)
fac_daily_l2_madsmall_psvnetinflow_turnover_proptinall_m10 = BashOperator(task_id="fac_daily_l2_madsmall_psvnetinflow_turnover_proptinall_m10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442781 ", dag=dag)
fac_daily_l2_madsmall_actnetinflow_turnover_proptinall_m10 = BashOperator(task_id="fac_daily_l2_madsmall_actnetinflow_turnover_proptinall_m10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442443 ", dag=dag)
fac_daily_l2_mainforce_turnover_netinflow_propt_closecorr10 = BashOperator(task_id="fac_daily_l2_mainforce_turnover_netinflow_propt_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442898 ", dag=dag)
fac_daily_l2_turnover_pertrans_closecorr10 = BashOperator(task_id="fac_daily_l2_turnover_pertrans_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441506 ", dag=dag)
fac_daily_l2_mainforce_netinflow_turnover_proptinall_m10 = BashOperator(task_id="fac_daily_l2_mainforce_netinflow_turnover_proptinall_m10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442907 ", dag=dag)
fac_daily_l2_small_netinflow_turnover_actnetinflow_propt_m10 = BashOperator(task_id="fac_daily_l2_small_netinflow_turnover_actnetinflow_propt_m10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441613 ", dag=dag)
fac_daily_l2_madsmall_passivesell_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_madsmall_passivesell_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441408 ", dag=dag)
fac_daily_l2_madl_psvntfl_to_proptinall_closecorr10 = BashOperator(task_id="fac_daily_l2_madl_psvntfl_to_proptinall_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442597 ", dag=dag)
fac_daily_l2_firstn_mainforce_netinflow_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_firstn_mainforce_netinflow_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441548 ", dag=dag)
fac_daily_l2_small_turnover_active_propt_closecorr10 = BashOperator(task_id="fac_daily_l2_small_turnover_active_propt_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441604 ", dag=dag)
fac_daily_l2_small_turnover_netinflow_propt_closecorr10 = BashOperator(task_id="fac_daily_l2_small_turnover_netinflow_propt_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1442856 ", dag=dag)
fac_daily_l2_small_actnetinflow_turnover_proptinall_m10 = BashOperator(task_id="fac_daily_l2_small_actnetinflow_turnover_proptinall_m10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1441627 ", dag=dag)
fac_daily_l2_madsmall_activebuy_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_madsmall_activebuy_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1440900 ", dag=dag)
fac_daily_l2_madl_actntfl_to_proptinall_msdelta = BashOperator(task_id="fac_daily_l2_madl_actntfl_to_proptinall_msdelta", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1405255 ", dag=dag)
fac_daily_l2_small_activebuy_turnover_closecorr10 = BashOperator(task_id="fac_daily_l2_small_activebuy_turnover_closecorr10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 1440774 ", dag=dag)
fac_daily_l2_actnetinflow_turnover_proptinall_openclose_delta = BashOperator(task_id="fac_daily_l2_actnetinflow_turnover_proptinall_openclose_delta", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3724836 ", dag=dag)
fac_daily_l2_contrade_tunrover_activebuy_propt_tsz20 = BashOperator(task_id="fac_daily_l2_contrade_tunrover_activebuy_propt_tsz20", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 3885605 ", dag=dag)
fac_daily_em_quote_addposdays10 = BashOperator(task_id="fac_daily_em_quote_addposdays10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5655788 ", dag=dag)
fac_daily_em_quote_close = BashOperator(task_id="fac_daily_em_quote_addposdays10", bash_command="sh /usr/lib/quant/factor/factor_repo/kdfactor/scripts/factor-exec.sh 5655802 ", dag=dag)

trigger_deap_and_check = TriggerDagRunOperator(
    task_id='trigger_deap_and_check',
    trigger_dag_id='KD-FACTOR-DEAP-AND-CHECK',
    trigger_rule='all_done',
    dag=dag
)
trigger_Interday_alpha_daily = TriggerDagRunOperator(
    task_id="trigger_Interday_alpha_daily",
    trigger_dag_id="Interday_alpha_daily",
    trigger_rule='all_success',
    dag=dag
)

fac_daily_barradastd_252_42_0 >> [fac_daily_barra_residvltl_1]
fac_quarter_s_fa_assetsturn >> [fac_daily_ncasset2mv]
fac_quarter_tot_cur_assets >> [fac_daily_ncasset2mv, fac_quarter_debt2ncassets]
fac_daily_interday_close >> [fac_daily_interday_dq_turn, fac_daily_interday_close_vol_corr_d10]
fac_daily_con_npcgrate_2y_roll >> [fac_daily_pegcon]
fac_daily_alpha_regbench_HS300_252_63_1 >> [fac_daily_barra_residvltl_1]
fac_daily_lnrtn >> [fac_daily_std_5_d, fac_daily_ret_10_d, fac_daily_std_15_d, fac_daily_std_20_d, fac_daily_ret_20_d, fac_daily_alpha_regbench_HS300_252_63_1, fac_daily_barradastd_252_42_0, fac_daily_ret_120_d, fac_daily_alpha_regbench_ZZ500_252_63_1, fac_daily_std_3_d, fac_daily_irff_120, fac_daily_barramom_252_126_21, fac_daily_dastd_252_42_True, fac_daily_irff_60, fac_daily_std_60_d, fac_daily_barrasduse3_63_21, fac_daily_cmra_21_12_True, fac_daily_ret_60_d, fac_daily_alpha_regbench_ZZ800_252_63_1, fac_daily_std_10_d, fac_daily_ret_15_d, fac_daily_ret_3_d, fac_daily_std_120_d, fac_daily_barracmra_21_12, fac_daily_irff_20, fac_daily_ret_5_d]

fac_daily_l2_actbsdelta_ordercnt >> [fac_daily_l2_madsmall_netinflow_turnover_proptinall_m10,
                                     fac_daily_l2_madsmall_passivebuy_turnover_closecorr10,
                                     fac_daily_l2_madl_actntfl_to_proptinall_closecorr10,
                                     fac_daily_l2_mainforce_psvnetinflow_turnover_proptinall_m10,
                                     fac_daily_l2_small_passivesell_turnover_closecorr10,
                                     fac_daily_l2_madlarge_turnover_netinflow_propt_closecorr10,
                                     fac_daily_l2_small_netinflow_turnover_closecorr10,
                                     fac_daily_l2_mf_ntfl_to_actntfl_propt_closecorr10,
                                     fac_daily_l2_mainforce_turnover_active_propt_closecorr10,
                                     fac_daily_l2_madsmall_turnover_netinflow_propt_closecorr10, fac_daily_l2_mainforce_activebuy_turnover_closecorr10, fac_daily_l2_actnetinflow_turnover_closecorr10, fac_daily_l2_small_buy_turnover_pertrans_closecorr10, fac_daily_l2_madsmall_activesell_turnover_closecorr10, fac_daily_l2_madlarge_activesell_turnover_closecorr10, fac_daily_l2_small_psvnetinflow_turnover_proptinall_m10, fac_daily_l2_mainforce_passivebuy_turnover_closecorr10, fac_daily_l2_madsmall_turnover_active_propt_closecorr10, fac_daily_l2_small_netinflow_turnover_proptinall_closecorr10, fac_daily_l2_small_passivebuy_turnover_closecorr10, fac_daily_l2_firstn_mainforce_turnover_closecorr10, fac_daily_l2_firstn_mainforce_turnover_netinflow_propt_m10, fac_daily_l2_firstn_mainforce_sell_turnover_closecorr10, fac_daily_l2_activebuy_turnover_closecorr10, fac_daily_l2_madlarge_activebuy_turnover_closecorr10, fac_daily_l2_activesell_turnover_closecorr10, fac_daily_l2_actnetinflow_turnover_proptinall_closecorr10, fac_daily_l2_firstn_mainforce_buy_turnover_closecorr10, fac_daily_l2_actbsdelta_volume_proptinall_mptorate, fac_daily_l2_turnover_madsmall_propt_closecorr10, fac_daily_l2_firstn_mf_ntfl_to_proptinall_closecorr10, fac_daily_l2_turnover_mainforce_propt_closecorr10, fac_daily_l2_small_activesell_turnover_closecorr10, fac_daily_l2_madl_ntfl_to_actntfl_propt_closecorr10, fac_daily_l2_madlarge_netinflow_turnover_closecorr10, fac_daily_l2_mainforce_sell_turnover_pertrans_closecorr10, fac_daily_l2_madlarge_turnover_closecorr10, fac_daily_l2_madsmall_turnover_closecorr10, fac_daily_l2_madlarge_passivebuy_turnover_closecorr10, fac_daily_l2_actnetinflow_turnover_proptinall_openclose_delta, fac_daily_l2_turnover_closecorr10, fac_daily_l2_madl_ntfl_to_proptinall_closecorr10, fac_daily_l2_ceil_board_seconds, fac_daily_l2_mainforce_activesell_turnover_closecorr10, fac_daily_l2_mainforce_netinflow_turnover_closecorr10, fac_daily_l2_mainforce_buy_turnover_pertrans_closecorr10, fac_daily_l2_madsmall_netinflow_turnover_closecorr10, fac_daily_l2_turnover_small_propt_closecorr10, fac_daily_l2_madlarge_buy_turnover_pertrans_closecorr10, fac_daily_l2_small_turnover_active_propt_closecorr10, fac_daily_l2_turnover_madlarge_propt_closecorr10, fac_daily_l2_mainforce_passivesell_turnover_closecorr10, fac_daily_l2_madsmall_buy_turnover_pertrans_closecorr10, fac_daily_l2_madsmall_ntfl_to_actntfl_propt_closecorr10, fac_daily_l2_mainforce_actnetinflow_turnover_proptinall_m10, fac_daily_l2_madlarge_sell_turnover_pertrans_closecorr10, fac_daily_l2_small_netinflow_turnover_actnetinflow_propt_m10, fac_daily_l2_madsmall_psvnetinflow_turnover_proptinall_m10, fac_daily_l2_small_sell_turnover_pertrans_closecorr10,
                                     fac_daily_l2_madlarge_turnover_active_propt_closecorr10,
                                     fac_daily_l2_mainforce_turnover_closecorr10, fac_daily_l2_contrade_tunrover_activebuy_propt, fac_daily_l2_madsmall_sell_turnover_pertrans_closecorr10,
                                     fac_daily_l2_small_turnover_closecorr10, fac_daily_l2_madsmall_actnetinflow_turnover_proptinall_m10,
                                     fac_daily_l2_mainforce_turnover_netinflow_propt_closecorr10, fac_daily_l2_turnover_pertrans_closecorr10,
                                     fac_daily_l2_mainforce_netinflow_turnover_proptinall_m10, fac_daily_l2_madsmall_passivesell_turnover_closecorr10,
                                     fac_daily_l2_madl_psvntfl_to_proptinall_closecorr10, fac_daily_l2_firstn_mainforce_netinflow_turnover_closecorr10,
                                     fac_daily_l2_madlarge_passivesell_turnover_closecorr10, fac_daily_l2_small_turnover_netinflow_propt_closecorr10,
                                     fac_daily_l2_small_actnetinflow_turnover_proptinall_m10, fac_daily_l2_madsmall_activebuy_turnover_closecorr10, fac_daily_l2_madl_actntfl_to_proptinall_msdelta,
                                     fac_daily_l2_small_activebuy_turnover_closecorr10] >> trigger_deap_and_check

check_qsdata >> [fac_daily_em_quote_addposdays10, fac_daily_em_quote_close, fac_daily_alpha_zs_8, fac_daily_fastmadivslowma_20_60, fac_quarter_s_fa_assetsturn, fac_daily_netprofit_grow_rate, fac_daily_hc2cl_15_d, fac_daily_close, fac_daily_alpha_zs_1, fac_daily_alpha_zs_2, fac_daily_alpha_zs_5_31, fac_daily_alpha_zs_4, fac_daily_alpha_zs_6, fac_daily_alpha_zs_7, fac_daily_con_npcgrate_2y_roll, fac_daily_hc2cl_5_d, fac_daily_h2c_120_d, fac_daily_l2c_3_d, fac_daily_l2c_120_d, fac_daily_l2c_20_d, fac_daily_h2c_20_d, fac_daily_kd_negative_score, fac_daily_h2c_3_d, fac_daily_hc2cl_3_d, fac_daily_h2l_3_d, fac_daily_h2l_120_d, fac_daily_alpha_zs_5_31_daily, fac_daily_l2c_15_d, fac_daily_h2l_60_d, fac_daily_hc2cl_10_d, fac_daily_h2c_10_d, fac_daily_h2c_5_d, fac_daily_rtn_20, fac_daily_h2l_20_d, fac_daily_hc2cl_60_d, fac_quarter_net_profit_excl_min_int_inc, fac_daily_lnrtn, fac_daily_alpha_zs_3, fac_quarter_tot_cur_assets, fac_daily_beta, fac_daily_h2l_10_d, fac_daily_l2c_10_d, fac_daily_l2c_5_d, fac_daily_fastmadivslowma_20_90, fac_daily_interday_close, fac_daily_random_daily_factor, fac_daily_h2l_15_d, fac_daily_h2c_60_d, fac_daily_hc2cl_120_d, fac_daily_l2c_60_d, fac_daily_hc2cl_20_d, fac_daily_con_eps, fac_quarter_s_qfa_yoynetprofit, fac_daily_fastmadivslowma_20_120, fac_daily_alpha_ZS_5_daily, fac_daily_h2c_15_d, fac_daily_nextday_close, fac_daily_smart_money, fac_daily_h2l_5_d, fac_daily_nw_abs_netbuyshares, l2_data_check, fac_daily_alpha_ZS_5, fac_daily_ln_s_dq_mv, fac_daily_tf_alpha_1, fac_daily_volume_ratio_d_5]
fac_daily_barracmra_21_12 >> [fac_daily_barra_residvltl_1]
fac_daily_l2_activebuy_turnover_close_propt >> [fac_daily_l2_actnetinflow_turnover_proptinall_openclose_delta]
fac_daily_l2_contrade_tunrover_activebuy_propt >> [fac_daily_l2_contrade_tunrover_activebuy_propt_tsz20]
fac_daily_beta >> [fac_daily_delta_rd_kurt]
fac_daily_nextday_close >> [fac_daily_nextday_close_vol_corr_d10, fac_daily_nextday_dq_turn]
l2_data_check >> [fac_daily_l2_actbsdelta_ordercnt, fac_daily_level2_act, fac_daily_l2_activebuy_turnover_close_propt, fac_daily_l2v2_close_madlarge_netinflow_turnover, fac_daily_level2_m_13_16_high, fac_daily_l2_madlarge_buy_madlarge_sell_turnover]
fac_daily_ln_s_dq_mv >> [trigger_Interday_alpha_daily, fac_daily_to_10_d, fac_daily_pegcon, fac_daily_barraliquidity_21, fac_daily_irff_60, fac_daily_irff_120, fac_daily_to_120_d, fac_daily_to_60_d, fac_daily_ncasset2mv, fac_daily_to_20_d, fac_daily_to_3_d, fac_daily_irff_20, fac_daily_l2_ceil_board_seconds, fac_daily_to_15_d, fac_daily_to_5_d]


