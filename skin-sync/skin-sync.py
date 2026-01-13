from pathlib import Path

skins_path = Path("../staging")
gta3_img_path = Path("../models/gta3.img")

def main(skins_path):
	with open("skin-sync.txt", "r") as f_in, open("skin-sync.txt", "w") as f_out:
		f_out.write(f"// Do not modify this file directly\n\n-open {gta3_img_path}\n")
		
		for skin_file in skins_path.rglob("*.dff"):
			f_out.write(f"-import {skin_file}\n")
		for skin_file in skins_path.rglob("*.txd"):
			f_out.write(f"-import {skin_file}\n")

	with open("skin-sync.txt", "a") as append:
		append.write("\n-exit")

if __name__ == "__main__":
	main(skins_path)