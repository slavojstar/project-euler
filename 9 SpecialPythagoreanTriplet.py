# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Pythagorean triplets can be generated using 2 natural numbers m and n in the following way:
# (m^2 - n^2, 2mn, m^2 + n^2) or (n^2 - m^2, 2mn, m^2 + n^2)
# so we just need to find m and n subject to:
#    a + b + c = 1000
# => m(m + n) = 500
# We see m = 20, n = 5 by inspection, so the answer is 2(m^2 - n^2)mn(m^2 + n^2) = 2(m^4 - n^4)mn = 31875000.

print(31875000)
return 31875000