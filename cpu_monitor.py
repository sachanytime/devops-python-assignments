import psutil
import time

THRESHOLD = 80        # CPU usage threshold (%)
INTERVAL = 2          # Time interval in seconds


def monitor_cpu():
    print("Monitoring CPU usage... (Press Ctrl+C to stop)\n")

    try:
        while True:
            # Get CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=1)

            if cpu_usage > THRESHOLD:
                print(f"⚠️ Alert! CPU usage exceeds threshold: {cpu_usage}%")
            else:
                print(f"CPU usage: {cpu_usage}%")

            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

    except Exception as e:
        print(f"Error occurred during CPU monitoring: {e}")


if __name__ == "__main__":
    monitor_cpu()
