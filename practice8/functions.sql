CREATE OR REPLACE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE(username VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.username, c.phone
    FROM contacts c
    WHERE c.username ILIKE '%' || p_pattern || '%'
       OR c.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts_page(
    p_limit INTEGER,
    p_offset INTEGER
)
RETURNS TABLE(username VARCHAR, phone VARCHAR)
AS $$
BEGIN
    IF p_limit <= 0 OR p_offset < 0 THEN
        RAISE EXCEPTION 'Invalid limit or offset';
    END IF;

    RETURN QUERY
    SELECT c.username, c.phone
    FROM contacts c
    ORDER BY c.username
    LIMIT p_limit
    OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;