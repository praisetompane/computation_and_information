echo "adding asdf python plugin"
asdf plugin add python
echo "done"

echo "installing python"
asdf install python latest
echo "done"

echo "set latest version to system wide version"
asdf global python latest
echo "done"

echo "installing pipenv"
brew install pipenv
echo "done"

echo "installing all packages for python"
pipenv install
echo "done"