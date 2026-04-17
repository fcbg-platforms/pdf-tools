# pdf-tools
A variety a python PDF tools

# Usage

```python
folder = './PDF_test'

# output folder of merged PDFs - None if same as input folder
output = './merged_pdf'

# templates to merge to each PDF
template = ['./FCBG_MEG_Operational_costs_2026.pdf',
            './FCBG_CSR_Operational_costs_2026.pdf']

# suffix to append to the merged filename - None if no suffix
suffix = '_w_FNS_grid'


# merge PDFs
merge_each_from_path(pdf_path = folder,
                     template_pdf = template,
                     output_path = output,
                     suffix = suffix)
                     
```
                