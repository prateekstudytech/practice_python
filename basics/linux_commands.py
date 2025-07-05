#!python
import os
import subprocess
import re

def run_cmd_system(cmd: str):
    try:
        return_code = os.system(cmd)
        if return_code == 0:
            print(f"Command executed successfully")
            return True
        else:
            print(f"Command not executed successfully")
            return False
    except Exception as e:
        print("Command failed with exception", e)

def run_cmd_subprocess(cmd: str) -> str:
    try:
        result = subprocess.run(cmd.split(), shell=False, text=True, capture_output=True, check=True)
        if result.returncode == 0:
            return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code: {e.returncode} \nException: {e.stderr}")
        return None
    except Exception as e:
        print(f"Command threw exception: {e}")
        return None


def check_file_exists(filename: str) -> bool:
    try:
        cmd = ['ls',filename]
        result = subprocess.run(cmd, shell=False, capture_output=True, check=True, text=True)
        return True
    
    except subprocess.CalledProcessError as e:
        print(f"Command failed: \nReturn code: {e.returncode} \nException: {e.stderr}")
    except Exception as e:
        print(f"Command failed with generic exception \n{e}")

    return False

def check_file_exists_pythonic(filename: str) -> bool:
    return os.path.isfile(filename)

def check_disk_usage(percent: int):
    try:
        result = subprocess.run(['df', '-h'], text=True, shell=False, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"Command faile with exception: {e.stderr}")
        return
    except Exception as e:
        print(f"Command failed with generic exception: \n{e}")
        return
    lines = result.stdout.split('\n')
    pattern = re.compile(r'(\d+)%')
    for line in lines:
        usage = pattern.search(line)
        if usage and int(usage.group(1)) > percent:
            print(line)

def check_process_cpu_usage(percent: int) -> list:
    cmd = 'ps aux'
    output = run_cmd_subprocess(cmd)
    proc_list = []
    if output:
        lines = output.strip().split('\n')
        headers = lines[0].split()
        try:
            cpu_index = headers.index("%CPU")
        except ValueError:
            print("Could not find %CPU column in ps output.")
            return []

        for line in lines[1:]:
            parts = line.split(None, len(headers) - 1)
            try:
                cpu = float(parts[cpu_index])
                if cpu >= percent:
                    proc_list.append(line)
            except (IndexError, ValueError):
                continue
    return proc_list

if __name__ == '__main__':
    process = check_process_cpu_usage(1)
    print(process)
