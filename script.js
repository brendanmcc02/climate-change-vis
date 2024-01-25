// --------------------------------------- CHANGE NAV-BAR COLOUR ON SCROLL ----------------------------------------------

$(function () {                                                                        // Initialise Function
  $(document).scroll(function () {
	  var $nav = $(".navbar-fixed-top");
	  $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());                 // changes colour when the scroll distance exceeds the nav-bar height
	});
});

// ------------------------------------- REVEAL IRELAND DIV ON-CLICK ----------------------------------------------

function showIreDiv() {                                                                 // Initialise Function
  var x = document.getElementById("IreDiv");                                            // Create Variable
  if (x.style.display === "none") {                                                     // "if" statement - when button is clicked
    x.style.display = "block";                                                          // "block" - visible
    document.getElementById('IreAna').scrollIntoView();                                 // Scrolls into view when clicked
  } else {                                                                              // "else" statement - when button is clicked again
    x.style.display = "none";                                                           // "none" - invisible
    document.getElementById('image2').scrollIntoView();                                 // Scrolls into view when clicked
  }
}

// ------------------------------------ REVEAL IRELAND CONCLUSIONS ON-CLICK ----------------------------------------------

function showIreCon() {                                                                 // Initialise Function
  var x = document.getElementById("IreCon");                                            // Create Variable
  if (x.style.display === "none") {                                                     // "if" statement - when button is clicked
    x.style.display = "block";                                                          // "block" - visible
    document.getElementById('IreDiv').scrollIntoView();                                 // Scrolls into view when clicked
  } else {                                                                              // "else" statement - when button is clicked again
    x.style.display = "none";                                                           // "none" - invisible
    document.getElementById('IreAna').scrollIntoView();                                 // Scrolls into view when clicked
  }
}

// --------------------------------------- REVEAL USA DIV ON-CLICK ----------------------------------------------

function showUsaDiv() {                                                                 // Initialise Function
  var x = document.getElementById("UsaDiv");                                            // Create Variable
  if (x.style.display === "none") {                                                     // "if" statement - when button is clicked
    x.style.display = "block";                                                          // "block" - visible
    document.getElementById('UsaAna').scrollIntoView();                                 // Scrolls into view when clicked
  } else {                                                                              // "else" statement - when button is clicked again
    x.style.display = "none";                                                           // "none" - invisible
    document.getElementById('image5').scrollIntoView();                                 // Scrolls into view when clicked
  }
}

// ---------------------------------------- REVEAL USA CONCLUSIONS ON-CLICK ----------------------------------------------

function showUsaCon() {                                                                 // Initialise Function
  var x = document.getElementById("UsaCon");                                            // Create Variable
  if (x.style.display === "none") {                                                     // "if" statement - when button is clicked
    x.style.display = "block";                                                          // "block" - visible
    document.getElementById('UsaDiv').scrollIntoView();                                 // Scrolls into view when clicked
  } else {                                                                              // "else" statement - when button is clicked again
    x.style.display = "none";                                                           // "none" - invisible
    document.getElementById('UsaAna').scrollIntoView();                                 // Scrolls into view when clicked
  }
}

// --------------------------------------- TAB BUTTONS TO ALTERNATE BETWEEN DIV'S [EUROPE] ----------------------------------------------

function openEUPage(pageName, elmnt) {                                                   // Initialise Function
  document.getElementById('EUDiv').scrollIntoView();                                     // Scrolls into view when clicked
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");                            // Create Variable
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";                                                // "for" statement - when tab button is unclicked, "none" - invisible
  }

  document.getElementById(pageName).style.display = "block";                             // When tab button is clicked, "block" - becomes visible
}

// --------------------------------------- REVEAL UK CONCLUSIONS ON-CLICK ----------------------------------------------

function showUKCon() {                                                                 // Initialise Function
  var x = document.getElementById("UKCon");                                            // Create Variable
  if (x.style.display === "none") {                                                    // "if" statement - when button is clicked
    x.style.display = "block";                                                         // "block" - visible
    document.getElementById('ukconbutton').scrollIntoView();                           // Scrolls into view when clicked
  } else {                                                                             // "else" statement - when button is clicked again
    x.style.display = "none";                                                          // "none" - invisible
    document.getElementById('EUDiv').scrollIntoView();                                 // Scrolls into view when clicked
  }
}

// --------------------------------------- REVEAL FRANCE CONCLUSIONS ON-CLICK ----------------------------------------------

function showFraCon() {                                                                 // Initialise Function
  var x = document.getElementById("FraCon");                                            // Create Variable
  if (x.style.display === "none") {                                                     // "if" statement - when button is clicked
    x.style.display = "block";                                                          // "block" - visible
    document.getElementById('fraconbutton').scrollIntoView();                           // Scrolls into view when clicked
  } else {                                                                              // "else" statement - when button is clicked again
    x.style.display = "none";                                                           // "none" - invisible
    document.getElementById('EUDiv').scrollIntoView();                                  // Scrolls into view when clicked
  }
}

// --------------------------------------- REVEAL SPAIN CONCLUSIONS ON-CLICK ----------------------------------------------

function showSpaCon() {                                                                 // Initialise Function
  var x = document.getElementById("SpaCon");                                            // Create Variable
  if (x.style.display === "none") {                                                     // "if" statement - when button is clicked
    x.style.display = "block";                                                          // "block" - visible
    document.getElementById('spaconbutton').scrollIntoView();                           // Scrolls into view when clicked
  } else {                                                                              // "else" statement - when button is clicked again
    x.style.display = "none";                                                           // "none" - invisible
    document.getElementById('EUDiv').scrollIntoView();                                  // Scrolls into view when clicked
  }
}

// --------------------------------------- TAB BUTTONS TO ALTERNATE BETWEEN DIV'S [ASIA] ----------------------------------------------

function openAsiaPage(pageName, elmnt) {                                                  // Initialise Function
  document.getElementById('AsiaDiv').scrollIntoView();                                    // Scrolls into view when clicked
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");                             // Create Variable
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";                                                 // "for" statement - when tab button is unclicked, "none" - invisible
  }

  document.getElementById(pageName).style.display = "block";                              // When tab button is clicked, "block" - becomes visible
}


// --------------------------------------- REVEAL CHINA CONCLUSIONS ON-CLICK ----------------------------------------------

function showChiCon() {                                                                 // Initialise Function
  var x = document.getElementById("ChiCon");                                            // Create Variable
  if (x.style.display === "none") {                                                     // "if" statement - when button is clicked
    x.style.display = "block";                                                          // "block" - visible
    document.getElementById('chiconbutton').scrollIntoView();                           // Scrolls into view when clicked
  } else {                                                                              // "else" statement - when button is clicked again
    x.style.display = "none";                                                           // "none" - invisible
    document.getElementById('AsiaDiv').scrollIntoView();                                // Scrolls into view when clicked
  }
}

// --------------------------------------- REVEAL JAPAN CONCLUSIONS ON-CLICK ----------------------------------------------

function showJapCon() {                                                                        // Initialise Function
  var x = document.getElementById("JapCon");                                                   // Create Variable
  if (x.style.display === "none") {                                                            // "if" statement - when button is clicked
    x.style.display = "block";                                                                 // "block" - visible
    document.getElementById('japconbutton').scrollIntoView();                                  // Scrolls into view when clicked
  } else {                                                                                     // "else" statement - when button is clicked again
    x.style.display = "none";                                                                  // "none" - invisible
    document.getElementById('AsiaDiv').scrollIntoView();                                       // Scrolls into view when clicked
  }
}