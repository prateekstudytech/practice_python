# practice_python
This repo is for testing python codes for various purposes

# Python Practice
This repository is for practicing Python code snippets and exercises. It includes various examples and challenges to help improve Python programming skills.

# Getting Started
## Prerequisites
- Python 3.x installed on your machine
- [uv package manager](https://github.com/astral-sh/uv) installed globally (see uv docs)
- Basic understanding of Python programming

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/practice_python.git
```
2. Navigate to the project directory:
```bash
cd practice_python
```
3. Create a virtual environment using uv:
```bash
uv venv .venv
```
4. Activate the virtual environment:
- On Windows:
```cmd
.venv\Scripts\activate
```
- On macOS/Linux:
```bash
source .venv/bin/activate
```
5. Install required packages using uv:
```bash
uv pip install -r requirements.txt
```

# Usage
Run Python scripts as usual, for example:
```bash
python algorithms/graph.py
```

# Notes
- All development should use the `.venv` created by uv for consistency.
- If you add new dependencies, update `requirements.txt` and re-run the install step.

# License
MIT
