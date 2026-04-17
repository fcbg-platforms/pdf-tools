# pdf-tools
A variety a python PDF tools

## Installation

Install using pip:

```bash
pip install git+https://github.com/fcbg-platforms/pdf-tools.git
```

## Example

```python
# example to merge each PDF in a folder with templates PDF

from pdf_merger import merge_each_from_path

# input folder
folder = './PDF_test'

# output folder of merged PDFs - None if same as input folder
output = './merged_pdf'

# templates to merge to each PDF
template = ['template_01.pdf',
            'template_02.pdf']

# suffix to append to the merged filename - None if no suffix
suffix = '_w_template'

# merge PDFs
merge_each_from_path(pdf_path = folder,
                     template_pdf = template,
                     output_path = output,
                     suffix = suffix)
                     
# each PDF in the folder './PDF_test' has been merged with 'template_01.pdf' and 'template_02.pdf'
                     
```
                