import re

def extract_symbol_definition(library_content, symbol_name):
    """
    Extracts the s-expression definition of a specific symbol from the library content.
    """
    pattern = re.compile(r"(symbol \"" + re.escape(symbol_name) + r"[\s\S]*?(embedded_fonts no)\s*)", re.MULTILINE)
    match = pattern.search(library_content)
    if match:
        return match.group(0)
    return None

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract a specific symbol definition from a KiCad symbol library file.")
    parser.add_argument("library_file", help="Path to the KiCad symbol library file (.kicad_sym)")
    parser.add_argument("symbol_name", help="Name of the symbol to extract (e.g., 'R', 'C_ polarized', 'ESP32-DevKitC')")
    parser.add_argument("output_file", help="Path to the output file where the extracted symbol will be saved.")

    args = parser.parse_args()

    try:
        with open(args.library_file, "r", encoding="utf-8") as f:
            library_content = f.read()
    except FileNotFoundError:
        print(f"Error: Library file not found at {args.library_file}")
        exit(1)
    except Exception as e:
        print(f"Error reading library file: {e}")
        exit(1)

    extracted_symbol = extract_symbol_definition(library_content, args.symbol_name)

    if extracted_symbol:
        try:
            with open(args.output_file, "w", encoding="utf-8") as f:
                f.write(extracted_symbol)
            print(f"Successfully extracted symbol '{args.symbol_name}' to {args.output_file}")
        except Exception as e:
            print(f"Error writing output file: {e}")
            exit(1)
    else:
        print(f"Error: Symbol '{args.symbol_name}' not found in {args.library_file}")
        exit(1)
