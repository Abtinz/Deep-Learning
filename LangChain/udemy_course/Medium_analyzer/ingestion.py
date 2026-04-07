import os
from pathlib import Path

from dotenv import load_dotenv
from dotenv import dotenv_values


load_dotenv()


def load_env_params(env_path: str | Path = ".env") -> dict[str, str]:
    raw_params = dotenv_values(env_path)
    return {k: v for k, v in raw_params.items() if v is not None}


if __name__ == '__main__':
    print("Ingesting...")
