# from PIL import Image
# import os

# def resize_image(input_path, output_path, target_size_bytes):
#     # Open the image
#     image = Image.open(input_path)

#     # Calculate the initial quality setting
#     quality = 85

#     while True:
#         # Save the image with the current quality setting
#         image.save(output_path, quality=quality, optimize=True)

#         # Check the file size of the saved image
#         file_size = os.path.getsize(output_path)

#         # If the file size is smaller than the target, break the loop
#         if file_size <= target_size_bytes:
#             break

#         # Reduce the quality and try again
#         quality -= 5
#         if quality <= 5:
#             break

#     print(f"Final quality setting: {quality}")
#     print(f"Final file size: {file_size} bytes")

# input_image_path = "input.jpg"
# output_image_path = "output.jpg"
# target_size_kb = 10  

# target_size_bytes = target_size_kb * 1024

# resize_image(input_image_path, output_image_path, target_size_bytes)



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
        # Save the image with the current quality setting
        output = "output.jpg"
        image.save(output, quality=quality, optimize=True)

        # Check the file size of the saved image
        file_size = os.path.getsize(output)

        # If the file size is smaller than the target, break the loop
        target_size_bytes = 10 * 1024
        if file_size <= target_size_bytes:
            break

        # Reduce the quality and try again
        quality -= 5
        if quality <= 5:
            break

    return f"Final quality setting: {quality}",f"Final file size: {file_size} bytes"


if __name__=="__main__":
    main()