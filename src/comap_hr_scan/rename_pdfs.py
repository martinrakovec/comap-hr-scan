import os
import shutil
import sys
import tempfile
import glob
import argparse

# Install https://github.com/UB-Mannheim/tesseract/wiki first
import pytesseract
from PIL import Image
# Install http://blog.alivate.com.au/poppler-windows/ version 0.50
from pdf2image import convert_from_path


def convert_pdf_to_jpg(in_pdf, out_jpg):
    pages = convert_from_path(in_pdf, 500)
    if len(pages) > 0:
        pages[0].save(out_jpg, 'JPEG')
        return True
    else:
        print(f'No pages found in {in_pdf}')
        return False


def process_pdfs(in_dir, out_dir, name_transform_method):
    tmp_dir = tempfile.mkdtemp()
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    in_dir = os.path.abspath(in_dir)
    search_str = os.path.join(in_dir, '**', '*.pdf')
    for file in glob.glob(search_str, recursive=True):
        print(f'Processing {file}')
        # Convert PDF to JPG
        img_file = os.path.join(tmp_dir, 'img.jpg')
        if not convert_pdf_to_jpg(file, img_file):
            sys.exit(1)
        # Read lines from file
        lines = pytesseract.image_to_string(Image.open(img_file), lang='ces').split('\n')
        # Transform file name
        new_name = name_transform_method(lines)
        # Copy file to new location with new name
        new_file = os.path.join(out_dir, new_name)
        print(f'Coping {file} into {new_file}')
        shutil.copy(file, new_file)
    shutil.rmtree(tmp_dir)


def get_filename_from_pdf(lines):
    doc_title = lines[4]
    for line in lines[5:]:
        if "jméno, příjmení" in line:
            fname, sname = line.split(':')[1].strip().split(' ')
            return f'{sname}_{doc_title}.pdf'
    return None


def main():
    parser = argparse.ArgumentParser(description='Rename PDF based on its content.')
    parser.add_argument('input_dir', type=str, help='Directory with original PDFs. It won\'t be modified.')
    parser.add_argument('output_dir', type=str, help='Directory where renamed PDFs will be stored.')
    args = parser.parse_args()
    process_pdfs(args.input_dir, args.output_dir, get_filename_from_pdf)


if __name__ == '__main__':
    main()
