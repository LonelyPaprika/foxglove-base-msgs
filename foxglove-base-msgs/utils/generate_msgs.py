import os
from build_msgs import build_msgs
from generate_py_module import generate_py_modules

if __name__ == "__main__":
    generate_py_modules(os.path.join(os.getcwd(), 'foxglove-base-msgs/msgs'))
    build_msgs(dir)