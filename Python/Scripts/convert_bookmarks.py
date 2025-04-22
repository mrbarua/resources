from bs4 import BeautifulSoup

# Load the HTML file
with open('bookmarks.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Open a Markdown file for writing
with open('bookmarks.md', 'w', encoding='utf-8') as md_file:
    md_file.write("# Bookmarks\n\n")
    for link in soup.find_all('a'):
        title = link.text or "Untitled"
        url = link.get('href')
        md_file.write(f"- [{title}]({url})\n")
