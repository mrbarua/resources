from bs4 import BeautifulSoup
import os

def parse_bookmarks(html_file, output_md_file):
    """
    Convert Chrome bookmarks HTML to Markdown.

    :param html_file: Path to the bookmarks.html file
    :param output_md_file: Path to save the Markdown (.md) file
    """
    try:
        with open(html_file, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

        # Open the Markdown file for writing
        with open(output_md_file, 'w', encoding='utf-8') as md_file:
            def process_folder(folder, depth=0):
                """Recursively process folders and write to Markdown."""
                indent = '  ' * depth
                folder_name = folder.get_text(strip=True)
                md_file.write(f"{indent}# {folder_name}\n")

                for item in folder.find_next_siblings('dl', limit=1):
                    for child in item.find_all(['a', 'h3']):
                        if child.name == 'a':
                            link_title = child.get_text(strip=True)
                            link_href = child.get('href')
                            md_file.write(f"{indent}- [{link_title}]({link_href})\n")
                        elif child.name == 'h3':
                            process_folder(child, depth + 1)

            # Start processing folders at the root
            for h3 in soup.find_all('h3'):
                process_folder(h3)

        print(f"Markdown file generated: {output_md_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Input and output file paths
    html_file = "bookmarks.html"  # Change this to your bookmarks.html path
    output_md_file = "bookmarks.md"  # Desired Markdown output path

    if os.path.exists(html_file):
        parse_bookmarks(html_file, output_md_file)
    else:
        print(f"File not found: {html_file}")
