from helpers.db_con import execute_update

@execute_update
def update_values(query_obj):
    return """
    UPDATE [dbo].[E_Schedules]
    SET 
        :column_name = :date
    WHERE nno IN (:nno);
    """
@execute_update
def update_values_i(query_obj):
    return """
    UPDATE [dbo].[I_Schedules]
    SET 
        :column_name = :date
    WHERE nno IN (:nno);
    """