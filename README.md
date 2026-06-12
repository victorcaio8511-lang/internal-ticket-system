# Sistema de Controle de Chamados

Sistema web desenvolvido em Python e Flask para gerenciamento de chamados internos de TI.

## Sobre o Projeto

O Sistema de Controle de Chamados permite o registro, acompanhamento e gerenciamento de solicitações de suporte interno.

O sistema possibilita a criação, consulta, edição e visualização detalhada dos chamados, além da distribuição automática de responsáveis com base na quantidade de chamados ativos.

---

## Funcionalidades

- Criar novos chamados
- Listar todos os chamados
- Visualizar detalhes de um chamado
- Editar informações de um chamado
- Alterar status dos chamados
- Buscar chamados por título
- Filtrar chamados na listagem
- Atribuição automática de responsável

### Controle de status

Os chamados podem possuir os seguintes status:

- Aberto
- Em Andamento
- Resolvido
- Fechado

Chamados com status **Resolvido** ou **Fechado** não entram na contagem para distribuição automática.

---

## Tecnologias Utilizadas

### Back-end

- Python 3
- Flask

### Front-end

- HTML5
- CSS3
- JavaScript

---

## Estrutura do Projeto

```text
internal-ticket-system/
│
├── app.py
│
├── models/
│   └── ticket.py
│
├── routes/
│   └── ticket_routes.py
│
├── services/
│   └── ticket_service.py
│
├── templates/
│   ├── create_ticket.html
│   ├── details.html
│   ├── edit_ticket.html
│   └── index.html
│
├── static/
│   └── style.css
│
├── requirements.txt
└── README.md
```

---

## Arquitetura Utilizada

O projeto foi organizado com separação de responsabilidades:

### Models

Responsáveis pela estrutura dos dados da aplicação.

### Services

Responsáveis pelas regras de negócio, como cadastro, busca e distribuição automática de responsáveis.

### Routes

Responsáveis pelas rotas HTTP da aplicação.

### Templates

Responsáveis pela interface visual da aplicação.

### Static

Arquivos estáticos como CSS.

---

## Como Executar o Projeto

1. Clonar o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

2. Acessar a pasta do projeto:

```bash
cd internal-ticket-system
```

3. Criar e ativar um ambiente virtual (recomendado):

```bash
python -m venv venv
source venv/bin/activate
```

4. Instalar as dependências:

```bash
pip install -r requirements.txt
```

5. Executar a aplicação:

```bash
python app.py
```

6. Abrir o navegador em:

```text
http://localhost:5000
```

---

## Responsáveis Disponíveis

O sistema possui os seguintes responsáveis cadastrados:

- João
- Maria
- Carlos

Quando a opção **AUTO** é selecionada, o sistema atribui o chamado ao responsável com menor quantidade de chamados ativos.

---

## Fluxo de Utilização

### Criar chamado

1. Acesse a tela de criação.
2. Informe:
   - Nome do solicitante
   - Setor
   - Título
   - Descrição
   - Prioridade
   - Responsável
3. Clique em **Criar Chamado**.

### Consultar chamado

1. Acesse a lista de chamados.
2. Clique no título do chamado desejado.

### Editar chamado

1. Abra os detalhes do chamado.
2. Clique em **Editar Chamado**.
3. Atualize as informações.
4. Salve as alterações.

---

## Funcionalidades Implementadas

| Funcionalidade | Status |
|---------------|--------|
| Criar chamado | ✅ |
| Listar chamados | ✅ |
| Buscar chamado | ✅ |
| Visualizar detalhes | ✅ |
| Editar chamado | ✅ |
| Alterar status | ✅ |
| Responsável automático | ✅ |
| Interface web | ✅ |
| Regras de negócio | ✅ |

---

## Melhorias Futuras

- Persistência em banco de dados
- Autenticação de usuários
- Dashboard com métricas
- Histórico de alterações
- Comentários em chamados
- API REST
- Integração com banco PostgreSQL
- Upload de anexos

---

## Autor

**Caio Victor do Nascimento Leocadio**

Desenvolvido como projeto de estudo para prática de desenvolvimento web utilizando Flask, HTML, CSS e JavaScript.

---

## Licença

Projeto desenvolvido para fins acadêmicos e educacionais.
