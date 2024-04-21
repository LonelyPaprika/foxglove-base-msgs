import os
from build_msgs import build_msgs
from generate_py_module import generate_py_modules

if __name__ == "__main__":
    dir = os.path.join(os.getcwd(), 'foxglove-base-msgs/msgs')
    generate_py_modules(dir)
    build_msgs(dir)