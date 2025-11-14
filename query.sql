SELECT 
    oi.order_id,
    o.order_date,
    c.first_name || ' ' || c.last_name AS customer_name,
    p.product_name,
    oi.quantity,
    oi.price_per_item,
    oi.quantity * oi.price_per_item AS total_line_price,
    c.country AS customer_country
FROM 
    order_items oi
    INNER JOIN orders o ON oi.order_id = o.order_id
    INNER JOIN customers c ON o.customer_id = c.customer_id
    INNER JOIN products p ON oi.product_id = p.product_id
ORDER BY 
    o.order_date DESC;

