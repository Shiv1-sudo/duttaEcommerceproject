
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from duttaEcommerceapp.models.product import Product

def cart_view(request):
    cart = request.session.get('cart', {})
    
    # Ensure cart is a dictionary
    if not isinstance(cart, dict):
        cart = {}

    cart_products = Product.objects.filter(id__in=cart.keys())
    cart_details = []

    for product in cart_products:
        cart_details.append({
            'product': product,
            'quantity': cart[str(product.id)],
            'total_price': cart[str(product.id)] * product.price
        })

    return render(request, 'cart.html', {'cart_details': cart_details})

@csrf_exempt  # Disable CSRF protection for this view
def update_cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Validate the presence of 'product_id' in the request data
            if 'product_id' not in data:
                return JsonResponse({'success': False, 'error': 'Product ID is required'}, status=400)
            
            product_id = str(data['product_id'])
            
            # Ensure cart is a dictionary in session
            if 'cart' not in request.session:
                request.session['cart'] = {}
            elif isinstance(request.session['cart'], list):
                # Convert cart to dictionary if it is a list
                temp_cart = {}
                for item in request.session['cart']:
                    temp_cart[item] = 1  # Default quantity for each item
                request.session['cart'] = temp_cart

            # Debugging statement to ensure cart structure
            print("Cart before update:", request.session['cart'])

            # Update cart quantity
            if product_id in request.session['cart']:
                request.session['cart'][product_id] += 1
            else:
                request.session['cart'][product_id] = 1
            
            request.session.modified = True

            # Debugging statement to ensure cart structure
            print("Cart after update:", request.session['cart'])

            return JsonResponse({'success': True})
        
        except json.JSONDecodeError as json_error:
            # Specific error handling for JSON decode errors
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)
        
        except KeyError as key_error:
            # Specific error handling for missing keys
            return JsonResponse({'success': False, 'error': f'Missing key: {str(key_error)}'}, status=400)
        
        except Exception as e:
            # General error handling
            print(e)  # Log the error for debugging
            return JsonResponse({'success': False, 'error': 'Internal server error'}, status=500)
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

'''
@csrf_exempt  # Disable CSRF protection for this view
def remove_from_cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Validate the presence of 'product_id' in the request data
            if 'product_id' not in data:
                return JsonResponse({'success': False, 'error': 'Product ID is required'}, status=400)
            
            product_id = str(data['product_id'])
            
            # Ensure cart is a dictionary in session
            if 'cart' in request.session and product_id in request.session['cart']:
                # Decrement the quantity or remove the item if quantity is 1
                if request.session['cart'][product_id] > 1:
                    request.session['cart'][product_id] -= 1
                else:
                    del request.session['cart'][product_id]
                request.session.modified = True

                # Return the updated cart details
                cart_items = [{'product_id': pid, 'quantity': qty} for pid, qty in request.session['cart'].items()]
                return JsonResponse({'success': True, 'cart_items': cart_items})
            else:
                return JsonResponse({'success': False, 'error': 'Product not in cart'}, status=400)
        
        except json.JSONDecodeError as json_error:
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)
        
        except Exception as e:
            print(e)  # Log the error for debugging
            return JsonResponse({'success': False, 'error': 'Internal server error'}, status=500)
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)
'''
@csrf_exempt  # Disable CSRF protection for this view
def remove_from_cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print('Received data:', data)  # Debugging line
            
            # Validate the presence of 'product_id' in the request data
            if 'product_id' not in data:
                return JsonResponse({'success': False, 'error': 'Product ID is required'}, status=400)
            
            product_id = str(data['product_id'])
            
            # Ensure cart is a dictionary in session
            if 'cart' in request.session and product_id in request.session['cart']:
                # Decrement the quantity or remove the item if quantity is 1
                if request.session['cart'][product_id] > 1:
                    request.session['cart'][product_id] -= 1
                else:
                    del request.session['cart'][product_id]
                request.session.modified = True
                print('Updated cart:', request.session['cart'])  # Debugging line

                # Fetch updated cart details
                cart_products = Product.objects.filter(id__in=request.session['cart'].keys())
                cart_details = []

                for product in cart_products:
                    cart_details.append({
                        'product_id': product.id,
                        'name': product.name,
                        'description': product.description,
                        'price': product.price,
                        'quantity': request.session['cart'][str(product.id)],
                        'total_price': request.session['cart'][str(product.id)] * product.price,
                        'image_url': product.image.url if product.image else '/static/img/placeholder.png'
                    })
                print('Cart details:', cart_details)  # Debugging line

                return JsonResponse({'success': True, 'cart_items': cart_details})
            else:
                return JsonResponse({'success': False, 'error': 'Product not in cart'}, status=400)
        
        except json.JSONDecodeError as json_error:
            print('JSON Decode Error:', json_error)  # Debugging line
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)
        
        except Exception as e:
            print('Exception:', e)  # Debugging line
            return JsonResponse({'success': False, 'error': 'Internal server error'}, status=500)
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

@csrf_exempt
def update_quantity(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = str(data['product_id'])
        quantity = int(data['quantity'])

        if 'cart' in request.session:
            if quantity > 0:
                request.session['cart'][product_id] = quantity
            else:
                del request.session['cart'][product_id]
            request.session.modified = True

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

