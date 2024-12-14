from helpers.db_con import execute_update

@execute_update
def update_values(query_obj):
    return """
    UPDATE [dbo].[E_Schedules]
    SET [%(column_name)s] = %(date)s
    WHERE nno IN %(nno)s
    """

@execute_update
def update_values_i(query_obj):
    return """
    UPDATE [dbo].[I_Schedules]
    SET [%(column_name)s] = %(date)s
    WHERE nno IN %(nno)s
    """