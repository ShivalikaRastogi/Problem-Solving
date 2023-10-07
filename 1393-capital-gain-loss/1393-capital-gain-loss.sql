# Write your MySQL query statement below
SELECT BS.stock_name, Sum(BS.price) as capital_gain_loss 
FROM
(SELECT B.stock_name, -SUM(B.price) as price
FROM Stocks B
WHERE B.operation ='Buy'
GROUP BY B.stock_name
UNION ALL
SELECT S.stock_name,  SUM(S.price) as price
FROM Stocks S
WHERE S.operation ='Sell'
GROUP BY S.stock_name) as BS
GROUP BY BS.stock_name