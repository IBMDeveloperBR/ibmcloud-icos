# ibmcloud-icos

Este repositório contém pedaços de código para facilitar o uso do IBM Cloud Object Storage. Ele automatiza a leitura e extração do JSON gerado pela IBM Cloud com as credenciais do serviço, prontas para serem usadas com a biblioteca Python oficial do ICOS.

## Como utilizar:

- Crie uma instância do [ICOS na IBM Cloud](https://cloud.ibm.com/catalog/services/cloud-object-storage)
- Na página Web do serviço instanciado na IBM Cloud, clique na aba `service credentials`.
- Crie uma nova credencial se necessário, e copie todo o conteúdo do JSON gerado.
- Cole o conteúdo do JSON no arquivo `icos_credentials.json`.
- Já é possível executar o código do arquivo `icos.py`!
