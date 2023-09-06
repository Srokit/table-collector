"Logging module"

# Set this to True to enable logging
ENABLE_LOGGING = False

def log_table(table):
    if not ENABLE_LOGGING:
        return
    msg = f"===Found table===\n{table}"
    print(msg)

