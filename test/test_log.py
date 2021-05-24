import threading

is_import_success = True

try:
    from je_log_system import LogSystem
except ImportError:
    is_import_success = False
    print("Log is disable install je_log_system to open", file=sys.stderr)

if is_import_success:
    log_system = LogSystem(threading.Lock)
