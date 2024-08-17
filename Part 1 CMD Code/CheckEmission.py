import psutil
import csv
import time

def get_process_stats(process_name):
    for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'io_counters']):
        if process.info['name'] == process_name:
            return process.info

def get_network_stats():
    net_stats = psutil.net_io_counters()
    return net_stats.bytes_sent / 1000000 , net_stats.bytes_recv / 1000000

def get_disk_stats():
    disk_stats = psutil.disk_usage('/')
    return disk_stats.percent

def write_to_csv(filename, data):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main():
    process_name = 'chrome.exe'  # Replace with the name of the process you want to monitor
    csv_filename = 'Book8.csv'
    header = ['Timestamp', 'Process Name', 'PID', 'CPU Utilization (%)', 'RAM Consumption (MB)', 'Sent MB', 'Received MB', 'Disk Utilization (%)']

    # Write header to CSV file
    write_to_csv(csv_filename, header)

    try:
        while True:
            process_stats = get_process_stats(process_name)
            if process_stats:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                ram_mb = process_stats['memory_info'].rss / 1000000
                sent_mb, received_mb = get_network_stats()
                disk_utilization = get_disk_stats()

                row_data = [timestamp, process_stats['name'], process_stats['pid'],
                            process_stats['cpu_percent'], ram_mb, sent_mb, received_mb, disk_utilization]

                write_to_csv(csv_filename, row_data)
            else:
                print(f"Process '{process_name}' not found.")

            time.sleep(10)
    except KeyboardInterrupt:
        print("Monitoring stopped. Data saved to", csv_filename)

if __name__ == "__main__":
    main()
    