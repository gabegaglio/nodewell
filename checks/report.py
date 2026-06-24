import subprocess
from datetime import datetime


def generate_report(results):

    report = ""
    
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")  # → "2026-06-23 20:45:12"
    file_ts = now.strftime("%Y-%m-%d_%H-%M-%S")  
    
    report += timestamp + "\n"
    
    for result in results:
        
        line = f"{result['name']} ({result['ip']}): {result['status']}\n"
        report += line
    
    return report, file_ts