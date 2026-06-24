from pathlib import Path
from checks import ping, report

def run(conf):

    try:
        results = ping.check_hosts(conf.get("hosts", []))
   
        content, file_ts = report.generate_report(results)

        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)
        filename = reports_dir / f"{file_ts}.txt"
        filename.write_text(content, encoding="utf-8")
        print(f"Report written to {filename}")
    
    except Exception as e:

        print(f"Error occurred while generating report: {e}")
        