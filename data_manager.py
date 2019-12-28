import database_common


@database_common.connection_handler
def get_mentor_names_by_first_name(cursor, first_name):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    WHERE first_name = %(first_name)s ORDER BY first_name;
                   """,
                   {'first_name': first_name})
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_all_first_name_and_last_name(cursor):
    cursor.execute(
        """
                    SELECT first_name, last_name FROM mentors;
                    """
    )
    first_and_last_name = cursor.fetchall()
    return first_and_last_name


@database_common.connection_handler
def get_mentors_nicknames_by_city(cursor, city):
    cursor.execute("""SELECT nick_name FROM mentors
                      WHERE city = %(city)s ORDER BY nick_name;
                   """,
                   {'city': city})
    mentors_nicknames = cursor.fetchall()
    return mentors_nicknames


@database_common.connection_handler
def get_applicant_fullname_and_phone_number_by_first_name(cursor, first_name):
    cursor.execute(
        """
        SELECT first_name || ' ' || last_name AS full_name, phone_number
        FROM applicants
        WHERE first_name = '{first_name}'
        """.format(first_name=first_name)

    )
    full_name_and_phone_number = cursor.fetchall()
    return full_name_and_phone_number


@database_common.connection_handler
def get_applicant_fullname_and_phone_number_by_email(cursor, email):
    cursor.execute(
        """
        SELECT first_name || ' ' || last_name AS full_name, phone_number
        FROM applicants
        WHERE email LIKE '%{email}'
        """.format(email=email)
    )
    get_full_name_and_phone_number = cursor.fetchall()
    return get_full_name_and_phone_number


@database_common.connection_handler
def add_new_applicant(cursor, first_name, last_name, phone_number, email, application_code):
    cursor.execute(
        """
       INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
       VALUES ('{first_name}', '{last_name}', '{phone_number}', '{email}', '{application_code}');
        """.format(first_name=first_name,
                   last_name=last_name,
                   phone_number=phone_number,
                   email=email,
                   application_code=application_code)
    )

@database_common.connection_handler
def get_applicant_details(cursor, application_code):
    cursor.execute(
        """
        SELECT * FROM applicants
        WHERE application_code = '{application_code}';
        """.format(application_code=application_code)
    )
    details = cursor.fetchall()
    return details


@database_common.connection_handler
def update_applicant_phone_number(cursor, first_name, last_name, phone_number):
    cursor.execute(
        """
        UPDATE applicants
        SET phone_number = '{phone_number}'
        WHERE first_name = '{first_name}' AND last_name = '{last_name}';
        """.format(phone_number=phone_number,
                   first_name=first_name,
                   last_name=last_name,)
    )


@database_common.connection_handler
def remove_applicants_by_domain(cursor, domain):
    cursor.execute(
        """
        DELETE FROM applicants
        WHERE email LIKE '%{domain}'
        """.format(domain=domain)
    )