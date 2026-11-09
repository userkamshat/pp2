CREATE OR REPLACE PROCEDURE upsert_contact(
    p_username VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM contacts
        WHERE username = p_username
    ) THEN

        UPDATE contacts
        SET phone = p_phone
        WHERE username = p_username;

        RAISE NOTICE 'Contact updated!';

    ELSE

        INSERT INTO contacts(username, phone)
        VALUES(p_username, p_phone);

        RAISE NOTICE 'New contact inserted!';

    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE insert_many_contacts(
    IN p_contacts JSONB,
    OUT invalid_data JSONB
)
LANGUAGE plpgsql
AS $$
DECLARE
    contact JSONB;
    v_username VARCHAR;
    v_phone VARCHAR;

BEGIN
    invalid_data := '[]'::JSONB;

    FOR contact IN
        SELECT * FROM jsonb_array_elements(p_contacts)
    LOOP

        v_username := contact->>'username';
        v_phone := contact->>'phone';

        IF v_username IS NULL OR v_phone IS NULL
           OR v_username = '' OR v_phone = '' THEN

            invalid_data := invalid_data ||
                jsonb_build_array(
                    jsonb_build_object(
                        'username', v_username,
                        'phone', v_phone,
                        'reason', 'Missing username or phone'
                    )
                );

        ELSIF v_phone !~ '^\+?[0-9]{10,15}$' THEN

            invalid_data := invalid_data ||
                jsonb_build_array(
                    jsonb_build_object(
                        'username', v_username,
                        'phone', v_phone,
                        'reason', 'Invalid phone number'
                    )
                );

        ELSE

            IF EXISTS (
                SELECT 1 FROM contacts
                WHERE username = v_username
            ) THEN

                UPDATE contacts
                SET phone = v_phone
                WHERE username = v_username;

            ELSE

                INSERT INTO contacts(username, phone)
                VALUES(v_username, v_phone);

            END IF;

        END IF;

    END LOOP;
END;
$$;
CREATE OR REPLACE PROCEDURE delete_contact(
    p_value VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN

    IF p_type = 'username' THEN

        DELETE FROM contacts
        WHERE username = p_value;

    ELSIF p_type = 'phone' THEN

        DELETE FROM contacts
        WHERE phone = p_value;

    ELSE

        RAISE EXCEPTION 'Invalid delete type!';

    END IF;

    IF NOT FOUND THEN
        RAISE NOTICE 'Contact not found!';
    ELSE
        RAISE NOTICE 'Contact deleted!';
    END IF;

END;
$$;