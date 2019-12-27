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

