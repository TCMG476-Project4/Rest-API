import subprocess


subprocess.call("python cli.py is-prime 8")
subprocess.call("python cli.py kv-record KEY Value")
subprocess.call("python cli.py kv-retrieve Value ")

subprocess.call("python cli.py md5 test")
subprocess.call("python cli.py factorial 5")
subprocess.call("python cli.py fibonacci 8")


subprocess.call("python cli.py is-prime 1")
subprocess.call("python cli.py slack-alert test")
print()
print("Output should match below:")
print()
print("False")
print("False")
print("Value")
print("098f6bcd4621d373cade4e832627b4f6")
print("120")
print("[0, 1, 1, 2, 3, 5, 8]")
print("False")
print("True")

