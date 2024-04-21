import os
import subprocess
import argparse

def generate_py_modules(p_d):
    for p_f in [f for f in os.listdir(p_d) if f.endswith('.proto')]:
        print(p_f)
        subprocess.run(['protoc', '--python_out=' + '.', p_f])    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('proto_dir', help='dir which contains .proto files')
    args = parser.parse_args()
    generate_py_modules(args.proto_dir)
