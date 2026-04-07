from pathlib import Path
from pypdf import PdfWriter, PdfReader


def merge_from_list(pdf_list: list[str|Path] = None,
              output: str|Path = 'output.pdf') -> None:
    
    """
    Merge multiple PDFs in on file.

    Args:
        pdf_list: List of PDF filenames to merge
        output: Merged PDF filename

    """
    
    if pdf_list is None:
        pdf_list = []
    
    # init output PDF
    writer = PdfWriter()
    
    # add all pages from all pdfs to the writer
    for pdf in pdf_list:
        for page in PdfReader(pdf).pages:
            writer.add_page(page)
            
    # write merged pdf in output file
    with open(output, 'wb') as f:
        writer.write(f)


def merge_each_from_path(pdf_path: str|Path, template_pdf: list[str|Path]|str|Path,
                         output_path: str|Path = None, suffix: str = None) -> None:
    
    """
    Merge each PDF in a folder with fixed given PDFs.

    Args:
        pdf_path: folder name of input PDFs
        template_pdf: PDF(s) to merge to each PDF in pdf_path
        output_path (str): Merged PDF pathname

    """
    
    if (output_path is None) and (suffix is None):
        print("output_path and suffix cannot be both None")
        return
    
    if not isinstance(template_pdf, list):
        template_pdf = [template_pdf]
    
    folder = Path(pdf_path)
    
    if output_path is None:
        output_path = folder.parent
    else:
        output_path = Path(output_path)
        output_path.mkdir(parents=True, exist_ok=True)
    
    if suffix is None:
        suffix = ''
    
    
    # build list of PDFs in folder
    pdf_files = [f for f in folder.iterdir() if f.suffix.lower() == ".pdf"]
    
    # merge each PDF of the list with the template
    for pdf in pdf_files:
        print(f'Merging {str(pdf)} with template(s)...')
        pdf_list = [pdf] + template_pdf
        
        output = output_path / f"{pdf.with_suffix('').name}{suffix}.pdf"
        merge_from_list(pdf_list, output)
    
