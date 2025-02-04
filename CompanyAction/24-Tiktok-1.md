In Spark SQL, assume your table is named `orders` and it contains the following fields:

- **order_id** (Order ID)
- **city** (City)
- **order_date** (Order Date)
- **sales** (Sales Volume)

Below is the SQL query used to retrieve the top 10 cities by sales volume for each day:

Q5-SQL coding knowledge


Q5： SQL query execution order
1. FROM (Select data)
2. WHERE (Filter records)
3. GROUP BY (Group and aggregate by city and order_date)
4. SELECT (Calculate window functions and generate columns such as rank)
5. Outer SELECT and ORDER BY (Filter and sort the final results)
Don't modify the sentences here, just repeat the pronunciation in English.

order_id	city	order_date	sales
1	Beijing	2025-01-01	100
2	Shanghai	2025-01-01	150
3	Guangzhou	2025-01-01	120
4	Beijing	2025-01-01	200
5	Shanghai	2025-01-01	100
6	Beijing	2025-01-02	300
7	Shanghai	2025-01-02	250
8	Guangzhou	2025-01-02	180
9	Beijing	2025-01-02	50

```SQL
WITH aggregated AS (
  SELECT
    city,
    order_date,
    SUM(sales) AS daily_sales,
    ROW_NUMBER() OVER (PARTITION BY order_date ORDER BY SUM(sales) DESC) AS rank
  FROM orders
  WHERE order_date >= DATE_SUB(CURRENT_DATE(), 30)
  GROUP BY city, order_date
)
```

```SQL
SELECT
  order_date,
  city,
  daily_sales,
  rank,

  SUM(daily_sales) OVER (PARTITION BY order_date) AS total_daily_sales,

  SUM(daily_sales) OVER (
    PARTITION BY order_date
    ORDER BY daily_sales DESC
  ) AS cumulative_total

FROM aggregated

ORDER BY order_date ASC, daily_sales DESC;
```


Expected Output:
order_date	city	daily_sales	rank	total_daily_sales	cumulative_total
2025-01-01	Beijing	300	1	670	300
2025-01-01	Shanghai	250	2	670	550
2025-01-01	Guangzhou	120	3	670	670
2025-01-02	Beijing	350	1	780	350
2025-01-02	Shanghai	250	2	780	600
2025-01-02	Guangzhou	180	3	780	780
Whole-Partition Aggregation (no ORDER BY): Each row displays the total sum for the partition (e.g., 670).

Cumulative Sum (with ORDER BY and window frame): Each row shows the running total from the start of the partition up to that row.
