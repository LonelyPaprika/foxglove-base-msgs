import os
import argparse
from build_msgs import build_msgs
from generate_py_module import generate_py_modules

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('proto_dir', help='dir which contains .proto files')
    args = parser.parse_args()
    generate_py_modules(args.proto_dir)
    build_msgs(args.proto_dir, args.proto_dir)