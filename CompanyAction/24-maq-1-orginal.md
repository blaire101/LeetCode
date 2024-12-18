## 1. SQL: Identify customers with an average spend per day > 3

```python
customer_id	txn_date	txn_time	txn_amount
A	2022-11-17	9am	3
A	2021-10-16	10am	9
A	2023-07-20	2pm	1
B	2023-04-01	12 am	2
B	2021-12-13	12pm	10
B	2022-03-09	4pm	15
B	2021-10-16	6am	8
B	2021-10-16	3pm	2
```
 
```python 
Identify customers with an average spend per day > 3
with daily_spend as (
    select customer_id, 
            txn_date,
            sum(txn_amount) as sum_spend
            from transaction
            group by customer_id, txn_date
)

select customer_id, 
        avg(sum_spend) as average_spend
        from daily_spend
        group by customer_id
        having avg(sum_spend)>3
How do get the average number of days between transactions for every customer
```

## 2. SQL: How do get the average number of days between transactions for every customer

```python
with transaction_date as (
    select customer_id, 
            txn_date,
            lag(txn_date) over (partition by customer_id order by txn_date) as prev_transaction_date
            from transaction
),

with date_diff as (
    select customer_id, 
            date_diff(txn_date,prev_transaction_date) as date_between_transactions
            from transaction_date
            where prev_transaction_date is not NULL
)
select customer_id,
    avg(date_between_transactions) as avg_days_transactions
    from date_diff
    group by customer_id
```

## 3. python tuples

```python
A = [1, 2, 3, 4]
B = [2, 4, 5, 6]
C = [1, 3, 4, 9]
D = [7, 4, 9, 10]
Question - Find how many tuples are there that fulfils:
A[i] + B[j] + C[k] = D[l]
Example of a tuple: 
(1,2,1,4)  - A[0] + B[0] + C[0] = D[1]
(2,2,3,7) - A[1] + B[0] + C[1] = D[0]
sum_AB = {}

for i in range(len(A)):
    for j in range(len(B)):
        sum_AB[i+j] +=1

count = 0
for i in range(len(C)):
    for j in range(len(D)):
        target = D[j]-C[i]
        if target in sum_AB:
            count += sum_AB[target]
```
     
## 4. python udf
     
```python            
def check(col,common_words):
     if col in common_words:
        return 1
    else 
       return 0

common_words=[]
check_udf = udf(lambda col:check(col,common_words),IntegerType())
df = df.withColumn('after_checking',check_udf(df['before_checking'],common_words))
```