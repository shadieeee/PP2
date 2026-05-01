-- groups
CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- contacts
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100),
    birthday DATE,
    group_id INTEGER REFERENCES groups(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS phones (
    id SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
    phone VARCHAR(20) NOT NULL,
    type VARCHAR(10) CHECK (type IN ('home', 'work', 'mobile'))
);

-- индекс для ускорения поиска группы
CREATE UNIQUE INDEX IF NOT EXISTS idx_groups_name ON groups(name);

-- индекс для поиска контактов
CREATE INDEX IF NOT EXISTS idx_contacts_name ON contacts(first_name);

-- индекс для поиска телефонов
CREATE INDEX IF NOT EXISTS idx_phones_contact_id ON phones(contact_id);