from celery.schedules import crontab

imports = ('main_app.tasks')
result_expires = 30
timezone = 'UTC'

accept_content = ['json', 'msgpack', 'yaml']
task_serializer = 'json'
result_serializer = 'json'

beat_schedule = {
    'save-memory-data': {
        'task': 'main_app.tasks.save_memory_data',
        # Every minute
        'schedule': crontab(minute="*"),
    }
}
