document.addEventListener("DOMContentLoaded",function(){
    /*window.getCookie*/function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }   
        }
        return cookieValue;
    }

    window.addToCart=function addToCart(productId) {
        if (!productId) {
            showNotification("Invalid product ID");
            return;
        }
    
        console.log('Adding product to cart:', productId);  // Debugging line
    
        fetch('/update_cart/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ product_id: productId })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Response from server:', data);  // Debugging line
            if (data.success) {
                showNotification("Product added to cart!");
                updateCartContent(data.cart_items || []); // Update cart content
            } else {
                console.error('Server error:', data.error);  // Debugging line
            }
        })
        .catch(error => {
            console.error('Error:', error);  // Debugging line
        });
    }

    window.removeFromCart=function removeFromCart(productId) {
        console.log('Removing product from cart:', productId);  // Debugging line

        fetch('/remove_from_cart/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ product_id: productId })
        })
        .then(response => {
            console.log('Response status:', response.status);  // Debugging line
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Response data:', data);  // Debugging line
            if (data.success) {
                showNotification("Product removed from cart!");
                updateCartContent(data.cart_items || []); // Update cart content
            } else {
                showNotification("Failed to remove product from cart.");
                console.error('Server error:', data.error);  // Debugging line
            }
        })
        .catch(error => {
            console.error('Error:', error);  // Debugging line
            showNotification("An error occurred. Please try again.");
        });
    }

    window.updateQuantity=function updateQuantity(productId, quantity) {
        console.log('Updating quantity for product:', productId, 'to', quantity);  // Debugging line

        fetch('/update_quantity/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ product_id: productId, quantity: quantity })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Response from server:', data);  // Debugging line
            if (data.success) {
                updateCartContent(data.cart_items || []); // Update cart content
            } else {
                showNotification("Failed to update quantity.");
                console.error('Server error:', data.error);  // Debugging line
            }
        })
        .catch(error => {
            console.error('Error:', error);  // Debugging line
            showNotification("An error occurred. Please try again.");
        });
    }

    /* Function to handle proceeding to the payment section */
    window.proceedToPayment=function proceedToPayment() {
        console.log('Proceeding to payment'); // Debugging line

        const cartSection = document.getElementById('cart-section');
        const paymentSection = document.getElementById('payment-section');
        const proceedButton = document.getElementById('proceed-to-payment');
        const paymentUrl = proceedButton.getAttribute('data-url'); // Get the URL from the data attribute
        //PaymentURL 
        console.log('Payment URL:',paymentUrl);

        if (cartSection && paymentSection) {
            cartSection.style.display = 'none';
            paymentSection.style.display = 'block';
            console.log('Sections updated'); // Debugging line

            // Fetch and load the content from proceed_to_payment.html
            //fetch("{% url 'proceed_to_payment' %}")
            fetch(paymentUrl)
                .then(response => response.text())
                .then(html => {
                    paymentSection.innerHTML = html;
                })
                .catch(error => console.error('Error loading payment section:', error));
        } else {
            console.error('Sections not found'); // Error message
        }
    }
        // Attach the proceedToPayment function to the button
        const proceedButton = document.getElementById('proceed-to-payment');
        if (proceedButton) {
            proceedButton.addEventListener('click', proceedToPayment);
        } else {
            console.error('Proceed to Payment button not found');
        }

    window.showNotification=function showNotification(message) {
        const notification = document.createElement('div');
        notification.className = 'notification';
        notification.innerText = message;
    
        document.body.appendChild(notification);
    
        setTimeout(() => {
            notification.remove();
        }, 3000); // Remove notification after 3 seconds
    }

    window.updateCartContent=function updateCartContent(cartItems) {
        const cartList = document.getElementById('cart-list');
        cartList.innerHTML = ''; // Clear the existing content

        if (cartItems.length === 0) {
            cartList.innerHTML = '<p>Your cart is empty.</p>';
        } else {
            cartItems.forEach(item => {
                const cartItem = document.createElement('div');
                cartItem.className = 'cart-item';
                const price = Number(item.price) || 0; // Ensure price is a number
                const totalPrice = Number(item.total_price) || 0; // Ensure total_price is a number
            
                // Generate the cart item content
                cartItem.innerHTML = `
                    <img src="${item.image_url}" alt="Image of ${item.name}" class="small-image">
                    <h2>${item.name}</h2>
                    <p>${item.description}</p>
                    <p>Price: $${price.toFixed(2)}</p>
                    <p>Quantity: <input type="number" value="${item.quantity}" min="1" onchange="updateQuantity('${item.product_id}', this.value)"></p>
                    <p>Total: $${totalPrice.toFixed(2)}</p>
                    <button class="remove-from-cart" onclick="removeFromCart('${item.product_id}')">Remove from Cart</button>
                    <button class="add-to-wishlist" onclick="addToWishlist('${item.product_id}')">Add to Wishlist</button>
                `;
                cartList.appendChild(cartItem);
            });
        }
    }

    window.updateCartCount=function updateCartCount() {
        // Implement logic to update the cart count displayed on the page
        // This can involve fetching the cart details from the server or updating a local variable
    }
    // Function to navigate to the cart page
    /*window.viewCart=function viewCart() {
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
    }*/
    /*function viewCart() {
        console.log('Viewing cart');  // Debugging line
        window.location.href = "/cart/";
    } */
   // Fetch phone extensions and populate the dropdown
   /*try {
    const phoneExtensionSelect = document.getElementById('phone_extension');
    if (phoneExtensionSelect) {
        fetch('https://restcountries.com/v3.1/all')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                try {
                    data.forEach(country => {
                        if (country.idd && country.idd.root && country.idd.suffixes) {
                            country.idd.suffixes.forEach(suffix => {
                                const option = document.createElement('option');
                                option.value = `${country.idd.root}${suffix}`;
                                option.textContent = `${country.idd.root}${suffix} (${country.name.common})`;
                                phoneExtensionSelect.appendChild(option);
                            });
                        }
                    });
                } catch (innerError) {
                    console.error('Error processing country data:', innerError);
                }
            })
            .catch(error => console.error('Error fetching phone extensions:', error));
    } else {
        console.error('Phone extension dropdown not found');
    }
} catch (outerError) {
    console.error('Error initializing phone extensions fetching:', outerError);
}*/
});
