# Program to take screenshot
import pyscreenshot

image = pyscreenshot.grab()

image.show()

filename = input("Name of the screenshot: ")

if not filename.lower().endswith(".png"):
	filename += ".png"

image.save(filename)

print(f"Saved as {filename}")
