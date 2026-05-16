-- Tabela de contas dos usuários
CREATE TABLE user_account (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL
);

-- Endereço base (sem prédio)
CREATE TABLE localization (
    id SERIAL PRIMARY KEY,
    cep VARCHAR(8) NOT NULL,
    neighborhood VARCHAR(255) NOT NULL,
    street VARCHAR(255) NOT NULL
);

-- Prédios vinculados a uma localização
CREATE TABLE building (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    localization_id INTEGER NOT NULL,
    CONSTRAINT fk_building_localization
        FOREIGN KEY (localization_id)
        REFERENCES localization(id),
    UNIQUE (name, localization_id) -- evita prédio duplicado no mesmo local
);

-- Espaços dentro de um prédio (ex: sala, laboratório)
CREATE TABLE building_space (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    building_id INTEGER NOT NULL,
    CONSTRAINT fk_space_building
        FOREIGN KEY (building_id)
        REFERENCES building(id),
    UNIQUE (name, building_id) -- evita duplicação dentro do prédio
);

-- Categorias de itens
CREATE TABLE category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);

-- Item base (herança)
CREATE TABLE item (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    registration_date DATE NOT NULL,
    category_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    CONSTRAINT fk_item_category
        FOREIGN KEY (category_id)
        REFERENCES category(id),
    CONSTRAINT fk_item_account
        FOREIGN KEY (user_id)
        REFERENCES user_account(id)
);

-- Item perdido (especialização)
CREATE TABLE lost_item (
    id INTEGER PRIMARY KEY,
    lost_space_id INTEGER NOT NULL,
    CONSTRAINT fk_lost_item
        FOREIGN KEY (id)
        REFERENCES item(id),
    CONSTRAINT fk_lost_space
        FOREIGN KEY (lost_space_id)
        REFERENCES building_space(id)
);

-- Item encontrado (especialização)
CREATE TABLE found_item (
    id INTEGER PRIMARY KEY,
    found_space_id INTEGER NOT NULL,
    left_space_id INTEGER NOT NULL,
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
    id SERIAL PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    item_id INTEGER NOT NULL,
    CONSTRAINT fk_image_item
        FOREIGN KEY (item_id)
        REFERENCES item(id)
        ON DELETE CASCADE -- remove imagens quando o item for deletado
);

-- Insert categories
INSERT INTO category(name) VALUES ('Material Escolar'), ('Acessório Pessoal'), ('Documento'), ('Eletrônico');

-- Insert localization
INSERT INTO localization(cep, neighborhood, street) VALUES ('65075441', 'Jardim Renascença', 'Coronel Colares Moreira');

-- Insert building
INSERT INTO building(name, localization_id) VALUES ('Centro Universitário UNDB', 1);

-- Insert building spaces
INSERT INTO building_space(name, building_id) VALUES ('Sala 206', 1), ('Refeitório', 1), ('Recepção', 1);
