import os

# Define your characters
ids = [
    "hinataHyuuga", "inoYamanaka", "sakura", "makimaChainsawMan",
    "orihimeInoue", "shizukaMarikawa", "meikoShiraki", "akenoHimejima",
    "mitsuriKanroji", "yumekoJabami", "nicoRobinTimeSkip", "namiOnePiece",
    "boaHancock", "asunaYuuki", "tinkerBell", "miiaMonsterMusume",
    "ramonaFlowers", "lunaCustom"
]

base_dir = "waifu-assets/characters"

# Create directories and dummy files
for char_id in ids:
    char_path = os.path.join(base_dir, char_id)
    gallery_path = os.path.join(char_path, "gallery")
    
    os.makedirs(gallery_path, exist_ok=True)
    
    # Create empty placeholder files
    files = [
        "thumbnail.png",
        "portrait.jpg",
        "fullbody.gif",
        "background.jpg"
    ]
    
    for f in files:
        with open(os.path.join(char_path, f), 'w') as fp:
            fp.write("PLACEHOLDER")
            
    # Create gallery placeholders
    for i in range(1, 3):
        with open(os.path.join(gallery_path, f"{i:03d}.jpg"), 'w') as fp:
            fp.write("PLACEHOLDER")

print(f"✅ Created folders for {len(ids)} characters in '{base_dir}'")
print("1. Drag your real images into these folders.")
print("2. Initialize a git repo inside 'waifu-assets'.")
print("3. Push to your PRIVATE GitHub repository..")