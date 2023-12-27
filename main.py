import PyPDF2

def split_pdf(input_path, output_path):
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)

        for page_number in range(pdf_reader.numPages):
            pdf_writer = PyPDF2.PdfFileWriter()
            pdf_writer.addPage(pdf_reader.getPage(page_number))

            with open(f"{output_path}_page_{page_number + 1}.pdf", 'wb') as output_file:
                pdf_writer.write(output_file)

input_file = 'arquivosPDF/Frances_para_Dummies-Varios_autores.pdf'
output_path = 'outputPDF'
split_pdf(input_file, output_path)
