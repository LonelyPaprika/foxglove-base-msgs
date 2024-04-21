import os
import subprocess

def generate_py_modules(dir):
    files = [f for f in os.listdir(dir) if f.endswith('.proto')]
    
    command = [
        'protoc', 
        f'--proto_path={dir}', 
        f'--python_out={dir}'] + files
    
    subprocess.run(command)