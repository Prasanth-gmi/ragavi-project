# import requests
# import json
# import markdown
# from bs4 import BeautifulSoup

# def figma_create_file(access_token, file_name, team_id=None):
#     url = "https://api.figma.com/v1/files"
#     headers = {
#         "X-Figma-Token": access_token,
#         "Content-Type": "application/json"
#     }
#     data = {"name": file_name}
#     if team_id:
#         data["teamId"] = team_id
    
#     response = requests.post(url, headers=headers, json=data)
#     response.raise_for_status()
#     return response.json()["key"]

# def figma_create_text_node(access_token, file_key, text, x, y):
#     url = f"https://api.figma.com/v1/files/{file_key}/nodes"
#     headers = {
#         "X-Figma-Token": access_token,
#         "Content-Type": "application/json"
#     }
#     data = {
#         "nodes": [{
#             "type": "TEXT",
#             "characters": text,
#             "x": x,
#             "y": y
#         }]
#     }
    
#     response = requests.post(url, headers=headers, json=data)
#     response.raise_for_status()
#     return response.json()["nodes"][0]["id"]

# def figma_export_png(access_token, file_key, node_id, scale=1):
#     url = f"https://api.figma.com/v1/images/{file_key}"
#     headers = {
#         "X-Figma-Token": access_token
#     }
#     params = {
#         "ids": node_id,
#         "scale": scale,
#         "format": "png"
#     }
    
#     response = requests.get(url, headers=headers, params=params)
#     response.raise_for_status()
#     return response.json()["images"][node_id]

# def parse_markdown(md_content):
#     html = markdown.markdown(md_content)
#     soup = BeautifulSoup(html, 'html.parser')
#     return soup

# def extract_structure(soup):
#     structure = []
#     for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'li', 'a', 'img', 'code']):
#         if element.name.startswith('h'):
#             structure.append(('header', element.name, element.text))
#         elif element.name == 'p':
#             structure.append(('paragraph', element.text))
#         elif element.name in ['ul', 'ol']:
#             structure.append(('list', element.name, [li.text for li in element.find_all('li')]))
#         elif element.name == 'a':
#             structure.append(('link', element.text, element.get('href')))
#         elif element.name == 'img':
#             structure.append(('image', element.get('alt'), element.get('src')))
#         elif element.name == 'code':
#             structure.append(('code', element.text))
#     return structure

# def create_figma_elements(access_token, file_key, structure):
#     y_position = 0
#     for element in structure:
#         if element[0] == 'header':
#             size = 72 - (int(element[1][1]) * 8)  
#             node_id = figma_create_text_node(access_token, file_key, element[2], 0, y_position)
#             y_position += size + 20
#         elif element[0] == 'paragraph':
#             node_id = figma_create_text_node(access_token, file_key, element[1], 0, y_position)
#             y_position += 40  
#         elif element[0] == 'list':
#             for item in element[2]:
#                 node_id = figma_create_text_node(access_token, file_key, f"• {item}", 20, y_position)
#                 y_position += 30
#         elif element[0] == 'link':
#             node_id = figma_create_text_node(access_token, file_key, element[1], 0, y_position)
#             y_position += 30
#         elif element[0] == 'image':
#             node_id = figma_create_text_node(access_token, file_key, f"[Image: {element[1]}]", 0, y_position)
#             y_position += 100
#         elif element[0] == 'code':
#             node_id = figma_create_text_node(access_token, file_key, element[1], 0, y_position)
#             y_position += 60

#     return "canvas"  


import re
from crewai_tools import tool


@tool
def read_content(file_path):
    """
    Read content to the specified file path.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


@tool
def write_content(file_path, content):
    """
    Write content to the specified file path.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


@tool
def clean_html(content):
    """
    Clean HTML content by removing comments, extra whitespace, and extracting
    the content within <html>...</html> tags.
    """
    
    # Remove HTML comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

    # Extract content within <html>...</html> tags
    match = re.search(r'(?s)<!DOCTYPE html.*?>.*?</html>', content)
    if match:
        content = match.group(0)
    else:
        content = ''  # If no <html>...</html> tags are found, result in empty content

    # Remove extra whitespace and blank lines
    content = re.sub(r'\n\s*\n', '\n', content)
    content = content.strip()

    return content

@tool
def clean_css(content):
    """
    Clean CSS content by removing everything before the first CSS rule starts
    and everything after the last CSS rule ends. Also add responsive design rules.
    """
    # Find the content between the first '{' and the last '}'
    match = re.search(r'\{.*?\}', content, flags=re.DOTALL)
    if match:
        # Extract the portion of content from the first '{' to the last '}'
        start_index = content.find('.mobile-frame {')
        end_index = content.rfind('}') + 1
        # Extract the CSS rules
        cleaned_content = content[start_index:end_index]
    else:
        # If no rules are found, return an empty string
        cleaned_content = ''

    # Remove CSS comments
    cleaned_content = re.sub(r'/\*.*?\*/', '', cleaned_content, flags=re.DOTALL)

    # Remove extra whitespace and blank lines
    cleaned_content = re.sub(r'\n\s*\n', '\n', cleaned_content)
    cleaned_content = cleaned_content.strip()

    # Add responsive design CSS
    responsive_css = '''
/* Responsive Design */
@media only screen and (min-width: 768px) {
  .mobile-frame {
    width: 360px;
    height: 640px;
    border: none;
    box-shadow: none;
  }
}
    '''
    final_css = f"{cleaned_content}\n\n{responsive_css}"
    
    return final_css


@tool
def main():
    """
    Main function to read, clean, and write HTML and CSS files.
    """
    # Paths for HTML and CSS files
    html_input_file_path = 'outs/wireframe_html5.html'
    html_output_file_path = 'outs/wireframe_html5.html'
    css_input_file_path = 'outs/wireframe_css5.css'
    css_output_file_path = 'outs/wireframe_css5.css'

    # Clean HTML content
    html_content = read_content(html_input_file_path)
    cleaned_html_content = clean_html(html_content)
    write_content(html_output_file_path, cleaned_html_content)
    print(f"Cleaned HTML content has been written to '{html_output_file_path}'.")

    # Clean CSS content
    css_content = read_content(css_input_file_path)
    cleaned_css_content = clean_css(css_content)
    write_content(css_output_file_path, cleaned_css_content)
    print(f"Cleaned CSS content has been written to '{css_output_file_path}'.")

if __name__ == "__main__":
    main()
