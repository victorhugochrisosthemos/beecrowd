SELECT products.name AS name, 
       providers.name AS name 
FROM products
JOIN providers ON products.id_providers = providers.id 
WHERE providers.name = 'Ajax SA';