<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Front Page</title>
    <style>
        /* Add the CSS provided above here */
.language-switch {
    position: absolute;
    top: 50px;
    left: 70px;
    z-index: 1000; /* Increased z-index to ensure it stays on top */
}

.language-switch span {
    margin-right: 5px;
    color: #ffffff; /* Color for the text */
    font-size: 20px; /* Adjust the font size */
}

.language-switch img {
    width: 50px;
    height: 50px;
}
.header {
    position: relative;
    width: 100%;
    height: 60vh; /* Reduced height to half */
    background: url("web/banner.jpg");
    background-attachment: fixed; /* Parallax effect */
    background-size: contain;
    font-family: 'Harrington';font-size: 22px;
}
.summary h1 {
    text-align: center;
    color: white; /* Set header text color to white */
}
.summary {
    position: absolute;
    top: 50%;
    left: 25%; /* Adjust this value to move the text to the left */
    transform: translate(-50%, -50%);
    background: rgba(135, 4, 22, 1);
    padding: 20px;
    border-radius: 10px;
}
.header-buttons {
    margin-top: 60px;
    font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif; font-size: 17px;
}
.button {
    background-color: #ffffff;
    color: rgba(135, 4, 22, 1);
    padding: 10px 20px;
    margin: 30px;
    text-decoration: none;
    border-radius: 5px;
}
.button:hover {
    background-color: #137200;
}
.about-section {
    padding: 30px;
    background-color: #f4f4f4;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family:'Courier New', Courier, monospace
}

.about-content {
    text-align: center; /* Center the text */
    width: 80%; /* Reduced width */
    max-width: 1200px;
}
.team-section {
    padding: 50px;
    text-align: center;
    color: white;
    background-color: rgba(135, 4, 22, 1)
}
.team-members {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    font-family:'Courier New', Courier, monospace
}
.team-member {
    flex: 1 1 21%;
    margin: 10px;
    padding: 20px;
    background: #f4f4f4;
    border-radius: 10px;
    text-align: center;
    color: black;
}
.team-member img {
    width: 115px;
    height: 115px;
    border-radius: 50%;
    margin-bottom: 10px;
}
.social-icons {
    margin: 10px 0;
}
.social-icons a {
    margin: 0 5px;
    display: inline-block;
}
.social-icons img {
    width: 30px;
    height: 30px;
}
    </style>
</head>
<body>
    <div class="language-switch">
        <a href="web/index_eng.html">
            <img src="web/flag_uk.png" alt="Change Language">
        </a>
    </div>
    <div class="header">
        <div class="summary">
            <h1>Pop-Up Joulumyymälä</h1>
            <div class="header-buttons">
                <a href="https://bearit-dataprojekti.streamlit.app/" class="button">Streamlit</a>
                <a href="https://github.com/stlgithub/BearIT-Data" class="button">GitHub Repo</a>
                <a href="https://github.com/stlgithub/BearIT-Data" class="button">PowerBI Raportti</a>
                <a href="web/pilvi.html" class="button">Pilvitietokanta Raportti</a>
            </div>
        </div>
    </div>
    
    <div class="about-section">
        <div class="about-content">
            <h2>About the Project</h2>
            <p>Tässä harjoitusprojektissa tehtiin paikallinen ja pilvessä olevat tietokannat kuvitteelliselle Pop-Up Joulumyymälälle. Tietokantoihin syötettiin tietoa kanta-asiakkaista, tuotteista ja myyntitapahtumista, ja tietoa tulkittiin siitä tehdyin erilaisin raportein. Projekti toteutettiin käyttäen Scrum metodeja, ja projektin kesto oli kaksi sprinttiä tai neljä viikkoa. Projekti tehtiin osana BearIT:n järjestämää ICT-Camp -kurssia.</p>
        </div>
    </div>
    <div class="team-section">
        <h2>Meet the Team</h2>
        <div class="team-members">
            <div class="team-member">
                <img src="web/kari-matti.jpg" alt="Member 1">
                <h3>Kari-Matti Sillanpää</h3>
                <p>Pilvitietokannan suunnittelu ja toteutus</p>
                <div class="social-icons">
                    <a href="https://github.com/sillaka1" target="_blank">
                        <img src="web/github-mark.png" alt="Icon 1">
                    </a>
                    <a href="https://linkedin.com/in/kari-matti-sillanpaa" target="_blank">
                        <img src="web/linkedin.png" alt="Icon 2">
                    </a>
                </div>
            </div>
            <div class="team-member">
                <img src="web/maarit.jpg" alt="Member 2">
                <h3>Maarit Ahlgren</h3>
                <p>Paikallisen tietokannan suunnittelu ja toteutus, Data-analyysi</p>
                <div class="social-icons">
                    <a href="https://github.com/ahlanmaa" target="_blank">
                        <img src="web/github-mark.png" alt="Icon 1">
                    </a>
                    <a href="https://linkedin.com/in/maarit-a-7a20b8197" target="_blank">
                        <img src="web/linkedin.png" alt="Icon 2">
                    </a>
                </div>
            </div>
            <div class="team-member">
                <img src="web/pic3.png" alt="Member 3">
                <h3>Ville Naumanen</h3>
                <p>Paikallisen tietokannan suunnittelu ja toteutus, Data-analyysi</p>
                <div class="social-icons">
                    <a href="https://github.com/NaumVi" target="_blank">
                        <img src="web/github-mark.png" alt="Icon 1">
                    </a>
                    <a href="https://linkedin.com/in/villenaumanen" target="_blank">
                        <img src="web/linkedin.png" alt="Icon 2">
                    </a>
                </div>
            </div>
            <div class="team-member">
                <img src="web/sami.jpg" alt="Member 4">
                <h3>Sami Lappalainen</h3>
                <p>Scrum Master / Projektinhallinta, Data-analyysi</p>
                <div class="social-icons">
                    <a href="https://github.com/stlgithub" target="_blank">
                        <img src="web/github-mark.png" alt="Icon 1">
                    </a>
                    <a href="https://linkedin.com/in/sami-lappalainen" target="_blank">
                        <img src="web/linkedin.png" alt="Icon 2">
                    </a>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
