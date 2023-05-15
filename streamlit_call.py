import subprocess
import sys

args = ["streamlit", "run", "app.py",
        "--server.enableWebsocketCompression=false",
        "--server.enableXsrfProtection=false"]
subprocess.check_call(args, stdout=sys.stdout)
