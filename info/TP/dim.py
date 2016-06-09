def dim(img):
  """Donne le couple (n, p) des dimensions de la matrice img. n :
  nombre de lignes, p : nombre de colonnes. La matrice est supposée
  avoir au moins une ligne."""
  n = len(img)
  p = len(img[0])
  return (n,p)
