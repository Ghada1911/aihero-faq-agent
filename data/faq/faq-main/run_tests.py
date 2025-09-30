"""
Test runner script for the FAQ site generator
"""
import subprocess
import sys
from pathlib import Path


def run_tests():
    """Run all tests with proper configuration"""
    
    # Change to project root
    project_root = Path(__file__).parent
    
    # Test commands to run
    commands = [
        # Run unit tests
        ["python", "-m", "uv", "run", "--extra", "dev", "pytest", "tests/unit/", "-v"],
        
        # Run integration tests  
        ["python", "-m", "uv", "run", "--extra", "dev", "pytest", "tests/integration/", "-v"],
        
        # Run all tests with coverage if available
        ["python", "-m", "uv", "run", "--extra", "dev", "pytest", "tests/", "-v", "--tb=short"]
    ]
    
    print("=" * 60)
    print("FAQ Site Generator Test Suite")
    print("=" * 60)
    
    for i, cmd in enumerate(commands, 1):
        print(f"\n{i}. Running: {' '.join(cmd[4:])}")  # Skip python -m uv run
        print("-" * 40)
        
        try:
            result = subprocess.run(cmd, cwd=project_root, capture_output=False)
            if result.returncode != 0:
                print(f"\n❌ Test command failed with exit code {result.returncode}")
                return result.returncode
            else:
                print(f"\n✅ Test command completed successfully")
        except Exception as e:
            print(f"\n❌ Error running tests: {e}")
            return 1
    
    print("\n" + "=" * 60)
    print("🎉 All tests completed successfully!")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)