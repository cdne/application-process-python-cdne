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
def get_mentors_names(cursor):
    cursor.execute(
        """
                    SELECT first_name, last_name FROM mentors;
                    """
    )

    first_and_last_name = cursor.fetchall()
    return first_and_last_name


@database_common.connection_handler
def get_nickname_miskolc(cursor):
    cursor.execute("""SELECT nick_name FROM mentors
                      WHERE city = 'Miskolc';""")

    mentors_nickname = cursor.fetchall()
    return mentors_nickname


@database_common.connection_handler
def get_applicant_details(cursor, student, email):
    if student == 'Carol' and not None:
        cursor.execute("""
                       SELECT first_name || ' ' || last_name AS full_name, phone_number
                       FROM applicants 
                       WHERE first_name LIKE '%Carol%';
                       """)

        applicant_details = cursor.fetchall()
        return applicant_details
    elif email == '@adipiscingenimmi.edu' and not None:
        cursor.execute("""
                       SELECT first_name || ' ' || last_name AS full_name, phone_number
                       FROM applicants 
                       WHERE email LIKE '%@adipiscingenimmi.edu';
                       """)

        applicant_details = cursor.fetchall()
        return applicant_details


@database_common.connection_handler
def add_new_applicant(cursor):
    cursor.execute(
        """
       INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
       VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', '54823');
        """
    )


@database_common.connection_handler
def get_new_applicant_details(cursor):
    cursor.execute(
        """
        SELECT * FROM applicants
        WHERE application_code = 54823;
        """
    )

    details = cursor.fetchall()
    return details
