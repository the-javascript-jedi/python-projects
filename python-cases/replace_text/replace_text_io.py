import os
import re

def replace_text():
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

    # Define arrays for find and replace
    findText = ["aa", "aa-bb", "hello", "world"]
    replacementText = ["cc", "test-dd", "hi", "earth"]

    # Validate arrays have same length
    if len(findText) != len(replacementText):
        print("❌ Error: findText and replacementText arrays must have the same length!")
        return

    print("🔍 BATCH TEXT REPLACER (Case-Insensitive)")
    print("-" * 50)
    print("📝 Replacement Rules:")
    for i, (find, replace) in enumerate(zip(findText, replacementText), 1):
        print(f"   {i}. '{find}' → '{replace}'")
    print("-" * 50)

    try:
        # Read the entire file content
        with open(input_path, 'r', encoding='utf-8') as infile:
            content = infile.read()

        # Perform all replacements
        updated_content = content
        total_replacements = 0

        for find, replace in zip(findText, replacementText):
            # Case-insensitive replacement using regex
            pattern = re.escape(find)
            matches = re.findall(pattern, updated_content, re.IGNORECASE)
            count = len(matches)

            if count > 0:
                updated_content = re.sub(pattern, replace, updated_content, flags=re.IGNORECASE)
                print(f"✅ Replaced {count} occurrence(s) of '{find}' with '{replace}'")
                total_replacements += count
            else:
                print(f"⚠️  No occurrences found for '{find}'")

        # Write to output file
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(updated_content)

        print("-" * 50)
        print(f"🎉 Batch replacement completed!")
        print(f"📊 Total replacements made: {total_replacements}")
        print(f"📁 Input: {input_path}")
        print(f"📁 Output: {output_path}")

    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")


if __name__ == "__main__":
    replace_text()