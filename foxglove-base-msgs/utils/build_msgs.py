import os
import subprocess

def build_msgs(msgs_dir):
    for proto_file in [f for f in os.listdir(msgs_dir) if f.endswith('.proto')]:

        command = [
            'protoc',
            f'--proto_path={msgs_dir}',
            f'--descriptor_set_out={os.path.join(msgs_dir, proto_file.replace('proto', 'bin'))}',
            '--include_imports',
            os.path.join(msgs_dir, proto_file)
        ]

        subprocess.run(command)
