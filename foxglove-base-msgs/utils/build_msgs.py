import os
import subprocess

def build_msgs(dir):
    for proto_file in [f for f in os.listdir(dir) if f.endswith('.proto')]:

        command = [
            'protoc',
            f'--proto_path={dir}',
            f'--descriptor_set_out={os.path.join(dir, proto_file.replace('proto', 'bin'))}',
            '--include_imports',
            os.path.join(dir, proto_file)
        ]

        subprocess.run(command)
