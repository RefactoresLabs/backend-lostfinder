# backend-lostfinder
API e motor de gamificação para o ecossistema FindIt. Gerencia o inventário de itens, sistema de pontos, conquistas e autenticação de usuários universitários.
#Estive aqui. Professor Rondineli
Estrutura de Pastas
```text
backend/
│
├── app/
│   │
│   ├── presentation/                 # Camada de apresentação (API REST)
│   │   ├── controllers/              # Controladores que recebem requisições HTTP e chamam os serviços da aplicação
│   │   ├── routes/                   # Definição das rotas/endpoints da API
│   │   ├── schemas/                  # Modelos de entrada e saída da API
│   │
│   ├── application/                  # Camada de aplicação (casos de uso do sistema)
│   │   ├── services/                 # Lógicas reutilizáveis utilizadas pelos casos de uso
│   │   ├── dtos/                      # Objetos de transferência de dados entre apresentação e domínio
│   │   ├── use_cases/                # Casos de uso
│   │   ├── interfaces/               # Interfaces fora do domínio
│   │
│   ├── domain/                       # Núcleo do sistema (regras de negócio independentes de tecnologia)
│   │   ├── entities/                 # Entidades principais do sistema (Usuário, Item, Pedido de Devolução)
│   │   ├── value_objects/            # Objetos de valor imutáveis (Endereço, Coordenadas, Categoria)
│   │   ├── repositories/             # Interfaces de repositório (contratos de persistência)
│   │   ├── strategies/               # Implementações do padrão Strategy (ex: ordenação de itens)
│   │   ├── specifications/           # Implementações do padrão Specification (filtros e critérios de busca)
│   │   ├── states/                   # Implementações do padrão State (estados do pedido de devolução)
│   │   ├── enums/                    # Enumerações do domínio (ex: status, categorias)
│   │   ├── exceptions/               # Exceções específicas do domínio
│   │
│   ├── infrastructure/               # Camada de infraestrutura (detalhes técnicos e externos)
│   │   ├── persistence/
│   │   │   ├── models/               # Modelos do banco de dados (ORM)
│   │   │   ├── repositories/         # Implementações concretas dos repositórios
│   │   │
│   │   ├── external/
│   │   │   ├── maps/                 # Integração com APIs externas (Adapter Pattern - ex: geolocalização)
│   │   │
│   │   ├── security/                 # Serviços de segurança (hash de senha, autenticação, criptografia)
│   │   ├── storage/                  # Manipulação de arquivos (upload e armazenamento de imagens)
│   │   ├── database/                   # Conexões e sessões do banco de dados
│   │
│   ├── main.py                       # Ponto de entrada da aplicação (inicialização do servidor)

