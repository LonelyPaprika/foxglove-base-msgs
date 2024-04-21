import os
from build_msgs import build_msgs
from generate_py_module import generate_py_modules

if __name__ == "__main__":
    msgs_dir = os.path.join(os.getcwd(), 'foxglove_base_msgs/msgs')
    generate_py_modules(msgs_dir)
    build_msgs(msgs_dir)