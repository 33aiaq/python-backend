def analyze_log(input_file, output_file):
    status_codes = {"200": 0, "404": 0, "500": 0}

    try:
        with open(input_file, 'r') as logfile:
            for line_number, line in enumerate(logfile, start=1):
                parts = line.strip().split()
                if len(parts) < 3:
                    print(f"Warning: Line {line_number} is malformed and will be skipped.")
                    continue

                ip, status, url = parts[0], parts[1], parts[2]
                if status in status_codes:
                    status_codes[status] += 1
                else:
                    pass

        with open(output_file, 'w') as report:
            report.write(f"Successful (200): {status_codes['200']}\n")
            report.write(f"Not Found (404): {status_codes['404']}\n")
            report.write(f"Server Error (500): {status_codes['500']}\n")

        print(f"Report generated successfully in '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The log file '{input_file}' was not found.")
    except IOError as e:
        print(f"Error reading the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

analyze_log("server.log", "report.txt")
