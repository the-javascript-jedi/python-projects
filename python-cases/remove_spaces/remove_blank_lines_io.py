import os

def remove_blank_lines():
    # Define input and output folders
    input_folder = "input"
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)  # Ensure output folder exists

    input_path = os.path.join(input_folder, "input.txt")
    output_path = os.path.join(output_folder, "output.txt")

    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"❌ '{input_path}' not found. Please make sure it exists.")
        return

    # Read and filter lines
    with open(input_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    non_blank_lines = [line for line in lines if line.strip() != '']

    # Write to output file
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.writelines(non_blank_lines)

    print(f"✅ Blank lines removed.\nInput: {input_path}\nOutput: {output_path}")

if __name__ == "__main__":
    remove_blank_lines()