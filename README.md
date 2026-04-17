# pdf-tools
A variety a python PDF tools

# Examps

```python
# example to merge each PDF in a folder to templates PDF

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
                     
```
                