import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

# Substitua pelos valores da sua conta Azure Form Recognizer
endpoint = "https://<your-form-recognizer-resource-name>.cognitiveservices.azure.com/"
api_key = "<your-form-recognizer-api-key>"

# Criar um cliente de análise de documentos
client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))

# Função para analisar um documento
def analyze_document(document_path):
    with open(document_path, "rb") as document:
        poller = client.begin_analyze_document("prebuilt-receipt", document)
        result = poller.result()

    # Extrair e imprimir os campos desejados
    print("Análise do Documento:")
    for page in result.pages:
        print(f"Página {page.page_number}")
        
        for field_name, field in page.fields.items():
            if field_name in ["MerchantName", "TransactionDate", "Total"]:
                print(f"{field_name}: {field.value} (Confiança: {field.confidence})")

# Caminho para o documento que você deseja analisar
document_path = "path/to/your/document.jpg"  # ou .pdf, .png, etc.
analyze_document(document_path)
