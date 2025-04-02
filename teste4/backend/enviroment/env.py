from dotenv import load_dotenv
import os

load_dotenv()

env = {
    'POSTGRES_USER': os.getenv('POSTGRES_USER'),
    'POSTGRES_PASSWORD': os.getenv('POSTGRES_PASSWORD'),
    'POSTGRES_HOST': os.getenv('POSTGRES_HOST'),
    'POSTGRES_PORT': os.getenv('POSTGRES_PORT'),
    'POSTGRES_DB': os.getenv('POSTGRES_DB'),
}

if __name__ == '__main__':
    for key, value in env.items():
        if value is None or value == '':
            raise ValueError(f"Environment variable {key} is not set.")

    print("All environment variables are set.")
