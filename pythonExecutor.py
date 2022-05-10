import subprocess
result = subprocess.run(["schemachange", "-f", "/home/runner/work/snowflakeCi-Cd/snowflakeCi-Cd/migrations", "-a", "$SF_ACCOUNT", "-u", "$SF_USERNAME", "-r", "$SF_ROLE", "-w", "$SF_WAREHOUSE", "-d", "$SF_DATABASE", "-c", "$SF_DATABASE.demo.CHANGE_HISTORY", "--create-change-history-table"], stderr=subprocess.PIPE, text=True)
print(result.stderr)