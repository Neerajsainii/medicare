import subprocess

def install_dependencies():
    # Install system dependencies using pip
    subprocess.run(["pip", "install", "--no-cache-dir", "lxml"])

if __name__ == "__main__":
    install_dependencies()
