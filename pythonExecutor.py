import subprocess
result = subprocess.run(["schemachange", "-f", "/home/runner/work/snowflakeCi-Cd/snowflakeCi-Cd/migrations", "-a", "elysiumpartner.snowflakecomputing.com", "-u", "app", "-r", "SYSADMIN", "-w", "demo_wh", "-d", "tenant3", "-c", "tenant3.demo.CHANGE_HISTORY", "--create-change-history-table"], stderr=subprocess.PIPE, text=True)
print(result.stderr)