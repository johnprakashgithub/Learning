
from datetime import datetime

output = ""
for _ in range(int(input())):
    t1 = datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    output += str(abs(int((t1-t2).total_seconds()))) + "\n"
print(output)
