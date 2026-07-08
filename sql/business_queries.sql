USE phonepe;


-- 1. Top 10 states by total transaction amount

SELECT 
state,
SUM(transaction_amount) AS total_amount

FROM aggregated_transaction

GROUP BY state

ORDER BY total_amount DESC

LIMIT 10;



-- 2. Year-wise transaction growth

SELECT

year,

SUM(transaction_amount) AS total_amount,

SUM(transaction_count) AS total_transactions

FROM aggregated_transaction

GROUP BY year

ORDER BY year;



-- 3. Most used transaction types

SELECT

transaction_type,

SUM(transaction_count) AS total_transactions

FROM aggregated_transaction

GROUP BY transaction_type

ORDER BY total_transactions DESC;



-- 4. Top states by registered users

SELECT

state,

MAX(registered_users) AS users

FROM aggregated_user

GROUP BY state

ORDER BY users DESC

LIMIT 10;



-- 5. User growth by year

SELECT

year,

SUM(registered_users) AS total_users

FROM aggregated_user

GROUP BY year

ORDER BY year;



-- 6. Top insurance states

SELECT

state,

SUM(transaction_amount) AS insurance_value

FROM aggregated_insurance

GROUP BY state

ORDER BY insurance_value DESC

LIMIT 10;



-- 7. Highest transaction districts

SELECT

district,

SUM(transaction_amount) AS amount

FROM map_transaction

GROUP BY district

ORDER BY amount DESC

LIMIT 10;



-- 8. Top districts by users

SELECT

district,

MAX(registered_users) AS users

FROM map_user

GROUP BY district

ORDER BY users DESC

LIMIT 10;



-- 9. Quarterly transaction trend

SELECT

year,

quarter,

SUM(transaction_amount) AS amount

FROM aggregated_transaction

GROUP BY year,quarter

ORDER BY year,quarter;