from pypdf import PdfReader
import pikepdf
from tika import parser
import os

class TextExtracter:
    def __init__(self, file_path):
        # path to attachment 
        self.file_path = file_path
        # directory the attachment came from
        self.file_directory = os.path.dirname(self.file_path)
        # attachment file name
        self.file_name = os.path.split(self.file_path)[-1].split(".")[0] 
        # attachment file type (pdf, docx, doc )
        self.file_type = "." + self.file_path.split(".")[-1]
        
    def get_file_directory(self):
        return self.file_directory
    
    def get_file_path(self):
        return self.file_path

    def get_file_name(self):
        return self.file_name
    
    def get_file_type(self):
        return self.file_type
    
    def create_extracted_text_file_path(self, library_used):
        return f"{self.file_directory}/{self.file_name}_{library_used}.txt"

    def extract_text_pypdf(self):
        """
        The extract text method will use the pypdf library to extract text from a pdf
        Text contents are then saved in a new txt file with the ending _pypdf.txt
        Attributes
        ----------
        
        Returns
        -------
        text
            a string of the extracted text from the file
        """
        library_used = "pypdf"
        with open(self.file_path, "rb") as file:
            reader = PdfReader(file)
            tot_pages = len(reader.pages)
            text = ""
            print(text)
            for i in range(tot_pages):
                text+= reader.pages[i].extract_text()

        with open(self.create_extracted_text_file_path(library_used), "w") as extracted_text_file:
            print(text, file = extracted_text_file)


    # def extract_text_pikepdf():
    #     pdf = pikepdf.open(self.file_path)
    #     # extract the text from the pdf file and store in the extracted_data variable
    #     extracted_data = ''
    #     for i in range(len(pdf.pages)):
    #         page = pdf.getPage(i)
    #         extracted_data += pdf.pages[i].Content()
    #     return ""

    # def extract_text_tika():
    #     parsed_pdf = parser.from_file(self.file_path)
    #     data = parsed_pdf['text'] 


    # def get_attachment_subject():
    #     #TODO Possibly the first line of the file?
    #     return ""
