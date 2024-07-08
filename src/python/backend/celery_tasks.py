# tasks.py
from celery import Celery

CELERY_SETTINGS = {
    "result_expires": 60,  # expire results after 60s (default: 1 day)
    "task_always_eager": False,
    # by default, we ignore the results (otherwise this will cause Celery to spawn a new queue for every
    # completed task, consuming a lot of resources)
    "task_ignore_result": True,
    "task_soft_time_limit": 300,  # timeout every task after 5m unless specified
    "broker_connection_timeout": 60,
    "broker_heartbeat": None,
    "broker_pool_limit": 10,
    "broker_transport_options": {
        "max_retries": int(3),  # Should be limited by 'connect_retries_timeout' already, but lets not take any chances
        "interval_start": 1,  # Wait `interval_start` second(s) before first retry
        "interval_step": 1,  # Increase the delay by `interval_step` second(s) after each retry
        "interval_max": 5,  # Wait max 5 `interval_max` second(s) before next retry
        # Spend no more than `connect_retries_timeout` seconds trying to connect
    },
    "event_queue_expires": 60,
    "worker_concurrency": 10,
    "worker_prefetch_multiplier": 1,
    "worker_send_task_events": True,
    "worker_max_tasks_per_child": 50,
    "broker_connection_retry_on_startup": True,
}

celery_app = Celery("celery_tasks", broker="pyamqp://admin:mypass@rabbit//")  # type: ignore
celery_app.conf.task_default_queue = "tasks"
celery_app.conf.event_serializer = "json"  # this event_serializer is optional
celery_app.conf.task_serializer = "json"
celery_app.conf.result_serializer = "json"
celery_app.conf.accept_content = ["application/json", "application/x-python-serialize"]

celery_app.config_from_object(CELERY_SETTINGS)
celery_app.autodiscover_tasks()


@celery_app.task(queue="tasks", name="tasks.add")  # type: ignore
def add(x, y):  # type: ignore
    """Test.

    Args:
        x (test): test
        y (test): test

    Returns:
        test: test!
    """
    print(f"X + Y = {x+y}")
    return x + y  # type: ignore


if __name__ == "__main__":
    print("Starting celery worker")
    celery_app.worker_main(
        argv=[
            "worker",
            "--loglevel",
            "INFO",
            "-Q",
            "tasks",
        ]
    )
    result = add.apply_async((4, 4))
    print(f"Task ID: {result.id}")
