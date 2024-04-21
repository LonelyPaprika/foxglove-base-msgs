import os
import subprocess

def generate_py_modules(msgs_dir):
    files = [f for f in os.listdir(msgs_dir) if f.endswith('.proto')]
    
    command = [
        'protoc', 
        f'--proto_path={msgs_dir}', 
        f'--python_out={msgs_dir}'] + files
    
    subprocess.run(command)