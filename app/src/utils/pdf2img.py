import pdf2image
import os


def convert_pdf_to_images(pdf_path, output_folder):
    # Check if the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert the PDF file to images
    images = pdf2image.convert_from_path(pdf_path, dpi=360, fmt="jpg")

    # Save the images to the output folder
    for i, image in enumerate(images):
        image.save(os.path.join(output_folder, f"page_{i}.jpg"))


if __name__ == "__main__":
    pdf_path = "/home/rb074/Downloads/test"
    output_folder = "/home/rb074/Downloads/test"
    convert_pdf_to_images(pdf_path, output_folder)
