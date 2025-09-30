#!/usr/bin/env python3

import re
from pathlib import Path

def extract_sort_order(content):
    """Extract sort_order from YAML frontmatter"""
    match = re.search(r'^sort_order:\s*(\d+)', content, re.MULTILINE)
    return int(match.group(1)) if match else None

def get_clean_filename(filename):
    """Extract filename after the first underscore, removing any digit prefixes"""
    # Split on underscore only once to get the part after the first underscore
    parts = filename.split('_', 1)
    if len(parts) > 1:
        return parts[1]  # Return everything after the first underscore
    else:
        return filename  # If no underscore, return original filename

def main():
    questions_dir = Path("_questions")
    
    if not questions_dir.exists():
        print("_questions directory not found!")
        return
    
    md_files = list(questions_dir.rglob("*.md"))
    print(f"Found {len(md_files)} markdown files")
    
    renamed_count = 0
    error_count = 0
    
    for md_file in md_files:
        try:
            # Read the file to get sort_order
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            sort_order = extract_sort_order(content)
            if sort_order is None:
                print(f"No sort_order found in {md_file}")
                continue
            
            # Get clean filename (everything after first underscore)
            current_name = md_file.name
            clean_name = get_clean_filename(current_name)
            
            # Create new filename with 3-digit zero-padded sort_order
            new_name = f"{sort_order:03d}_{clean_name}"
            
            # Skip if filename is already correct
            if current_name == new_name:
                continue
                
            new_path = md_file.parent / new_name
            
            # Rename the file
            md_file.rename(new_path)
            print(f"Renamed: {current_name} -> {new_name}")
            renamed_count += 1
            
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
            error_count += 1
    
    print(f"\nCompleted! Renamed {renamed_count} files. {error_count} errors/skipped.")

if __name__ == "__main__":
    main()