sql_drop_table_courses = """DROP TABLE courses;"""

sql_drop_table_announcements = """DROP TABLE announcements;"""

sql_create_table_courses = """CREATE TABLE IF NOT EXISTS courses (
                        id INTEGER, 
                        name TEXT, 
                        course_code TEXT, 
                        start_at REAL,
                        end_at REAL, 
                        timestamp NUMERIC,
                        subscribed_to NUMERIC,
                        PRIMARY KEY(id)
                    );"""

sql_create_table_announcements = """CREATE TABLE IF NOT EXISTS announcements (
                        id INTEGER, 
                        title TEXT, 
                        text TEXT, 
                        author TEXT,
                        context_code TEXT, 
                        posted_at REAL,
                        timestamp NUMERIC,
                        sent_discord NUMERIC,
                        PRIMARY KEY(id)
                    );"""


def sql_insert_table_courses(
    id,
    name,
    course_code,
    start_at,
    end_at,
    timestamp,
    subscribed_to):
    query = f"""
        INSERT INTO courses (
            id,
            name,
            course_code,
            start_at,
            end_at,
            timestamp,
            subscribed_to) 
        VALUES (
            "{id}",
            "{name}",
            "{course_code}",
            "{start_at}",
            "{end_at}",
            "{timestamp}",
            "{subscribed_to}"
            );
    """
    return query

def sql_insert_table_announcements(
    id,
    title,
    text,
    author,
    context_code,
    posted_at,
    timestamp,
    sent_discord):
    query = f"""
        UPDATE courses (
            id,
            title,
            text,
            author,
            context_code,
            posted_at,
            timestamp,
            sent_discord) 
        VALUES (
            "{id}",
            "{title}",
            "{text}",
            "{author}",
            "{context_code}",
            "{posted_at}",
            "{timestamp}",
            "{sent_discord}"
            );
    """
    return query

sql_select_courses ="""SELECT course_name, course_id FROM courses;"""

# Returns 1 if exists and 0 if not (as SQLITE doesn't support boolean)
def sql_check_if_exists(attribute, value, table): 
    query = f"""
    SELECT COUNT({attribute}) FROM {table} WHERE {attribute} = {value}
    """
    return query