python_sources(
    name="backend",
)

pex_binary(
    name="main",
    entry_point="main.py",
    environment="python_slim",
)
# python_source(
#     name="tasks",
#     source="celery_tasks.py",
#     dependencies=[
#         "3rdparty/python:requirements#celery",
#     ],
# )

pex_binary(
    name="celery_app",
    entry_point="celery_tasks.py",
    dependencies=[
        # ":tasks",
        ":backend"
    ],
    environment="python_slim",
)

# pex_binary(
#     name="celery_app",
#     entry_point="celery_tasks.py",
#     environment="python_slim",
#     dependencies=[
#         ":backend",
#     ],
#     layout="packed",
# )

# https://www.pantsbuild.org/2.18/docs/writing-plugins/macros
# https://github.com/pantsbuild/pants/discussions/18756
