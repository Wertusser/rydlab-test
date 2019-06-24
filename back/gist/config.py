import os

db_name = os.environ.get('DB_NAME', 'snippets')
db_user = os.environ.get('DB_USER', 'root')
db_pass = os.environ.get('DB_PASS', 'root')
db_host = os.environ.get('DB_HOST', 'db')
max_file_size = os.environ.get('MAX_FILE_SIZE', 1024 * 1024)
