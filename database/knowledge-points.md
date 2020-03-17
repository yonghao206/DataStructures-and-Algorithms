# Knowledge Points

1. SQL执行顺序
   1. ```text
      # SQL Syntax Running Priority
      顺序: 
      (1)FROM [left_table]
      (3)<join_type> JOIN <right_table>
      (2)ON <join_condition>
      (4)WHERE <where_condition>
      (5)GROUP BY <group_by_list>
      (6)WITH <CUBE | RollUP>
      (7)HAVING <having_condition>
      (8)SELECT 
      (9)DISTINCT 
      (10)ORDER BY <order_by_list>
      (11)<Top Num> <select list>

      ```
2. 相关子查询
   1. ```sql
      # 相关子查询的内层查询由于与外层查询有关，因此必须反复求值
      https://blog.csdn.net/mascf/article/details/50288199

      select t.sno,t.sname,t.sage,t.sgentle,t.sbirth,sdept 
      from student t 
      where 80<=(select f.score 
                from grade f 
                where f.sno=t.sno and f.cname='计算机基础')
      （1）从外层查询中取出一个元组，将元组相关列的值传给内层查询。
      （2）执行内层查询，得到子查询操作的值。
      （3）外查询根据子查询返回的结果或结果集得到满足条件的行。
      （4）然后外层查询取出下一个元组重复做步骤1-3，直到外层的元组全部处理完毕。 
      // 178题
      select score, (select count(distinct tb2.score) 
                from Scores as tb2 
                where tb2.Score >= tb1.Score) as Rank
      from Scores as tb1
      order by Scores desc
      ```
3. ```sql
   CASE WHEN sex = '1' THEN '男'
   	 WHEN sex = '2' THEN '女'
   ELSE '其它' END;

   limit n,m 表示从第n+1条开始,取m条.limit 2,3表示取3,4,5条

   UNION 去重 UNION ALL:不去重

   //IFNULL, 查询句子外面套一个IFNULL，如果为空，返回下面那个值
   SELECT IFNULL(查询句子为空返回右边这个w3school, "W3Schools.com")

   // distinct
   distinct是对所有列去重，下面这个就是对AB同时去重
   select distinct A, B from tb1;
   这里是对 AB值相同的时候才会去重
   当select语句中包含distinct时，无论遇到多少个空值，结果中只返回一个null

   //order by 
   order by 1, 4 desc 按照先根据第一列的升序，然后根据第四列的降序进行排
   ```

4. Window Function
   1. ```sql

      ```

{% embed url="https://www.mysqltutorial.org/mysql-date-functions/" %}





