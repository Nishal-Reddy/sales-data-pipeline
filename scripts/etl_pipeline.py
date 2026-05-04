import os
# import logging

# logging.basicConfig(level=logging.INFO)

# logging.info("Starting ETL pipeline...")
base_dir = os.path.dirname(os.path.abspath(__file__))
transform_data = os.path.join(base_dir, "transform_data.py")
load_data = os.path.join(base_dir, "load_data.py")

os.system(f'python "{transform_data}"')
os.system(f'python "{load_data}"')
