# test_environment.py - Simple environment test
import sys
print("=" * 50)
print("ENVIRONMENT TEST")
print("=" * 50)
print(f"Python version: {sys.version}\n")

# List of packages to test
packages = ["pandas", "numpy", "matplotlib", "seaborn", "jupyter", "python-dotenv"]

print("Testing package imports...")
print("-" * 30)

success_count = 0
for package in packages:
    try:
        __import__(package)
        print(f"✅ {package}: OK")
        success_count += 1
    except ImportError:
        print(f"❌ {package}: NOT INSTALLED")

print("\n" + "=" * 50)
print(f"RESULT: {success_count}/{len(packages)} packages installed")

if success_count == len(packages):
    print("🎉 All packages installed successfully!")
    print("You're ready for Week 1 tasks!")
else:
    print("\n⚠️ Some packages are missing.")
    print("Run this command to install them:")
    print("pip install pandas numpy matplotlib seaborn jupyter python-dotenv")
