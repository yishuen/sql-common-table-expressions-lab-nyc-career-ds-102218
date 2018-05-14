def cte_deletes_duplicates():
    return """WITH duplicates AS
            (
            SELECT sale_id, amount, MIN(id) AS minimum_id
            FROM sales
            GROUP BY sale_id
            )
            DELETE FROM sales WHERE id NOT IN (SELECT minimum_id FROM duplicates);"""

def correct_above_avg_sales():
    return """WITH average_sales AS
            (
            SELECT AVG(amount) AS average FROM sales
            )
            SELECT locations.city, sales.date_of_sale, sales.amount FROM sales
            INNER JOIN locations
            ON locations.id = sales.location_id
            WHERE amount > (SELECT average FROM average_sales);"""
