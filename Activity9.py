price_a = 1.50
price_b = 3.00

temp    = price_a   # Step 1: save price_a
price_a = price_b   # Step 2: move price_b into price_a
price_b = temp      # Step 3: put saved value into price_b

print("After swap:", price_a, "and", price_b)