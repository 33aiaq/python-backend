with open("input.txt", "r") as infile:
    content = infile.read()

processed_content = content.strip().upper() 

with open("output.txt", "w") as outfile:
    outfile.write(processed_content)

print("Processing complete. Check 'output.txt'.")
print("Processed content:")
print(processed_content)
