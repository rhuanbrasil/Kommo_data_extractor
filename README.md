```markdown
# Kommo CRM Leads Integrator

Este projeto é um script em Python desenvolvido para extrair leads da API do Kommo CRM utilizando autenticação OAuth 2.0. 
O script processa os dados brutos, extrai as tags dos leads e organiza as informações em um DataFrame do Pandas para análise ou exportação.

## 🚀 Pré-requisitos

Antes de começar, você precisará de:

- Python 3.8 ou superior
- Uma conta no **Kommo CRM**
- Um "Integration" criado no painel de desenvolvedor do Kommo para obter as credenciais

## 🛠️ Instalação e Configuração

### 1. Clonar o repositório e configurar o ambiente

Primeiro, prepare o seu ambiente virtual para manter as dependências isoladas:

```bash
# Inicializar a venv
python -m venv venv

# Ativar a venv (Windows)
.\venv\Scripts\activate

# Ativar a venv (Linux/macOS)
source venv/bin/activate
```

### 2. Instalar dependências

Com a venv ativa, instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente (`.env`)

Crie um arquivo chamado `.env` na raiz do projeto e preencha com as suas credenciais do Kommo:

```env
client_id=SEU_CLIENT_ID
client_secret=SEU_CLIENT_SECRET
code=SEU_AUTHORIZATION_CODE
subdomain=SEU_SUBDOMINIO
```

> **Nota**: O `code` (Authorization Code) é obtido após autorizar a integração no painel do Kommo e possui validade curta para a primeira geração dos tokens.

## 📖 Como Utilizar

Basta executar o script principal:

```bash
python seu_script.py
```

O script seguirá o fluxo:

1. Verifica se já existe um arquivo `tokens.json`
2. Caso não exista, utiliza o `code` do `.env` para gerar novos tokens de acesso e refresh
3. Consome a API de Leads do Kommo
4. Processa as tags (que vêm em listas aninhadas) para um formato de texto separado por vírgulas
5. Exibe os 10 primeiros resultados no console

## ⚙️ Personalização

### Alterar colunas exibidas

No código, localize a linha de filtro do DataFrame para adicionar ou remover campos:

```python
# Exemplo: adicionando o nome do lead e o valor
df = df[['id', 'name', 'price', 'responsible_user_id', 'pipeline_id', 'created_at', 'tags']]
```

### Exportar para CSV/Excel

Para salvar os dados em um arquivo CSV em vez de apenas imprimir no console:

```python
df.to_csv("Leads_Exportados.csv", index=False, encoding="utf-8")
# ou
df.to_excel("Leads_Exportados.xlsx", index=False)
```

### Formatação de Datas

Os leads do Kommo vêm com data em formato Unix Timestamp. Para converter para o formato brasileiro:

```python
df['created_at'] = pd.to_datetime(df['created_at'], unit='s').dt.strftime('%d/%m/%Y %H:%M')
```

## 🔒 Segurança

- O arquivo `tokens.json` e o `.env` **nunca** devem ser enviados para o GitHub
- Adicione-os ao seu `.gitignore`:

```gitignore
.env
tokens.json
*.csv
*.xlsx
__pycache__/
venv/
```

## 📦 requirements.txt

Certifique-se de que seu `requirements.txt` contenha pelo menos:

```txt
pandas
python-dotenv
requests
```

## 🎯 Desenvolvido para

Servir como código reulizável para futuras interações com a API do Kommo.
