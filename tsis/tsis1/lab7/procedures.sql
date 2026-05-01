
CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    cid INT;
BEGIN
    SELECT id INTO cid
    FROM contacts
    WHERE first_name = p_contact_name
    ORDER BY id
    LIMIT 1;

    IF cid IS NULL THEN
        RAISE EXCEPTION 'Contact not found';
    END IF;

    INSERT INTO phones(contact_id, phone, type)
    VALUES (cid, p_phone, p_type);
END;
$$;



CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    gid INT;
BEGIN
    SELECT id INTO gid
    FROM groups
    WHERE name = p_group_name;

    IF gid IS NULL THEN
        INSERT INTO groups(name)
        VALUES (p_group_name)
        RETURNING id INTO gid;
    END IF;

    UPDATE contacts
    SET group_id = gid
    WHERE first_name = p_contact_name;
END;
$$;


CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE (
    id INT,
    first_name VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR,
    phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT
        c.id,
        c.first_name,
        c.email,
        c.birthday,
        g.name,
        p.phone
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON p.contact_id = c.id
    WHERE c.first_name ILIKE '%' || p_query || '%'
       OR COALESCE(c.email, '') ILIKE '%' || p_query || '%'
       OR COALESCE(p.phone, '') ILIKE '%' || p_query || '%'
    ORDER BY c.id;
END;
$$;