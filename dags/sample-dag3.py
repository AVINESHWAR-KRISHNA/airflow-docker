from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id="sample-dag3",
    default_args=default_args,
    description="This is my second sample dag.",
    start_date= datetime(2024,5,20, 2),
    schedule_interval='@daily'

    ) as dag:
    
    
    task1 = BashOperator(
        task_id="task1",
        bash_command="echo 'This is task1, this is my first sample dag.'"
    )

    task2 = BashOperator(
        task_id="task2",
        bash_command="echo 'This is task2, this is my first sample dag.'"
    )

    task3 = BashOperator(
        task_id="task3",
        bash_command="echo 'This is task3, this is my first sample dag.'"
    )

    task1 >> task2
    task1 >> task3

    # task1 >> [task2,task3]