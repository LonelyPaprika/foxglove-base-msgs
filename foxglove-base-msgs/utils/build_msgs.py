import os
import subprocess
import argparse

def build_msgs(p_d, p_b):
    for p_f in [f for f in os.listdir(p_d) if f.endswith('.proto')]:
        subprocess.run(['protoc', '--include_imports', '--descriptor_set_out=' + os.path.join(p_b, p_f.replace('.proto', '.bin')), os.path.join(p_d, p_f)])    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('proto_dir', help='dir which contains .proto files')
    parser.add_argument('bin_dir', help='dir which contains .bin files')
    args = parser.parse_args()
    build_msgs(args.proto_dir, args.bin_dir)
