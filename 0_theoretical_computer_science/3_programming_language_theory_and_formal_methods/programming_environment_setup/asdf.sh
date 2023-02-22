echo "downloading asdf"
brew install asdf
echo "done"

echo "installing asdf"
echo -e "\n. $(brew --prefix asdf)/libexec/asdf.sh" >> ${ZDOTDIR:-~}/.zshrc
echo "done"