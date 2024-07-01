# tasks.py
from celery import Celery

app = Celery("tasks", broker="amqp://admin:mypass@rabbit//")  # type: ignore


@app.task  # type: ignore
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


