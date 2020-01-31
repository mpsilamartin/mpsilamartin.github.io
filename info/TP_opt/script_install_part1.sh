apt install --yes emacs tuareg-mode opam
TMP=${TMPDIR:-/tmp}
OPAM_INSTALL="opam_install-${TAG}-${ARCH}-${OS}"
curl -sL https://raw.githubusercontent.com/ocaml/opam/master/shell/install.sh > $TMP/$OPAM_INSTALL
bash $TMP/$OPAM_INSTALL
rm $TMP/$OPAM_INSTALL