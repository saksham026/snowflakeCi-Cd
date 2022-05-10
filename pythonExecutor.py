import subprocess
import os

os.environ["SF_ACCOUNT"] = "elysiumpartner.snowflakecomputing.com"
os.environ["SF_USERNAME"] = "app"
os.environ["SF_ROLE"] = "sysadmin"
os.environ["SF_WAREHOUSE"] = "demo_wh"
os.environ["SF_DATABASE"] = "tenant3"
os.environ["SNOWFLAKE_PASSWORD"] = "bigData123$"


result = subprocess.run(["schemachange", "-f", "/home/runner/work/snowflakeCi-Cd/snowflakeCi-Cd/migrations", "-a", "elysiumpartner", "-u", "app", "-r", "SYSADMIN", "-w", "demo_wh", "-d", "tenant3", "-c", "tenant3.demo.CHANGE_HISTORY", "--create-change-history-table"], stderr=subprocess.PIPE, text=True)
print(result.stderr)