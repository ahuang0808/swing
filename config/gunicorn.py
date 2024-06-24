from pathlib import Path

from dotenv import load_dotenv

for env_file in (".env", ".flaskenv"):
    env = Path.cwd() / env_file
    if Path.exists(env):
        load_dotenv(env)
