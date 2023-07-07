import sys

sys.path.append('test_empty_module.py')

print(sys.path)

try:
    import test_empty_module
    print("Custom module imported successfully.")
except ImportError:
    print("Failed to import custom module.")
