# -*- coding: utf-8 -*-
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'afroot01'
}

dag = DAG(
    'sync_kd_event',
    default_args=default_args,
    schedule_interval='0 20 * * *',
    start_date=datetime(2020, 12, 21, 20, 0)
)
# ==========================================================tasks======================================================
event_share_issue = BashOperator(task_id="event_share_issue", bash_command="sh /usr/lib/carter/kd_event/scripts/exe_event_pipeline_dev.sh stock_share_issue_pipeline.py ", dag=dag)
event_share_pledge = BashOperator(task_id="event_share_pledge", bash_command="sh /usr/lib/carter/kd_event/scripts/exe_event_pipeline_dev.sh stock_share_pledge_pipeline.py ", dag=dag)
event_mgt_accident = BashOperator(task_id="event_mgt_accident", bash_command="sh /usr/lib/carter/kd_event/scripts/exe_event_pipeline_dev.sh stock_mgt_accident_pipeline.py ", dag=dag)
event_stock_allotment = BashOperator(task_id="event_stock_allotment", bash_command="sh /usr/lib/carter/kd_event/scripts/exe_event_pipeline_dev.sh stock_allotment_pipeline.py ", dag=dag)
event_share_restrict = BashOperator(task_id="event_share_restrict", bash_command="sh /usr/lib/carter/kd_event/scripts/exe_event_pipeline_dev.sh stock_share_restrict_pipeline.py ", dag=dag)
event_personnel_change = BashOperator(task_id="event_personnel_change", bash_command="sh /usr/lib/carter/kd_event/scripts/exe_event_pipeline_dev.sh stock_personnel_change_pipeline.py ", dag=dag)
event_trade_suspension = BashOperator(task_id="event_trade_suspension", bash_command="sh /usr/lib/carter/kd_event/scripts/exe_event_pipeline_dev.sh stock_trade_suspension_pipeline.py ", dag=dag)
event_bonus_share = BashOperator(task_id="event_bonus_share", bash_command="sh /usr/lib/carter/kd_event/scripts/exe_event_pipeline_dev.sh stock_bonus_share_pipeline.py ", dag=dag)
event_stock_asset_regroup = BashOperator(task_id="event_stock_asset_regroup", bash_command="sh /usr/lib/carter/kd_event/scripts/exe_event_pipeline_dev.sh stock_asset_regroup_pipeline.py ", dag=dag)
event_stock_performance = BashOperator(task_id="event_stock_performance", bash_command="sh /usr/lib/carter/kd_event/scripts/exe_event_pipeline_dev.sh stock_performance_pipeline.py ", dag=dag)
event_mgt_data = BashOperator(task_id="event_mgt_data", bash_command="sh /usr/lib/carter/kd_event/scripts/exe_event_pipeline_dev.sh stock_mgt_data_pipeline.py ", dag=dag)
event_share_holding = BashOperator(task_id="event_share_holding", bash_command="sh /usr/lib/carter/kd_event/scripts/exe_event_pipeline_dev.sh stock_share_holding_pipeline.py ", dag=dag)
event_acceptance_of_bid = BashOperator(task_id="event_acceptance_of_bid", bash_command="sh /usr/lib/carter/kd_event/scripts/exe_event_pipeline_dev.sh stock_acceptance_of_bid_pipeline.py ", dag=dag)
event_stock_meeting = BashOperator(task_id="event_stock_meeting", bash_command="sh /usr/lib/carter/kd_event/scripts/exe_event_pipeline_dev.sh stock_meeting_pipeline.py ", dag=dag)
event_indicator_change = BashOperator(task_id="event_indicator_change", bash_command="sh /usr/lib/carter/kd_event/scripts/event_indicator_change_dev.sh ", dag=dag)
event_credit_rating = BashOperator(task_id="event_credit_rating", bash_command="sh /usr/lib/carter/kd_event/scripts/exe_event_pipeline_dev.sh stock_credit_rating_pipeline.py ", dag=dag)
event_stock_repurchase = BashOperator(task_id="event_stock_repurchase", bash_command="sh /usr/lib/carter/kd_event/scripts/exe_event_pipeline_dev.sh stock_repurchase_pipeline.py ", dag=dag)
event_wechat = BashOperator(task_id="event_wechat", bash_command="sh /usr/lib/carter/kd_event/scripts/event_wechat_dev.sh ", dag=dag)

[event_share_issue, event_share_pledge, event_mgt_accident, event_trade_suspension, event_share_restrict,
 event_personnel_change, event_stock_allotment, event_bonus_share, event_stock_performance, event_stock_meeting,
 event_mgt_data, event_share_holding, event_acceptance_of_bid, event_stock_asset_regroup, event_credit_rating,
 event_stock_repurchase] >> event_wechat

event_indicator_change
