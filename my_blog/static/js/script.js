    // // Attend que le document soit prêt
    // document.addEventListener("DOMContentLoaded", function() {
    //     // Récupère les éléments du DOM
    //     var formulaire = document.getElementById("formDeRecherche");
    //     var barreDeRecherche = document.getElementById("barreDeRecherche");
    //     var boutonRechercher = document.getElementById("boutonRechercher");

    //     // Ajoute un gestionnaire d'événements au clic sur le bouton
    //     boutonRechercher.addEventListener("click", function() {
    //         // Récupère la valeur de la barre de recherche
    //         var valeurRecherche = barreDeRecherche.value;

    //         // Effectue l'action de recherche (remplacez cela par votre propre logique de recherche)
    //         //alert("Recherche en cours avec : " + valeurRecherche);
            
    //         // Vous pouvez également soumettre le formulaire si nécessaire
    //         formulaire.submit();
    //     });
    // });

  $(document).ready(function(){
    $('input').keyup(function(){
      let textSaisi = $(this).val();
      let attrName = $(this).attr(name);
      let validatorElement = ".div-error-"+attrName;

      if (textSaisi ===""){
          if(!$(this).hasClass('is-invalid')){
            $(this).addClass('is-invalid');

            $(validatorElement).show();
          }
        } else {
          $(this).removeClass('is-invalid');
          
          $(validatorElement).hide();
        }

    })
})