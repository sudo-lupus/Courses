import shutil
import psutil

du = shutil.disk_usage("/")
percentage_free = du.free/du.total * 100

print(percentage_free)

cpu_usage = psutil.cpu_percent(0.5)
print(cpu_usage)

