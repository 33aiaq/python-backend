def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def temperature_converter(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        with open(output_file, 'w') as outfile:
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                try:
                    celsius = float(line)
                    fahrenheit = celsius_to_fahrenheit(celsius)
                    outfile.write(f"{celsius:.2f}C = {fahrenheit:.2f}F\n")
                except ValueError:
                    print(f"Warning: '{line}' is not a valid number and will be skipped.")

        print(f"Conversion complete. Check '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except IOError as e:
        print(f"I/O error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

temperature_converter("celsius.txt", "fahrenheit.txt")
