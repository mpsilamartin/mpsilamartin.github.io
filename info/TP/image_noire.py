def image_noire(n, p):
   """Construit la matrice n*p d'une image noire."""
   img = [0]*n
   for i in range(n):
      img[i] = [0]*p
   return img
