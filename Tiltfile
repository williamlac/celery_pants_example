docker_compose('docker-compose.yml')
# https://docs.tilt.dev/custom_build.html
custom_build(
    'my_backend',
    'pants package src/docker/backend:my_backend',
    deps=['src/python/backend', 'src/docker/backend/Dockerfile'],
    tag='latest'
)
custom_build(
    'my_celery',
    'pants package src/docker/backend:my_celery',
    deps=['src/python/backend', 'src/docker/backend/Dockerfile.celery'],
    tag='latest'
)
