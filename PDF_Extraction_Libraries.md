# Python Libraries used to extract text from PDFs
* [pikepdf](https://pypi.org/project/pikepdf/)
    - Can do anything PyPdf2 can do, but better
    - More abilities, such as repairing errors
    - Relies on QPDF (Pre-existing, mature PDF tool)
    - Can deal with encryption
* [PyPDF2](https://pypi.org/project/PyPDF2/)
* [PDFMiner](https://pypi.org/project/pdfminer/)
    - No longer updated
* [pdfminer.six](https://github.com/pdfminer/pdfminer.six)
    - Updated/Maintained fork of PDFMiner
* [PDFPlumber](https://pypi.org/project/pdfplumber/)
    - Capable tool for extracting text from PDFs
    - Sometimes works better than PyPDF2 depending on PDF
* [python-pdfbox](https://pypi.org/project/python-pdfbox/)
    - Python3 interface for Apache PDFBox
    - Requires Java
* [PyMuPdf](https://pypi.org/project/PyMuPDF/1.16.14/)
    - More geared towards viewing rather than extracting/manipulating

* Note
    - there is not necessarily one library that is objectively better. It depends on the PDF and some libaries will perform better on one PDF than another. To get consistent results, we will ultimately want to OCR so that we can have a clean slate to work with.