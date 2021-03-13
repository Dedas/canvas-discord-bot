# Internal modules
from datetime import datetime

# Local modules
from canvas.http_requests import *
from database.interactions import *
from database.queries import *

# Third party modules
from apscheduler.schedulers.background import BackgroundScheduler

def init_monitor():
    # Create scheduler object
    scheduler = BackgroundScheduler()

    # Set scheduler action and interval
    scheduler.add_job(update_db, 'interval', seconds=5)

    # Run scheduler
    scheduler.start()

    
def update_db():

    ##########################
    # HANDLE COURSES UPDATES #
    ##########################

    # Fetch data from courses request to Canvas
    data_courses = fetch_courses()

    if data_courses is not None:

        # Insert every fetched course
        for i in range(len(data_courses)):

            # Check if course exists, if it doesn't insert it
            if not (sql_query_fetchone_result(sql_check_if_exists('id', data_courses[i]['id'], 'courses'))):
                sql_query_commit(
                    sql_insert_table_courses(
                        data_courses[i]['id'], 
                        data_courses[i]['name'], 
                        data_courses[i]['course_code'],
                        data_courses[i]['start_at'], 
                        data_courses[i]['end_at'],
                        timestamp(),
                        0 # Initial value for subscribed to 0
                    )
                )
            else:
                sql_query_commit(
                    sql_update_table_courses(
                        data_courses[i]['id'], 
                        data_courses[i]['name'], 
                        data_courses[i]['course_code'],
                        data_courses[i]['start_at'], 
                        data_courses[i]['end_at'],
                        timestamp()
                    )
                )

        print('Courses inserted: ' + str(datetime.now()))
    else:
        print('Database error!')

    ################################
    # HANDLE ANNOUNCEMENTS UPDATES #
    ################################

    # A list of every course ID in database  
    course_id_list = sql_query_fetchall_result(sql_select_table_courses_id)

    # Fetch announcements for every course in Canvas table
    for i in range(len(course_id_list)):
        
        data_announcements = fetch_announcements(course_id_list[i])

        for f in range(len(data_announcements)):

            # Check if announcement exists, if it doesn't insert it
            if not (sql_query_fetchone_result(sql_check_if_exists('id', data_announcements[f]['id'], 'announcements'))):
                sql_query_commit(
                    sql_insert_table_announcements(
                        data_announcements[f]['id'], 
                        data_announcements[f]['title'], 
                        data_announcements[f]['message'],
                        data_announcements[f]['author']['display_name'], 
                        data_announcements[f]['context_code'],
                        data_announcements[f]['posted_at'],
                        timestamp(),
                        0 # Sent to Discord initial value 0
                    )
                )
            else:
                sql_query_commit(
                    sql_update_table_announcements(
                        data_announcements[f]['id'], 
                        data_announcements[f]['title'], 
                        data_announcements[f]['message'],
                        data_announcements[f]['author']['display_name'], 
                        data_announcements[f]['context_code'],
                        data_announcements[f]['posted_at'],
                        timestamp()
                    )
                )