import os
import re

# Define the path to your 'api' folder
api_folder_path = 'garden_planner/src/api'  # update if needed

def extract_routes_from_file(file_path):
    routes = []
    with open(file_path, 'r') as f:
        content = f.read()
        # Match any .route (e.g., bp.route, app.route)
        pattern = r"@.*?\.route\(\s*['\"](.*?)['\"]\s*(?:,\s*methods=\[(.*?)\])?\)"
        matches = re.findall(pattern, content)
        for path, methods_str in matches:
            if methods_str:
                methods = [m.strip().strip("'\"") for m in methods_str.split(',')]
            else:
                methods = ['GET']  # default method
            routes.append({"path": path, "methods": methods})
    return routes

all_routes = []
for root, dirs, files in os.walk(api_folder_path):
    for file in files:
        if file.endswith('.py'):
            full_path = os.path.join(root, file)
            all_routes.extend(extract_routes_from_file(full_path))

for route in all_routes:
    print(f"Path: {route['path']}, Methods: {route['methods']}")