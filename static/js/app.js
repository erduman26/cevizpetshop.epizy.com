// Dark and Light
(function () {
    [...document.querySelectorAll(".control")].forEach(button => {
        button.addEventListener("click", function() {
            document.querySelector(".active-btn").classList.remove("active-btn");
            this.classList.add("active-btn");
            document.querySelector(".active").classList.remove("active");
            document.getElementById(button.dataset.id).classList.add("active");
        })
    });
    document.querySelector(".theme-btn").addEventListener("click", () => {
        document.body.classList.toggle("light-mode");
    })
})();

// Scroll
$(window).scroll(function() {
    if ($(this).scrollTop() >= 350) {
        $('#up').fadeIn(200);
    } else {
         $('#up').fadeOut(200);
    }
});

// Click
$('#up').on('click', function() {
    $("html, body").animate({scrollTop: 0}, 1000);
});

// Butona tıklandığında içeriği gizle ve göster
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
// Açılır listenin dışına tıklanırsa listeği kapat
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
      }
    }
  }
}