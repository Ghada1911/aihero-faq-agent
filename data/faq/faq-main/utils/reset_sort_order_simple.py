#!/usr/bin/env python3

import re
from pathlib import Path

def extract_sort_order(content):
    """Extract sort_order from YAML frontmatter"""
    match = re.search(r'^sort_order:\s*(\d+)', content, re.MULTILINE)
    return int(match.group(1)) if match else None

def update_sort_order_in_content(content, new_sort_order):
    """Update sort_order in YAML frontmatter"""
    pattern = r'^(sort_order:\s*)\d+'
    replacement = f'\\g<1>{new_sort_order}'
    return re.sub(pattern, replacement, content, flags=re.MULTILINE)

def main():
    questions_dir = Path("_questions")
    
    if not questions_dir.exists():
        print("_questions directory not found!")
        return
    
    total_files = 0
    updated_files = 0
    
    # Process each course directory
    for course_dir in questions_dir.iterdir():
        if not course_dir.is_dir():
            continue
            
        print(f"\nProcessing course: {course_dir.name}")
        
        # Process each module directory within the course
        for module_dir in course_dir.iterdir():
            if not module_dir.is_dir() or module_dir.name.startswith('_'):
                continue
                
            print(f"  Processing module: {module_dir.name}")
            
            # Get all markdown files in this module directory
            md_files = list(module_dir.glob("*.md"))
            
            if not md_files:
                continue
                
            # Sort files by current sort_order
            files_with_sort_order = []
            for md_file in md_files:
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    sort_order = extract_sort_order(content)
                    if sort_order is not None:
                        files_with_sort_order.append((sort_order, md_file, content))
                    total_files += 1
                        
                except Exception as e:
                    print(f"    Error reading {md_file}: {e}")
            
            # Sort by current sort_order
            files_with_sort_order.sort(key=lambda x: x[0])
            
            # Update with simple sequential numbers
            for i, (old_sort_order, md_file, content) in enumerate(files_with_sort_order, 1):
                if old_sort_order != i:
                    new_content = update_sort_order_in_content(content, i)
                    
                    try:
                        with open(md_file, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"    Updated {md_file.name}: {old_sort_order} -> {i}")
                        updated_files += 1
                    except Exception as e:
                        print(f"    Error updating {md_file}: {e}")
    
    print(f"\nCompleted! Processed {total_files} files, updated {updated_files} files.")

if __name__ == "__main__":
    main()