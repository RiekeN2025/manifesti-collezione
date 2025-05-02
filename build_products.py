import os
import json

# Basisordner mit allen Boxen
base_dir = "/Users/Rieke/Desktop/manifesti"

# Pfad zur Ausgabedatei
output_file = os.path.join(base_dir, "products.json")

products = []
price_default = 19.99
product_index = 1

# Alle Unterordner rekursiv durchgehen
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            # Produktinfos zusammenbauen
            file_path = os.path.relpath(os.path.join(root, file), base_dir)
            filename_no_ext = os.path.splitext(file)[0]
            title = filename_no_ext.replace("_", " ").replace("-", " ").strip()

            product = {
                "id": f"poster-{product_index:05}",
                "name": title,
                "price": price_default,
                "description": f"Original Kinoplakat: {title}",
                "image": file_path.replace("\\", "/")  # für Windows
            }

            products.append(product)
            product_index += 1

# JSON-Datei schreiben
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print(f"{len(products)} Produkte gespeichert in {output_file}")
