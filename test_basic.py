import subprocess
def test_profile():
    subprocess.run(['python','-m','ml_utils.cli','profiler','sample.csv'])

if __name__ == '__main__':
    test_profile()
