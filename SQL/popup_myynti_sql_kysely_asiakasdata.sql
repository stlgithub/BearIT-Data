##MYYNTI JA ASIAKASDATA
SELECT 
    m1.ostotapahtuma_id,
    m1.aika,
	m1.tuote_id,
    tk.kategoria_id,
    tk.pääkategoria_nimi,
    tk.alakategoria_nimi,
    t.tuote_nimi,
    t.tukkuhinta,
    t.myyntihinta,
    tk.alv,
	ROUND(t.myyntihinta - t.myyntihinta * (tk.alv/100),2) AS myyntihinta_ilman_alv,
	m2.ostoksen_myyntihinta,
    m2.ostoksen_myyntihinta_ilman_alv,
    m2.ostoksen_kate,
    a.asiakas_id,
    a.puhelinnumero,
    a.sähköposti,
    a.ikä,
    (CASE
        WHEN a.ikä < 30 THEN '18-29'
        WHEN a.ikä BETWEEN 30 AND 39 THEN '30-39'
        WHEN a.ikä BETWEEN 40 AND 49 THEN '40-49'
        WHEN a.ikä BETWEEN 50 AND 59 THEN '50-59'
        WHEN a.ikä BETWEEN 60 AND 69 THEN '60-69'
        WHEN a.ikä BETWEEN 70 AND 79 THEN '70-79'
        ELSE '80+'
    END) AS ikäryhmä,
    (CASE 
		WHEN a.sukupuoli = 'F' THEN 'Nainen'
        WHEN a.sukupuoli = 'M' THEN 'Mies'
        ELSE 'Muu'
    END) AS sukupuoli,
    (CASE 
		WHEN a.puhelinnumero IS NOT NULL AND (a.sähköposti IS NULL OR a.sähköposti = '') THEN 'puhelinnumero'
		WHEN (a.puhelinnumero IS NULL OR a.puhelinnumero = '') AND a.sähköposti IS NOT NULL THEN 'sähköposti'
		ELSE 'molemmat'
    END) AS yhteystiedot
FROM
    myynti m1
        JOIN
    tuotteet t ON t.tuote_id = m1.tuote_id
        JOIN
    tuotekategoriat tk ON t.kategoria_id = tk.kategoria_id
        JOIN
    asiakas a ON a.asiakas_id = m1.asiakas_id
		JOIN
	(SELECT 
	m.ostotapahtuma_id,
    m.aika,
    SUM(t.myyntihinta) AS ostoksen_myyntihinta,
    ROUND(SUM(t.myyntihinta - t.myyntihinta * (tk.alv/100)),2) AS ostoksen_myyntihinta_ilman_alv,
    (SUM(t.myyntihinta) - SUM(t.tukkuhinta)) AS ostoksen_kate
FROM myynti m
JOIN tuotteet t ON t.tuote_id = m.tuote_id
JOIN tuotekategoriat tk ON t.kategoria_id = tk.kategoria_id
GROUP BY m.ostotapahtuma_id, m.aika) AS m2 ON m1.ostotapahtuma_id = m2.ostotapahtuma_id ##koko ostoksen myyntihinta ja kate
ORDER BY m1.ostotapahtuma_id;