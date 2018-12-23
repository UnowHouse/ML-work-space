lines = []

with open('proxy_ip.txt','r+') as f:
    for line in f:
        (key,value) = line.strip().split()
        lines.append({key:value})
    print(lines)