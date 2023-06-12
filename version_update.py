import toml

print("Running version update script...")

# Read the version number from pyproject.toml
with open("pyproject.toml", "r") as f:
    pyproject = toml.load(f)
    version = pyproject["tool"]["poetry"]["version"]

print(f"Version from pyproject.toml: {version}")

# Write the version number to _version.py
with open("yaml_indent/_version.py", "w") as f:
    f.write(f'__version__ = "{version}"\n')
