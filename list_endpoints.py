import os
import re

# Define the path to your 'api' folder
api_folder_path = '/path/to/your/api/folder'  # Replace with the actual path

# Function to extract route information from a file
def extract_routes_from_file(file_path):
    routes = []
    with open(file_path, 'r') as f:
        content = f.read()
        # Regex pattern to match @app.route decorators
        pattern = r"@.*?\.route\(['\"](.*?)['\"].*?,\s*methods=\[(.*?)\]\)"
        matches = re.findall(pattern, content)
        for match in matches:
            path = match[0]
            methods = [m.strip().strip("'\"") for m in match[1].split(',')]
            routes.append({"path": path, "methods": methods})
    return routes

# Walk through the 'api' directory and extract all route decorators
all_routes = []
for root, dirs, files in os.walk(api_folder_path):
    for file in files:
        if file.endswith('.py'):
            full_path = os.path.join(root, file)
            all_routes.extend(extract_routes_from_file(full_path))

# Display the extracted routes
for route in all_routes:
    print(f"Path: {route['path']}, Methods: {route['methods']}")