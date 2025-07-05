def read_file(file_path: str) -> str:
    try:
        with open(file_path, "r") as fo:
            return fo.read()
    except FileNotFoundError as e:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"Error reading file: {e}"

