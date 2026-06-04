/* GLOBAL BODY STYLE */

body{
    background: linear-gradient(135deg,#4facfe,#00f2fe);
    min-height:100vh;
    font-family: "Segoe UI", Arial, sans-serif;
}

.custom-navbar{
    background: rgba(0,0,0,0.25);
    backdrop-filter: blur(8px);
    border-bottom:1px solid rgba(255,255,255,0.2);
}

.navbar-brand{
    font-weight:bold;
    font-size:22px;
}

.nav-link{
    font-weight:500;
}


/* NAVBAR */



/* TITLE SECTION */

.title{
    font-weight:bold;
    font-size:40px;
    letter-spacing:1px;
}


/* MAIN CARD */

.main-card{
    margin-top:40px;
    border-radius:15px;
    box-shadow:0px 10px 25px rgba(0,0,0,0.2);
    border:none;
}


/* INPUT FIELD */

input.form-control{
    height:50px;
    font-size:16px;
    border-radius:8px;
}


/* BUTTON */

button.btn{
    padding:10px 20px;
    font-size:16px;
    border-radius:8px;
}


/* REPORT STATS CARDS */

.card{
    border-radius:12px;
}

.card h5{
    font-weight:600;
}

.card h3{
    font-weight:bold;
    color:#007bff;
}


/* SCREENSHOT IMAGE */

.screenshot{
    border-radius:10px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.2);
    margin-top:15px;
}


/* LOADER */

.loader{
    display:none;
    margin-top:20px;
}


/* LIST ITEMS */

.list-group-item{
    font-size:15px;
}


/* FOOTER */

footer{
    margin-top:60px;
}


/* HOVER EFFECTS */

.card:hover{
    transform:translateY(-4px);
    transition:0.3s;
}


/* MOBILE RESPONSIVE */

@media(max-width:768px){

.title{
    font-size:30px;
}

.main-card{
    margin-top:20px;
}

}