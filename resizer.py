from PIL import Image
import os

def main():
    try:
        resize_image('inputt.jpg')
    except (FileNotFoundError, FileExistsError):
        resize_image("aaa.jpg")
    
def resize_image(input_path):
    image = Image.open(input_path)
    quality = 150
    while True:
        output = "output.jpg"
        image.save(output, quality=quality, optimize=True)

        file_size = os.path.getsize(output)

        target_size_bytes = 10 * 1024
        if file_size <= target_size_bytes:
            break
        
        a = file_size / 1024
        
        quality -= 5
        if quality <= 5:
            break

    return f"Final quality setting: {quality}",f"Final file size: {a} bytes"


if __name__=="__main__":
    main()
