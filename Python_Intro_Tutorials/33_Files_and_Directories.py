from pathlib import Path

# Absolute path: Path Starting from root of hard disk
    # c:\Program Files\Microsoft
    # /usr/local/bin
# Relative Path: path starting from current directory

path = Path("ecommerce")
print(path.exists()) # checks to see if path exists
path = Path("Ecommerce01")

if not path.exists():
    path.mkdir() # Makes a new folder

if path.exists():
    path.rmdir() # Removes a Directory


path = Path()
for file in path.glob('*.py'):
    print(file) # Search all files in a directory