SELECT ANIMAL_TYPE, count(*)
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY
    CASE WHEN ANIMAL_TYPE='Cat' THEN 1 ELSE 2 END
