import subprocess

def install_dependencies():
    try:
        # Install system dependencies using pip
        subprocess.run(["pip", "install", "--no-cache-dir", "lxml"], check=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        # Handle the error here, such as logging or raising an exception

if __name__ == "__main__":
    install_dependencies()
