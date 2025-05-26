#!/usr/bin/env python3
"""
MindTrack Setup Script
Automated setup for the MindTrack mental health platform
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def print_banner():
    """Print the MindTrack banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║                    🧠 MindTrack Setup                        ║
    ║                                                              ║
    ║           University Mental Health Platform                  ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]}")

def check_dependencies():
    """Check if required system dependencies are available"""
    dependencies = ['pip', 'git']
    
    for dep in dependencies:
        if shutil.which(dep) is None:
            print(f"❌ Error: {dep} is not installed or not in PATH")
            sys.exit(1)
        print(f"✅ {dep} is available")

def create_virtual_environment():
    """Create a virtual environment for the project"""
    print("\n📦 Creating virtual environment...")
    
    try:
        subprocess.run([sys.executable, '-m', 'venv', 'venv'], check=True)
        print("✅ Virtual environment created successfully")
        
        # Determine the correct activation script path
        if os.name == 'nt':  # Windows
            activate_script = os.path.join('venv', 'Scripts', 'activate.bat')
            pip_path = os.path.join('venv', 'Scripts', 'pip')
        else:  # Unix/Linux/macOS
            activate_script = os.path.join('venv', 'bin', 'activate')
            pip_path = os.path.join('venv', 'bin', 'pip')
        
        print(f"📝 To activate the virtual environment, run:")
        if os.name == 'nt':
            print(f"   venv\\Scripts\\activate")
        else:
            print(f"   source venv/bin/activate")
            
        return pip_path
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating virtual environment: {e}")
        sys.exit(1)

def install_python_dependencies(pip_path):
    """Install Python dependencies"""
    print("\n📚 Installing Python dependencies...")
    
    requirements_file = os.path.join('backend', 'requirements.txt')
    
    if not os.path.exists(requirements_file):
        print(f"❌ Error: {requirements_file} not found")
        sys.exit(1)
    
    try:
        subprocess.run([pip_path, 'install', '--upgrade', 'pip'], check=True)
        subprocess.run([pip_path, 'install', '-r', requirements_file], check=True)
        print("✅ Python dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        sys.exit(1)

def setup_environment_file():
    """Setup environment configuration file"""
    print("\n⚙️  Setting up environment configuration...")
    
    env_example = os.path.join('backend', '.env.example')
    env_file = os.path.join('backend', '.env')
    
    if os.path.exists(env_example):
        if not os.path.exists(env_file):
            shutil.copy(env_example, env_file)
            print("✅ Environment file created from template")
            print("📝 Please edit backend/.env with your actual configuration values")
        else:
            print("✅ Environment file already exists")
    else:
        print("⚠️  Warning: .env.example not found")

def setup_database():
    """Setup database instructions"""
    print("\n🗄️  Database Setup Instructions:")
    print("1. Install PostgreSQL on your system")
    print("2. Create a database named 'mindtrack':")
    print("   CREATE DATABASE mindtrack;")
    print("3. Update the DATABASE_URL in backend/.env")
    print("4. Run the schema file:")
    print("   psql -d mindtrack -f database/schema.sql")

def create_directories():
    """Create necessary directories"""
    print("\n📁 Creating necessary directories...")
    
    directories = [
        'logs',
        'uploads',
        'backend/uploads',
        'ml_models',
        'docs'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created directory: {directory}")

def setup_git_hooks():
    """Setup git hooks for development"""
    print("\n🔧 Setting up development tools...")
    
    if os.path.exists('.git'):
        print("✅ Git repository detected")
        
        # Create a simple pre-commit hook
        hooks_dir = os.path.join('.git', 'hooks')
        pre_commit_hook = os.path.join(hooks_dir, 'pre-commit')
        
        if not os.path.exists(pre_commit_hook):
            hook_content = """#!/bin/sh
# Simple pre-commit hook for MindTrack
echo "Running pre-commit checks..."

# Check for Python syntax errors
python -m py_compile backend/main.py
if [ $? -ne 0 ]; then
    echo "❌ Python syntax errors found"
    exit 1
fi

echo "✅ Pre-commit checks passed"
"""
            with open(pre_commit_hook, 'w') as f:
                f.write(hook_content)
            
            # Make it executable on Unix systems
            if os.name != 'nt':
                os.chmod(pre_commit_hook, 0o755)
            
            print("✅ Git pre-commit hook installed")
    else:
        print("⚠️  Not a git repository - skipping git hooks")

def print_next_steps():
    """Print next steps for the user"""
    print("\n" + "="*60)
    print("🎉 MindTrack setup completed successfully!")
    print("="*60)
    
    print("\n📋 Next Steps:")
    print("1. Activate the virtual environment:")
    if os.name == 'nt':
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    
    print("\n2. Configure your environment:")
    print("   - Edit backend/.env with your database and email settings")
    print("   - Set up PostgreSQL database")
    print("   - Run database/schema.sql")
    
    print("\n3. Start the application:")
    print("   cd backend")
    print("   python main.py")
    
    print("\n4. Access the application:")
    print("   Open your browser to: http://localhost:8000")
    
    print("\n📚 Documentation:")
    print("   - README.md - Project overview")
    print("   - database/schema.sql - Database structure")
    print("   - backend/.env.example - Configuration template")
    
    print("\n🆘 Need Help?")
    print("   - Check the README.md file")
    print("   - Review the error logs in logs/")
    print("   - Ensure all dependencies are installed")
    
    print("\n💡 Development Tips:")
    print("   - Use 'python -m pytest' to run tests")
    print("   - Check logs/ directory for application logs")
    print("   - Use the admin dashboard for user management")

def main():
    """Main setup function"""
    print_banner()
    
    print("🔍 Checking system requirements...")
    check_python_version()
    check_dependencies()
    
    print("\n🚀 Starting MindTrack setup...")
    
    # Setup steps
    pip_path = create_virtual_environment()
    install_python_dependencies(pip_path)
    setup_environment_file()
    create_directories()
    setup_git_hooks()
    setup_database()
    
    print_next_steps()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup failed with error: {e}")
        sys.exit(1)
