import pdfplumber
import csv
import zipfile
import io


def zip_file(csv_buffer, zip_path):
    """
    Cria um arquivo ZIP e adiciona o conteúdo do buffer CSV a ele.
    """
    
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.writestr("extracted_table.csv", csv_buffer.getvalue())
    except:
        raise ValueError("Erro ao criar o arquivo ZIP.")



def extract_tables_from_pdf(pdf_path, zip_path):
    """
    Extrai tabelas de um arquivo PDF e salva em um arquivo ZIP.
    """

    with pdfplumber.open(pdf_path) as pdf:
        tables = []
        header = None
        
        for page in pdf.pages:
            extracted_table = page.extract_table()
            if extracted_table:
                if header is None:
                    header = extracted_table[0]
                    header[3] = "Seg. Odontológica"
                    header[4] = "Seg. Ambulatorial"
                    tables.append(header)
                tables.extend(extracted_table[1:])
        

        if tables:
            csv_buffer = io.StringIO()
            writer = csv.writer(csv_buffer)
            writer.writerows(tables)
            zip_file(csv_buffer, zip_path)
        else:
            raise ValueError("Nenhuma tabela encontrada no PDF.")



pdf_path = "./teste2/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
zip_path = "./teste2/Teste_LucasPerrone.zip"

extract_tables_from_pdf(pdf_path, zip_path)