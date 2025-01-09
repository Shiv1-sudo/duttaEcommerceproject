document.addEventListener("DOMContentLoaded",function(){
    // Toggle the display of subcategories under a category
    window.toggleSubcategories=function toggleSubcategories(categoryId) {
        const subcategoryList = document.getElementById(`subcategory-${categoryId}`);
        if (subcategoryList.style.display === "none" || subcategoryList.style.display === "") {
            subcategoryList.style.display = "block";
        } else {
            subcategoryList.style.display = "none";
        }
    }

    // Show products based on selected subcategory
    window.showProducts=function showProducts(subcategoryId) {
        const productItems = document.querySelectorAll('.product-item');
        let productsFound = false;

        productItems.forEach(item => {
            if (item.dataset.subcategoryId == subcategoryId) {
                item.style.display = 'block';
                productsFound = true;
            } else {
                item.style.display = 'none';
            }
        });

        const noProductsMessage = document.getElementById('no-products');
        if (productsFound) {
            noProductsMessage.style.display = 'none';
        } else {
            noProductsMessage.style.display = 'block';
        }
    }

    // Search products based on input in the search bar
    window.searchProducts=function searchProducts() {
        const searchTerm = document.getElementById('search-bar').value.toLowerCase();
        const productItems = document.querySelectorAll('.product-item');
        let productsFound = false;

        productItems.forEach(item => {
            const productName = item.querySelector('h2').innerText.toLowerCase();
            if (productName.includes(searchTerm)) {
                item.style.display = 'block';
                productsFound = true;
            } else {
                item.style.display = 'none';
            }
        });

        const noProductsMessage = document.getElementById('no-products');
        if (productsFound) {
            noProductsMessage.style.display = 'none';
        } else {
            noProductsMessage.style.display = 'block';
        }
    }
    // Function to navigate to the cart page
    window.viewCart=function viewCart() {
        console.log('Viewing cart');  // Debugging line
        window.location.href = "/cart/";
    }

    // Other functions and event listeners specific to the product listing page

    // Attach the viewCart function to the button
    const viewCartButton = document.getElementById('view-cart-button');
    if (viewCartButton) {
        viewCartButton.addEventListener('click', viewCart);
    } else {
        console.error('View Cart button not found');
    } 
});
