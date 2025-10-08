<<<<<<< HEAD

import os
import random
import datetime

# Define log levels
log_levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG']

# Generate 1000 log entries with random timestamps
logs = []
for i in range(10000):
    random_date = datetime.datetime(
        year=2025,
        month=random.randint(1, 12),
        day=random.randint(1, 28),
        hour=random.randint(0, 23),
        minute=random.randint(0, 59),
        second=random.randint(0, 59)
    )
    log_entry = {
        'timestamp': random_date,
        'level': random.choice(log_levels),
        'message': f'Log entry number {i + 1}'
    }
    logs.append(log_entry)

# Sort logs by timestamp
sorted_logs = sorted(logs, key=lambda x: x['timestamp'])

# Define custom directory
log_dir = './logs/'
os.makedirs(log_dir, exist_ok=True)

# Define log file path
log_file_path = os.path.join(log_dir, 'logs.log')

# Save logs to the .log file
with open(log_file_path, 'w') as f:
    for log in sorted_logs:
        f.write(f"{log['timestamp'].isoformat()} [{log['level']}] {log['message']}\n")

print(f"Sorted logs have been saved to {log_file_path}")


=======

import os
import random
import datetime

# Define log levels
log_levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG']

# Generate 1000 log entries with random timestamps
logs = []
for i in range(10000):
    random_date = datetime.datetime(
        year=2025,
        month=random.randint(1, 12),
        day=random.randint(1, 28),
        hour=random.randint(0, 23),
        minute=random.randint(0, 59),
        second=random.randint(0, 59)
    )
    log_entry = {
        'timestamp': random_date,
        'level': random.choice(log_levels),
        'message': f'Log entry number {i + 1}'
    }
    logs.append(log_entry)

# Sort logs by timestamp
sorted_logs = sorted(logs, key=lambda x: x['timestamp'])

# Define custom directory
log_dir = './logs/'
os.makedirs(log_dir, exist_ok=True)

# Define log file path
log_file_path = os.path.join(log_dir, 'logs.log')

# Save logs to the .log file
with open(log_file_path, 'w') as f:
    for log in sorted_logs:
        f.write(f"{log['timestamp'].isoformat()} [{log['level']}] {log['message']}\n")

print(f"Sorted logs have been saved to {log_file_path}")


>>>>>>> 6c6c746ac1d67107a6b1fa091cb809a3a34db4aa
