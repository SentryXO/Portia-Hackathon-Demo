// Main application code
function loadProducts() {
    fetch('/api/products')
        .then(response => response.json())
        .then(data => displayProducts(data));
    // BUG: No error handling
}

function displayProducts(products) {
    const container = document.getElementById('products');
    products.forEach(product => {
        container.innerHTML += `<div>${product.name} - ${product.price}</div>`;
    });
}

loadProducts();