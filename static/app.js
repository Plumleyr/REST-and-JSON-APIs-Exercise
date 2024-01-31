$(document).ready(function(){

    async function getCupcakes(){
        try {
            let resp = await axios.get("/api/cupcakes");
            console.log(resp.data.cupcakes);
    
            for (let cupcake of resp.data.cupcakes){
                let listItem = $('<li>');
                listItem.append($('<div>').text("Flavor: " + cupcake.flavor));
                listItem.append($('<div>').text("Size: " + cupcake.size));
                listItem.append($('<div>').text("Rating: " + cupcake.rating));
                
                // Create the image element with max size attributes
                let imageElement = $('<img>').attr({
                    'src': cupcake.image,
                    'alt': 'Cupcake Image',
                    'style': 'max-width: 200px; max-height: 200px;'
                });
    
                // Append the image to the list item
                listItem.append(imageElement);
                
                // Append the list item to the list
                $('#cupcakes-list').append(listItem);
            }
        } catch (error) {
            console.error("Error fetching cupcakes:", error);
        }
    }
    

    async function createCupcake(evt){
        const flavor = $('#flavor').val();
        const size = $('#size').val();
        const rating = $('#rating').val();
        const image = $('#image').val();

        evt.preventDefault();

        await axios.post("/api/cupcakes", {
        flavor: flavor,
        size: size,
        rating: rating,
        image: image
       });
    }

    getCupcakes();

    $('.cupcake-form').on('submit', createCupcake);
});