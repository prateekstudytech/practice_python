#!python
import os
import subprocess
import pandas as pd

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

def run_cmd_subprocess(cmd: str):
    try:
        result = subprocess.run(cmd.split(), shell=False, text=True, capture_output=True, check=True)
        if result.returncode == 0:
            print(f"Command executed successfully: \n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code: {e.returncode} \nException: {e.stderr}")
    except Exception as e:
        print(f"Command threw exception: {e}")


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

def check_disk_usage(percent: int) -> str:
    try:
        result = subprocess.run(['df', '-h'], text=True, shell=False, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"Command faile with exception: {e.stderr}")
    except Exception as e:
        print(f"Command failed with generic exception: \n{e}")
    lines = result.stdout.splitlines
    columns = lines[0]
    df = pd.DataFrame(data=lines, columns=columns)
    print(df)
        

if __name__ == '__main__':
    # filename = "linked_list.pysdf"
    # exists = check_file_exists_pythonic(filename)
    # print(f"Filename '{filename}' exists: {exists}")
    check_disk_usage(80)
