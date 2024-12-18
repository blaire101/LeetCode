在 Spark SQL 中，假设你的表名是 `orders`，表中包含以下字段：

- `order_id`（订单 ID）
- `city`（城市）
- `order_date`（订单日期）
- `sales`（销量）

以下是 SQL 查询语句，用于获取每一天销量排名前 10 的城市：

```sql
WITH ranked_sales AS (
  SELECT
    city,
    order_date,
    SUM(sales) AS daily_sales,
    ROW_NUMBER() OVER (PARTITION BY order_date ORDER BY SUM(sales) DESC) AS rank
  FROM
    orders
  WHERE
    order_date >= DATE_SUB(CURRENT_DATE(), 30) -- 最近30天
  GROUP BY
    city,
    order_date
)
SELECT
  order_date,
  city,
  daily_sales
FROM
  ranked_sales
WHERE
  rank <= 10
ORDER BY
  order_date ASC,
  rank ASC;
```