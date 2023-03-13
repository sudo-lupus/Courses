import subprocess
print(subprocess.run(["date"]))
print(subprocess.run(["sleep", "2"]))
result = subprocess.run(["ls", "example.txttza"])
print(result.returncode)