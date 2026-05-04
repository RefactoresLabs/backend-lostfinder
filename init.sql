-- Ativar chaves estrangeiras
PRAGMA foreign_keys = ON;

-- Tabela de contas dos usuários
CREATE TABLE user_account (
    id INTEGER AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    PRIMARY KEY(id)
);

-- Endereço base (sem prédio)
CREATE TABLE localization (
    id INTEGER AUTOINCREMENT,
    cep VARCHAR(8) NOT NULL,
    bairro VARCHAR(255) NOT NULL,
    rua VARCHAR(255) NOT NULL,
    PRIMARY KEY(id)
);

-- Prédios vinculados a uma localização
CREATE TABLE building (
    id INTEGER AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    localization_id INTEGER NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_building_localization
        FOREIGN KEY (localization_id)
        REFERENCES localization(id),
    UNIQUE (name, localization_id) -- evita prédio duplicado no mesmo local
);

-- Espaços dentro de um prédio (ex: sala, laboratório)
CREATE TABLE building_space (
    id INTEGER AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    building_id INTEGER NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_space_building
        FOREIGN KEY (building_id)
        REFERENCES building(id),
    UNIQUE (name, building_id) -- evita duplicação dentro do prédio
);

-- Categorias de itens
CREATE TABLE category (
    id INTEGER AUTOINCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY(id)
);

-- Item base (herança)
CREATE TABLE item (
    id INTEGER AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    registry_date DATE NOT NULL,
    category_id INTEGER NOT NULL,
    account_id INTEGER NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_item_category
        FOREIGN KEY (category_id)
        REFERENCES category(id),
    CONSTRAINT fk_item_account
        FOREIGN KEY (account_id)
        REFERENCES account(id)
);

-- Item perdido (especialização)
CREATE TABLE lost_item (
    id INTEGER,
    lost_space_id INTEGER NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_lost_item
        FOREIGN KEY (id)
        REFERENCES item(id),
    CONSTRAINT fk_lost_space
        FOREIGN KEY (lost_space_id)
        REFERENCES building_space(id)
);

-- Item encontrado (especialização)
CREATE TABLE found_item (
    id INTEGER,
    found_space_id INTEGER NOT NULL,
    left_space_id INTEGER NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_found_item
        FOREIGN KEY (id)
        REFERENCES item(id),
    CONSTRAINT fk_found_space
        FOREIGN KEY (found_space_id)
        REFERENCES building_space(id),
    CONSTRAINT fk_left_space
        FOREIGN KEY (left_space_id)
        REFERENCES building_space(id)
);

-- Imagens associadas ao item
CREATE TABLE image (
    id INTEGER AUTOINCREMENT,
    url VARCHAR(255) NOT NULL,
    item_id INTEGER NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_image_item
        FOREIGN KEY (item_id)
        REFERENCES item(id)
        ON DELETE CASCADE -- remove imagens quando o item for deletado
);