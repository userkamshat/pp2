
CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Check if contact exists
    IF NOT EXISTS (
        SELECT 1
        FROM contacts
        WHERE username = p_contact_name
    ) THEN
        RAISE EXCEPTION 'Contact does not exist!';
    END IF;

    -- Check phone type
    IF p_type NOT IN ('home', 'work', 'mobile') THEN
        RAISE EXCEPTION 'Invalid phone type!';
    END IF;

    -- Insert new phone
    INSERT INTO phones (contact_name, phone, type)
    VALUES (p_contact_name, p_phone, p_type);

    RAISE NOTICE 'Phone added successfully!';
END;
$$;

CREATE OR REPLACE PROCEDURE public.move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_group_id INTEGER;
BEGIN
    -- Check if contact exists
    IF NOT EXISTS (
        SELECT 1
        FROM contacts
        WHERE username = p_contact_name
    ) THEN
        RAISE EXCEPTION 'Contact does not exist!';
    END IF;

    -- Find or create group
    INSERT INTO groups (name)
    VALUES (p_group_name)
    ON CONFLICT (name) DO NOTHING;

    SELECT id INTO v_group_id
    FROM groups
    WHERE name = p_group_name;

    -- Update contact group
    UPDATE contacts
    SET group_id = v_group_id
    WHERE username = p_contact_name;

    RAISE NOTICE 'Contact moved successfully!';
END;
$$;

CREATE OR REPLACE FUNCTION public.search_contacts(p_pattern TEXT)
RETURNS TABLE(
    username VARCHAR,
    phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT
        c.username,
        c.phone
    FROM contacts c
    LEFT JOIN phones p
        ON p.contact_name = c.username
    WHERE
        c.username ILIKE '%' || p_pattern || '%'
        OR c.email ILIKE '%' || p_pattern || '%'
        OR c.phone ILIKE '%' || p_pattern || '%'
        OR p.phone ILIKE '%' || p_pattern || '%';
END;
$$;




CREATE OR REPLACE PROCEDURE set_phone_type(
    p_contact_name VARCHAR,
    p_phone VARCHAR
) 
LANGUAGE plpgsql
AS $$
BEGIN
IF p_type NOT IN('home','work','mobile')THEN
    RAISE EXCEPTION 'Invalid phone type!';
END IF;
UPDATE phones
SET type=p_type
WHERE contact_name=p_contract_name
    AND phone=p_phone;
