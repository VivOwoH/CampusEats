// get search input
var searchInput = document.getElementById('search');

// Add event listener to the input serachInput field
searchInput.addEventListener('input', filterRestaurants);

function filterRestaurants(){
    // convert input to all lowercase
    var filterValue = searchInput.value.toLowerCase();
    var cards = document.querySelectorAll.apply('.card');
    
    // iterate over each card
    cards.forEach(function(card) {
        var restuarantName = card.getAttrbute('data-name').toLowerCase();
        console.log(restuarantName)
        if(restuarantName.includes(filterValue)){
            card.style.display = 'block';
        }else{
            card.style.display = 'none';
        }
    });

}