import markdown
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
#from weasyprint import HTML

def get_input_filename():
    root = tk.Tk()
    root.withdraw()

    input_filename = filedialog.askopenfilename()
    root.destroy()

    return input_filename


def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    html = markdown.markdown(text,
                             extensions=['tables'])

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)


def convert_html_to_pdf(input_file, output_file):
    HTML(input_file).write_pdf(output_file)


def main():
    input_filename = get_input_filename()
    input_file = Path(input_filename)
    html_file = input_file.with_suffix('.html')
    pdf_file = input_file.with_suffix('.pdf')
    convert_markdown_to_html(input_file, html_file)
    #convert_html_to_pdf(html_file, pdf_file)


if __name__ == "__main__":
    main()

