import sys

# Add a custom directory to sys.path
sys.path.append('test_empty_module.py')

# Print the updated sys.path
print(sys.path)

# Check if a module from the custom directory can be imported
try:
    import test_empty_module
    print("Custom module imported successfully.")
except ImportError:
    print("Failed to import custom module.")
