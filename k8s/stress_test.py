# stress_test.py
import requests
import concurrent.futures
import time

URL = "http://localhost:8000/agent/run" # 假设你做了端口转发
PAYLOAD = {"task": "查一下当前节点 CPU 飙高的原因，执行三次 top 命令。"}

def send_request(i):
    try:
        # 数据流转：并发发送排障请求，迫使 Agent 的代码循环执行消耗 CPU
        resp = requests.post(URL, json=PAYLOAD, timeout=30)
        print(f"Req {i}: {resp.status_code}")
    except Exception as e:
        print(f"Req {i} failed: {e}")

# 瞬间并发 20 个请求
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    for i in range(20):
        executor.submit(send_request, i)