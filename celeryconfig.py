from celery.schedules import crontab

imports = ('memory_data.tasks')
result_expires = 30
timezone = 'UTC'

accept_content = ['json', 'msgpack', 'yaml']
task_serializer = 'json'
result_serializer = 'json'

beat_schedule = {
    'save-memory-data': {
        'task': 'memory_data.tasks.save_memory_data',
        # Every minute
        'schedule': crontab(minute="*"),
    }
}
